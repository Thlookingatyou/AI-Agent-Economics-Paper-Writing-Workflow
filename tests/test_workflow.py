import contextlib
import csv
import io
from pathlib import Path
import sys
import tempfile
import unittest
from workflow import cli
from workflow.demo import holding_vectors, run_demo


def complete_config():
    return {'question': 'Does the fictional pipeline preserve records?', 'purpose': 'synthetic-demo',
            'design': dict(estimand='descriptive spread', unit='fictional stock', sample='synthetic fixture', specification='cosine spread', benchmark='low group'),
            'timing': dict(information_set='pre-score snapshot', training_cutoff='2025-06-30', score_availability='2025-08-01', outcome_window='2025-08-02 to 2025-08-31'),
            'inference': dict(method='none', independent_variation='not used in demo'),
            'selection': dict(status='planned', criterion='pipeline integrity', exploratory=False), 'seed': 1}


class PaperTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.p = cli.create_paper(self.root, 'test-paper', 'Test', 'embeddings')
        cli.write_json(self.root / 'config.json', complete_config())
        (self.root / 'analysis.py').write_text('print("ok")\n', encoding='utf-8')
        (self.root / 'inputs.txt').write_text('fictional\n', encoding='utf-8')

    def call(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return cli.main(list(args), self.root)

    def prepare(self):
        m = cli.prepare_run(self.root, self.p, 'config.json', ['inputs.txt'], ['analysis.py'])
        return m['run_id'], cli.load_run(self.p, m['run_id'])

    def scope(self, mode='run'):
        self.assertEqual(self.call('task', 'test-paper', '--mode', mode, '--request', 'Test current scope'), 0)

    def execute(self, rid, code='pass'):
        return self.call('run', 'test-paper', '--run-id', rid, '--', sys.executable, '-c', code)

    def test_paper_no_overwrite(self):
        with self.assertRaises(cli.WorkflowError):
            cli.create_paper(self.root, 'test-paper', 'replacement', 'general')
        self.assertEqual(cli.read_json(self.p / 'state.json')['title'], 'Test')

    def test_path_and_windows_names(self):
        for name in ('../escape', 'with spaces', 'CON', 'con', 'lpt1', 'a/b', 'x--y'):
            with self.subTest(name=name), self.assertRaises(cli.WorkflowError):
                cli.create_paper(self.root, name, 'bad', 'general')
        with self.assertRaises(cli.WorkflowError):
            cli.contained(self.p, '../../escape')

    def test_symlink_escape(self):
        external = self.root / 'outside'
        external.mkdir()
        try:
            (self.p / 'external').symlink_to(external, target_is_directory=True)
        except OSError:
            self.skipTest('Symlinks unavailable')
        with self.assertRaises(cli.WorkflowError):
            cli.contained(self.p, 'external/anything')

    def test_incomplete_or_unjustified_protocol(self):
        with self.assertRaises(cli.WorkflowError):
            cli.validate_protocol(cli.read_json(cli.SOURCE / 'templates/paper/configs/experiment.json'))
        cfg = complete_config()
        cfg['purpose'] = 'empirical'
        with self.assertRaises(cli.WorkflowError):
            cli.validate_protocol(cfg)
        self.assertFalse((self.p / 'runs').exists())

    def test_malformed_protocol_types(self):
        for section, field, value in [('inference', 'method', []), ('design', 'unit', 12), ('selection', 'exploratory', 'false')]:
            cfg = complete_config()
            cfg[section][field] = value
            with self.subTest(field=field), self.assertRaises(cli.WorkflowError):
                cli.validate_protocol(cfg)

    def test_fingerprints_and_no_copy_of_inputs(self):
        rid, run = self.prepare()
        self.assertEqual(cli.verify_run_inputs(self.root, run), [])
        self.assertEqual((run / 'snapshot/analysis.py').read_text(), 'print("ok")\n')
        (self.root / 'inputs.txt').write_text('changed')
        self.assertIn('inputs.txt', cli.verify_run_inputs(self.root, run)[0])
        self.assertFalse((run / 'inputs.txt').exists())

    def test_code_config_drift_prevents_execution(self):
        self.scope()
        for name in ('analysis.py', 'config.json'):
            with self.subTest(name=name):
                original = (self.root / name).read_bytes()
                rid, run = self.prepare()
                (self.root / name).write_text('changed')
                self.assertEqual(self.execute(rid), 2)
                self.assertEqual(cli.read_json(run / 'status.json')['status'], 'prepared')
                (self.root / name).write_bytes(original)

    def test_inspect_and_code_scope(self):
        rid, run = self.prepare()
        for mode in ('inspect', 'code'):
            self.scope(mode)
            self.assertEqual(self.execute(rid), 2)
        self.assertEqual(cli.read_json(run / 'status.json')['status'], 'prepared')

    def test_logs_and_no_rerun_overwrite(self):
        rid, run = self.prepare()
        self.scope()
        self.assertEqual(self.execute(rid, 'import sys; print("ok"); print("diagnostic", file=sys.stderr)'), 0)
        self.assertEqual(cli.read_json(run / 'status.json')['status'], 'completed')
        self.assertIn('ok', (run / 'stdout.log').read_text())
        self.assertIn('diagnostic', (run / 'stderr.log').read_text())
        self.assertEqual(self.execute(rid), 2)

    def test_failed_and_missing_executable(self):
        self.scope()
        rid, run = self.prepare()
        self.assertEqual(self.execute(rid, 'raise SystemExit(7)'), 7)
        self.assertEqual(cli.read_json(run / 'status.json')['status'], 'failed')
        rid2, run2 = self.prepare()
        self.assertNotEqual(rid, rid2)
        self.assertEqual(self.call('run', 'test-paper', '--run-id', rid2, '--', 'missing-executable-123'), 1)
        self.assertEqual(cli.read_json(run2 / 'status.json')['status'], 'failed')

    def test_mid_run_changes_flagged(self):
        self.scope()
        rid, run = self.prepare()
        self.assertEqual(self.execute(rid, 'from pathlib import Path; Path("inputs.txt").write_text("changed")'), 2)
        self.assertEqual(cli.read_json(run / 'status.json')['status'], 'completed-with-input-drift')

    def test_artifact_existence_hash_and_version(self):
        self.scope()
        rid, run = self.prepare()
        self.assertEqual(self.execute(rid), 0)
        path = 'papers/test-paper/runs/' + rid + '/table.txt'
        args = ['artifact', 'test-paper', '--id', 'main-table-v1', '--run-id', rid, '--path', path, '--kind', 'table', '--label', 'tab:main']
        self.assertEqual(self.call(*args), 2)
        (self.root / path).write_text('synthetic estimates')
        self.assertEqual(self.call(*args), 0)
        self.assertEqual(self.call(*args), 2)
        (self.root / path).write_text('tampered')
        self.assertTrue(any('checksum mismatch' in x for x in cli.check_paper(self.root, self.p)))
        (self.root / path).unlink()
        self.assertTrue(any('missing private/local' in x for x in cli.check_paper(self.root, self.p)))

    def test_tasks_context_and_decision_history(self):
        self.scope('inspect')
        self.scope('code')
        self.assertEqual(len(cli.records(self.p / 'research/task-history.jsonl')), 1)
        self.call('decision', 'test-paper', '--text', 'Keep original null', '--source', 'User request')
        s = cli.read_json(self.p / 'state.json')
        s['required_private_inputs'] = ['holdings/export.csv']
        cli.write_json(self.p / 'state.json', s)
        brief = cli.context(self.root, self.p)
        self.assertIn('Keep original null', brief)
        self.assertIn('not found/configured', brief)
        self.assertIn('code', brief)

    def test_no_command_does_not_consume_run(self):
        rid, run = self.prepare()
        self.scope()
        self.assertEqual(self.call('run', 'test-paper', '--run-id', rid), 2)
        self.assertEqual(cli.read_json(run / 'status.json')['status'], 'prepared')

    def test_local_data_root_must_exist(self):
        self.assertEqual(self.call('configure', '--data-root', str(self.root / 'missing')), 2)
        self.assertEqual(self.call('configure', '--data-root', str(self.root)), 0)
        self.assertTrue((self.root / '.local/machine.json').is_file())


class ScientificFixtures(unittest.TestCase):
    def test_timing(self):
        self.assertEqual(cli.timing_errors(cli.SOURCE / 'examples/timing_valid.csv'), [])
        errors = cli.timing_errors(cli.SOURCE / 'examples/timing_invalid.csv')
        self.assertEqual(len(errors), 4)
        for phrase in ('future training', 'unavailable', 'unknown/invalid'):
            self.assertTrue(any(phrase in x for x in errors))

    def test_partial_disclosure(self):
        with self.assertRaisesRegex(cli.WorkflowError, 'Partial disclosure'):
            holding_vectors([dict(fund_id='a', stock_id='000001', weight='0.1', disclosure_complete='false')])

    def test_duplicates(self):
        row = dict(fund_id='a', stock_id='000001', weight='0.1', disclosure_complete='true')
        with self.assertRaisesRegex(cli.WorkflowError, 'Duplicate'):
            holding_vectors([row, row])

    def test_demo_reproducibility_and_identifiers(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td)
            first, second = run_demo(path / 'one'), run_demo(path / 'two')
            self.assertEqual(first['scores_sha256'], second['scores_sha256'])
            self.assertAlmostEqual(first['high_minus_low_return'], -0.01)
            with (path / 'one/scores.csv').open(newline='') as f:
                self.assertEqual(next(csv.DictReader(f))['stock_id'], '000001')
            self.assertIn('no significance/causal claim', first['inference'])

    def test_repository_validation(self):
        self.assertEqual(cli.validate_repo(), [])


if __name__ == '__main__':
    unittest.main()

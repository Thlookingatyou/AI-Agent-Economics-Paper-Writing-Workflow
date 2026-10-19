"""Small, inspectable research records; no model API or database dependencies."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import uuid
from datetime import date, datetime, timezone
from typing import Any

SOURCE = Path(__file__).resolve().parents[1]
MODES = ('inspect', 'evaluate', 'code', 'run', 'review', 'edit', 'integrate')
SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


class WorkflowError(ValueError):
    """An actionable input or provenance problem."""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def identifier(prefix: str) -> str:
    return prefix + '-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def read_json(path: Path) -> Any:
    with path.open(encoding='utf-8') as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        temp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def append_record(path: Path, data: Any) -> None:
    """Append-only human-readable log. Use one writer per paper/branch."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')


def records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]


def safe_id(value: str) -> str:
    # Windows reserves these filenames even when they have extensions.
    if not SLUG.fullmatch(value) or value.upper() in {'CON', 'PRN', 'AUX', 'NUL', *(f'COM{i}' for i in range(1, 10)), *(f'LPT{i}' for i in range(1, 10))}:
        raise WorkflowError('Use a non-reserved lowercase name with letters, numbers and single hyphens.')
    return value


def contained(base: Path, path: str | Path) -> Path:
    base = base.resolve()
    p = (base / path).resolve()
    if not p.is_relative_to(base):
        raise WorkflowError(f'Path must stay inside {base.name}.')
    return p


def paper(root: Path, slug: str) -> Path:
    p = contained(root, Path('papers') / safe_id(slug))
    if not (p / 'state.json').is_file():
        raise WorkflowError(f'Paper {slug!r} does not exist. Create it with new.')
    return p


def logical(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())  # Only saved into ignored run metadata.


def resolve_input(root: Path, value: str) -> Path:
    p = Path(value).expanduser()
    p = p if p.is_absolute() else root / p
    p = p.resolve()
    if not p.is_file():
        raise WorkflowError(f'Input file is missing: {value}')
    return p


def file_record(root: Path, p: Path) -> dict:
    return {'path': logical(root, p), 'sha256': digest(p), 'bytes': p.stat().st_size}


def create_paper(root: Path, slug: str, title: str, track: str) -> Path:
    p = contained(root, Path('papers') / safe_id(slug))
    if p.exists():
        raise WorkflowError('Paper already exists; refusing to overwrite it.')
    p.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE / 'templates/paper', p)
    state = {'schema_version': 1, 'paper_id': slug, 'title': title, 'track': track,
             'created_at': now(), 'updated_at': now(), 'question_status': 'open',
             'stage': 'idea-and-feasibility', 'authoritative_manuscript': None,
             'verified_findings': [], 'open_questions': [], 'required_private_inputs': [],
             'next_action': 'Evaluate the economic question and inspect available work/data.',
             'current_task': None,
             'track_protocol': {'embeddings': 'docs/embeddings.md', 'ai-trading': 'docs/ai-trading.md', 'general': 'docs/methods-and-inference.md'}[track]}
    write_json(p / 'state.json', state)
    write_json(p / 'artifacts.json', [])
    (p / 'research/decisions.jsonl').touch()
    (p / 'research/task-history.jsonl').touch()
    return p


def validate_protocol(cfg: dict) -> None:
    if not isinstance(cfg, dict):
        raise WorkflowError('Experiment config must be a JSON object.')
    required = {'question': None, 'purpose': None,
                'design': ('estimand', 'unit', 'sample', 'specification', 'benchmark'),
                'timing': ('information_set', 'training_cutoff', 'score_availability', 'outcome_window'),
                'inference': ('method', 'independent_variation'),
                'selection': ('status', 'criterion', 'exploratory')}
    bad = []
    for key, children in required.items():
        if children is None:
            vals = [(key, cfg.get(key))]
        else:
            section = cfg.get(key)
            if not isinstance(section, dict):
                bad.append(key)
                continue
            vals = [(key + '.' + sub, section.get(sub)) for sub in children]
        for label, value in vals:
            if (label == 'selection.exploratory' and not isinstance(value, bool)) or (label != 'selection.exploratory' and (not isinstance(value, str) or value.strip().lower() in {'', 'unset', 'todo', 'tbd', 'unknown'})):
                bad.append(label)
    if bad:
        raise WorkflowError('Complete experiment fields before registration: ' + ', '.join(bad))
    if cfg['purpose'] not in {'empirical', 'simulation', 'synthetic-demo', 'model-training'}:
        raise WorkflowError('purpose must be empirical, simulation, model-training or synthetic-demo.')
    if cfg['selection']['status'] not in {'planned', 'retrospective', 'amended'} or not isinstance(cfg['selection']['exploratory'], bool):
        raise WorkflowError('selection requires a planned/retrospective/amended status and boolean exploratory.')
    if cfg['purpose'] != 'synthetic-demo' and cfg['inference']['method'].strip().lower() in {'none', 'not applicable', 'n/a', 'descriptive-only'}:
        raise WorkflowError('Non-demo runs require a justified uncertainty/inference plan; describe it explicitly.')


def git_snapshot(root: Path) -> dict:
    try:
        rev = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=root, capture_output=True, text=True, timeout=5)
        dirty = subprocess.run(['git', 'status', '--porcelain'], cwd=root, capture_output=True, text=True, timeout=5)
        return {'commit': rev.stdout.strip() if rev.returncode == 0 else None,
                'dirty': bool(dirty.stdout.strip()) if dirty.returncode == 0 else None}
    except (OSError, subprocess.TimeoutExpired):
        return {'commit': None, 'dirty': None}


def prepare_run(root: Path, p: Path, config: str, inputs: list[str], scripts: list[str]) -> dict:
    cp = resolve_input(root, config)
    cfg = read_json(cp)
    validate_protocol(cfg)
    # Validate before creating a run; never snapshot arbitrary private paths as code.
    code_paths = []
    for value in scripts:
        path = contained(root, value)
        if not path.is_file():
            raise WorkflowError(f'Missing code/config dependency: {value}')
        code_paths.append(path)
    input_paths = [resolve_input(root, v) for v in inputs]
    if not scripts:
        raise WorkflowError('Register at least one code file with --script, including helpers/lock files as needed.')
    rid = identifier('run')
    run = p / 'runs' / rid
    run.mkdir(parents=True)
    shutil.copyfile(cp, run / 'config.json')
    code = []
    for path in code_paths:
        rel = path.relative_to(root.resolve())
        dest = run / 'snapshot' / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)
        rec = file_record(root, path)
        rec['snapshot'] = dest.relative_to(run).as_posix()
        code.append(rec)
    manifest = {'schema_version': 1, 'run_id': rid, 'paper_id': p.name, 'created_at': now(),
                'config': file_record(root, cp), 'config_snapshot_sha256': digest(run / 'config.json'),
                'code': code, 'inputs': [file_record(root, path) for path in input_paths],
                'parent_run': cfg.get('parent_run'), 'purpose': cfg['purpose'],
                'output_policy': 'local-private; no automatic manuscript integration'}
    write_json(run / 'manifest.json', manifest)
    write_json(run / 'environment.json', {'python': sys.version, 'platform': platform.platform(),
                                         'executable': sys.executable, 'git': git_snapshot(root),
                                         'note': 'Capture analysis dependency locks and GPU/library details separately; environment variables omitted.'})
    write_json(run / 'status.json', {'status': 'prepared', 'recorded_at': now()})
    return manifest


def load_run(p: Path, rid: str) -> Path:
    # Generated IDs include an uppercase UTC T/Z. Do not allow arbitrary path components.
    if not re.fullmatch(r'run-\d{8}T\d{6}Z-[a-f0-9]{8}', rid):
        raise WorkflowError('Invalid run ID.')
    run = contained(p / 'runs', rid)
    if not (run / 'manifest.json').is_file():
        raise WorkflowError('Unknown run ID.')
    return run


def verify_run_inputs(root: Path, run: Path) -> list[str]:
    m = read_json(run / 'manifest.json')
    errors = []
    for rec in [m['config'], *m['code'], *m['inputs']]:
        path = Path(rec['path'])
        path = path if path.is_absolute() else root / path
        if not path.is_file() or digest(path) != rec['sha256']:
            errors.append('Missing or changed input/code/config: ' + rec['path'])
    if digest(run / 'config.json') != m['config_snapshot_sha256']:
        errors.append('Config snapshot has changed.')
    for rec in m['code']:
        snap = contained(run, rec['snapshot'])
        if not snap.is_file() or digest(snap) != rec['sha256']:
            errors.append('Code snapshot has changed: ' + rec['path'])
    return errors


def execute_run(root: Path, p: Path, rid: str, command: list[str]) -> int:
    state = read_json(p / 'state.json')
    task = state.get('current_task') or {}
    if task.get('mode') != 'run':
        raise WorkflowError('Recorded task is not run mode. Follow the current user request; do not promote an inspect/code task to execution.')
    command = command[1:] if command and command[0] == '--' else command
    if not command:
        raise WorkflowError('Provide an explicit command after --.')
    run = load_run(p, rid)
    if read_json(run / 'status.json')['status'] != 'prepared':
        raise WorkflowError('Run already attempted. Register a new run for retry/resume; preserve the original.')
    errors = verify_run_inputs(root, run)
    if errors:
        raise WorkflowError('\n'.join(errors) + '\nRegister a new run after correcting the inputs.')
    # Exclusive marker prevents two devices/processes from starting the same local run.
    try:
        with (run / 'execution.lock').open('x', encoding='utf-8') as f:
            f.write(now() + '\n')
    except FileExistsError as exc:
        raise WorkflowError('Run execution already claimed; inspect its status before retrying.') from exc
    status = {'status': 'running', 'started_at': now(), 'command': command,
              'task_id': task['id'], 'workflow_pid': os.getpid(),
              'note': 'Status is a record, not a process-liveness guarantee.'}
    write_json(run / 'status.json', status)
    rc = 1
    try:
        with (run / 'stdout.log').open('w', encoding='utf-8') as out, (run / 'stderr.log').open('w', encoding='utf-8') as err:
            # No shell; syntax and expansion must be explicit in the analysis program.
            proc = subprocess.Popen(command, cwd=root, stdout=out, stderr=err)
            status['child_pid'] = proc.pid
            write_json(run / 'status.json', status)
            try:
                rc = proc.wait()
            except KeyboardInterrupt:
                proc.terminate()
                try:
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()
                status['status'] = 'interrupted'
                rc = 130
        if status['status'] != 'interrupted':
            status['status'] = 'completed' if rc == 0 else 'failed'
    except OSError as exc:
        status.update(status='failed', error=str(exc))
    finally:
        status.update(finished_at=now(), exit_code=rc)
        # Detect changes during execution too; the executed process may import unsnapshotted helpers.
        status['post_run_integrity_errors'] = verify_run_inputs(root, run)
        if status['post_run_integrity_errors'] and status['status'] == 'completed':
            status['status'] = 'completed-with-input-drift'
            rc = 2
            status['exit_code'] = rc
        write_json(run / 'status.json', status)
    print(json.dumps({'run_id': rid, 'status': status['status'], 'exit_code': rc, 'logs': logical(root, run)}, indent=2))
    return rc if 0 <= rc <= 255 else 1


def timing_errors(path: Path) -> list[str]:
    needed = ('training_cutoff', 'available_at', 'score_date', 'outcome_start', 'outcome_end')
    errors = []
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or not set(needed).issubset(reader.fieldnames):
            return ['CSV requires columns: ' + ', '.join(needed)]
        count = 0
        for line, row in enumerate(reader, 2):
            count += 1
            try:
                # Accept date-only data, requiring exact ISO syntax on Python versions that accept compact forms.
                if any(not re.fullmatch(r'\d{4}-\d{2}-\d{2}', row.get(k) or '') for k in needed):
                    raise ValueError('dates must be YYYY-MM-DD')
                d = {k: date.fromisoformat(row[k]) for k in needed}
                if d['training_cutoff'] > d['score_date']:
                    errors.append(f'Row {line}: future training information.')
                if d['available_at'] > d['score_date']:
                    errors.append(f'Row {line}: data unavailable at score date.')
                if not d['score_date'] < d['outcome_start'] <= d['outcome_end']:
                    errors.append(f'Row {line}: outcome must begin after the score and end on/after its start.')
            except (ValueError, TypeError) as exc:
                errors.append(f'Row {line}: unknown/invalid timing ({exc}).')
        if not count:
            errors.append('No observations to audit.')
    return errors


def check_paper(root: Path, p: Path) -> list[str]:
    errors = []
    state = read_json(p / 'state.json')
    if not state.get('authoritative_manuscript'):
        errors.append('Authoritative manuscript is not designated.')
    else:
        try:
            if not contained(root, state['authoritative_manuscript']).is_file():
                errors.append('Designated manuscript is missing on this device.')
        except WorkflowError as exc:
            errors.append(str(exc))
    for entry in read_json(p / 'artifacts.json'):
        path = contained(root, entry['path'])
        if not path.is_file():
            errors.append(f"Artifact {entry['id']}: missing private/local output.")
        elif digest(path) != entry['sha256']:
            errors.append(f"Artifact {entry['id']}: checksum mismatch.")
    for status_path in sorted((p / 'runs').glob('*/status.json')):
        s = read_json(status_path)
        if s['status'] == 'running':
            errors.append(f'{status_path.parent.name}: recorded running; process liveness is unverified.')
        if s.get('post_run_integrity_errors'):
            errors.append(f'{status_path.parent.name}: input/code changed during execution.')
    return errors


def context(root: Path, p: Path) -> str:
    s = read_json(p / 'state.json')
    lines = [f"# {s['title']} ({p.name})", f"Stage: {s['stage']} | Track: {s['track']}",
             'Preferences: profiles/researcher.md', 'Track protocol: ' + s['track_protocol'],
             'Authoritative manuscript: ' + str(s.get('authoritative_manuscript') or 'not designated'),
             '\n## Current task (recorded context; current instructions prevail)',
             json.dumps(s.get('current_task'), ensure_ascii=False, indent=2),
             '\n## Verified findings', json.dumps(s.get('verified_findings', []), ensure_ascii=False, indent=2),
             '\n## Open questions', json.dumps(s.get('open_questions', []), ensure_ascii=False, indent=2),
             '\n## Recent decisions (full history in research/decisions.jsonl)']
    for r in records(p / 'research/decisions.jsonl')[-8:]:
        lines.append(f"- {r['id']} [{r['kind']}] {r['text']} (source: {r['source']})")
    lines.append('\n## Indexed artifacts')
    for a in read_json(p / 'artifacts.json'):
        present = contained(root, a['path']).is_file()
        lines.append(f"- {a['id']} → {a['path']} | run {a['run_id']} | {'present' if present else 'missing on this device'}")
    lines.append('\n## Local run records (excluded from Git)')
    for status_path in sorted((p / 'runs').glob('*/status.json')):
        lines.append(f"- {status_path.parent.name}: {read_json(status_path)['status']} (not a liveness check)")
    local = root / '.local/machine.json'
    data_root = read_json(local).get('data_root') if local.exists() else None
    lines.extend(['\n## Required private inputs', f"Local data root: {'configured' if data_root else 'not configured'}"])
    for inp in s.get('required_private_inputs', []):
        # State contains relative logical inputs, never resolve escape paths outside configured root.
        rel = inp if isinstance(inp, str) else inp['path']
        exists = bool(data_root and contained(Path(data_root), rel).is_file())
        lines.append(f"- {rel}: {'present' if exists else 'not found/configured'}")
    lines.extend(['\n## Next action', s.get('next_action') or 'not recorded',
                  '\nRead actual source artifacts before treating a historical report as verified.'])
    return '\n'.join(lines) + '\n'


def validate_repo() -> list[str]:
    errors = []
    for req in ['AGENTS.md', 'profiles/researcher.md', 'templates/paper/configs/experiment.json', 'docs/skills.md']:
        if not (SOURCE / req).is_file():
            errors.append('Missing: ' + req)
    skills = list((SOURCE / '.agents/skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No research skills found.')
    names = set()
    for sk in skills:
        text = sk.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f'{sk.parent.name}: missing YAML frontmatter')
            continue
        fields = dict(line.split(':', 1) for line in parts[1].splitlines() if ':' in line)
        name = fields.get('name', '').strip()
        if name != sk.parent.name or not SLUG.fullmatch(name) or name in names:
            errors.append(f'{sk.parent.name}: invalid/duplicate skill name')
        names.add(name)
        if not fields.get('description', '').strip():
            errors.append(f'{name}: missing description')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if not target.startswith(('https://', 'http://', '#')) and not (sk.parent / target).is_file():
                errors.append(f'{name}: broken reference {target}')
    return errors


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('doctor')
    sub.add_parser('validate')
    configure = sub.add_parser('configure')
    configure.add_argument('--data-root', required=True)
    new = sub.add_parser('new')
    new.add_argument('paper')
    new.add_argument('--title', required=True)
    new.add_argument('--track', choices=('embeddings', 'ai-trading', 'general'), default='embeddings')
    for name in ['context', 'check']:
        sub.add_parser(name).add_argument('paper')
    task = sub.add_parser('task')
    task.add_argument('paper')
    task.add_argument('--mode', choices=MODES, required=True)
    task.add_argument('--request', required=True)
    task.add_argument('--stop-after', default='Complete the current request; no extra scope inferred.')
    dec = sub.add_parser('decision')
    dec.add_argument('paper')
    dec.add_argument('--text', required=True)
    dec.add_argument('--source', required=True)
    dec.add_argument('--kind', choices=('user-decision', 'assistant-suggestion', 'verified-evidence', 'historical-report'), default='user-decision')
    prep = sub.add_parser('prepare-run')
    prep.add_argument('paper')
    prep.add_argument('--config', required=True)
    prep.add_argument('--input', action='append', default=[])
    prep.add_argument('--script', action='append', default=[])
    run = sub.add_parser('run')
    run.add_argument('paper')
    run.add_argument('--run-id', required=True)
    # parse_known_args below preserves an explicit separator and command options.
    artifact = sub.add_parser('artifact')
    artifact.add_argument('paper')
    for key in ('id', 'run-id', 'path', 'kind', 'label'):
        artifact.add_argument('--' + key, required=True)
    sub.add_parser('audit-timing').add_argument('csv')
    sub.add_parser('demo')
    return ap


def main(argv: list[str] | None = None, root: Path | None = None) -> int:
    root = (root or SOURCE).resolve()
    args_list = list(sys.argv[1:] if argv is None else argv)
    command = []
    if args_list and args_list[0] == 'run' and '--' in args_list:
        sep = args_list.index('--')
        command = args_list[sep + 1:]
        args_list = args_list[:sep]
    args = build_parser().parse_args(args_list)
    try:
        if args.cmd == 'new':
            print(create_paper(root, args.paper, args.title, args.track).relative_to(root).as_posix())
        elif args.cmd == 'configure':
            loc = Path(args.data_root).expanduser().resolve()
            if not loc.is_dir():
                raise WorkflowError('Private-data root must already exist; no directory was created.')
            write_json(root / '.local/machine.json', {'data_root': str(loc), 'configured_at': now()})
            print('Saved machine-local data root; excluded from Git.')
        elif args.cmd in {'validate', 'doctor'}:
            errors = validate_repo()
            if args.cmd == 'doctor':
                print(json.dumps({'python': platform.python_version(), 'platform': platform.system(),
                                  'optional_tools': {k: bool(shutil.which(k)) for k in ('git', 'Rscript', 'stata', 'pdflatex', 'xelatex', 'latexmk')},
                                  'local_data_root_configured': (root / '.local/machine.json').is_file(),
                                  'skills': len(list((SOURCE / '.agents/skills').glob('*/SKILL.md'))),
                                  'database_access': 'not checked', 'issues': errors}, indent=2))
            else:
                print('\n'.join(errors) if errors else 'Repository structure and skills: OK')
            return int(bool(errors))
        elif args.cmd == 'audit-timing':
            errors = timing_errors(resolve_input(root, args.csv))
            print('\n'.join(errors) if errors else 'Declared date ordering: OK (not proof of no leakage).')
            return int(bool(errors))
        elif args.cmd == 'demo':
            from workflow.demo import run_demo
            print(json.dumps(run_demo(root / '.local/demo'), indent=2))
        else:
            p = paper(root, args.paper)
            if args.cmd == 'context':
                print(context(root, p), end='')
            elif args.cmd == 'check':
                errors = check_paper(root, p)
                print('\n'.join(errors) if errors else 'Recorded artifacts and designated source: OK (scientific validity not established).')
                return int(bool(errors))
            elif args.cmd == 'task':
                state = read_json(p / 'state.json')
                if state.get('current_task'):
                    append_record(p / 'research/task-history.jsonl', state['current_task'])
                state['current_task'] = {'id': identifier('task'), 'mode': args.mode, 'request': args.request,
                                         'stop_after': args.stop_after, 'recorded_at': now(),
                                         'source': 'Recorded from current request; verify against live user instructions.'}
                state['updated_at'] = now()
                write_json(p / 'state.json', state)
                print(state['current_task']['id'])
            elif args.cmd == 'decision':
                rec = {'id': identifier('decision'), 'recorded_at': now(), 'kind': args.kind,
                       'text': args.text, 'source': args.source}
                append_record(p / 'research/decisions.jsonl', rec)
                print(rec['id'])
            elif args.cmd == 'prepare-run':
                print(prepare_run(root, p, args.config, args.input, args.script)['run_id'])
            elif args.cmd == 'run':
                return execute_run(root, p, args.run_id, command)
            elif args.cmd == 'artifact':
                safe_id(args.id)
                run = load_run(p, args.run_id)
                if read_json(run / 'status.json')['status'] != 'completed':
                    raise WorkflowError('Index artifacts only from a completed, integrity-checked run.')
                path = contained(root, args.path)
                if not path.is_file():
                    raise WorkflowError('Cannot index a missing output.')
                index = read_json(p / 'artifacts.json')
                if any(a['id'] == args.id for a in index):
                    raise WorkflowError('Artifact ID already exists; preserve it and register a new version ID.')
                index.append({'id': args.id, 'run_id': args.run_id, 'kind': args.kind, 'manuscript_label': args.label,
                              'recorded_at': now(), **file_record(root, path)})
                write_json(p / 'artifacts.json', index)
                print(args.id)
        return 0
    except (WorkflowError, OSError, ValueError, KeyError, TypeError) as exc:
        print('Workflow: ' + str(exc), file=sys.stderr)
        return 2

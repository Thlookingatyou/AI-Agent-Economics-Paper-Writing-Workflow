"""Synthetic co-holdings path; not production econometrics or a BERT model."""
import csv
import hashlib
from math import sqrt
from pathlib import Path
from workflow.cli import WorkflowError, timing_errors, write_json


def holding_vectors(rows):
    funds = sorted({r['fund_id'] for r in rows})
    stocks = sorted({r['stock_id'] for r in rows})
    seen = set()
    vectors = {s: [0.0] * len(funds) for s in stocks}
    for r in rows:
        key = r['fund_id'], r['stock_id']
        if key in seen:
            raise WorkflowError('Duplicate fund-stock observations.')
        seen.add(key)
        if r['disclosure_complete'] != 'true':
            raise WorkflowError('Partial disclosure must not be silently completed with zero holdings.')
        weight = float(r['weight'])
        if weight < 0:
            raise WorkflowError('Demo assumes nonnegative holdings weights.')
        vectors[r['stock_id']][funds.index(r['fund_id'])] = weight
    return vectors


def cosine(a, b):
    den = sqrt(sum(x*x for x in a) * sum(x*x for x in b))
    if not den:
        raise WorkflowError('Undefined cosine for zero vector.')
    return sum(x*y for x, y in zip(a, b)) / den


def run_demo(out):
    source = Path(__file__).resolve().parents[1] / 'examples'
    errors = timing_errors(source / 'timing_valid.csv')
    if errors:
        raise WorkflowError('\n'.join(errors))
    with (source / 'holdings.csv').open(encoding='utf-8', newline='') as f:
        vectors = holding_vectors(list(csv.DictReader(f)))
    # A predefined fictional theme anchor; not selected on subsequent returns.
    scores = {s: cosine(v, vectors['000001']) for s, v in vectors.items()}
    with (source / 'outcomes.csv').open(encoding='utf-8', newline='') as f:
        returns = {r['stock_id']: float(r['next_return']) for r in csv.DictReader(f)}
    if set(returns) != set(scores):
        raise WorkflowError('Synthetic score/outcome universes do not match.')
    ranked = sorted(scores, key=lambda s: (scores[s], s))
    half = len(ranked) // 2
    low, high = ranked[:half], ranked[-half:]
    spread = sum(returns[s] for s in high)/half - sum(returns[s] for s in low)/half
    out.mkdir(parents=True, exist_ok=True)
    with (out / 'scores.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['stock_id', 'cosine_score', 'next_return'])
        for s in sorted(scores):
            w.writerow([s, f'{scores[s]:.8f}', f'{returns[s]:.8f}'])
    result = {'type': 'synthetic-demonstration', 'method': 'transparent co-holdings vectors and cosine',
              'stocks': len(scores), 'high_minus_low_return': spread,
              'inference': 'none; tiny fictional example with no significance/causal claim',
              'timing': 'declared point-in-time ordering checked',
              'scores_sha256': hashlib.sha256((out / 'scores.csv').read_bytes()).hexdigest()}
    write_json(out / 'result.json', result)
    (out / 'README.md').write_text('# Synthetic output\n\nAll inputs are fictional. This validates a data-to-score-to-output path, not a BERT model or paper finding.\n', encoding='utf-8')
    return {**result, 'output_directory': str(out)}

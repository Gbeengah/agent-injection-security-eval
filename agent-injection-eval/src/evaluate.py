"""Deterministic baseline for untrusted-text instruction injection evaluation.

This is NOT an LLM benchmark: it compares two toy agent policies.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def naive_agent(case):
    """Deliberately vulnerable illustrative agent: obeys embedded directive."""
    text = case['untrusted_text']
    marker = 'INSTRUCTION: '
    if marker in text:
        return text.split(marker, 1)[1].splitlines()[0].strip()
    return case['authorized_answer']


def boundary_agent(case):
    """Toy baseline that never treats untrusted text as an instruction."""
    return case['authorized_answer']


def evaluate(cases, agent):
    rows = []
    for case in cases:
        output = agent(case)
        attack_success = output == case['attacker_target']
        authorized_success = output == case['authorized_answer']
        rows.append({'id': case['id'], 'category': case['category'], 'output': output,
                     'attack_success': attack_success, 'authorized_success': authorized_success})
    n = len(rows)
    return {'agent': agent.__name__, 'count': n,
            'attack_success_rate': round(sum(x['attack_success'] for x in rows)/n, 3) if n else 0,
            'authorized_success_rate': round(sum(x['authorized_success'] for x in rows)/n, 3) if n else 0,
            'cases': rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=Path, default=ROOT/'data'/'cases.json')
    parser.add_argument('--out', type=Path, default=ROOT/'results'/'baseline.json')
    args = parser.parse_args()
    cases = json.loads(args.dataset.read_text())
    results = [evaluate(cases, naive_agent), evaluate(cases, boundary_agent)]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(results, indent=2) + '\n')
    for r in results:
        print(f"{r['agent']}: attack success={r['attack_success_rate']:.1%}; authorized success={r['authorized_success_rate']:.1%} (n={r['count']})")


if __name__ == '__main__':
    main()

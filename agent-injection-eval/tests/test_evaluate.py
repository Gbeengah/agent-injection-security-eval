import json
import unittest
from pathlib import Path
from src.evaluate import evaluate, naive_agent, boundary_agent

ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT/'data'/'cases.json').read_text())

class EvaluationTests(unittest.TestCase):
    def test_dataset_has_distinct_targets(self):
        self.assertTrue(all(c['authorized_answer'] != c['attacker_target'] for c in CASES))
    def test_naive_is_vulnerable_on_fixture(self):
        self.assertEqual(evaluate(CASES, naive_agent)['attack_success_rate'], 1.0)
    def test_boundary_agent_resists_fixture(self):
        self.assertEqual(evaluate(CASES, boundary_agent)['attack_success_rate'], 0.0)
    def test_empty_dataset(self):
        self.assertEqual(evaluate([], boundary_agent)['attack_success_rate'], 0)

if __name__ == '__main__':
    unittest.main()

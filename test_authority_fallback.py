#!/usr/bin/env python3
import json
import unittest
from pathlib import Path
from authority import select_authority

ROOT = Path(__file__).resolve().parent

class AuthorityFallbackTests(unittest.TestCase):
    def test_lt02_historical_exact_is_not_labeled_censored(self):
        observations = json.loads((ROOT / "observations.json").read_text())
        exact = json.loads((ROOT / "exact_evidence.json").read_text())
        lt02 = next(x for x in observations if x["invocation_id"].startswith("LT02-"))
        result = select_authority(lt02, exact)
        self.assertEqual(result["kind"], "historical_record")
        self.assertTrue(result["historical_end_present"])

if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
import json
import unittest
from pathlib import Path
from validator import validate_fixture

ROOT = Path(__file__).resolve().parent
FIXTURES = json.loads((ROOT / "fixtures.json").read_text())

class FixtureTests(unittest.TestCase):
    def test_all_declared_fixtures(self):
        for fixture in FIXTURES:
            with self.subTest(fixture=fixture["id"]):
                expected_raise = fixture["expected"].get("raises")
                if expected_raise:
                    with self.assertRaisesRegex(ValueError, expected_raise):
                        validate_fixture(fixture)
                else:
                    result = validate_fixture(fixture)
                    self.assertIn(result["classification"], {
                        "VOLUNTARY_FINAL", "ABRUPT_NONFINAL",
                        "TOOLPATH_LOSS_CANDIDATE", "PLATFORM_RUNTIME_KILL_CANDIDATE", "UNKNOWN"
                    })

    def test_fixture_ids_unique(self):
        ids = [f["id"] for f in FIXTURES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_no_fixture_combines_invocations_as_success(self):
        for fixture in FIXTURES:
            rec = fixture["record"]
            if rec.get("cross_invocation_sum_seconds") is not None:
                result = validate_fixture(fixture)
                self.assertFalse(result["valid"])
                self.assertIn("CROSS_INVOCATION_SUM_FORBIDDEN", result["violations"])

if __name__ == "__main__":
    unittest.main(verbosity=2)

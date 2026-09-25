#!/usr/bin/env python3
import unittest
from scheduler_v2 import next_from_reference, verify_readback

class SchedulerV2Tests(unittest.TestCase):
    def test_end_commit_plus_180(self):
        result = next_from_reference("2026-09-25T03:12:33Z")
        self.assertEqual(result.isoformat(), "2026-09-25T03:15:33+00:00")

    def test_exact_readback(self):
        result = verify_readback("2026-09-25T03:12:33Z", "2026-09-25T12:15:33+09:00")
        self.assertTrue(result["exact_match"])
        self.assertEqual(result["delta_seconds"], 0)

    def test_bool_lead_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid lead_seconds"):
            next_from_reference("2026-09-25T03:12:33Z", True)

if __name__ == "__main__":
    unittest.main(verbosity=2)

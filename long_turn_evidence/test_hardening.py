#!/usr/bin/env python3
import unittest
from validator import validate

BASE = {"invocation_id":"x","automation_id":"a","start":{"id":1,"created_at":"2026-09-24T00:00:00Z"},"scheduler_mutation_count":0}

class HardeningTests(unittest.TestCase):
    def test_missing_created_at(self):
        r = dict(BASE); r["start"] = {"id":1}
        with self.assertRaisesRegex(ValueError, "start: missing created_at"): validate(r)
    def test_bool_marker_id_rejected(self):
        r = dict(BASE); r["start"] = {"id":True,"created_at":"2026-09-24T00:00:00Z"}
        with self.assertRaisesRegex(ValueError, "start: invalid marker id"): validate(r)
    def test_bool_mutation_count_rejected(self):
        r = dict(BASE); r["scheduler_mutation_count"] = True
        with self.assertRaisesRegex(ValueError, "invalid scheduler_mutation_count"): validate(r)
    def test_naive_timestamp_rejected(self):
        r = dict(BASE); r["start"] = {"id":1,"created_at":"2026-09-24T00:00:00"}
        with self.assertRaisesRegex(ValueError, "timezone-aware"): validate(r)
    def test_nonpositive_target_rejected(self):
        r = dict(BASE); r["target_seconds"] = 0
        with self.assertRaisesRegex(ValueError, "invalid target_seconds"): validate(r)

if __name__ == "__main__": unittest.main(verbosity=2)

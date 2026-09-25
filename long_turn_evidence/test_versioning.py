#!/usr/bin/env python3
import unittest
from versioning import normalize_record

class VersioningTests(unittest.TestCase):
    def test_missing_version_is_legacy_v1(self):
        record = {"invocation_id": "x"}
        normalized, version = normalize_record(record)
        self.assertEqual(version, 1)
        self.assertEqual(normalized, record)
        self.assertIsNot(normalized, record)

    def test_explicit_v1_and_v2(self):
        self.assertEqual(normalize_record({"evidence_version": 1})[1], 1)
        self.assertEqual(normalize_record({"evidence_version": 2})[1], 2)

    def test_bool_string_and_unsupported_rejected(self):
        for value, message in [(True, "invalid"), ("2", "invalid"), (0, "unsupported"), (3, "unsupported")]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, message):
                    normalize_record({"evidence_version": value})

    def test_forbidden_legacy_field_is_preserved(self):
        record = {"evidence_version": 2, "cross_invocation_sum_seconds": 950}
        normalized, _ = normalize_record(record)
        self.assertEqual(normalized["cross_invocation_sum_seconds"], 950)

if __name__ == "__main__":
    unittest.main(verbosity=2)

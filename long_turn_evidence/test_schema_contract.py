#!/usr/bin/env python3
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent

class SchemaContractTests(unittest.TestCase):
    def test_v2_delta_declares_supported_versions(self):
        schema = json.loads((ROOT / "schema_v2_delta.json").read_text())
        self.assertEqual(schema["properties"]["evidence_version"]["enum"], [1, 2])

    def test_v2_delta_keeps_deprecated_cross_invocation_shape_visible(self):
        schema = json.loads((ROOT / "schema_v2_delta.json").read_text())
        field = schema["properties"]["cross_invocation_sum_seconds"]
        self.assertEqual(field["type"], "integer")
        self.assertEqual(field["minimum"], 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)

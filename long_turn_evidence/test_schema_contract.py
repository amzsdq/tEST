#!/usr/bin/env python3
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class SchemaContractTests(unittest.TestCase):
 def test_main_schema_declares_supported_versions(self):
  s=json.loads((ROOT/"schema.json").read_text());self.assertEqual(s["properties"]["evidence_version"]["enum"],[1,2])
 def test_main_schema_keeps_deprecated_cross_invocation_shape_visible(self):
  f=json.loads((ROOT/"schema.json").read_text())["properties"]["cross_invocation_sum_seconds"];self.assertEqual(f["type"],"integer");self.assertEqual(f["minimum"],0)
 def test_exact_evidence_contract_requires_lineage_and_markers(self):
  s=json.loads((ROOT/"exact_evidence.schema.json").read_text());req=set(s["items"]["required"])
  self.assertTrue({"evidence_id","invocation_id","automation_id","source","supersedes_observation_invocation_id","start","end"}<=req)
if __name__=="__main__":unittest.main(verbosity=2)

#!/usr/bin/env python3
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class SchemaContractTests(unittest.TestCase):
 def test_main_schema_declares_supported_versions(self):
  s=json.loads((ROOT/"schema.json").read_text());self.assertEqual(s["properties"]["evidence_version"]["enum"],[1,2])
 def test_main_schema_keeps_deprecated_cross_invocation_shape_visible(self):
  f=json.loads((ROOT/"schema.json").read_text())["properties"]["cross_invocation_sum_seconds"];self.assertEqual(f["type"],"integer");self.assertEqual(f["minimum"],0)
 def test_identity_schemas_reject_whitespace_only(self):
  main=json.loads((ROOT/"schema.json").read_text())
  for key in ("invocation_id","automation_id"):
   self.assertEqual(main["properties"][key]["pattern"],".*\\S.*")
  exact=json.loads((ROOT/"exact_evidence.schema.json").read_text())
  for key in ("evidence_id","invocation_id","automation_id","supersedes_observation_invocation_id"):
   self.assertEqual(exact["items"]["properties"][key]["pattern"],".*\\S.*")
 def test_marker_timestamp_pattern_is_canonical_github_shape(self):
  expected=r"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
  self.assertEqual(json.loads((ROOT/"schema.json").read_text())["$defs"]["marker"]["properties"]["created_at"]["pattern"],expected)
  self.assertEqual(json.loads((ROOT/"exact_evidence.schema.json").read_text())["$defs"]["marker"]["properties"]["created_at"]["pattern"],expected)
 def test_exact_evidence_contract_requires_lineage_and_markers(self):
  s=json.loads((ROOT/"exact_evidence.schema.json").read_text());req=set(s["items"]["required"])
  self.assertTrue({"evidence_id","invocation_id","automation_id","source","supersedes_observation_invocation_id","start","end"}<=req)
 def test_exact_evidence_contract_closes_structural_fields(self):
  s=json.loads((ROOT/"exact_evidence.schema.json").read_text());item=s["items"];marker=s["$defs"]["marker"]
  self.assertFalse(item["additionalProperties"]);self.assertFalse(marker["additionalProperties"])
  self.assertEqual(item["properties"]["source"]["const"],"raw_github_start_end")
if __name__=="__main__":unittest.main(verbosity=2)

#!/usr/bin/env python3
import copy,json,unittest
from pathlib import Path
from versioning import normalize_record
from validator import validate
ROOT=Path(__file__).resolve().parent
BASE={"invocation_id":"v","automation_id":"a","start":{"id":1,"created_at":"2026-01-01T00:00:00Z"},"scheduler_mutation_count":0}
class VersioningTests(unittest.TestCase):
 def test_missing_version_is_legacy_v1(self):
  r={"invocation_id":"x"};n,v=normalize_record(r);self.assertEqual(v,1);self.assertEqual(n,r);self.assertIsNot(n,r)
 def test_explicit_v1_v2(self):
  self.assertEqual(normalize_record({"evidence_version":1})[1],1);self.assertEqual(normalize_record({"evidence_version":2})[1],2)
 def test_bad_versions(self):
  for value,msg in [(True,"invalid"),("2","invalid"),(0,"unsupported"),(3,"unsupported")]:
   with self.subTest(value=value),self.assertRaisesRegex(ValueError,msg):normalize_record({"evidence_version":value})
 def test_v2_s5_stays_forbidden(self):
  r=dict(BASE,evidence_version=2,cross_invocation_sum_seconds=950);n,_=normalize_record(r);self.assertEqual(n["cross_invocation_sum_seconds"],950)
  out=validate(r);self.assertFalse(out["valid"]);self.assertIn("CROSS_INVOCATION_SUM_FORBIDDEN",out["violations"])
 def test_validate_does_not_mutate_v2_input(self):
  r=dict(BASE,evidence_version=2);before=copy.deepcopy(r);validate(r);self.assertEqual(r,before)
 def test_v1_v2_output_shape_stable(self):
  legacy=validate(dict(BASE));v2=validate(dict(BASE,evidence_version=2));self.assertEqual(set(legacy),set(v2))
 def test_schema_contract(self):
  p=json.loads((ROOT/"schema.json").read_text())["properties"];self.assertEqual(p["evidence_version"]["enum"],[1,2]);self.assertIn("cross_invocation_sum_seconds",p)
if __name__=="__main__":unittest.main(verbosity=2)

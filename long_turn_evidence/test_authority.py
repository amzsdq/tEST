#!/usr/bin/env python3
import json,unittest
from pathlib import Path
from authority import select_authority
ROOT=Path(__file__).resolve().parent
OBS=json.loads((ROOT/"observations.json").read_text());EXACT=json.loads((ROOT/"exact_evidence.json").read_text())
LT03=next(x for x in OBS if x["invocation_id"]=="LT03-DETERMINISTIC-ARTIFACT-CONTEXT-VOLUME-01")
class AuthorityTests(unittest.TestCase):
 def test_exact_940_preferred_without_rewriting_history(self):
  self.assertIsNone(LT03["end"]);r=select_authority(LT03,EXACT);self.assertEqual(r["exact_duration_seconds"],940);self.assertTrue(r["target_crossed"])
 def test_start_mismatch_fails_closed(self):
  bad=[dict(EXACT[0],start={"id":999,"created_at":"2026-09-24T15:16:24Z"})]
  with self.assertRaisesRegex(ValueError,"EXACT_START_MISMATCH"):select_authority(LT03,bad)
 def test_automation_mismatch_fails_closed(self):
  with self.assertRaisesRegex(ValueError,"EXACT_AUTOMATION_MISMATCH"):select_authority(LT03,[dict(EXACT[0],automation_id="wrong")])
 def test_ambiguous_exact_fails_closed(self):
  with self.assertRaisesRegex(ValueError,"AMBIGUOUS_EXACT_AUTHORITY"):select_authority(LT03,EXACT+[dict(EXACT[0],evidence_id="duplicate")])
 def test_missing_end_fails_closed(self):
  bad=dict(EXACT[0]);bad.pop("end")
  with self.assertRaisesRegex(ValueError,"EXACT_END_INVALID"):select_authority(LT03,[bad])
 def test_bool_end_id_fails_closed(self):
  bad=[dict(EXACT[0],end={"id":True,"created_at":"2026-09-24T15:32:04Z"})]
  with self.assertRaisesRegex(ValueError,"EXACT_END_ID_INVALID"):select_authority(LT03,bad)
 def test_bool_target_fails_closed(self):
  with self.assertRaisesRegex(ValueError,"AUTHORITY_TARGET_INVALID"):select_authority(dict(LT03,target_seconds=True),EXACT)
 def test_runtime_identity_shapes_fail_closed(self):
  for value in (None,'','   ',True,7,{}):
   with self.subTest(side='observation_invocation',value=value):
    with self.assertRaises(ValueError):select_authority(dict(LT03,invocation_id=value),EXACT)
   with self.subTest(side='observation_automation',value=value):
    with self.assertRaises(ValueError):select_authority(dict(LT03,automation_id=value),EXACT)
   for key in ('supersedes_observation_invocation_id','invocation_id','automation_id'):
    with self.subTest(side=key,value=value):
     with self.assertRaises(ValueError):select_authority(LT03,[dict(EXACT[0],**{key:value})])
 def test_whitespace_evidence_id_fails_closed(self):
  with self.assertRaisesRegex(ValueError,"EXACT_EVIDENCE_ID_INVALID"):select_authority(LT03,[dict(EXACT[0],evidence_id="   ")])
 def test_unknown_marker_field_fails_closed(self):
  bad=dict(EXACT[0]);bad["end"]=dict(bad["end"],extra="x")
  with self.assertRaisesRegex(ValueError,"EXACT_END_FIELDS_INVALID"):select_authority(LT03,[bad])
 def test_unknown_exact_record_field_fails_closed(self):
  with self.assertRaisesRegex(ValueError,"EXACT_RECORD_FIELDS_INVALID"):select_authority(LT03,[dict(EXACT[0],extra="x")])
 def test_nonpositive_target_fails_closed(self):
  with self.assertRaisesRegex(ValueError,"AUTHORITY_TARGET_INVALID"):select_authority(dict(LT03,target_seconds=0),EXACT)
if __name__=="__main__":unittest.main(verbosity=2)

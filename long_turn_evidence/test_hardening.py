#!/usr/bin/env python3
import unittest
from validator import validate
BASE={"invocation_id":"x","automation_id":"a","start":{"id":1,"created_at":"2026-09-24T00:00:00Z"},"scheduler_mutation_count":0}
class HardeningTests(unittest.TestCase):
 def bad(self,patch,msg):
  r=dict(BASE);r.update(patch)
  with self.assertRaisesRegex(ValueError,msg):validate(r)
 def test_null_start_is_rejected_deterministically(self):self.bad({'start':None},'start: marker must be object')
 def test_whitespace_runtime_identities_fail_closed(self):
  for key in ("invocation_id","automation_id"):
   for value in (" ","   ","\t","\n"):
    with self.subTest(key=key,value=repr(value)):self.bad({key:value},f"invalid {key}")
 def test_unknown_marker_field_fails_closed(self):self.bad({"start":{"id":1,"created_at":"2026-09-24T00:00:00Z","extra":"x"}},"unexpected marker fields")
 def test_missing_created_at(self):self.bad({"start":{"id":1}},"start: missing created_at")
 def test_bool_marker_id(self):self.bad({"start":{"id":True,"created_at":"2026-09-24T00:00:00Z"}},"start: invalid marker id")
 def test_bool_mutation(self):self.bad({"scheduler_mutation_count":True},"invalid scheduler_mutation_count")
 def test_naive_timestamp(self):self.bad({"start":{"id":1,"created_at":"2026-09-24T00:00:00"}},"canonical UTC Z timestamp")
 def test_nonpositive_target(self):self.bad({"target_seconds":0},"invalid target_seconds")
 def test_string_false_not_boolean(self):self.bad({"finalization_signature":"false"},"invalid finalization_signature")
 def test_string_claim_bool(self):self.bad({"claimed_target_crossed":"true"},"invalid claimed_target_crossed")
 def test_string_claim_exact(self):self.bad({"claimed_exact_seconds":"900"},"invalid claimed_exact_seconds")
 def test_unknown_observation_state(self):self.bad({"observation_state":"probably_done"},"invalid observation_state")
 def test_unknown_termination_evidence(self):self.bad({"termination_evidence":"timeout_maybe"},"invalid termination_evidence")
 def test_active_with_end_contradiction(self):self.bad({"observation_state":"active","end":{"id":2,"created_at":"2026-09-24T00:01:00Z"}},"active observation cannot have END")
 def test_closed_without_end_contradiction(self):self.bad({"observation_state":"closed"},"closed observation requires END")
 def test_active_with_kill_evidence_contradiction(self):self.bad({"observation_state":"active","last_durable_boundary":{"id":2,"created_at":"2026-09-24T00:01:00Z"},"termination_evidence":"platform_runtime_kill"},"termination evidence contradicts")
 def test_active_censored_is_unknown(self):
  r=dict(BASE);r.update({"last_durable_boundary":{"id":2,"created_at":"2026-09-24T00:05:00Z"},"observation_state":"active"})
  x=validate(r);self.assertEqual(x["classification"],"UNKNOWN");self.assertEqual(x["censored_lower_bound_seconds"],300)

 def test_noncanonical_raw_marker_timestamps_fail_closed(self):
  for value in ("2026-09-24T00:00:00+00:00","2026-09-24T00:00:00.000Z","2026-W39-4T00:00:00Z","2026-09-24 00:00:00Z"):
   with self.subTest(value=value):self.bad({"start":{"id":1,"created_at":value}},"canonical UTC Z timestamp")
if __name__=="__main__":unittest.main(verbosity=2)
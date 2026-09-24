#!/usr/bin/env python3
import unittest
from validator import validate
BASE={"invocation_id":"x","automation_id":"a","start":{"id":1,"created_at":"2026-09-24T00:00:00Z"},"scheduler_mutation_count":0}
class HardeningTests(unittest.TestCase):
 def bad(self,patch,msg):
  r=dict(BASE);r.update(patch)
  with self.assertRaisesRegex(ValueError,msg):validate(r)
 def test_missing_created_at(self):self.bad({"start":{"id":1}},"start: missing created_at")
 def test_bool_marker_id(self):self.bad({"start":{"id":True,"created_at":"2026-09-24T00:00:00Z"}},"start: invalid marker id")
 def test_bool_mutation(self):self.bad({"scheduler_mutation_count":True},"invalid scheduler_mutation_count")
 def test_naive_timestamp(self):self.bad({"start":{"id":1,"created_at":"2026-09-24T00:00:00"}},"timezone-aware")
 def test_nonpositive_target(self):self.bad({"target_seconds":0},"invalid target_seconds")
 def test_string_false_not_boolean(self):self.bad({"finalization_signature":"false"},"invalid finalization_signature")
 def test_unknown_observation_state(self):self.bad({"observation_state":"probably_done"},"invalid observation_state")
 def test_unknown_termination_evidence(self):self.bad({"termination_evidence":"timeout_maybe"},"invalid termination_evidence")
 def test_active_censored_is_unknown(self):
  r=dict(BASE);r.update({"last_durable_boundary":{"id":2,"created_at":"2026-09-24T00:05:00Z"},"observation_state":"active"})
  x=validate(r);self.assertEqual(x["classification"],"UNKNOWN");self.assertEqual(x["censored_lower_bound_seconds"],300)
if __name__=="__main__":unittest.main(verbosity=2)

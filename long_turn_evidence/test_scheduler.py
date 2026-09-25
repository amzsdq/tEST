#!/usr/bin/env python3
import unittest
from scheduler import final_next_from_baton,verify_readback
class SchedulerTests(unittest.TestCase):
 def test_lt02_exact_target(self):
  x=final_next_from_baton('2026-09-24T15:11:48Z')
  self.assertEqual(x.isoformat(),'2026-09-24T15:14:48+00:00')
 def test_exact_readback(self):
  x=verify_readback('2026-09-24T15:11:48Z','2026-09-25T00:14:48+09:00')
  self.assertTrue(x['exact_match']);self.assertEqual(x['delta_seconds'],0)
 def test_mismatch_visible(self):
  x=verify_readback('2026-09-24T15:11:48Z','2026-09-25T00:14:49+09:00')
  self.assertFalse(x['exact_match']);self.assertEqual(x['delta_seconds'],1)
 def test_nonstring_timestamp_fails_deterministically(self):
  for value in (None,True,7,{},[]):
   with self.subTest(value=value):
    with self.assertRaisesRegex(ValueError,'timestamp must be non-empty string'):final_next_from_baton(value)
 def test_bad_lead(self):
  with self.assertRaisesRegex(ValueError,'invalid lead_seconds'):final_next_from_baton('2026-09-24T15:11:48Z',True)
if __name__=='__main__':unittest.main(verbosity=2)

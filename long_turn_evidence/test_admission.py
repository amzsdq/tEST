#!/usr/bin/env python3
import unittest
from admission import decide
class AdmissionTests(unittest.TestCase):
 def test_899_continue(self):self.assertEqual(decide(899)['state'],'CONTINUE')
 def test_900_reserve(self):self.assertEqual(decide(900)['state'],'RESERVE_ENTRY')
 def test_1200_still_reserve(self):self.assertEqual(decide(1200)['state'],'RESERVE_ENTRY')
 def test_no_work_does_not_pad(self):self.assertEqual(decide(500,qualifying_work=False)['state'],'WORKLOAD_EXHAUSTED')
 def test_target_crossed_but_finalization_unsafe(self):self.assertEqual(decide(900,finalization_safe=False)['state'],'FINALIZATION_BLOCKED')
 def test_bad_relationship(self):
  with self.assertRaisesRegex(ValueError,'target/stretch'):decide(1,target_seconds=900,stretch_seconds=899)
if __name__=='__main__':unittest.main(verbosity=2)

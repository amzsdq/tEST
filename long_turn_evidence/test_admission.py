#!/usr/bin/env python3
import unittest
from admission import decide

class AdmissionTests(unittest.TestCase):
 def test_899_qualifying_continues(self):self.assertEqual(decide(899)['state'],'CONTINUE')
 def test_899_no_work_exhausted(self):self.assertEqual(decide(899,qualifying_work=False)['state'],'WORKLOAD_EXHAUSTED')
 def test_900_qualifying_stretches(self):self.assertEqual(decide(900)['state'],'CONTINUE_STRETCH')
 def test_900_no_work_reserves(self):self.assertEqual(decide(900,qualifying_work=False)['state'],'RESERVE_ENTRY')
 def test_900_unsafe_blocks(self):self.assertEqual(decide(900,finalization_safe=False)['state'],'FINALIZATION_BLOCKED')
 def test_1199_qualifying_stretches(self):self.assertEqual(decide(1199)['state'],'CONTINUE_STRETCH')
 def test_1199_no_work_reserves(self):self.assertEqual(decide(1199,qualifying_work=False)['state'],'RESERVE_ENTRY')
 def test_1199_unsafe_blocks(self):self.assertEqual(decide(1199,finalization_safe=False)['state'],'FINALIZATION_BLOCKED')
 def test_1200_qualifying_reserves(self):self.assertEqual(decide(1200)['state'],'RESERVE_ENTRY')
 def test_1200_no_work_reserves(self):self.assertEqual(decide(1200,qualifying_work=False)['state'],'RESERVE_ENTRY')
 def test_1200_unsafe_blocks(self):self.assertEqual(decide(1200,finalization_safe=False)['state'],'FINALIZATION_BLOCKED')
 def test_custom_target_stretch_interval(self):
  self.assertEqual(decide(9,target_seconds=10,stretch_seconds=20)['state'],'CONTINUE')
  self.assertEqual(decide(10,target_seconds=10,stretch_seconds=20)['state'],'CONTINUE_STRETCH')
  self.assertEqual(decide(19,target_seconds=10,stretch_seconds=20)['state'],'CONTINUE_STRETCH')
  self.assertEqual(decide(20,target_seconds=10,stretch_seconds=20)['state'],'RESERVE_ENTRY')
 def test_equal_target_and_stretch_has_no_stretch_interval(self):
  self.assertEqual(decide(10,target_seconds=10,stretch_seconds=10)['state'],'RESERVE_ENTRY')
 def test_bad_relationship(self):
  with self.assertRaisesRegex(ValueError,'target/stretch'):decide(1,target_seconds=900,stretch_seconds=899)
 def test_zero_target_rejected(self):
  with self.assertRaisesRegex(ValueError,'target/stretch'):decide(1,target_seconds=0)
 def test_bool_integer_inputs_rejected(self):
  for kw in ({'elapsed_server_seconds':True},{'target_seconds':True},{'stretch_seconds':True}):
   args={'elapsed_server_seconds':1};args.update(kw)
   with self.subTest(kw=kw),self.assertRaisesRegex(ValueError,'invalid'):decide(**args)
 def test_string_qualifying_gate_rejected(self):
  with self.assertRaisesRegex(ValueError,'invalid qualifying_work'):decide(1,qualifying_work='false')
 def test_string_finalization_gate_rejected(self):
  with self.assertRaisesRegex(ValueError,'invalid finalization_safe'):decide(900,finalization_safe='false')

if __name__=='__main__':unittest.main(verbosity=2)

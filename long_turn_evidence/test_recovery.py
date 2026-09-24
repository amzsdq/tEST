#!/usr/bin/env python3
import unittest
from recovery import decide
R={'automation_id':'A','start':{'id':1},'end':None,'last_durable_boundary':{'id':2}};L={'automation_id':'A','enabled':True,'rrule':'FREQ=HOURLY'}
class RecoveryTests(unittest.TestCase):
 def test_resume_censored(self):self.assertEqual(decide(R,L)['action'],'RESUME_CENSORED')
 def test_verified_finalized_not_resumed(self):
  r=dict(R);r.update({'end':{'id':3},'end_verified':True});self.assertEqual(decide(r,L)['action'],'DO_NOT_RESUME_FINALIZED')
 def test_unverified_end_reconstructs(self):
  r=dict(R);r['end']={'id':3};self.assertEqual(decide(r,L)['action'],'RECONSTRUCT_BEFORE_RESUME')
 def test_identity_mismatch(self):
  l=dict(L);l['automation_id']='B';self.assertEqual(decide(R,l)['action'],'AUTHORITY_BLOCK')
 def test_disabled_fallback(self):
  l=dict(L);l['enabled']=False;self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_rrule_changed(self):
  l=dict(L);l['rrule']='FREQ=DAILY';self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_no_boundary_reconstructs(self):
  r=dict(R);r['last_durable_boundary']=None;self.assertEqual(decide(r,L)['action'],'RECONSTRUCT_BEFORE_RESUME')
if __name__=='__main__':unittest.main(verbosity=2)

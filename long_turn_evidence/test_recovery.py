#!/usr/bin/env python3
import unittest
from recovery import decide
R={'automation_id':'A','start':{'id':1},'start_verified':True,'end':None,'last_durable_boundary':{'id':2}};L={'automation_id':'A','enabled':True,'timing_mode':'exact_schedule','rrule':'FREQ=HOURLY'}
class RecoveryTests(unittest.TestCase):
 def test_resume_censored(self):self.assertEqual(decide(R,L)['action'],'RESUME_CENSORED')
 def test_unverified_start_requires_verification(self):
  r=dict(R);r['start_verified']=False;self.assertEqual(decide(r,L)['action'],'VERIFY_START_BEFORE_RESUME')
 def test_missing_start_verification_requires_verification(self):
  r=dict(R);r.pop('start_verified');self.assertEqual(decide(r,L)['action'],'VERIFY_START_BEFORE_RESUME')
 def test_missing_start_object_is_invalid(self):
  r=dict(R);r.pop('start');self.assertEqual(decide(r,L)['action'],'INVALID_SESSION')
 def test_malformed_start_object_is_invalid(self):
  r=dict(R);r['start']='start';self.assertEqual(decide(r,L)['action'],'INVALID_SESSION')
 def test_malformed_boundary_reconstructs(self):
  r=dict(R);r['last_durable_boundary']='boundary';self.assertEqual(decide(r,L)['action'],'RECONSTRUCT_BEFORE_RESUME')
 def test_nonmapping_record_is_invalid(self):self.assertEqual(decide([],L)['action'],'INVALID_SESSION')
 def test_nonmapping_live_is_invalid(self):self.assertEqual(decide(R,[])['action'],'INVALID_SESSION')
 def test_verified_finalized_not_resumed(self):
  r=dict(R);r.update({'end':{'id':3},'end_verified':True});self.assertEqual(decide(r,L)['action'],'DO_NOT_RESUME_FINALIZED')
 def test_malformed_end_reconstructs(self):
  r=dict(R);r['end']='end';r['end_verified']=True;self.assertEqual(decide(r,L)['action'],'RECONSTRUCT_BEFORE_RESUME')
 def test_unverified_end_reconstructs(self):
  r=dict(R);r['end']={'id':3};self.assertEqual(decide(r,L)['action'],'RECONSTRUCT_BEFORE_RESUME')
 def test_identity_mismatch(self):
  l=dict(L);l['automation_id']='B';self.assertEqual(decide(R,l)['action'],'AUTHORITY_BLOCK')
 def test_disabled_fallback(self):
  l=dict(L);l['enabled']=False;self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_rrule_changed(self):
  l=dict(L);l['rrule']='FREQ=DAILY';self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_missing_timing_mode(self):
  l=dict(L);l.pop('timing_mode');self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_flexible_timing_mode(self):
  l=dict(L);l['timing_mode']='flexible_schedule';self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_parameterized_hourly_rejected(self):
  l=dict(L);l['rrule']='FREQ=HOURLY;COUNT=3';self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_full_vevent_schedule_accepted(self):
  l={'automation_id':'A','enabled':True,'timing_mode':'exact_schedule','schedule':'BEGIN:VEVENT\nDTSTART:20260925T120000Z\nRRULE:FREQ=HOURLY\nEND:VEVENT'};self.assertEqual(decide(R,l)['action'],'RESUME_CENSORED')
 def test_floating_dtstart_rejected(self):
  l={'automation_id':'A','enabled':True,'timing_mode':'exact_schedule','schedule':'BEGIN:VEVENT\nDTSTART:20260925T120000\nRRULE:FREQ=HOURLY\nEND:VEVENT'};self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_schedule_fragment_rejected(self):
  l={'automation_id':'A','enabled':True,'timing_mode':'exact_schedule','schedule':'RRULE:FREQ=HOURLY'};self.assertEqual(decide(R,l)['action'],'RECURRENCE_DEGRADED')
 def test_no_boundary_reconstructs(self):
  r=dict(R);r['last_durable_boundary']=None;self.assertEqual(decide(r,L)['action'],'RECONSTRUCT_BEFORE_RESUME')
if __name__=='__main__':unittest.main(verbosity=2)

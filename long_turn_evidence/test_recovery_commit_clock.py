#!/usr/bin/env python3
import unittest
from recovery_commit_clock import decide
SESSION={"automation_id":"A","start_commit":"start","start_verified":True,"end_commit":None}
LIVE={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","rrule":"FREQ=HOURLY"}
class CommitClockRecoveryTests(unittest.TestCase):
 def test_open_session_resumes(self):self.assertEqual(decide(SESSION,LIVE)["action"],"RESUME_OPEN_SESSION")
 def test_schedule_without_dtstart_is_rejected(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":"BEGIN:VEVENT\nRRULE:FREQ=HOURLY\nEND:VEVENT"};self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
 def test_nested_vevent_is_rejected(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":"BEGIN:VEVENT\nBEGIN:VEVENT\nDTSTART:20260925T120000Z\nRRULE:FREQ=HOURLY\nEND:VEVENT\nEND:VEVENT"};self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
 def test_unexpected_schedule_content_is_rejected(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":"BEGIN:VEVENT\nJUNK:X\nDTSTART:20260925T120000Z\nRRULE:FREQ=HOURLY\nEND:VEVENT"};self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
 def test_full_vevent_schedule_is_accepted(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":"BEGIN:VEVENT\nDTSTART:20260925T120000Z\nRRULE:FREQ=HOURLY\nEND:VEVENT"};self.assertEqual(decide(SESSION,live)["action"],"RESUME_OPEN_SESSION")
 def test_floating_dtstart_is_rejected(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":"BEGIN:VEVENT\nDTSTART:20260925T120000\nRRULE:FREQ=HOURLY\nEND:VEVENT"};self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
 def test_parameterized_rrule_is_rejected_for_canonical_liveness(self):
  for rrule in ("FREQ=HOURLY;COUNT=3","FREQ=HOURLY;UNTIL=20260926T000000Z","FREQ=HOURLY;INTERVAL=2"):
   with self.subTest(rrule=rrule):self.assertEqual(decide(SESSION,{"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","rrule":rrule})["action"],"RECURRENCE_DEGRADED")
 def test_hourly_prefix_spoof_is_rejected(self):
  for schedule in ("BEGIN:VEVENT\nRRULE:FREQ=HOURLYEVIL\nEND:VEVENT","BEGIN:VEVENT\nRRULE:FREQ=HOURLYTHING;COUNT=3\nEND:VEVENT"):
   with self.subTest(schedule=schedule):self.assertEqual(decide(SESSION,{"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":schedule})["action"],"RECURRENCE_DEGRADED")
 def test_duplicate_conflicting_freq_is_rejected(self):
  for rrule in ("FREQ=HOURLY;FREQ=DAILY","FREQ=HOURLY;COUNT=3;FREQ=HOURLY"):
   with self.subTest(rrule=rrule):self.assertEqual(decide(SESSION,{"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","rrule":rrule})["action"],"RECURRENCE_DEGRADED")
 def test_duplicate_nonfreq_key_is_rejected(self):
  rrule="FREQ=HOURLY;COUNT=3;COUNT=4"
  self.assertEqual(decide(SESSION,{"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","rrule":rrule})["action"],"RECURRENCE_DEGRADED")
 def test_multiple_rrule_lines_are_rejected(self):
  schedule="BEGIN:VEVENT\nRRULE:FREQ=HOURLY\nRRULE:FREQ=DAILY\nEND:VEVENT"
  self.assertEqual(decide(SESSION,{"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":schedule})["action"],"RECURRENCE_DEGRADED")
 def test_conflicting_rrule_representations_are_rejected(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","rrule":"FREQ=HOURLY","schedule":"BEGIN:VEVENT\nRRULE:FREQ=DAILY\nEND:VEVENT"}
  self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
 def test_nonexact_timing_mode_degrades(self):
  self.assertEqual(decide(SESSION,dict(LIVE,timing_mode="flexible_schedule"))["action"],"RECURRENCE_DEGRADED")
 def test_missing_timing_mode_degrades(self):
  live=dict(LIVE);live.pop("timing_mode");self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
 def test_schedule_fragment_without_vevent_envelope_is_rejected(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":"RRULE:FREQ=HOURLY"}
  self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
 def test_unverified_start_requires_verification(self):self.assertEqual(decide(dict(SESSION,start_verified=False),LIVE)["action"],"VERIFY_START_BEFORE_RESUME")
 def test_verified_end_is_final(self):self.assertEqual(decide(dict(SESSION,end_commit="end",end_verified=True),LIVE)["action"],"DO_NOT_RESUME_FINALIZED")
 def test_unverified_end_requires_verification(self):self.assertEqual(decide(dict(SESSION,end_commit="end"),LIVE)["action"],"VERIFY_END_BEFORE_RESUME")
 def test_missing_start_is_invalid(self):self.assertEqual(decide(dict(SESSION,start_commit=None),LIVE)["action"],"INVALID_SESSION")
 def test_malformed_start_commit_is_invalid(self):
  for value in ({"sha":"x"}, [], True, 7, "   "):
   with self.subTest(value=value):self.assertEqual(decide(dict(SESSION,start_commit=value),LIVE)["action"],"INVALID_SESSION")
 def test_malformed_end_commit_requires_verification(self):
  for value in ({"sha":"x"}, [], True, 7, "   "):
   with self.subTest(value=value):self.assertEqual(decide(dict(SESSION,end_commit=value,end_verified=True),LIVE)["action"],"VERIFY_END_BEFORE_RESUME")
 def test_nonmapping_containers_are_invalid(self):
  self.assertEqual(decide([],LIVE)["action"],"INVALID_SESSION")
  self.assertEqual(decide(SESSION,[])["action"],"INVALID_SESSION")
 def test_missing_or_malformed_automation_identity_is_invalid(self):
  for value in (None, "", "   ", True, 7, {}):
   with self.subTest(side="session",value=value):
    self.assertEqual(decide(dict(SESSION,automation_id=value),LIVE)["action"],"INVALID_SESSION")
   with self.subTest(side="live",value=value):
    self.assertEqual(decide(SESSION,dict(LIVE,automation_id=value))["action"],"INVALID_SESSION")
 def test_identity_mismatch_blocks(self):self.assertEqual(decide(SESSION,dict(LIVE,automation_id="B"))["action"],"AUTHORITY_BLOCK")
 def test_nonhourly_schedule_degrades(self):
  live={"automation_id":"A","enabled":True,"timing_mode":"exact_schedule","schedule":"BEGIN:VEVENT\nRRULE:FREQ=DAILY\nEND:VEVENT"};self.assertEqual(decide(SESSION,live)["action"],"RECURRENCE_DEGRADED")
if __name__=="__main__":unittest.main(verbosity=2)

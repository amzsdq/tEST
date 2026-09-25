#!/usr/bin/env python3
import unittest
from scheduler_v2 import next_from_reference,verify_readback,parse_github_commit_created_at
class SchedulerV2Tests(unittest.TestCase):
 def test_end_commit_plus_180(self):
  self.assertEqual(next_from_reference("2026-09-25T03:17:24Z").isoformat(),"2026-09-25T03:20:24+00:00")
 def test_iso_exact_readback(self):
  r=verify_readback("2026-09-25T03:17:24Z","2026-09-25T12:20:24+09:00");self.assertTrue(r["exact_match"]);self.assertEqual(r["delta_seconds"],0)
 def test_vevent_tzid_exact_readback(self):
  live="BEGIN:VEVENT\nDTSTART;TZID=Asia/Seoul:20260925T122024\nRRULE:FREQ=HOURLY\nEND:VEVENT";self.assertTrue(verify_readback("2026-09-25T03:17:24Z",live)["exact_match"])
 def test_vevent_z_exact_readback(self):
  live="BEGIN:VEVENT\nDTSTART:20260925T032024Z\nRRULE:FREQ=HOURLY\nEND:VEVENT";self.assertTrue(verify_readback("2026-09-25T03:17:24Z",live)["exact_match"])
 def test_junk_before_dtstart_rejected(self):
  live="junk\nDTSTART:20260925T032024Z"
  with self.assertRaisesRegex(ValueError,"VEVENT envelope"):verify_readback("2026-09-25T03:17:24Z",live)
 def test_junk_inside_vevent_rejected(self):
  live="BEGIN:VEVENT\nJUNK:X\nDTSTART:20260925T032024Z\nRRULE:FREQ=HOURLY\nEND:VEVENT"
  with self.assertRaisesRegex(ValueError,"unexpected live schedule content"):verify_readback("2026-09-25T03:17:24Z",live)
 def test_nested_vevent_rejected(self):
  live="BEGIN:VEVENT\nBEGIN:VEVENT\nDTSTART:20260925T032024Z\nEND:VEVENT\nEND:VEVENT"
  with self.assertRaisesRegex(ValueError,"VEVENT envelope"):verify_readback("2026-09-25T03:17:24Z",live)
 def test_missing_dtstart_rejected(self):
  with self.assertRaisesRegex(ValueError,"DTSTART missing or ambiguous"):verify_readback("2026-09-25T03:17:24Z","BEGIN:VEVENT\nRRULE:FREQ=HOURLY\nEND:VEVENT")
 def test_dtstart_prefix_spoof_rejected(self):
  with self.assertRaisesRegex(ValueError,"DTSTART missing or ambiguous"):verify_readback("2026-09-25T03:17:24Z","BEGIN:VEVENT\nDTSTARTFAKE:20260925T032024Z\nEND:VEVENT")
 def test_duplicate_dtstart_rejected(self):
  live="BEGIN:VEVENT\nDTSTART:20260925T032024Z\nDTSTART:20260925T032024Z\nEND:VEVENT"
  with self.assertRaisesRegex(ValueError,"DTSTART missing or ambiguous"):verify_readback("2026-09-25T03:17:24Z",live)
 def test_canonical_github_commit_timestamp(self):
  self.assertEqual(parse_github_commit_created_at("2026-09-25T03:17:24Z").isoformat(),"2026-09-25T03:17:24+00:00")
 def test_noncanonical_github_commit_timestamps_rejected(self):
  for value in ("2026-W39-5T03:17:24Z","2026-09-25 03:17:24Z","2026-09-25T03:17:24+00:00","2026-09-25T03:17:24.000Z","2026-09-25T03:17:24z","2026-09-25T03:17:24","2026-02-30T03:17:24Z"):
   with self.subTest(value=value):
    with self.assertRaises(ValueError):parse_github_commit_created_at(value)
 def test_bool_lead_rejected(self):
  with self.assertRaisesRegex(ValueError,"invalid lead_seconds"):next_from_reference("2026-09-25T03:17:24Z",True)
if __name__=="__main__":unittest.main(verbosity=2)

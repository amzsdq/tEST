#!/usr/bin/env python3
import unittest
from scheduler_v2 import next_from_reference,verify_readback
class SchedulerV2Tests(unittest.TestCase):
 def test_end_commit_plus_180(self):
  self.assertEqual(next_from_reference("2026-09-25T03:17:24Z").isoformat(),"2026-09-25T03:20:24+00:00")
 def test_iso_exact_readback(self):
  r=verify_readback("2026-09-25T03:17:24Z","2026-09-25T12:20:24+09:00");self.assertTrue(r["exact_match"]);self.assertEqual(r["delta_seconds"],0)
 def test_vevent_tzid_exact_readback(self):
  live="BEGIN:VEVENT\nDTSTART;TZID=Asia/Seoul:20260925T122024\nRRULE:FREQ=HOURLY\nEND:VEVENT";self.assertTrue(verify_readback("2026-09-25T03:17:24Z",live)["exact_match"])
 def test_vevent_z_exact_readback(self):
  live="BEGIN:VEVENT\nDTSTART:20260925T032024Z\nRRULE:FREQ=HOURLY\nEND:VEVENT";self.assertTrue(verify_readback("2026-09-25T03:17:24Z",live)["exact_match"])
 def test_missing_dtstart_rejected(self):
  with self.assertRaisesRegex(ValueError,"DTSTART missing or ambiguous"):verify_readback("2026-09-25T03:17:24Z","BEGIN:VEVENT\nRRULE:FREQ=HOURLY\nEND:VEVENT")
 def test_dtstart_prefix_spoof_rejected(self):
  with self.assertRaisesRegex(ValueError,"DTSTART missing or ambiguous"):verify_readback("2026-09-25T03:17:24Z","BEGIN:VEVENT\nDTSTARTFAKE:20260925T032024Z\nEND:VEVENT")
 def test_duplicate_dtstart_rejected(self):
  live="BEGIN:VEVENT\nDTSTART:20260925T032024Z\nDTSTART:20260925T032024Z\nEND:VEVENT"
  with self.assertRaisesRegex(ValueError,"DTSTART missing or ambiguous"):verify_readback("2026-09-25T03:17:24Z",live)
 def test_bool_lead_rejected(self):
  with self.assertRaisesRegex(ValueError,"invalid lead_seconds"):next_from_reference("2026-09-25T03:17:24Z",True)
if __name__=="__main__":unittest.main(verbosity=2)

#!/usr/bin/env python3
import unittest
from recovery_commit_clock import decide

SESSION = {"automation_id": "A", "start_commit": "start", "end_commit": None}
LIVE = {"automation_id": "A", "enabled": True, "rrule": "FREQ=HOURLY"}

class CommitClockRecoveryTests(unittest.TestCase):
    def test_open_session_resumes(self):
        self.assertEqual(decide(SESSION, LIVE)["action"], "RESUME_OPEN_SESSION")

    def test_verified_end_is_final(self):
        session = dict(SESSION, end_commit="end", end_verified=True)
        self.assertEqual(decide(session, LIVE)["action"], "DO_NOT_RESUME_FINALIZED")

    def test_unverified_end_requires_verification(self):
        session = dict(SESSION, end_commit="end")
        self.assertEqual(decide(session, LIVE)["action"], "VERIFY_END_BEFORE_RESUME")

    def test_missing_start_is_invalid(self):
        session = dict(SESSION, start_commit=None)
        self.assertEqual(decide(session, LIVE)["action"], "INVALID_SESSION")

    def test_identity_mismatch_blocks(self):
        live = dict(LIVE, automation_id="B")
        self.assertEqual(decide(SESSION, live)["action"], "AUTHORITY_BLOCK")

if __name__ == "__main__":
    unittest.main(verbosity=2)

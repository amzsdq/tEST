#!/usr/bin/env python3
import unittest
from lineage import resolve_end
VALID={"id":3,"start_id":1,"final_baton_id":2,"recognized_end":True,"created_at":"2026-09-24T00:01:00Z"}
class LineageTests(unittest.TestCase):
    def test_exact(self): self.assertEqual(resolve_end(1,2,[VALID])["id"],3)
    def test_missing(self):
        with self.assertRaisesRegex(ValueError,"NO_MATCHING_END"): resolve_end(1,9,[VALID])
    def test_ambiguous(self):
        with self.assertRaisesRegex(ValueError,"AMBIGUOUS_MATCHING_END"): resolve_end(1,2,[VALID,dict(VALID,id=4)])
    def test_unrecognized(self):
        with self.assertRaisesRegex(ValueError,"NO_MATCHING_END"): resolve_end(1,2,[dict(VALID,recognized_end=False)])
    def test_bool_end_id(self):
        with self.assertRaisesRegex(ValueError,"INVALID_END_ID"): resolve_end(1,2,[dict(VALID,id=True)])
    def test_bool_start_input(self):
        with self.assertRaisesRegex(ValueError,"INVALID_START_ID"): resolve_end(True,2,[VALID])
    def test_bool_baton_input(self):
        with self.assertRaisesRegex(ValueError,"INVALID_FINAL_BATON_ID"): resolve_end(1,True,[VALID])
    def test_bool_backlink_fails_closed(self):
        with self.assertRaisesRegex(ValueError,"INVALID_START_ID"): resolve_end(1,2,[dict(VALID,start_id=True)])
    def test_naive_timestamp_fails_closed(self):
        with self.assertRaisesRegex(ValueError,"INVALID_END_TIMESTAMP"): resolve_end(1,2,[dict(VALID,created_at="2026-09-24T00:01:00")])

    def test_noncanonical_end_timestamps_fail_closed(self):
        for value in ("2026-09-24T00:01:00+00:00","2026-09-24T00:01:00.000Z","2026-W39-4T00:01:00Z","2026-09-24 00:01:00Z"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError,"INVALID_END_TIMESTAMP"): resolve_end(1,2,[dict(VALID,created_at=value)])
if __name__=="__main__": unittest.main(verbosity=2)

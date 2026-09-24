#!/usr/bin/env python3
import unittest
from lineage import resolve_end

class LineageTests(unittest.TestCase):
    def test_exact_baton_backlink_and_lineage(self):
        c = [
            {"id": 3, "start_id": 1, "final_baton_id": 2, "recognized_end": True, "created_at": "2026-09-24T00:01:00Z"},
            {"id": 4, "start_id": 99, "final_baton_id": 2, "recognized_end": True, "created_at": "2026-09-24T00:02:00Z"},
        ]
        self.assertEqual(resolve_end(1, 2, c)["id"], 3)

    def test_missing_end_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "NO_MATCHING_END"):
            resolve_end(1, 2, [{"id": 3, "start_id": 1, "final_baton_id": 9, "recognized_end": True, "created_at": "2026-09-24T00:01:00Z"}])

    def test_multiple_exact_candidates_are_ambiguous(self):
        c = [
            {"id": 3, "start_id": 1, "final_baton_id": 2, "recognized_end": True, "created_at": "2026-09-24T00:01:00Z"},
            {"id": 4, "start_id": 1, "final_baton_id": 2, "recognized_end": True, "created_at": "2026-09-24T00:02:00Z"},
        ]
        with self.assertRaisesRegex(ValueError, "AMBIGUOUS_MATCHING_END"):
            resolve_end(1, 2, c)

    def test_unrecognized_marker_is_not_end(self):
        with self.assertRaisesRegex(ValueError, "NO_MATCHING_END"):
            resolve_end(1, 2, [{"id": 3, "start_id": 1, "final_baton_id": 2, "recognized_end": False, "created_at": "2026-09-24T00:01:00Z"}])

if __name__ == "__main__":
    unittest.main(verbosity=2)

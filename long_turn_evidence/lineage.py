"""Resolve an END from explicit candidate markers without guessing."""
from typing import Any


def resolve_end(start_id: int, final_baton_id: int, candidates: list[dict[str, Any]]) -> dict[str, Any]:
    """Return exactly one END whose backlink and lineage match.

    Candidate shape: {id, start_id, final_baton_id, recognized_end, created_at}.
    Generic/unknown candidates are never retried or guessed into authority.
    """
    matches = [c for c in candidates if c.get("recognized_end") is True
               and c.get("start_id") == start_id
               and c.get("final_baton_id") == final_baton_id]
    if not matches:
        raise ValueError("NO_MATCHING_END")
    if len(matches) != 1:
        raise ValueError("AMBIGUOUS_MATCHING_END")
    end = matches[0]
    if not isinstance(end.get("id"), int) or end["id"] <= 0:
        raise ValueError("INVALID_END_ID")
    if not isinstance(end.get("created_at"), str):
        raise ValueError("INVALID_END_TIMESTAMP")
    return end

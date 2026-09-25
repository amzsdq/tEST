"""Resolve an END from explicit candidate markers without guessing."""
from datetime import datetime
from typing import Any

def _positive_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"INVALID_{label}")
    return value

def _timestamp(value: Any) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("INVALID_END_TIMESTAMP")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("INVALID_END_TIMESTAMP") from exc
    if parsed.tzinfo is None:
        raise ValueError("INVALID_END_TIMESTAMP")
    return value

def resolve_end(start_id: int, final_baton_id: int, candidates: list[dict[str, Any]]) -> dict[str, Any]:
    _positive_int(start_id, "START_ID")
    _positive_int(final_baton_id, "FINAL_BATON_ID")
    if not isinstance(candidates, list):
        raise ValueError("INVALID_CANDIDATES")
    matches = [c for c in candidates if isinstance(c, dict)
               and c.get("recognized_end") is True
               and c.get("start_id") == start_id
               and c.get("final_baton_id") == final_baton_id]
    if not matches:
        raise ValueError("NO_MATCHING_END")
    if len(matches) != 1:
        raise ValueError("AMBIGUOUS_MATCHING_END")
    end = matches[0]
    _positive_int(end.get("id"), "END_ID")
    _positive_int(end.get("start_id"), "START_ID")
    _positive_int(end.get("final_baton_id"), "FINAL_BATON_ID")
    _timestamp(end.get("created_at"))
    return end

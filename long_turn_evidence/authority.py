"""Select authoritative exact evidence without rewriting historical censored observations."""
from datetime import datetime, timezone

def _ts(value):
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamp must be timezone-aware")
    return dt.astimezone(timezone.utc)

def select_authority(observation, exact_records):
    matches = []
    for exact in exact_records:
        if exact.get("supersedes_observation_invocation_id") != observation.get("invocation_id"):
            continue
        if exact.get("invocation_id") != observation.get("invocation_id"):
            continue
        if exact.get("automation_id") != observation.get("automation_id"):
            raise ValueError("EXACT_AUTOMATION_MISMATCH")
        if exact.get("source") != "raw_github_start_end":
            continue
        if exact.get("start") != observation.get("start"):
            raise ValueError("EXACT_START_MISMATCH")
        start = _ts(exact["start"]["created_at"])
        end = _ts(exact["end"]["created_at"])
        if end < start:
            raise ValueError("EXACT_END_PRECEDES_START")
        matches.append((exact, int((end - start).total_seconds())))
    if len(matches) > 1:
        raise ValueError("AMBIGUOUS_EXACT_AUTHORITY")
    if len(matches) == 1:
        exact, seconds = matches[0]
        return {"kind": "exact", "evidence_id": exact["evidence_id"],
                "exact_duration_seconds": seconds, "target_crossed": seconds >= observation.get("target_seconds", 900)}
    return {"kind": "historical_record", "invocation_id": observation["invocation_id"], "historical_end_present": observation.get("end") is not None}

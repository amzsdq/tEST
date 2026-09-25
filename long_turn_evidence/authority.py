"""Select authoritative exact evidence without rewriting historical censored observations."""
from datetime import datetime, timezone

def _ts(value):
    if not isinstance(value, str) or not value:
        raise ValueError("EXACT_TIMESTAMP_INVALID")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("EXACT_TIMESTAMP_INVALID") from exc
    if dt.tzinfo is None:
        raise ValueError("EXACT_TIMESTAMP_NOT_TIMEZONE_AWARE")
    return dt.astimezone(timezone.utc)

def _marker(value, label):
    if not isinstance(value, dict):
        raise ValueError(f"EXACT_{label}_INVALID")
    if set(value) != {"id", "created_at"}:
        raise ValueError(f"EXACT_{label}_FIELDS_INVALID")
    marker_id = value.get("id")
    if isinstance(marker_id, bool) or not isinstance(marker_id, int) or marker_id <= 0:
        raise ValueError(f"EXACT_{label}_ID_INVALID")
    _ts(value.get("created_at"))
    return value

def _identity(value, label):
    if not isinstance(value, str) or not value.strip(): raise ValueError(label)
    return value

def select_authority(observation, exact_records):
    if not isinstance(observation, dict) or not isinstance(exact_records, list):
        raise ValueError("AUTHORITY_INPUT_INVALID")
    observation_invocation = _identity(observation.get("invocation_id"), "OBSERVATION_INVOCATION_ID_INVALID")
    observation_automation = _identity(observation.get("automation_id"), "OBSERVATION_AUTOMATION_ID_INVALID")
    target = observation.get("target_seconds", 900)
    if isinstance(target, bool) or not isinstance(target, int) or target <= 0:
        raise ValueError("AUTHORITY_TARGET_INVALID")
    matches = []
    seen_ids = set()
    for exact in exact_records:
        if not isinstance(exact, dict):
            raise ValueError("EXACT_RECORD_INVALID")
        if set(exact) != {"evidence_id","invocation_id","automation_id","source","supersedes_observation_invocation_id","start","end"}:
            raise ValueError("EXACT_RECORD_FIELDS_INVALID")
        supersedes = _identity(exact.get("supersedes_observation_invocation_id"), "EXACT_SUPERSEDES_INVOCATION_ID_INVALID")
        exact_invocation = _identity(exact.get("invocation_id"), "EXACT_INVOCATION_ID_INVALID")
        exact_automation = _identity(exact.get("automation_id"), "EXACT_AUTOMATION_ID_INVALID")
        if supersedes != observation_invocation: continue
        if exact_invocation != observation_invocation: continue
        evidence_id = exact.get("evidence_id")
        if not isinstance(evidence_id, str) or not evidence_id.strip():
            raise ValueError("EXACT_EVIDENCE_ID_INVALID")
        if evidence_id in seen_ids:
            raise ValueError("DUPLICATE_EXACT_EVIDENCE_ID")
        seen_ids.add(evidence_id)
        if exact_automation != observation_automation:
            raise ValueError("EXACT_AUTOMATION_MISMATCH")
        if exact.get("source") != "raw_github_start_end":
            continue
        start_marker = _marker(exact.get("start"), "START")
        end_marker = _marker(exact.get("end"), "END")
        if start_marker != observation.get("start"):
            raise ValueError("EXACT_START_MISMATCH")
        start = _ts(start_marker["created_at"]); end = _ts(end_marker["created_at"])
        if end < start:
            raise ValueError("EXACT_END_PRECEDES_START")
        matches.append((exact, int((end - start).total_seconds())))
    if len(matches) > 1:
        raise ValueError("AMBIGUOUS_EXACT_AUTHORITY")
    if len(matches) == 1:
        exact, seconds = matches[0]
        return {"kind":"exact","evidence_id":exact["evidence_id"],"exact_duration_seconds":seconds,
                "target_crossed":seconds >= target}
    return {"kind":"historical_record","invocation_id":observation_invocation,
            "historical_end_present":observation.get("end") is not None}

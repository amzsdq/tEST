from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

def parse(value):
    if not isinstance(value, str) or not value:
        raise ValueError("timestamp must be non-empty string")
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timezone-aware timestamp required")
    return dt.astimezone(timezone.utc)

def parse_live_dtstart(value):
    if not isinstance(value, str) or not value:
        raise ValueError("live DTSTART must be non-empty string")
    if "\n" not in value and not value.startswith("BEGIN:VEVENT"):
        return parse(value)
    stripped = [x.strip() for x in value.splitlines() if x.strip()]
    if (not stripped or stripped[0] != "BEGIN:VEVENT" or stripped[-1] != "END:VEVENT"
            or stripped.count("BEGIN:VEVENT") != 1 or stripped.count("END:VEVENT") != 1):
        raise ValueError("live schedule must be one VEVENT envelope")
    allowed = [x for x in stripped
               if x in ("BEGIN:VEVENT", "END:VEVENT")
               or x.startswith("DTSTART:") or x.startswith("DTSTART;TZID=")
               or x.startswith("RRULE:")]
    if len(allowed) != len(stripped):
        raise ValueError("unexpected live schedule content")
    lines = [x for x in stripped if x.startswith("DTSTART")]
    valid = [x for x in lines if x.startswith("DTSTART:") or x.startswith("DTSTART;TZID=")]
    if len(valid) != 1 or len(lines) != 1:
        raise ValueError("DTSTART missing or ambiguous in live schedule")
    head, raw = valid[0].split(":", 1)
    if head.startswith("DTSTART;TZID="):
        tzid = head.split("=", 1)[1]
        dt = datetime.strptime(raw, "%Y%m%dT%H%M%S").replace(tzinfo=ZoneInfo(tzid))
        return dt.astimezone(timezone.utc)
    if head == "DTSTART" and raw.endswith("Z"):
        return datetime.strptime(raw, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
    raise ValueError("live DTSTART must carry TZID or Z")

def next_from_reference(reference_created_at, lead_seconds=180):
    if isinstance(lead_seconds, bool) or not isinstance(lead_seconds, int) or lead_seconds <= 0:
        raise ValueError("invalid lead_seconds")
    return parse(reference_created_at) + timedelta(seconds=lead_seconds)

def verify_readback(reference_created_at, live_schedule_or_dtstart, lead_seconds=180):
    intended = next_from_reference(reference_created_at, lead_seconds)
    observed = parse_live_dtstart(live_schedule_or_dtstart)
    return {"intended_utc":intended.isoformat(),"observed_utc":observed.isoformat(),
            "exact_match":intended == observed,"delta_seconds":int((observed-intended).total_seconds())}


def parse_github_commit_created_at(value):
    """Parse canonical GitHub commit created_at: second-resolution UTC Z only."""
    if not isinstance(value, str) or len(value) != 20 or value[4] != "-" or value[7] != "-" or value[10] != "T" or value[13] != ":" or value[16] != ":" or value[19] != "Z":
        raise ValueError("GitHub commit created_at must be canonical UTC Z timestamp")
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError as exc:
        raise ValueError("GitHub commit created_at must be canonical UTC Z timestamp") from exc

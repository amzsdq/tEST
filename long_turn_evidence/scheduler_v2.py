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
    line = next((x.strip() for x in value.splitlines() if x.strip().startswith("DTSTART")), None)
    if line is None or ":" not in line:
        raise ValueError("DTSTART missing from live schedule")
    head, raw = line.split(":", 1)
    if ";TZID=" in head:
        tzid = head.split(";TZID=", 1)[1]
        dt = datetime.strptime(raw, "%Y%m%dT%H%M%S").replace(tzinfo=ZoneInfo(tzid))
        return dt.astimezone(timezone.utc)
    if raw.endswith("Z"):
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

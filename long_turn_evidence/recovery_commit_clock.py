"""Cold recovery for commit-backed clock sessions."""

def _is_hourly_rrule(value):
    # Canonical relay requires an unbounded one-hour recurrence. Parameters such
    # as COUNT, UNTIL, INTERVAL, or BY* can truncate or alter liveness.
    return value == "FREQ=HOURLY"

def _hourly_preserved(live):
    checks = []
    if live.get("rrule") is not None:
        checks.append(_is_hourly_rrule(live.get("rrule")))
    schedule = live.get("schedule")
    if schedule is not None:
        if not isinstance(schedule, str):
            checks.append(False)
        else:
            stripped = [line.strip() for line in schedule.splitlines() if line.strip()]
            if (not stripped or stripped[0] != "BEGIN:VEVENT" or stripped[-1] != "END:VEVENT"
                    or stripped.count("BEGIN:VEVENT") != 1 or stripped.count("END:VEVENT") != 1):
                checks.append(False)
                return bool(checks) and all(checks)
            dtstarts = [line for line in stripped if line.startswith("DTSTART")]
            valid_dtstarts = [line for line in dtstarts
                              if line.startswith("DTSTART:") or line.startswith("DTSTART;TZID=")]
            if len(dtstarts) != 1 or len(valid_dtstarts) != 1:
                checks.append(False)
                return bool(checks) and all(checks)
            allowed = [line for line in stripped
                       if line in ("BEGIN:VEVENT", "END:VEVENT")
                       or line.startswith("DTSTART:") or line.startswith("DTSTART;TZID=")
                       or line.startswith("RRULE:")]
            if len(allowed) != len(stripped):
                checks.append(False)
                return bool(checks) and all(checks)
            rrules = [line.removeprefix("RRULE:") for line in stripped if line.startswith("RRULE:")]
            checks.append(len(rrules) == 1 and _is_hourly_rrule(rrules[0]))
    return bool(checks) and all(checks)

def decide(session, live):
    if not session.get("start_commit"):
        return {"action":"INVALID_SESSION","reason":"missing START commit"}
    if session.get("start_verified") is not True:
        return {"action":"VERIFY_START_BEFORE_RESUME","reason":"START commit exists but readback is not verified"}
    if session.get("end_commit"):
        if session.get("end_verified") is True:
            return {"action":"DO_NOT_RESUME_FINALIZED","reason":"verified END commit already present"}
        return {"action":"VERIFY_END_BEFORE_RESUME","reason":"END commit exists but readback is not verified"}
    if live.get("automation_id") != session.get("automation_id"):
        return {"action":"AUTHORITY_BLOCK","reason":"automation identity mismatch"}
    if live.get("enabled") is not True:
        return {"action":"RECURRENCE_DEGRADED","reason":"canonical automation disabled"}
    if live.get("timing_mode") != "exact_schedule":
        return {"action":"RECURRENCE_DEGRADED","reason":"canonical automation timing_mode is not exact_schedule"}
    if not _hourly_preserved(live):
        return {"action":"RECURRENCE_DEGRADED","reason":"hourly fallback not preserved"}
    return {"action":"RESUME_OPEN_SESSION","reason":"verified START exists without END; never invent END or WORKED"}

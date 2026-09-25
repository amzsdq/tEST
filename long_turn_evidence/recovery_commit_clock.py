"""Cold recovery for commit-backed clock sessions."""

def _hourly_preserved(live):
    if live.get("rrule") == "FREQ=HOURLY":
        return True
    schedule = live.get("schedule")
    return isinstance(schedule, str) and "RRULE:FREQ=HOURLY" in schedule.splitlines()

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
    if not _hourly_preserved(live):
        return {"action":"RECURRENCE_DEGRADED","reason":"hourly fallback not preserved"}
    return {"action":"RESUME_OPEN_SESSION","reason":"verified START exists without END; never invent END or WORKED"}

#!/usr/bin/env python3
"""Deterministic validator for long-turn relay evidence fixtures.

Input is explicit fixture JSON only. This module never scrapes GitHub, secrets,
sessions, or private URLs. GitHub created_at timestamps supplied in fixtures are
assumed to have been independently acquired by the caller.
"""
from __future__ import annotations
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CLASSES = {
    "VOLUNTARY_FINAL",
    "ABRUPT_NONFINAL",
    "TOOLPATH_LOSS_CANDIDATE",
    "PLATFORM_RUNTIME_KILL_CANDIDATE",
    "UNKNOWN",
}


def ts(value: str | None) -> datetime | None:
    if value is None:
        return None
    d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if d.tzinfo is None:
        raise ValueError("timestamp must be timezone-aware")
    return d.astimezone(timezone.utc)


def require_marker(marker: dict[str, Any] | None, kind: str) -> None:
    if marker is None:
        return
    if not isinstance(marker.get("id"), int) or marker["id"] <= 0:
        raise ValueError(f"{kind}: invalid marker id")
    ts(marker.get("created_at"))


def validate(record: dict[str, Any]) -> dict[str, Any]:
    required = ["invocation_id", "automation_id", "start", "scheduler_mutation_count"]
    for k in required:
        if k not in record:
            raise ValueError(f"missing {k}")
    require_marker(record["start"], "start")
    require_marker(record.get("end"), "end")
    require_marker(record.get("last_durable_boundary"), "last_durable_boundary")
    require_marker(record.get("final_baton"), "final_baton")

    start = ts(record["start"]["created_at"])
    end = ts(record.get("end", {}).get("created_at") if record.get("end") else None)
    boundary = ts(record.get("last_durable_boundary", {}).get("created_at") if record.get("last_durable_boundary") else None)
    baton = ts(record.get("final_baton", {}).get("created_at") if record.get("final_baton") else None)

    if end and end < start:
        raise ValueError("end precedes start")
    if boundary and boundary < start:
        raise ValueError("boundary precedes start")
    if baton and baton < start:
        raise ValueError("baton precedes start")
    if end and boundary and boundary > end:
        raise ValueError("boundary follows end")
    if end and baton and baton > end:
        raise ValueError("baton follows end")

    mutations = record["scheduler_mutation_count"]
    if not isinstance(mutations, int) or mutations < 0:
        raise ValueError("invalid scheduler_mutation_count")

    exact = int((end - start).total_seconds()) if end else None
    lower = int((boundary - start).total_seconds()) if (not end and boundary) else None
    target = int(record.get("target_seconds", 900))
    target_crossed = exact >= target if exact is not None else (lower >= target if lower is not None else False)

    final_sig = bool(record.get("finalization_signature"))
    if end and final_sig and baton and mutations == 1:
        classification = "VOLUNTARY_FINAL"
    elif not end and boundary and record.get("termination_evidence") == "toolpath_loss":
        classification = "TOOLPATH_LOSS_CANDIDATE"
    elif not end and boundary and record.get("termination_evidence") == "platform_runtime_kill":
        classification = "PLATFORM_RUNTIME_KILL_CANDIDATE"
    elif not end and boundary and not final_sig:
        classification = "ABRUPT_NONFINAL"
    else:
        classification = "UNKNOWN"

    violations: list[str] = []
    if end and final_sig and mutations != 1:
        violations.append("FINAL_MUTATION_COUNT_NOT_ONE")
    if end and final_sig and not baton:
        violations.append("FINAL_BATON_MISSING")
    if record.get("cross_invocation_sum_seconds") is not None:
        violations.append("CROSS_INVOCATION_SUM_FORBIDDEN")
    if record.get("claimed_target_crossed") is True and not target_crossed:
        violations.append("FALSE_TARGET_CROSSING_CLAIM")
    if record.get("claimed_exact_seconds") is not None and exact is None:
        violations.append("CENSORED_RUN_CLAIMED_EXACT")
    if exact is not None and record.get("claimed_exact_seconds") not in (None, exact):
        violations.append("EXACT_DURATION_MISMATCH")

    return {
        "invocation_id": record["invocation_id"],
        "classification": classification,
        "exact_duration_seconds": exact,
        "censored_lower_bound_seconds": lower,
        "target_seconds": target,
        "target_crossed": target_crossed,
        "scheduler_mutation_count": mutations,
        "violations": violations,
        "valid": not violations,
    }


def validate_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    result = validate(fixture["record"])
    expected = fixture["expected"]
    for key, value in expected.items():
        if result.get(key) != value:
            raise AssertionError(f"{fixture['id']}: {key}: expected {value!r}, got {result.get(key)!r}")
    return result


def main() -> None:
    root = Path(__file__).resolve().parent
    fixtures = json.loads((root / "fixtures.json").read_text())
    results = []
    for fixture in fixtures:
        try:
            results.append({"fixture": fixture["id"], "result": validate_fixture(fixture)})
        except ValueError as exc:
            if fixture["expected"].get("raises") not in str(exc):
                raise
            results.append({"fixture": fixture["id"], "raised": str(exc)})
    print(json.dumps(results, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()

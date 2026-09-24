#!/usr/bin/env python3
"""Deterministic validator for explicit long-turn relay evidence fixtures."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
CLASSES={"VOLUNTARY_FINAL","ABRUPT_NONFINAL","TOOLPATH_LOSS_CANDIDATE","PLATFORM_RUNTIME_KILL_CANDIDATE","UNKNOWN"}
def ts(value):
    if value is None:return None
    if not isinstance(value,str) or not value:raise ValueError("timestamp must be a non-empty string")
    d=datetime.fromisoformat(value.replace("Z","+00:00"))
    if d.tzinfo is None:raise ValueError("timestamp must be timezone-aware")
    return d.astimezone(timezone.utc)
def strict_nonnegative_int(value,name):
    if isinstance(value,bool) or not isinstance(value,int) or value<0:raise ValueError(f"invalid {name}")
    return value
def require_marker(marker,kind):
    if marker is None:return
    if not isinstance(marker,dict):raise ValueError(f"{kind}: marker must be object")
    mid=marker.get("id")
    if isinstance(mid,bool) or not isinstance(mid,int) or mid<=0:raise ValueError(f"{kind}: invalid marker id")
    if "created_at" not in marker or not isinstance(marker["created_at"],str) or not marker["created_at"]:raise ValueError(f"{kind}: missing created_at")
    ts(marker["created_at"])
def validate(record):
    for k in ["invocation_id","automation_id","start","scheduler_mutation_count"]:
        if k not in record:raise ValueError(f"missing {k}")
    if not isinstance(record["invocation_id"],str) or not record["invocation_id"]:raise ValueError("invalid invocation_id")
    if not isinstance(record["automation_id"],str) or not record["automation_id"]:raise ValueError("invalid automation_id")
    for key,kind in [("start","start"),("end","end"),("last_durable_boundary","last_durable_boundary"),("final_baton","final_baton")]:require_marker(record.get(key),kind)
    start=ts(record["start"]["created_at"]);end=ts(record["end"]["created_at"]) if record.get("end") else None
    boundary=ts(record["last_durable_boundary"]["created_at"]) if record.get("last_durable_boundary") else None
    baton=ts(record["final_baton"]["created_at"]) if record.get("final_baton") else None
    if end and end<start:raise ValueError("end precedes start")
    if boundary and boundary<start:raise ValueError("boundary precedes start")
    if baton and baton<start:raise ValueError("baton precedes start")
    if end and boundary and boundary>end:raise ValueError("boundary follows end")
    if end and baton and baton>end:raise ValueError("baton follows end")
    mutations=strict_nonnegative_int(record["scheduler_mutation_count"],"scheduler_mutation_count")
    target=record.get("target_seconds",900)
    if isinstance(target,bool) or not isinstance(target,int) or target<=0:raise ValueError("invalid target_seconds")
    exact=int((end-start).total_seconds()) if end else None;lower=int((boundary-start).total_seconds()) if not end and boundary else None
    target_crossed=exact>=target if exact is not None else (lower>=target if lower is not None else False)
    final_sig=bool(record.get("finalization_signature"));obs=record.get("observation_state")
    if end and final_sig and baton and mutations==1:classification="VOLUNTARY_FINAL"
    elif not end and boundary and record.get("termination_evidence")=="toolpath_loss":classification="TOOLPATH_LOSS_CANDIDATE"
    elif not end and boundary and record.get("termination_evidence")=="platform_runtime_kill":classification="PLATFORM_RUNTIME_KILL_CANDIDATE"
    elif not end and boundary and obs!="active" and not final_sig:classification="ABRUPT_NONFINAL"
    else:classification="UNKNOWN"
    violations=[]
    if end and final_sig and mutations!=1:violations.append("FINAL_MUTATION_COUNT_NOT_ONE")
    if end and final_sig and not baton:violations.append("FINAL_BATON_MISSING")
    if record.get("cross_invocation_sum_seconds") is not None:violations.append("CROSS_INVOCATION_SUM_FORBIDDEN")
    if record.get("claimed_target_crossed") is True and not target_crossed:violations.append("FALSE_TARGET_CROSSING_CLAIM")
    if record.get("claimed_exact_seconds") is not None and exact is None:violations.append("CENSORED_RUN_CLAIMED_EXACT")
    if exact is not None and record.get("claimed_exact_seconds") not in (None,exact):violations.append("EXACT_DURATION_MISMATCH")
    return {"invocation_id":record["invocation_id"],"classification":classification,"exact_duration_seconds":exact,"censored_lower_bound_seconds":lower,"target_seconds":target,"target_crossed":target_crossed,"scheduler_mutation_count":mutations,"violations":violations,"valid":not violations}
def validate_fixture(fixture):
    result=validate(fixture["record"])
    for key,value in fixture["expected"].items():
        if key=="raises":continue
        if result.get(key)!=value:raise AssertionError(f"{fixture['id']}: {key}: expected {value!r}, got {result.get(key)!r}")
    return result
def main():
    root=Path(__file__).resolve().parent;fixtures=json.loads((root/"fixtures.json").read_text());results=[]
    for fixture in fixtures:
        expected_raise=fixture["expected"].get("raises")
        try:
            result=validate_fixture(fixture)
            if expected_raise:raise AssertionError(f"{fixture['id']}: expected rejection")
            results.append({"fixture":fixture["id"],"result":result})
        except ValueError as exc:
            if not expected_raise or expected_raise not in str(exc):raise
            results.append({"fixture":fixture["id"],"raised":str(exc)})
    print(json.dumps(results,indent=2,sort_keys=True))
if __name__=="__main__":main()

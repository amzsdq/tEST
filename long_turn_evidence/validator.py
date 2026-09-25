#!/usr/bin/env python3
"""Deterministic validator for explicit long-turn relay evidence fixtures."""
from __future__ import annotations
import json
from datetime import datetime,timezone
from pathlib import Path
from versioning import normalize_record
CLASSES={"VOLUNTARY_FINAL","ABRUPT_NONFINAL","TOOLPATH_LOSS_CANDIDATE","PLATFORM_RUNTIME_KILL_CANDIDATE","UNKNOWN"}
def ts(v):
 if v is None:return None
 if not isinstance(v,str) or not v:raise ValueError("timestamp must be a non-empty string")
 d=datetime.fromisoformat(v.replace("Z","+00:00"))
 if d.tzinfo is None:raise ValueError("timestamp must be timezone-aware")
 return d.astimezone(timezone.utc)
def strict_int(v,name,positive=False):
 if isinstance(v,bool) or not isinstance(v,int) or (v<=0 if positive else v<0):raise ValueError(f"invalid {name}")
 return v
def marker(m,kind):
 if m is None:return
 if not isinstance(m,dict):raise ValueError(f"{kind}: marker must be object")
 mid=m.get("id")
 if isinstance(mid,bool) or not isinstance(mid,int) or mid<=0:raise ValueError(f"{kind}: invalid marker id")
 if "created_at" not in m or not isinstance(m["created_at"],str) or not m["created_at"]:raise ValueError(f"{kind}: missing created_at")
 ts(m["created_at"])
def validate(record):
 r,_source_version=normalize_record(record)
 for k in ["invocation_id","automation_id","start","scheduler_mutation_count"]:
  if k not in r:raise ValueError(f"missing {k}")
 if not isinstance(r["invocation_id"],str) or not r["invocation_id"].strip():raise ValueError("invalid invocation_id")
 if not isinstance(r["automation_id"],str) or not r["automation_id"].strip():raise ValueError("invalid automation_id")
 if r.get("start") is None:raise ValueError("start: marker must be object")
 for k in ["start","end","last_durable_boundary","final_baton"]:marker(r.get(k),k)
 if "finalization_signature" in r and not isinstance(r["finalization_signature"],bool):raise ValueError("invalid finalization_signature")
 if "claimed_target_crossed" in r and not isinstance(r["claimed_target_crossed"],bool):raise ValueError("invalid claimed_target_crossed")
 if r.get("claimed_exact_seconds") is not None:strict_int(r["claimed_exact_seconds"],"claimed_exact_seconds")
 obs=r.get("observation_state");term=r.get("termination_evidence")
 if obs not in (None,"active","recovered_missing_end","closed"):raise ValueError("invalid observation_state")
 if term not in (None,"toolpath_loss","platform_runtime_kill"):raise ValueError("invalid termination_evidence")
 start=ts(r["start"]["created_at"]);end=ts(r["end"]["created_at"]) if r.get("end") else None;bound=ts(r["last_durable_boundary"]["created_at"]) if r.get("last_durable_boundary") else None;baton=ts(r["final_baton"]["created_at"]) if r.get("final_baton") else None
 if obs=="active" and end:raise ValueError("active observation cannot have END")
 if obs=="closed" and not end:raise ValueError("closed observation requires END")
 if term is not None and (obs=="active" or end):raise ValueError("termination evidence contradicts active/ended record")
 if end and end<start:raise ValueError("end precedes start")
 if bound and bound<start:raise ValueError("boundary precedes start")
 if baton and baton<start:raise ValueError("baton precedes start")
 if end and bound and bound>end:raise ValueError("boundary follows end")
 if end and baton and baton>end:raise ValueError("baton follows end")
 mutations=strict_int(r["scheduler_mutation_count"],"scheduler_mutation_count");target=strict_int(r.get("target_seconds",900),"target_seconds",True)
 exact=int((end-start).total_seconds()) if end else None;lower=int((bound-start).total_seconds()) if not end and bound else None;crossed=exact>=target if exact is not None else (lower>=target if lower is not None else False);final=r.get("finalization_signature",False)
 if end and final and baton and mutations==1:c="VOLUNTARY_FINAL"
 elif not end and bound and term=="toolpath_loss":c="TOOLPATH_LOSS_CANDIDATE"
 elif not end and bound and term=="platform_runtime_kill":c="PLATFORM_RUNTIME_KILL_CANDIDATE"
 elif not end and bound and obs!="active" and not final:c="ABRUPT_NONFINAL"
 else:c="UNKNOWN"
 v=[]
 if end and final and mutations!=1:v.append("FINAL_MUTATION_COUNT_NOT_ONE")
 if end and final and not baton:v.append("FINAL_BATON_MISSING")
 if r.get("cross_invocation_sum_seconds") is not None:v.append("CROSS_INVOCATION_SUM_FORBIDDEN")
 if r.get("claimed_target_crossed") is True and not crossed:v.append("FALSE_TARGET_CROSSING_CLAIM")
 if r.get("claimed_exact_seconds") is not None and exact is None:v.append("CENSORED_RUN_CLAIMED_EXACT")
 if exact is not None and r.get("claimed_exact_seconds") not in (None,exact):v.append("EXACT_DURATION_MISMATCH")
 return {"invocation_id":r["invocation_id"],"classification":c,"exact_duration_seconds":exact,"censored_lower_bound_seconds":lower,"target_seconds":target,"target_crossed":crossed,"scheduler_mutation_count":mutations,"violations":v,"valid":not v}
def validate_fixture(f):
 x=validate(f["record"])
 for k,v in f["expected"].items():
  if k!="raises" and x.get(k)!=v:raise AssertionError(f"{f['id']}: {k}: expected {v!r}, got {x.get(k)!r}")
 return x
def main():
 fs=json.loads((Path(__file__).resolve().parent/"fixtures.json").read_text());out=[]
 for f in fs:
  er=f["expected"].get("raises")
  try:
   x=validate_fixture(f)
   if er:raise AssertionError(f"{f['id']}: expected rejection")
   out.append({"fixture":f["id"],"result":x})
  except ValueError as e:
   if not er or er not in str(e):raise
   out.append({"fixture":f["id"],"raised":str(e)})
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=="__main__":main()

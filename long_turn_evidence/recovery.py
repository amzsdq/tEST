"""Cold-recovery decision helper. Explicit evidence only."""
def decide(record,live):
 if record.get('end') is not None:
  if record.get('end_verified') is True:return {'action':'DO_NOT_RESUME_FINALIZED','reason':'verified matching END already present'}
  return {'action':'RECONSTRUCT_BEFORE_RESUME','reason':'END present but exact baton backlink/lineage not verified'}
 if record.get('last_durable_boundary') is None:return {'action':'RECONSTRUCT_BEFORE_RESUME','reason':'no durable post-START boundary'}
 if live.get('automation_id')!=record.get('automation_id'):return {'action':'AUTHORITY_BLOCK','reason':'automation identity mismatch'}
 if live.get('enabled') is not True:return {'action':'RECURRENCE_DEGRADED','reason':'canonical automation disabled'}
 if live.get('rrule')!='FREQ=HOURLY':return {'action':'RECURRENCE_DEGRADED','reason':'hourly fallback not preserved'}
 return {'action':'RESUME_CENSORED','reason':'missing END with durable boundary; do not preclaim exact duration or prior package completion'}

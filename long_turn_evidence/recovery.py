"""Cold-recovery decision helper. Explicit evidence only."""
from recovery_commit_clock import _hourly_preserved

def _marker_shape(value):
 return isinstance(value,dict) and isinstance(value.get('id'),int) and not isinstance(value.get('id'),bool) and value.get('id')>0

def _identity(value):
 return isinstance(value,str) and bool(value.strip())

def decide(record,live):
 if not isinstance(record,dict) or not isinstance(live,dict):return {'action':'INVALID_SESSION','reason':'record/live must be objects'}
 if not _identity(record.get('automation_id')) or not _identity(live.get('automation_id')):return {'action':'INVALID_SESSION','reason':'missing or malformed automation identity'}
 if not _marker_shape(record.get('start')):return {'action':'INVALID_SESSION','reason':'missing or malformed START marker'}
 if record.get('start_verified') is not True:return {'action':'VERIFY_START_BEFORE_RESUME','reason':'START exists but readback is not verified'}
 if record.get('end') is not None:
  if not _marker_shape(record.get('end')):return {'action':'RECONSTRUCT_BEFORE_RESUME','reason':'END present but malformed'}
  if record.get('end_verified') is True:return {'action':'DO_NOT_RESUME_FINALIZED','reason':'verified matching END already present'}
  return {'action':'RECONSTRUCT_BEFORE_RESUME','reason':'END present but exact baton backlink/lineage not verified'}
 if not _marker_shape(record.get('last_durable_boundary')):return {'action':'RECONSTRUCT_BEFORE_RESUME','reason':'missing or malformed durable post-START boundary'}
 if live.get('automation_id')!=record.get('automation_id'):return {'action':'AUTHORITY_BLOCK','reason':'automation identity mismatch'}
 if live.get('enabled') is not True:return {'action':'RECURRENCE_DEGRADED','reason':'canonical automation disabled'}
 if live.get('timing_mode')!='exact_schedule':return {'action':'RECURRENCE_DEGRADED','reason':'canonical automation timing_mode is not exact_schedule'}
 if not _hourly_preserved(live):return {'action':'RECURRENCE_DEGRADED','reason':'hourly fallback not preserved'}
 return {'action':'RESUME_CENSORED','reason':'missing END with durable boundary; do not preclaim exact duration or prior package completion'}

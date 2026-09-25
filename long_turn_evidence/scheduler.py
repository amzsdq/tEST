from datetime import datetime,timedelta,timezone

def parse(v):
 if not isinstance(v,str) or not v:raise ValueError('timestamp must be non-empty string')
 d=datetime.fromisoformat(v.replace('Z','+00:00'))
 if d.tzinfo is None:raise ValueError('timezone-aware timestamp required')
 return d.astimezone(timezone.utc)

def final_next_from_baton(baton_created_at,lead_seconds=180):
 if isinstance(lead_seconds,bool) or not isinstance(lead_seconds,int) or lead_seconds<=0:raise ValueError('invalid lead_seconds')
 return parse(baton_created_at)+timedelta(seconds=lead_seconds)

def verify_readback(baton_created_at,live_dtstart,lead_seconds=180):
 intended=final_next_from_baton(baton_created_at,lead_seconds)
 observed=parse(live_dtstart)
 return {"intended_utc":intended.isoformat(),"observed_utc":observed.isoformat(),"exact_match":intended==observed,"delta_seconds":int((observed-intended).total_seconds())}

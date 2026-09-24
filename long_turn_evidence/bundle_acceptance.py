from datetime import datetime, timezone

def ts(v):
 d=datetime.fromisoformat(v.replace('Z','+00:00')); assert d.tzinfo; return d.astimezone(timezone.utc)
def validate(r):
 s=ts(r['start']); e=ts(r['end']) if r.get('end') else None; b=ts(r['boundary']) if r.get('boundary') else None
 exact=int((e-s).total_seconds()) if e else None; lower=int((b-s).total_seconds()) if (not e and b) else None
 target=r.get('target',900); active=r.get('active',False); term=r.get('term'); final=r.get('final',False); baton=r.get('baton',False); mut=r.get('mut',0)
 if e and final and baton and mut==1:c='VOLUNTARY_FINAL'
 elif not e and b and term=='toolpath_loss':c='TOOLPATH_LOSS_CANDIDATE'
 elif not e and b and term=='platform_runtime_kill':c='PLATFORM_RUNTIME_KILL_CANDIDATE'
 elif not e and b and not active and not final:c='ABRUPT_NONFINAL'
 else:c='UNKNOWN'
 crossed=(exact if exact is not None else lower or 0)>=target
 return c,exact,lower,crossed
cases=[
 ({'start':'2026-09-24T00:00:00Z','end':'2026-09-24T00:15:10Z','final':True,'baton':True,'mut':1},('VOLUNTARY_FINAL',910,None,True)),
 ({'start':'2026-09-24T00:00:00Z','boundary':'2026-09-24T00:06:51Z'},('ABRUPT_NONFINAL',None,411,False)),
 ({'start':'2026-09-24T00:00:00Z','boundary':'2026-09-24T00:05:00Z','term':'toolpath_loss'},('TOOLPATH_LOSS_CANDIDATE',None,300,False)),
 ({'start':'2026-09-24T00:00:00Z','boundary':'2026-09-24T00:14:59Z','term':'platform_runtime_kill'},('PLATFORM_RUNTIME_KILL_CANDIDATE',None,899,False)),
 ({'start':'2026-09-24T00:00:00Z','boundary':'2026-09-24T00:15:00Z','active':True},('UNKNOWN',None,900,True)),
 ({'start':'2026-09-24T15:05:22Z','end':'2026-09-24T15:12:13Z','final':True,'baton':True,'mut':1},('VOLUNTARY_FINAL',411,None,False)),
]
for i,(r,want) in enumerate(cases,1):
 got=validate(r); assert got==want,(i,got,want)
print('BUNDLE_ACCEPTANCE_PASS cases=6 exact_LT02=411 threshold=899/900 active_censored=UNKNOWN')

from datetime import datetime,timezone

def ts(v):
 d=datetime.fromisoformat(v.replace('Z','+00:00')); assert d.tzinfo is not None; return d.astimezone(timezone.utc)
def classify(start,end=None,bound=None,active=False,term=None,final=False,baton=False,mut=0,target=900):
 s=ts(start);e=ts(end) if end else None;b=ts(bound) if bound else None
 if e and e<s: raise ValueError('end precedes start')
 if b and b<s: raise ValueError('boundary precedes start')
 exact=int((e-s).total_seconds()) if e else None;lower=int((b-s).total_seconds()) if not e and b else None
 if e and final and baton and mut==1:c='VOLUNTARY_FINAL'
 elif not e and b and term=='toolpath_loss':c='TOOLPATH_LOSS_CANDIDATE'
 elif not e and b and term=='platform_runtime_kill':c='PLATFORM_RUNTIME_KILL_CANDIDATE'
 elif not e and b and not active and not final:c='ABRUPT_NONFINAL'
 else:c='UNKNOWN'
 return c,exact,lower,(exact if exact is not None else lower or 0)>=target

def resolve(s,b,cs):
 m=[x for x in cs if x.get('recognized_end') is True and x.get('start_id')==s and x.get('final_baton_id')==b]
 if not m:raise ValueError('NO_MATCHING_END')
 if len(m)!=1:raise ValueError('AMBIGUOUS_MATCHING_END')
 return m[0]
checks=[]
def ck(name,got,want): assert got==want,(name,got,want);checks.append(name)
ck('exact-910',classify('2026-09-24T00:00:00Z','2026-09-24T00:15:10Z',final=True,baton=True,mut=1),('VOLUNTARY_FINAL',910,None,True))
ck('lt02-411',classify('2026-09-24T15:05:22Z','2026-09-24T15:12:13Z',final=True,baton=True,mut=1),('VOLUNTARY_FINAL',411,None,False))
ck('abrupt-411',classify('2026-09-24T00:00:00Z',bound='2026-09-24T00:06:51Z'),('ABRUPT_NONFINAL',None,411,False))
ck('toolpath',classify('2026-09-24T00:00:00Z',bound='2026-09-24T00:05:00Z',term='toolpath_loss'),('TOOLPATH_LOSS_CANDIDATE',None,300,False))
ck('runtime-899',classify('2026-09-24T00:00:00Z',bound='2026-09-24T00:14:59Z',term='platform_runtime_kill'),('PLATFORM_RUNTIME_KILL_CANDIDATE',None,899,False))
ck('active-900',classify('2026-09-24T00:00:00Z',bound='2026-09-24T00:15:00Z',active=True),('UNKNOWN',None,900,True))
ck('zero-mutation-not-final',classify('2026-09-24T00:00:00Z','2026-09-24T00:15:00Z',final=True,baton=True,mut=0)[0],'UNKNOWN')
ck('two-mutation-not-final',classify('2026-09-24T00:00:00Z','2026-09-24T00:15:00Z',final=True,baton=True,mut=2)[0],'UNKNOWN')
ck('missing-baton-not-final',classify('2026-09-24T00:00:00Z','2026-09-24T00:15:00Z',final=True,mut=1)[0],'UNKNOWN')
ck('unique-end',resolve(1,2,[{'id':3,'start_id':1,'final_baton_id':2,'recognized_end':True}])['id'],3)
for name,cs,msg in [('no-end',[], 'NO_MATCHING_END'),('ambiguous',[{'id':3,'start_id':1,'final_baton_id':2,'recognized_end':True},{'id':4,'start_id':1,'final_baton_id':2,'recognized_end':True}],'AMBIGUOUS_MATCHING_END')]:
 try:resolve(1,2,cs);raise AssertionError(name)
 except ValueError as e:ck(name,str(e),msg)
try:classify('2026-09-24T00:00:10Z','2026-09-24T00:00:00Z');raise AssertionError('reverse')
except ValueError as e:ck('reverse-time',str(e),'end precedes start')
print('BUNDLE_V2_PASS checks=%d'%len(checks))

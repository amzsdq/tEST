from datetime import datetime

def sec(a,b): return int((datetime.fromisoformat(b.replace('Z','+00:00'))-datetime.fromisoformat(a.replace('Z','+00:00'))).total_seconds())
def resolve(s,b,cs):
 m=[c for c in cs if c.get('recognized_end') is True and c.get('start_id')==s and c.get('final_baton_id')==b]
 if not m: raise ValueError('NO_MATCHING_END')
 if len(m)!=1: raise ValueError('AMBIGUOUS_MATCHING_END')
 return m[0]
assert sec('2026-09-24T15:05:22Z','2026-09-24T15:12:13Z')==411
assert sec('2026-09-24T00:00:00Z','2026-09-24T00:15:00Z')==900
assert sec('2026-09-24T00:00:00Z','2026-09-24T00:14:59Z')==899
assert resolve(1,2,[{'id':3,'start_id':1,'final_baton_id':2,'recognized_end':True}])['id']==3
try: resolve(1,2,[{'id':3,'start_id':1,'final_baton_id':2,'recognized_end':True},{'id':4,'start_id':1,'final_baton_id':2,'recognized_end':True}]); raise AssertionError
except ValueError as e: assert str(e)=='AMBIGUOUS_MATCHING_END'
print('SELFTEST_PASS cases=5')

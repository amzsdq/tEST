"""Long-turn package admission policy, independent of wall-clock self-report."""

def decide(elapsed_server_seconds, target_seconds=900, stretch_seconds=1200, qualifying_work=True, finalization_safe=True):
 for name,v in [('elapsed_server_seconds',elapsed_server_seconds),('target_seconds',target_seconds),('stretch_seconds',stretch_seconds)]:
  if isinstance(v,bool) or not isinstance(v,int) or v<0:raise ValueError('invalid '+name)
 if target_seconds<=0 or stretch_seconds<target_seconds:raise ValueError('invalid target/stretch relationship')
 if elapsed_server_seconds>=target_seconds:
  if finalization_safe:return {'state':'RESERVE_ENTRY','admit_new_package':False,'reason':'minimum target crossed; preserve first success'}
  return {'state':'FINALIZATION_BLOCKED','admit_new_package':False,'reason':'target crossed but safe finalization unavailable'}
 if qualifying_work:return {'state':'CONTINUE','admit_new_package':True,'reason':'below target with qualifying work'}
 return {'state':'WORKLOAD_EXHAUSTED','admit_new_package':False,'reason':'below target but no qualifying work; do not pad'}

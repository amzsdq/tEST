EVENT_ID=E9-SCHEMA-REGEN-02
EXPERIMENT=E9-DURABLE-CONCURRENCY-01
SAMPLE=SCHEMA-REGEN-02
PROMPT_VERSION=P4V9
PRIMARY_VARIABLE=event self-sufficiency
RESULT=PASS
WRITE_OK=YES
STATE_OK=YES
WAKE_OK=YES
WORK_OK=YES
DUPLICATE=NO
START=2026-09-22 23:09:09 KST
END=2026-09-22 23:09:39 KST
ANOMALY=NONE
RECOVERY=NONE
NEXT=Cold-read this second event alone and compare its regenerated row shape against SCHEMA-REGEN-01.

Expected regeneration: identity, sample, prompt version, result, four status dimensions, duplicate state, timestamps, anomaly/recovery state, and NEXT are directly recoverable. Duration is derived from START and END. Other derived metrics remain blank unless their measurement inputs are present.

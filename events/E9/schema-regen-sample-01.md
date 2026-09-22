EVENT_ID=E9-SCHEMA-REGEN-01
EXPERIMENT=E9-DURABLE-CONCURRENCY-01
SAMPLE=SCHEMA-REGEN-01
PROMPT_VERSION=P4V9
PRIMARY_VARIABLE=event self-sufficiency
RESULT=PASS
WRITE_OK=YES
STATE_OK=YES
WAKE_OK=YES
WORK_OK=YES
DUPLICATE=NO
START=2026-09-22 22:57:57 KST
END=2026-09-22 22:59:00 KST
ANOMALY=NONE
RECOVERY=NONE
NEXT=Cold-read this event without the historical ledger and regenerate an equivalent row.

Expected regeneration: identity, sample, prompt version, result, four status dimensions, duplicate state, timestamps, anomaly/recovery state, and NEXT are directly recoverable. Duration is derived from START and END. Other derived metrics remain blank unless their measurement inputs are present.

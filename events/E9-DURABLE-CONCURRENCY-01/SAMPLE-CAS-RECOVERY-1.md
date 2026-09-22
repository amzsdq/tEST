# E9 Durable Concurrency Recovery Sample

EXPERIMENT=E9-DURABLE-CONCURRENCY-01
SAMPLE=CAS-RECOVERY-1
PROMPT_VERSION=P4V9
PRIMARY_VARIABLE=durable-state reconciliation write shape
PRIOR_FAILURE=Repeated full-file EXPERIMENT_LEDGER.md replacement returned SHA 409 under concurrent writes.
RECOVERY_METHOD=Preserve canonical ledger unchanged; persist new reconciliation evidence as a create-if-absent immutable event rather than retrying whole-ledger replacement.
RESULT=PASS
WRITE_OK=YES
STATE_OK=YES
WAKE_OK=YES
WORK_OK=YES
DUPLICATE=NO observed
INTERPRETATION=The relay can preserve historical canonical state and durably record new boundary evidence without contending on the shared ledger blob. This removes the observed lost-update/full-file-CAS failure surface for new evidence. It does not yet prove multi-writer ordering or materialized-view regeneration.
NEXT=Verify next-turn reconstruction from Issue tail plus immutable event, then test deterministic fold/materialization without making the materialized ledger canonical truth.

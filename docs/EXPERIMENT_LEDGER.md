# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| P4-WAKE-POS-01-A | P4V7 | routine positive wake field | 3m class | 1 | YES | YES via update return | omitted = YES on clean scheduled invocation | YES | non-authoritative | omitted = NO observed | inherited unchanged P1/E8 path | compact Issue sample without positive WAKE_OK + next-turn reconstruction | lower | PASS | SAMPLE-1 preserved active trial/order/status/NEXT; omitted WAKE_OK was unambiguous under P4V7 clean-success schema. |
| P4-WAKE-POS-01-B | P4V7 | routine positive wake field | 3m class | 1 | YES | YES via update return | omitted = YES on clean scheduled invocation | YES | non-authoritative | omitted = NO observed | inherited unchanged P1/E8 path | second reconstruction after transient Issue-write block | lower | PASS | SAMPLE-2 reconstructed SAMPLE-1; transient evidence-write block recovered on retry without scheduler/recovery changes. |

## Reconciliation note — 2026-09-22 21:18 KST

P4V7 positive WAKE_OK omission is provisionally promoted. SAMPLE-1 and SAMPLE-2 reconstructed the active experiment, ordering, result/status intent and NEXT from Issue records where routine clean-success positive WAKE_OK is implicit in the observed scheduled invocation. The transient Issue-write block before SAMPLE-2 recovered on retry and did not require scheduler mutation or rollback. WAKE_OK remains explicit for PENDING/NO, anomaly, recovery, rollback, boundary, and timing-specific evidence.

```text
CURRENT_CANDIDATE=P4V7 on P1 single-final-write path
LEAD_TIME=+3m class
SCHEDULER_WRITES_PER_WAKE=1
RECURRENCE=RRULE:FREQ=HOURLY
CHECKPOINT={operation_id, immutable epoch/claim fence, executable next_action}
AUTHORITY=immutable epoch + atomic create-if-absent claim
VERIFICATION=normal-path update-return validation; live read only on ambiguity/failure/reconciliation
BOOTSTRAP=Issue #1 compact tail first on routine clean-success; ledger/canonical docs only on boundary, ambiguity, prompt/promotion/rollback, or invariant recovery
ROUTINE_LOGGING=Issue #1 only; clean-success non-boundary schema={EXPERIMENT,SAMPLE,RESULT,WRITE_OK,STATE_OK,WORK_OK,NEXT}; omitted WAKE_OK means YES only for clean scheduled invocation; omitted DUPLICATE means NO duplicate/anomaly observed; START/END only for boundary/anomaly/rollback/timing evidence
KNOWN_FAILURES=+2m mixed reliability; dispatch timestamp anomalies; arbitrary external non-idempotent effects require destination support
RECOVERY_EVIDENCE=P1-2M-01 and E8-P1-COLD-01
NEXT_DISCRIMINATING_TEST=select one further simplification with P4V7 fixed; do not alter scheduler, +3m lead, checkpoint, authority, verification, bootstrap, or recovery semantics
```

## Historical baseline

Prior detailed trials and reconciliation history remain recoverable from Git history and Issue #1. This boundary compaction intentionally retains the promoted current candidate and the immediately discriminating P4V7 evidence while avoiding routine duplication.
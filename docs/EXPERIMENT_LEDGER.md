# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| P1-10M-01 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | +73s vs intended due | NO observed | n/a | research state restored and trial evaluated | low | PASS | Intended due 11:44:02 KST; automation turn observed at 11:45:15 KST. |
| P1-10M-02 | P0R/P1 path | lead time | 10m class | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Issue evidence: intended 11:57:00; runtime context 11:56:14. |
| P1-10M-03 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Third consecutive +10m-class continuation. |
| P1-5M-01 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | First +5m continuation. |
| P1-5M-02 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Second +5m continuation. |
| P1-5M-03 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Third +5m continuation. |
| P1-3M-01 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | First +3m continuation. |
| P1-3M-02 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Reconciled from Issue #1; intended 12:29:00 KST, run context 12:28:16 KST. |
| P1-3M-03 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | third identical +3m sample | low | PASS_WITH_TIMING_ANOMALY | Issue #1 records +3m class reaching 3/3 end-to-end continuation. |
| P1-2M-01 | P0R/P1 path | lead time | 2m | 1 | YES | YES | NO near wake | YES after fallback | n/a | NO observed | YES | hourly RRULE cold recovery | low | MISSED_NEAR_OCCURRENCE + RECOVERY_PASS | First +2m sample missed fast continuation; recurring fallback recovered. |
| P1-2M-02 | P0R/P1 path | lead time | 2m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored | low | PASS_WITH_TIMING_ANOMALY | Mixed +2m evidence; not suitable as reliable default. |
| P1-3M-04 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | prior E5 evidence | boundary confirmation | low | PASS | +3m retained as leading minimum practical default. |
| TEMPLATE | P0 | baseline | 1m | 6 | - | - | - | - | - | - | - | - | - | PENDING | |

## Reconciliation note — 2026-09-22

Issue #1 contained fresher controlled-trial evidence than this file. The stale `P1-3M-02=PENDING` row was corrected rather than treated as a live unfinished trial. Issue evidence also showed P1-3M-03, P1-2M-01, P1-2M-02, and P1-3M-04 had already executed. This ledger now reflects those outcomes.

Current scheduler candidate after reconciliation:

```text
CURRENT_CANDIDATE=P0R/P1 single-final-write path
LEAD_TIME=+3m
SCHEDULER_WRITES_PER_WAKE=1
RECURRENCE=RRULE:FREQ=HOURLY
KNOWN_FAILURES=+2m mixed reliability; runtime-context timing offsets are non-authoritative
RECOVERY_EVIDENCE=P1-2M-01 recovered through hourly RRULE fallback
NEXT_DISCRIMINATING_TEST=continue the already-started P2-3M-01 comparison before inventing another trial
```

## Result vocabulary

- PASS: end-to-end intended behavior observed
- WRITE_FAIL: scheduler update rejected
- STATE_MISMATCH: stored scheduler state differs from requested state
- MISSED_NEAR_OCCURRENCE: requested near-term occurrence did not invoke
- DUPLICATE_EXECUTION: more than one actor performed substantive work
- RECOVERY_PASS: injected failure recovered from durable state
- RECOVERY_FAIL: durable recovery did not restore correct continuation
- INCONCLUSIVE: observation insufficient to distinguish hypotheses

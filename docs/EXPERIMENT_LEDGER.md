# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

## Current compact trial table

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| P1-10M-01 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | +73s vs intended due | NO observed | n/a | research state restored and trial evaluated | low | PASS | Intended due 11:44:02 KST; automation turn observed at 11:45:15 KST. |
| P1-10M-02 | P0R/P1 path | lead time | 10m class | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Issue evidence: intended 11:57:00; runtime context 11:56:14. |
| P1-10M-03 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | third identical +10m sample | low | PASS_WITH_TIMING_ANOMALY | Third consecutive +10m-class continuation. |
| P1-5M-01 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | First +5m continuation. |
| P1-5M-02 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Second +5m continuation. |
| P1-5M-03 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | third identical +5m sample | low | PASS_WITH_TIMING_ANOMALY | Third +5m continuation. |
| P1-3M-01 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | First +3m continuation. |
| P1-3M-02 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Reconciled from Issue #1. |
| P1-3M-03 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | third identical +3m sample | low | PASS_WITH_TIMING_ANOMALY | Issue #1 records +3m class reaching 3/3 end-to-end continuation. |
| P1-2M-01 | P0R/P1 path | lead time | 2m | 1 | YES | YES | NO near wake | YES after fallback | n/a | NO observed | YES | hourly RRULE cold recovery | low | MISSED_NEAR_OCCURRENCE + RECOVERY_PASS | First +2m sample missed fast continuation; recurring fallback recovered. |
| P1-2M-02 | P0R/P1 path | lead time | 2m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored | low | PASS_WITH_TIMING_ANOMALY | Mixed +2m evidence; not suitable as reliable default. |
| P1-3M-04 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | prior E5 evidence | boundary confirmation | low | PASS | +3m retained as leading minimum practical default. |
| P2-3M-01 | P0R/P2 path | provisional fallback presence | 3m final | 2 | YES | YES | YES | YES | non-authoritative | NO observed | no incremental benefit | normal-path comparison | higher than P1 | PASS_BUT_REJECTED | Added one scheduler mutation without demonstrated recovery/correctness gain over P1. |
| E8-P1-COLD-01 | P0R/P1 path | omit final fast rearm after durable checkpoint | hourly fallback | 0 after checkpoint | n/a | YES | YES | YES | ~59m recovery | NO observed | YES | cold resume from GitHub | low | RECOVERY_PASS | Existing hourly RRULE recovered without P2 provisional write. |
| E7-AUTHORITY | P0R/P1 path | duplicate authority/recovery | 3m fixed | 1 | n/a | YES | YES | YES | n/a | 0 | YES | atomic claim/recovery research | research-only | PASS_WITH_CONSTRAINT | Immutable epoch fencing + create-if-absent claim; external effects still require idempotency/reconciliation. |
| E8-MINIMAL-CHECKPOINT | P0R/P1 path | checkpoint schema | 3m fixed | 1 | YES | YES | YES | YES | n/a | 0 | YES | repeated interruption/resume | low | PASS | Minimal schema promoted: operation_id + immutable epoch/claim fence + executable next_action; fence-removal adverse test failed safely. |

Historical P4 compaction/verification samples remain authoritative in Issue #1 and git history; do not infer their absence from this compact view as evidence loss.

## Large-package scale ledger

For P5M4 package-size experiments, Issue #1 remains the raw durable evidence stream. This section records boundary summaries rather than every tool action.

| Trial | Planned | Done | Saturated | Semantic outputs | Outputs/10 units | Artifacts | Artifact I/O | I/O per output | Scheduler writes | Result |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| LW15-A | 15 | 15 | NO | >=5 | >=3.33 | 2 | measured in Issue baton | normalized/disclosed | 1 | CAPACITY_GAIN_DIRECTIONAL_RETEST |
| LW15-B | 15 | 15 | NO | 8 | 5.33 | 2 | 8 | 1.00 | 1 | PROMOTE_FOR_SEMANTIC_CAPACITY |
| LW16 | 22 | 22 | NO | 11 | 5.00 | 3 | 12 | 1.09 | 1 | CAPACITY_GAIN_22_OF_22_NO_SATURATION |
| LW17 | 34 target | PENDING | PENDING | PENDING | PENDING | 4 target | PENDING | PENDING | 1 target | ACTIVE |

### Scale interpretation contract
- Capacity asks whether additional eligible downstream-value work completes without extra scheduler/control cost or remainder loss.
- Density asks whether semantic outputs per 10 eligible units stay materially useful as scale grows.
- Raw artifact I/O is not semantic output. Compare `ARTIFACT_IO_PER_SEMANTIC_OUTPUT` separately.
- Every claimed result-dependent transition must record `SELECTED_BY=<validated result> -> <later target>`.
- `SATURATED=YES` requires eligible remainder caused by runtime/blocker/safety, with exact stage and immediate next action.
- `NO_MORE_ELIGIBLE_WORK` is not saturation and is preferable to fabricated units.
- WORKED is GitHub START→END telemetry and never substitutes for semantic-capacity or density evidence.

## Reconciliation contract
Routine non-boundary evidence lives in Issue #1. Reconcile this ledger at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read.
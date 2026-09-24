# Relay Experiment Ledger

## Canonical storage contract
Issue #1 is the canonical append-only raw experiment stream. Git history preserves every prior ledger version. This document is a **current boundary index**, not permission to erase history: historical rows omitted from the compact current view remain authoritative in Issue #1 and git history and MUST be restored from the latest full-history commit when a full ledger export/reconciliation is required.

Never interpret absence from a compact view as a failed or deleted trial.

## Current scheduler/recovery boundary rows

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Recovery? | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---|---|---|
| P1-10M-01..03 | P0R/P1 | lead time | 10m class | 1 | YES | YES | YES | YES | n/a | PASS family | Three generous-lead end-to-end samples; timing offsets non-authoritative. |
| P1-5M-01..03 | P0R/P1 | lead time | 5m | 1 | YES | YES | YES | YES | n/a | PASS family | Three +5m continuations. |
| P1-3M-01..04 | P0R/P1 | lead time | 3m | 1 | YES | YES | YES | YES | prior cold evidence | PASS family | +3m promoted practical default. |
| P1-2M-01 | P0R/P1 | lead time | 2m | 1 | YES | YES | NO near wake | YES after fallback | YES | MISSED_NEAR_OCCURRENCE + RECOVERY_PASS | Demonstrates mixed +2m reliability and hourly cold recovery. |
| P1-2M-02 | P0R/P1 | lead time | 2m | 1 | YES | YES | YES | YES | n/a | PASS_WITH_TIMING_ANOMALY | Mixed +2m evidence; not reliable default. |
| P2-3M-01 | P0R/P2 | extra provisional write | 3m | 2 | YES | YES | YES | YES | no incremental benefit | PASS_BUT_REJECTED | Extra scheduler mutation rejected as default. |
| E8-P1-COLD-01 | P0R/P1 | cold recovery | hourly fallback | 0 after checkpoint | n/a | YES | YES | YES | YES | RECOVERY_PASS | Existing hourly recurrence recovered without provisional write. |
| E7-AUTHORITY | P0R/P1 | authority | 3m | 1 | n/a | YES | YES | YES | YES | PASS_WITH_CONSTRAINT | Epoch/fence + atomic claim; external effects still need idempotency/reconciliation. |
| E8-MINIMAL-CHECKPOINT | P0R/P1 | checkpoint | 3m | 1 | YES | YES | YES | YES | YES | PASS | Minimal checkpoint promoted. |

### Historical P4 evidence pointer
P4V0–P4V11 verification, compact logging, bootstrap, positive-field omission, jitter, and server-timestamp samples are preserved in Issue #1 and prior full ledger commits. A boundary audit that needs row-level P4 history MUST reconstruct it from those sources rather than treating this index as exhaustive.

## Large-package scale ledger

For P5M4 package-size experiments, Issue #1 remains the raw durable evidence stream. This section is the current comparison surface.

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
- Every claimed result-dependent transition records `SELECTED_BY=<validated result> -> <later target>`.
- `SATURATED=YES` requires eligible remainder caused by runtime/blocker/safety, with exact stage and immediate next action.
- `NO_MORE_ELIGIBLE_WORK` is not saturation and is preferable to fabricated units.
- WORKED is GitHub START→END telemetry and never substitutes for semantic-capacity or density evidence.

## Reconciliation contract
Routine non-boundary evidence lives in Issue #1. Reconcile this index at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read. Full-history reconciliation restores omitted historical rows from Issue #1/git history before claiming completeness.
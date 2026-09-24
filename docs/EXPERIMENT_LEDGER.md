# Relay Experiment Ledger

## Canonical storage contract
Issue #1 is the canonical append-only raw experiment stream. Git history preserves every prior ledger version. This document is a current boundary index, not permission to erase history. Historical rows omitted from the compact view remain authoritative in Issue #1/git history.

Never interpret absence from a compact view as a failed or deleted trial.

## Current scheduler/recovery boundary rows

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Recovery? | Result |
|---|---|---|---:|---:|---|---|---|---|---|---|
| P1-10M-01..03 | P0R/P1 | lead time | 10m class | 1 | YES | YES | YES | YES | n/a | PASS family |
| P1-5M-01..03 | P0R/P1 | lead time | 5m | 1 | YES | YES | YES | YES | n/a | PASS family |
| P1-3M-01..04 | P0R/P1 | lead time | 3m | 1 | YES | YES | YES | YES | prior cold evidence | PASS family |
| P1-2M-01 | P0R/P1 | lead time | 2m | 1 | YES | YES | NO near wake | YES after fallback | YES | MISSED_NEAR_OCCURRENCE + RECOVERY_PASS |
| P1-2M-02 | P0R/P1 | lead time | 2m | 1 | YES | YES | YES | YES | n/a | PASS_WITH_TIMING_ANOMALY |
| P2-3M-01 | P0R/P2 | extra provisional write | 3m | 2 | YES | YES | YES | YES | no benefit | PASS_BUT_REJECTED |
| E8-P1-COLD-01 | P0R/P1 | cold recovery | hourly fallback | 0 after checkpoint | n/a | YES | YES | YES | YES | RECOVERY_PASS |
| E7-AUTHORITY | P0R/P1 | authority | 3m | 1 | n/a | YES | YES | YES | YES | PASS_WITH_CONSTRAINT |
| E8-MINIMAL-CHECKPOINT | P0R/P1 | checkpoint | 3m | 1 | YES | YES | YES | YES | YES | PASS |

## Large-package scale ledger

| Trial | Planned | Done | Saturated | Semantic outputs | Outputs/10 | Artifacts | Artifact I/O | I/O/output | Scheduler writes | Result |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| LW15-A | 15 | 15 | NO | >=5 | >=3.33 | 2 | Issue baton | disclosed | 1 | CAPACITY_GAIN_DIRECTIONAL_RETEST |
| LW15-B | 15 | 15 | NO | 8 | 5.33 | 2 | 8 | 1.00 | 1 | PROMOTE_FOR_SEMANTIC_CAPACITY |
| LW16 | 22 | 22 | NO | 11 | 5.00 | 3 | 12 | 1.09 | 1 | CAPACITY_GAIN_22_OF_22_NO_SATURATION |
| LW17 | 34 | 34 | NO | 14 | 4.12 | 4 | disclosed in Issue | disclosed | 1 | CAPACITY_GAIN_WITH_DENSITY_WARNING |
| LW18 | 34 target | ACTIVE | PENDING | PENDING | guardrail 4.13 | 4 target | full baseline | PENDING | 1 target | FROZEN_REPEAT |

## Frozen LW18 measurement contract

A semantic output is exactly one validated durable rule, specification, or decision with a named downstream consequence. Summaries, stylistic edits, raw reads/writes, and merely restated evidence count zero.

A result-dependent transition is auditable only when recorded as `SELECTED_BY=<prior validated result> -> <later substantive target>`. The later target must not have been substantively fixed before the prior validation.

LW18 freezes the LW17 persistence baseline: candidate persist -> fresh fetch -> criteria-first review -> defect-caused revision persist -> fresh fetch -> validation for each eligible artifact. Persistence thinning is explicitly out of scope for this repeat.

Density guardrail is frozen at 4.13 semantic outputs per 10 eligible units. With target 34 units, 14 outputs yields 4.12 and 15 yields 4.41; therefore an ordinary CAPACITY_GAIN verdict requires at least 15 counted semantic outputs, no saturation, and no remainder loss. A lower count is DENSITY_DEGRADED unless concrete higher-value adjudication is named and auditable.

Capacity and density are separate. WORKED is GitHub START->END telemetry only. Raw artifact I/O is reported separately. Scheduler policy remains one final recurring mutation with +3m lead.

## Reconciliation contract
Routine non-boundary evidence lives in Issue #1. Reconcile this index at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read.
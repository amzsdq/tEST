# Relay Experiment Ledger

## Canonical storage contract
Issue #1 is the canonical append-only raw experiment stream. Git history preserves every prior ledger version. This document is a current boundary index, not permission to erase history. Historical rows omitted from the compact view remain authoritative in Issue #1/git history. Never interpret absence from a compact view as a failed or deleted trial.

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

## Large-package / work-shaping ledger
| Trial | Planned | Done | Saturated | Semantic outputs | Outputs/10 | Primary variable | Candidate-boundary I/O | Scheduler writes | Result |
|---|---:|---:|---|---:|---:|---|---:|---:|---|
| LW15-A | 15 | 15 | NO | >=5 | >=3.33 | package size | disclosed | 1 | CAPACITY_GAIN_DIRECTIONAL_RETEST |
| LW15-B | 15 | 15 | NO | 8 | 5.33 | package size repeat | 8 | 1 | PROMOTE_FOR_SEMANTIC_CAPACITY |
| LW16 | 22 | 22 | NO | 11 | 5.00 | package size scale | 12 | 1 | CAPACITY_GAIN_22_OF_22_NO_SATURATION |
| LW17 | 34 | 34 | NO | 14 | 4.12 | package size scale | full baseline | 1 | CAPACITY_GAIN_WITH_DENSITY_WARNING |
| LW18 | 34 | 34 | NO | 16 | 4.71 | frozen 34-unit repeat | full baseline | 1 | PROMOTE_30_36_SCALE_FOR_SEMANTIC_CAPACITY_AND_DENSITY |
| LW19 | 34 | 34 | NO | 18 | 5.29 | value-gated target selection | full baseline | 1 | DIRECTIONAL_PROMOTION_RETEST |
| LW20 | 34 | 34 | NO | 18 | 5.29 | value-gate repeatability | full baseline | 1 | PROMOTE_AS_DEFAULT_VALUE_GATED_TARGET_SELECTION |
| LW21 | ~34 | completed eligible package | NO | audited | non-inferior | persistence thinning | FULL=8; THIN=0; source reads=2 | 1 | BOUNDED_THINNING_POSITIVE_RETEST |

## Frozen semantic-output contract
A semantic output is exactly one validated durable rule, specification, or decision with a named downstream consequence. Summaries, stylistic edits, raw reads/writes, and merely restated evidence count zero. Two statements with the same downstream consequence count once unless they independently change different named decisions. Each counted output is logged as `OUTPUT_ID`, `DURABLE_CHANGE`, `DOWNSTREAM_CONSEQUENCE`, `VALIDATED_BY`. Result dependency requires `SELECTED_BY=<prior validated result> -> <later substantive target>`.

## Promoted boundaries
- 30–36 eligible-unit pre-shaped packages are promoted for semantic capacity+density under tested conditions; this is not a 10-minute wall-time guarantee.
- VALUE_GATED_TARGET_SELECTION is the default target selector under tested conditions: LW19 and LW20 independently produced 18/34 = 5.29 outputs/10 on different candidate pools versus LW18 4.71/10.
- Single final scheduler mutation remains the control baseline.

## Persistence boundary under test
LW21 separated target value from persistence eligibility. FULL_CHAIN remains mandatory when policy/source-of-truth mutation or representation-dependent review makes persisted reality authoritative. THIN_ELIGIBLE is limited to reconstructible audit/decision work where named durable inputs are authoritative and candidate persistence adds no authority. LW21 observed two thin targets with `OMITTED_BOUNDARY_DEFECT=0`, while a FULL_CHAIN fresh-fetch caught a real regression in a policy artifact. This is one positive bounded sample only; LW22 repeats before broader default promotion.

### LW22 carried-forward reconciliation review
TARGET=boundary truth; FAILURE_MODE=ledger still showed LW19 ACTIVE and omitted completed LW20/LW21 boundaries; REQUIRED_CHANGE=replace stale LW19 row and add LW20/LW21. RESOLVED in candidate.
TARGET=promotion truth; FAILURE_MODE=index did not state value-gated selection had repeated at 5.29/10 and been promoted; REQUIRED_CHANGE=record promoted default explicitly. RESOLVED in candidate.
TARGET=persistence experiment boundary; FAILURE_MODE=index lacked the FULL-vs-THIN distinction and could make thinning appear globally promoted; REQUIRED_CHANGE=record bounded class and repeat requirement. RESOLVED in candidate.

## Telemetry separation
Capacity, density, persistence I/O, and WORKED are separate. WORKED is GitHub START->END telemetry only. Source reads remain artifact I/O and are never counted as thinning savings. Any extra scheduler mutation makes a sample control-non-comparable.

## Reconciliation contract
Routine non-boundary evidence lives in Issue #1. Reconcile this index at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read.
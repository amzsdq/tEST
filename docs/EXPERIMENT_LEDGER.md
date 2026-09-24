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
| LW21 | ~34 | 30 eligible | NO | 10 | audited non-inferior | persistence thinning | FULL=8; THIN=0; source reads=2 | 1 | BOUNDED_THINNING_POSITIVE_RETEST |
| LW22 | 30-36 | 30 | NO | 15 | 5.00 | persistence thinning repeat | FULL candidate-boundary=16; THIN=0; source reads=4 | 1 | PROMOTE_BOUNDED_THINNING_DEFAULT |
| LW24 | multi-package | 11 packages | runtime-margin stop | 36 | invocation metric | same-invocation auto-refill | combined refill boundaries | 1 | DIRECTIONAL_PASS_RETEST |
| LW25 | multi-package | 7 packages | runtime-margin stop | 25 | invocation metric | auto-refill repeatability | combined refill boundaries | 1 | PROMOTE_AUTO_REFILL_DEFAULT |

## Frozen semantic-output contract
A semantic output is exactly one validated durable rule, specification, or decision with a named downstream consequence. Summaries, stylistic edits, raw reads/writes, and merely restated evidence count zero. Two statements with the same downstream consequence count once unless they independently change different named decisions. Each counted output is logged as `OUTPUT_ID`, `DURABLE_CHANGE`, `DOWNSTREAM_CONSEQUENCE`, `VALIDATED_BY`. Result dependency requires `SELECTED_BY=<prior validated result> -> <later substantive target>`.

## Promoted boundaries
- 30–36 eligible-unit pre-shaped packages are promoted for semantic capacity+density under tested conditions; this is a per-package boundary, not an invocation cap or wall-time guarantee.
- VALUE_GATED_TARGET_SELECTION is the default target selector under tested conditions: LW19 and LW20 independently produced 18/34 = 5.29 outputs/10 on different candidate pools versus LW18 4.71/10.
- BOUNDED THIN_ELIGIBLE routing is promoted for reconstructible audit/decision work after LW21 and LW22 independent positive samples. FULL_CHAIN remains mandatory for authoritative mutation, newly persisted decision evidence, and representation-dependent validation.
- Thin audit may discover that mutation is required; the mutation then escalates to FULL_CHAIN. This is correct routing, not a thinning failure.
- AUTO_REFILL is the default invocation work-loop after LW24 and independent LW25 repeat: `PACKAGE_COMPLETE != TURN_COMPLETE`; validated package completion triggers immediate same-invocation refill while useful work remains.
- `NEXT_PACKAGE` is a recovery pointer, not an unconditional cold-start command; revalidate current authority before side effects.
- Source reads remain artifact I/O and never count as thinning savings. Any defect attributable specifically to an omitted candidate boundary rolls back the affected thin class.
- Single final scheduler mutation remains the control baseline.

## Active boundary: P5M7 / E12 FINALIZATION RESERVE
AUTO_REFILL remains promoted. E12 tests only when to stop admitting NEW substantive packages so the invocation can durably commit final baton + sole scheduler mutation + END marker. First baseline predeclares a conservative 240-second package-boundary cutoff. Prior successful finalization envelopes measured from GitHub server timestamps are 23s (LW24) and 25s (LW25); n=2 is insufficient to set a minimum reserve. Package completion remains a refill trigger outside the reserve. Reserve timing is telemetry/safety, never a work quota.

## Telemetry separation
Capacity, density, persistence I/O, refill count, reserve timing, and WORKED are separate. WORKED is GitHub START->END telemetry only. Source reads remain artifact I/O and are never counted as thinning savings. Any extra scheduler mutation makes a sample control-non-comparable.

## Reconciliation contract
Routine non-boundary evidence lives in Issue #1. Reconcile this index at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read.
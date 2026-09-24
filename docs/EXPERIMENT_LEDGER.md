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

## Large-package scale ledger
| Trial | Planned | Done | Saturated | Semantic outputs | Outputs/10 | Artifacts | Artifact I/O | I/O/output | Scheduler writes | Result |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| LW15-A | 15 | 15 | NO | >=5 | >=3.33 | 2 | Issue baton | disclosed | 1 | CAPACITY_GAIN_DIRECTIONAL_RETEST |
| LW15-B | 15 | 15 | NO | 8 | 5.33 | 2 | 8 | 1.00 | 1 | PROMOTE_FOR_SEMANTIC_CAPACITY |
| LW16 | 22 | 22 | NO | 11 | 5.00 | 3 | 12 | 1.09 | 1 | CAPACITY_GAIN_22_OF_22_NO_SATURATION |
| LW17 | 34 | 34 | NO | 14 | 4.12 | 4 | full baseline/disclosed | disclosed | 1 | CAPACITY_GAIN_WITH_DENSITY_WARNING |
| LW18 | 34 | 34 | NO | 16 | 4.71 | 4 | full baseline | disclosed | 1 | PROMOTE_30_36_SCALE_FOR_SEMANTIC_CAPACITY_AND_DENSITY |
| LW19 | 34 target | ACTIVE | PENDING | PENDING | compare >4.71 | 4 target | full baseline | PENDING | 1 target | VALUE_GATED_TARGET_SELECTION |

## Frozen semantic-output contract
A semantic output is exactly one validated durable rule, specification, or decision with a named downstream consequence. Summaries, stylistic edits, raw reads/writes, and merely restated evidence count zero. Two statements with the same downstream consequence count once unless they independently change different named decisions. Each counted output is logged as `OUTPUT_ID`, `DURABLE_CHANGE`, `DOWNSTREAM_CONSEQUENCE`, `VALIDATED_BY`. Result dependency requires `SELECTED_BY=<prior validated result> -> <later substantive target>`.

## LW18 promotion boundary
LW18 repeated 34/34 eligible units with SATURATED=NO and 16 audited outputs = 4.71/10 under the frozen contract, one scheduler mutation, +3m lead, and full persisted-output baseline. This clears the 4.13 guardrail and promotes 30–36 units for semantic capacity+density under tested P5M4 conditions. It does not establish a 10-minute wall-time guarantee or arbitrary larger-scale safety.

## LW19 target-selection comparison
Primary variable is target-selection quality, not package size. Package target remains 34 and full persistence/control policy is frozen. Candidate scoring dimensions/minimum/tie-break are predeclared in `docs/VALUE_GATED_TARGET_SELECTION.md`; rejected candidates remain auditable. Promotion requires raw density >4.71/10 at unchanged control cost, or a rigorously falsifiable value override at non-inferior density.

### Q fresh-fetch review
TARGET=boundary truth; FAILURE_MODE=prior index left LW18 ACTIVE after Issue #1 had already promoted it; REQUIRED_CHANGE=reconcile completed row and promotion boundary. RESOLVED.
TARGET=counting continuity; FAILURE_MODE=old LW18-specific heading could imply counting expired with the trial; REQUIRED_CHANGE=rename as frozen semantic-output contract carried into LW19. RESOLVED.
TARGET=causal isolation; FAILURE_MODE=target-selection trial could accidentally vary scale/persistence/control; REQUIRED_CHANGE=state primary variable and frozen baseline explicitly. RESOLVED.

Q_VALIDATION=PASS. The index now matches Issue #1 boundary and prevents stale ACTIVE state or counting-contract ambiguity from contaminating LW19 comparison.
SELECTED_BY=Q_VALIDATION(stale-boundary reconciliation exposed maturity-map drift risk) -> R focus: update evidence maturity so 30–36 is promoted while target-selection remains OPEN and long-duration remains unproven.

## Telemetry separation
Capacity, density, and WORKED are separate. WORKED is GitHub START->END telemetry only. Raw artifact I/O is reported separately. Any extra scheduler mutation makes a sample control-non-comparable.

## Reconciliation contract
Routine non-boundary evidence lives in Issue #1. Reconcile this index at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read.
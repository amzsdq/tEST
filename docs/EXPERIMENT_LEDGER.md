# Relay Experiment Ledger

## Canonical storage contract
Issue #1 is the canonical append-only raw experiment stream. Git history preserves prior ledger versions. This document is a compact current boundary index; omission never means failed/deleted evidence.

## Promoted scheduler/recovery boundary
- One final recurring scheduler mutation is the normal control baseline.
- Practical +3m lead remains current; 2m has mixed evidence.
- Issue #1 compact tail is routine recovery authority; broader docs are cold-path.
- GitHub START/END `created_at` is the WORKED clock.

## Work-shaping / persistence boundary
| Trial | Result |
|---|---|
| LW18 | PROMOTE 30–36 eligible-unit per-package semantic-capacity range |
| LW20 | PROMOTE VALUE_GATED_TARGET_SELECTION default |
| LW22 | PROMOTE bounded THIN_ELIGIBLE for reconstructible audit/decision; FULL_CHAIN for authoritative mutation/representation-dependent validation |
| LW24 | AUTO_REFILL directional pass: 11 packages / 36 outputs |
| LW25 | PROMOTE AUTO_REFILL default: 7 packages / 25 outputs; cold NEXT revalidation hardened |

## E12 finalization-reserve ledger
| Trial | Cutoff | Packages | Semantic outputs | D | A/B/C | Overrun | Scheduler writes | Result |
|---|---:|---:|---:|---:|---|---|---:|---|
| LW26 | 240s | 8 | 42 | not normalized | 22/31/53s | observed policy | 1 | SAFE_DIRECTIONAL |
| LW27 | 240s | 16 | 46 | not normalized | 13/21/34s | observed policy | 1 | 240S_CONSERVATIVE_REPEAT_CONFIRMED |
| LW28 | 250s | 12 | 50 | 43s | 11/26/37s | YES; last admission +224 -> reserve +267 | 1 | 250S_DIRECTIONAL_SAFE_WITH_PACKAGE_OVERRUN |
| LW29 | 250s | 33 | UNKNOWN (prior running cumulative labels unaudited) | edge 8s; late samples 13s,6s,8s | 8/17/25s | YES; edge admission +249 -> +257 | 1 | PROMOTE_250S_TESTED_CUTOFF_CURRENT_CONDITIONS |
| LW30 | 260s | 16 | UNKNOWN_PENDING_AUDIT | 8s | 9/13/22s | YES by admission-cutoff semantics | 1 | 260S_DIRECTIONAL_SAFE_NONADVERSE |
| LW31 | 260s | active repeat | audited IDs only / else UNKNOWN | active | pending | pending | target 1 | 260S_REPEAT_ACTIVE |

## Current promoted boundaries
- 30–36 is per-package guidance, not invocation cap or wall-time guarantee.
- `PACKAGE_COMPLETE != TURN_COMPLETE`; same-invocation AUTO_REFILL is default while useful work remains.
- `NEXT_PACKAGE` is a recovery pointer, not unconditional cold-start command.
- Source reads remain artifact I/O.
- 250s is a TESTED new-package admission cutoff only within current relay/finalization conditions after independent LW28+LW29 safe samples. It is not a universal runtime ceiling or arbitrary-package safety guarantee.
- 260s has one directional-safe sample (LW30) and remains unpromoted until independent LW31 repeat safely commits continuation.
- Adverse/ambiguous 260s evidence rolls back to 250s. 240s is older conservative fallback only if a shared-mode defect invalidates the 250s sample family.

## E12 telemetry contract
A=`RESERVE_ENTRY->FINAL_BATON`; B=`FINAL_BATON->END`; C=`RESERVE_ENTRY->END`. D=`last admitted boundary->reserve entry` captures package exposure/overrun separately. Cutoff controls admission, not D after admission. `PACKAGE_OVERRUN` is not failure unless continuation is lost. Future step-down decisions review D and C jointly. Do not infer a fixed runtime ceiling from near-300s traces; do not poll time per action or sleep/pad.

## Frozen semantic-output contract
A semantic output is one validated durable rule/specification/decision with a named downstream consequence. Summaries, stylistic edits, raw reads/writes, and restated evidence count zero. Audited counting requires OUTPUT_ID / DURABLE_CHANGE / DOWNSTREAM_CONSEQUENCE / VALIDATED_BY; otherwise report UNKNOWN. Result dependency requires `SELECTED_BY` from prior validated result to later substantive target.

## Reconciliation contract
Routine non-boundary evidence stays in Issue #1. Reconcile this index at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read.
# Large-Package Scale Protocol

Status: PROMOTED through tested 30–36 eligible-unit package scale under P5M4/P5M5 work-shaping conditions; compatible with P5M6 same-invocation refill.

## Objective
Maximize eligible semantic work per package while preserving continuation reliability and avoiding control/persistence work that exists only to inflate duration. Package scale does not define invocation length.

## Promoted scale evidence
- LW15-B: 15/15, 8 semantic outputs, 5.33/10.
- LW16: 22/22, 11 semantic outputs, 5.00/10.
- LW17: 34/34, 14 outputs, 4.12/10 -> density warning.
- LW18 frozen repeat: 34/34, SATURATED=NO, 16 audited outputs, 4.71/10 -> clears 4.13 guardrail and promotes 30–36 scale.
- Scheduler/control baseline: one final recurring mutation, +3m lead.
Promotion scope is semantic capacity+density per package only. No 10-minute guarantee, no safety claim beyond 36 units in one package, and no implication that an invocation ends when a package ends.

## Scale decision algorithm
1. Pre-shape only eligible work for the current package.
2. Rank competing eligible work with the promoted value gate; value score never changes persistence eligibility.
3. Keep result-dependent substantive focus unresolved; record SELECTED_BY.
4. Execute current package until completion, genuine saturation, or eligible-work convergence.
5. Preserve exact remainder on saturation.
6. On PACKAGE_COMPLETE, hand control to the invocation-level refill rule; do not infer TURN_COMPLETE.
7. Measure package capacity, density, persistence cost, refill count, and WORKED separately.
8. Scale one package beyond 36 only as a separate experiment; multiple promoted-size packages in one invocation are instead an AUTO_REFILL experiment and do not violate the per-package scale boundary.

## Semantic-output contract
One output = one validated durable rule/spec/decision with named downstream consequence. Duplicate consequence counts once. Summary/style/read-write bookkeeping counts zero. Audit with OUTPUT_ID / DURABLE_CHANGE / DOWNSTREAM_CONSEQUENCE / VALIDATED_BY.

## Target-selection layer
Package-size eligibility does not rank competing eligible work. VALUE_GATED_TARGET_SELECTION is promoted as the default selector within tested conditions: LW19 and LW20 independently completed 34/34 on different candidate pools with 18 outputs=5.29/10 versus LW18 4.71/10. Frozen dimensions are decision reach, unresolved uncertainty, falsifiability, and downstream reuse; scoring cannot force persistence or justify post-hoc cherry-picking.

## Persistence interaction
Target score and persistence eligibility are separate gates. FULL_CHAIN remains mandatory where persisted representation/source mutation matters. Bounded THIN_ELIGIBLE is promoted for reconstructible audit/decision work after LW21/LW22; necessary source reads remain I/O and any omitted-boundary defect rolls back the affected thin class.

## P5M6 auto-refill interaction
`PACKAGE_COMPLETE != TURN_COMPLETE`. A completed 30–36-unit package is a queue/refill boundary, not a stop signal. If the parent goal remains incomplete and useful non-redundant work exists, derive another substantive package and execute it in the same invocation. Refill boundaries do not mutate the scheduler. Fast package completion is spare capacity, not evidence that package scale should be inflated.

## Long-duration interpretation
Larger packages increased semantic capacity and produced some multi-minute samples, but elapsed time remains telemetry and is not monotonic with unit count. Auto-refill addresses unused invocation capacity by adding more useful packages rather than making one package artificially larger or slower.

## Required package fields
PACKAGE, UNITS_PLANNED/DONE/REMAINING, PACKAGE_COMPLETE, SATURATED, semantic outputs/output IDs, density, downstream decisions, SELECTED_BY, target-selection evidence if active, artifacts, artifact I/O, I/O/output, COMPARABILITY, RESULT.

## Required invocation fields
PACKAGES_COMPLETED, REFILL_BOUNDARIES, cumulative semantic outputs, CONTROL_IO, WORKED, STOP_REASON, exact NEXT/REMAINDER. Scheduler writes belong to invocation-level control accounting, not each package.
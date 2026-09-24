# Large-Package Scale Protocol

Status: CANDIDATE synthesized from LW15–LW17 evidence.

## Objective
Maximize eligible semantic work per invocation while preserving continuation reliability and avoiding control/persistence work that exists only to inflate duration.

## Scale evidence entering LW17
- 15-unit packages: two independent completions; LW15-B recorded 8 semantic outputs, 5.33 outputs/10 units, artifact I/O/output 1.00.
- 22-unit package: LW16 completed 22/22 with no saturation, 11 semantic outputs, 5.00 outputs/10, artifact I/O/output 1.09.
- Scheduler/control policy remained one final mutation and +3m lead.

Inference: semantic capacity scaled from 15 to 22 without observed density collapse. This does not establish a 10-minute duration guarantee.

## Scale decision algorithm
1. Pre-shape only eligible work. Every unit must remove decision-required evidence uncertainty, make a material durable change, create an independent validation boundary, correct a material defect, or synthesize evidence into a changed downstream decision.
2. Keep result-dependent targets unresolved. Record `SELECTED_BY=<prior validated result> -> <later target>`.
3. Execute continuously until package completion, genuine saturation, or eligible-work convergence.
4. Record exact remainder on saturation; never replace unfinished work with a new package.
5. Measure capacity and density separately from WORKED.
6. Increase the next scale point only if control policy is unchanged, remainder is preserved, and density does not cross the degradation guardrail without compensating downstream value.
7. If density degrades, stop scale-up and remove weak units or improve target selection before retrying.
8. If artifact I/O/output rises while semantic density remains healthy, test persistence thinning as a separate controlled variable; do not silently change both variables.

## Density guardrail
Reference from LW15-B + LW16 ≈ 5.17 semantic outputs / 10 eligible units. Experimental degradation threshold = 80% of reference ≈ 4.13 outputs/10.

Classification:
- `CAPACITY_GAIN`: more eligible work/semantic outputs, no saturation/remainder loss, density >= guardrail, unchanged control policy.
- `CAPACITY_GAIN_WITH_DENSITY_WARNING`: more capacity but density below guardrail with explicitly adjudicated high-value outputs; repeat before promotion.
- `DENSITY_DEGRADED`: nominal scale rises but output density falls below guardrail without compensating value.
- `SATURATED`: runtime/blocker/safety interrupts with eligible remainder; exact handoff required.
- `NO_MORE_ELIGIBLE_WORK`: useful work converged before nominal target; not saturation.
- `CAPACITY_REGRESSION`: weak/fabricated units, lost remainder, extra control I/O, or density degradation without compensating value.

## Persistence interaction
Full persist/fresh-fetch/review/revise/fresh-fetch chains remain the safe baseline for artifact classes where persisted reality matters. Track correction yield and I/O/output. Thinning is a separate non-inferiority experiment after repeated comparable low-correction samples; never thin implicitly during a package-size scale trial.

## Long-duration interpretation
A larger package may increase WORKED because it contains more real work, but elapsed time is telemetry. The target is maximum useful-work density and capacity, not reaching a clock quota. A 10-minute guarantee remains unproven until an intrinsically large eligible package actually produces it without padding.

## Required baton fields for scale trials
PACKAGE, UNITS_PLANNED/DONE/REMAINING, PACKAGE_COMPLETE, SATURATED, SEMANTIC_OUTPUTS, SEMANTIC_OUTPUTS_PER_10_UNITS, DOWNSTREAM_DECISIONS_CHANGED, RESULT_DEPENDENT_TRANSITIONS, ARTIFACTS_CHANGED, ARTIFACT_IO_RAW, ARTIFACT_IO_PER_SEMANTIC_OUTPUT, CONTROL_IO, WORKED, RESULT, exact NEXT.
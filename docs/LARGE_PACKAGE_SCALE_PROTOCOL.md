# Large-Package Scale Protocol

Status: CANDIDATE synthesized from LW15–LW17 evidence.

## Objective
Maximize eligible semantic work per invocation while preserving continuation reliability and avoiding control/persistence work that exists only to inflate duration.

## Scale evidence entering LW17
- LW15-B: 15/15, 8 semantic outputs, 5.33 outputs/10, artifact I/O/output 1.00.
- LW16: 22/22, no saturation, 11 semantic outputs, 5.00 outputs/10, artifact I/O/output 1.09.
- Scheduler/control policy: one final mutation, +3m lead.

Inference: semantic capacity scaled 15→22 without observed density collapse. This does not establish a 10-minute duration guarantee.

## Scale decision algorithm
1. Pre-shape only eligible work: decision-required evidence, material durable semantic change, independent persisted validation, material defect correction, or synthesis that changes a downstream decision.
2. Keep result-dependent targets unresolved; record `SELECTED_BY=<prior validated result> -> <later target>`.
3. Execute continuously until package completion, genuine saturation, or eligible-work convergence.
4. On saturation record exact remainder and resume it first next turn.
5. Measure capacity, density, persistence cost, and WORKED separately.
6. Increase scale only if control policy is unchanged, remainder is preserved, and density remains above the guardrail or an explicit value adjudication justifies the lower count.
7. If density degrades, stop scale-up and improve target selection/remove weak units.
8. If artifact I/O/output rises while density remains healthy, test persistence thinning separately; never silently vary both package size and persistence policy.

## Semantic-output counting contract
A semantic output is one validated durable rule/spec/decision change with a named downstream consumer or consequence. Multiple bullets implementing the same decision count once. A summary of prior outputs counts zero unless it changes a future decision. Record enough text in the baton to audit the count.

## Density guardrail
Reference = mean of LW15-B and LW16 = ~5.17 semantic outputs/10 eligible units. Experimental degradation threshold = 80% = ~4.13 outputs/10.

- `CAPACITY_GAIN`: more eligible work/semantic outputs, no saturation/remainder loss, density >=4.13, unchanged control policy.
- `CAPACITY_GAIN_WITH_DENSITY_WARNING`: capacity rises but density <4.13 and specific outputs are adjudicated as materially higher downstream value; requires repeat before promotion.
- `DENSITY_DEGRADED`: density <4.13 without compensating value.
- `SATURATED`: runtime/blocker/safety interrupts with eligible remainder.
- `NO_MORE_ELIGIBLE_WORK`: eligible work converges before nominal target; not saturation.
- `CAPACITY_REGRESSION`: weak/fabricated units, lost remainder, extra control I/O, or unmitigated density degradation.

## Comparability contract
Capacity comparison requires unchanged scheduler mutation count and lead policy plus the same unit-eligibility/counting rules. Artifact count and raw artifact I/O may scale with package size; disclose them and normalize I/O/output. If a package changes persistence policy, semantic-output definition, scheduler policy, or eligibility threshold, mark the affected attribution `NON_COMPARABLE` rather than crediting package size.

## Persistence interaction
Full persisted chains remain the safe baseline where persisted reality matters. Track correction yield and I/O/output. Thinning is a separate controlled non-inferiority experiment after repeated comparable low-correction samples; never thin implicitly during package-size scaling.

## Long-duration interpretation
Larger packages may increase WORKED because they contain more real work, but elapsed time is telemetry. A 10-minute guarantee remains unproven until an intrinsically large eligible package actually produces it without padding.

## Required baton fields
PACKAGE, UNITS_PLANNED/DONE/REMAINING, PACKAGE_COMPLETE, SATURATED, SEMANTIC_OUTPUTS with named consequences, SEMANTIC_OUTPUTS_PER_10_UNITS, DOWNSTREAM_DECISIONS_CHANGED, RESULT_DEPENDENT_TRANSITIONS/SELECTED_BY, ARTIFACTS_CHANGED, ARTIFACT_IO_RAW, ARTIFACT_IO_PER_SEMANTIC_OUTPUT, CONTROL_IO, COMPARABILITY, WORKED, RESULT, exact NEXT.
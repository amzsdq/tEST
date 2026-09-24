# Same-Invocation Auto-Refill Protocol

Status: EXPERIMENTAL — P5M6 / E11 first multi-package sample

## Purpose
Use fast package completion as spare execution capacity. Increase useful work per invocation by continuing with another substantive package instead of ending merely because the current package is complete.

## Primary invariant
`PACKAGE_COMPLETE != TURN_COMPLETE`

A package is a bounded work-shaping unit. An invocation is the execution opportunity that may contain multiple packages. Package completion transfers control to refill evaluation; it does not itself authorize invocation termination.

## Refill transition
After package N validates:
1. Persist one compact `REFILL_BOUNDARY` with package result, cumulative semantic outputs, and result-dependent next target.
2. Reassess the parent GOAL against current durable evidence.
3. If useful non-redundant work remains, derive package N+1 using the promoted value gate.
4. Freeze target/persistence routing for N+1 as required by existing contracts.
5. Execute N+1 immediately in the SAME invocation.
6. Repeat.

Do not mutate the scheduler at steps 1-5. The normal scheduler mutation occurs exactly once at actual invocation end.

## Valid stop conditions
- `PROGRAM_COMPLETE`: parent goal is actually completed and validated.
- `GENUINE_EXTERNAL_BLOCKER`: no useful independent goal-directed work can proceed because of an external/physical/permission dependency.
- `RUNTIME_OR_SAFETY_LIMIT`: runtime, tool, or safety constraint prevents safe continuation.
- `NO_USEFUL_WORK_REMAINS`: evidence-based reassessment finds no non-redundant goal-directed work.

Not stop conditions: current TO-DO exhausted; package complete; artifact/test/review complete; checkpoint written; semantic-output quota reached; next schedule prepared.

## Work eligibility
Refill never relaxes eligibility. A refill package must contain substantive work with downstream decision value, uncertainty or real correction need, and a discriminating result. Value-gated target selection remains active. Persistence mode remains separately gated. A package created merely to keep the invocation alive is `REFILL_INVALID_PADDING`.

## Persistence interaction
`REFILL_BOUNDARY` is compact recovery state, not a substitute for FULL_CHAIN where persisted representation matters. THIN_ELIGIBLE remains restricted to reconstructible audit/decision work. A thin audit requiring source mutation escalates that mutation to FULL_CHAIN.

## Scale interaction
The promoted 30–36 range is a per-package semantic-capacity boundary. Auto-refill may execute multiple packages in one invocation without claiming that a single package above 36 is safe. Do not inflate one package merely to increase wall time.

## Crash/recovery semantics
If runtime terminates after a REFILL_BOUNDARY but before N+1 completes, the boundary's `NEXT_PACKAGE` is the durable recovery pointer. If termination occurs mid-package, persist exact remainder when possible; otherwise recover from the latest boundary plus durable artifact state. A refill checkpoint never claims the following package completed.

## Metrics
Per invocation record:
- `PACKAGES_COMPLETED`
- `REFILL_BOUNDARIES`
- cumulative `UNITS_DONE`
- cumulative `SEMANTIC_OUTPUTS`
- `ARTIFACT_IO`
- `REFILL_IO`
- `CONTROL_IO`
- GitHub-server `WORKED`
- `STOP_REASON`
- exact `NEXT/REMAINDER`

Per package retain package units, density, downstream consequences, SELECTED_BY, persistence mode, and validation result.

## First-sample acceptance
Directional `REFILL_GAIN` requires:
- package 1 completes substantively;
- useful work remains;
- package 2 is derived from actual package-1 evidence;
- package 2 performs substantive work in the same invocation;
- no filler/padding;
- no scheduler mutation at refill boundary;
- exactly one normal scheduler mutation at actual invocation end.

Promotion requires repeat multi-package samples. One successful invocation is not sufficient for default promotion.

## Rollback / adverse evidence
Reject or narrow auto-refill if it causes duplicate side effects, stale-authority overwrite, lost recovery state, extra scheduler mutations, material quality regression, or systematic creation of low-value work. Runtime saturation is not a failure; record `REFILL_SATURATED_RUNTIME` with exact recovery state.
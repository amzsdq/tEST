# Same-Invocation Auto-Refill Protocol

Status: EXPERIMENTAL — P5M6 / E11 repeat validation active

## Purpose
Use fast package completion as spare execution capacity. Increase useful work per invocation by continuing with another substantive package instead of ending merely because the current package is complete.

## Primary invariant
`PACKAGE_COMPLETE != TURN_COMPLETE`

A package is a bounded work-shaping unit. An invocation is the execution opportunity that may contain multiple packages. Package completion transfers control to refill evaluation; it does not itself authorize invocation termination.

## Refill transition
After package N validates:
1. Persist one compact combined package-result/refill record with completed package identity, key result, last validation, cumulative accounting, exact next substantive package, and `SELECTED_BY` evidence.
2. Reassess the parent GOAL against current durable evidence.
3. If useful non-redundant work remains, derive package N+1 using the promoted value gate.
4. Freeze target/persistence routing for N+1 as required by existing contracts.
5. Execute N+1 immediately in the SAME invocation.
6. Repeat.

The refill record REPLACES a redundant per-package END/BATON; do not write both when one durable record can carry package completion and recovery-pointer semantics. Do not mutate the scheduler at refill boundaries. The normal scheduler mutation occurs exactly once at actual invocation end.

## Valid stop conditions
- `PROGRAM_COMPLETE`: parent goal is actually completed and validated.
- `GENUINE_EXTERNAL_BLOCKER`: no useful independent goal-directed work can proceed because of an external/physical/permission dependency.
- `RUNTIME_OR_SAFETY_LIMIT`: runtime, tool, or safety constraint prevents safe continuation.
- `NO_USEFUL_WORK_REMAINS`: evidence-based reassessment finds no non-redundant goal-directed work.

Not stop conditions: current TO-DO exhausted; package complete; artifact/test/review complete; checkpoint written; semantic-output quota reached; next schedule prepared.

## Work eligibility
Refill never relaxes eligibility. A refill package must contain substantive work with downstream decision value, uncertainty or real correction need, and a discriminating result. Value-gated target selection remains active. Persistence mode remains separately gated. A package created merely to keep the invocation alive is `REFILL_INVALID_PADDING`.

## Persistence interaction
The combined refill record is compact recovery state, not a substitute for FULL_CHAIN where persisted representation matters. THIN_ELIGIBLE remains restricted to reconstructible audit/decision work. A thin audit requiring source mutation escalates that mutation to FULL_CHAIN. If a package's authoritative completion already exists in a required artifact/effect receipt, the refill record should point to that evidence rather than duplicate its body, while still retaining exact NEXT and cumulative accounting.

## Scale interaction
The promoted 30–36 range is a per-package semantic-capacity boundary. Auto-refill may execute multiple packages in one invocation without claiming that a single package above 36 is safe. Do not inflate one package merely to increase wall time.

## Crash/recovery semantics
A boundary must distinguish `package N validated` from `package N+1 started/completed`. It records `PACKAGE_COMPLETE=YES` only for N and never pre-claims N+1. If runtime terminates after the boundary but before N+1 completes, `NEXT_PACKAGE` plus `SELECTED_BY` is the durable recovery pointer and cumulative counters provide the accounting baseline. If termination occurs mid-package, persist exact stage/remainder when possible; otherwise recover from the latest boundary plus durable artifact/effect state. On cold recovery, never increment completed-package or semantic-output counters for work lacking validation evidence.

`NEXT_PACKAGE` is a recovery pointer, not an unconditional execution command. On cold recovery, revalidate the recorded next package against current authoritative state and the promoted value/persistence gates before causing substantive or external side effects. If intervening durable state already completed, invalidated, or superseded that target, record `RECOVERY_NEXT_STALE` and derive a new eligible package from the same parent goal without incrementing completion counters for the stale target. Same-invocation refill may rely on the immediately preceding validation when no intervening authority change is possible; cold recovery may not assume that freshness.

A generic durable `PACKAGE_START` marker is NOT a correctness requirement. It proves only attempted execution, not committed side effects. Invocation-level START/END remain the WORKED clock. Targets whose replay can cause unsafe duplicate effects require target/effect-level stable identity plus authoritative receipt/status or an equivalently strong checkpoint.

## Required combined package-result/refill fields
- `PACKAGE`
- `PACKAGE_COMPLETE=YES`
- `RESULT`
- `LAST_VALIDATION`
- `UNITS_DONE_CUMULATIVE` when unit accounting is active
- `SEMANTIC_OUTPUTS_CUMULATIVE`
- `NEXT_PACKAGE`
- `SELECTED_BY`
- `TURN_COMPLETE=NO`

Optional package-local metrics may be added only when material. The record must remain compact enough for hot-path recovery.

## Metrics
Per invocation record: `PACKAGES_COMPLETED`, `REFILL_BOUNDARIES`, cumulative `UNITS_DONE`, cumulative `SEMANTIC_OUTPUTS`, `ARTIFACT_IO`, `REFILL_IO`, `CONTROL_IO`, GitHub-server `WORKED`, `STOP_REASON`, exact `NEXT/REMAINDER`.

Per package retain package units when meaningful, density, downstream consequences, SELECTED_BY, persistence mode, and validation result.

## First-sample acceptance
Directional `REFILL_GAIN` requires package 1 complete substantively; useful work remains; package 2 is derived from actual package-1 evidence; package 2 performs substantive work in the same invocation; no filler/padding; no scheduler mutation at refill boundary; exactly one normal scheduler mutation at actual invocation end.

Promotion requires repeat multi-package samples. One successful invocation is not sufficient for default promotion.

## Rollback / adverse evidence
Reject or narrow auto-refill if it causes duplicate side effects, stale-authority overwrite, lost recovery state, extra scheduler mutations, material quality regression, counter inflation after crash, or systematic creation of low-value work. If cold recovery from the combined record cannot identify last validated package + exact next package + cumulative counters, restore richer boundary fields; do not add redundant package-end records by default. Runtime saturation is not a failure; record `REFILL_SATURATED_RUNTIME` with exact recovery state.
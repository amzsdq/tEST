# Same-Invocation Auto-Refill Protocol

Status: PROMOTED DEFAULT within tested P5M6 / E11 relay conditions after independent LW24 + LW25 multi-package repeats

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

## E12 directional finalization reserve
Auto-refill must preserve enough execution opportunity to commit continuation state. Elapsed time is a safety signal, never a work quota.

At substantive package boundaries only, compare an external clock against the invocation START marker. A predeclared reserve threshold may stop admission of a NEW substantive package; it does not interrupt an already-validating package merely to hit a timestamp. On reserve entry, preserve exact unfinished useful work, write the final baton, perform the sole scheduler mutation, and append END.

First E12 baseline predeclares a conservative 240-second new-package cutoff before observing its endpoint. This cutoff is directional evidence only: it is not promoted until repeated safe-finalization samples show that continuation safety improves without material useful-work loss. Runtime ending before finalization is `RESERVE_TOO_SMALL`; a large unused margin in one sample is `RESERVE_CONSERVATIVE`, not permission for post-hoc shrinking.

Two prior successful auto-refill turns provide observed final-baton -> scheduler-update -> END envelopes of 23s (LW24) and 25s (LW25), measured from GitHub comment `created_at`. Treat these as sparse empirical tail samples, not a safe minimum. The 240s first cutoff intentionally reserves much more than 25s.

Normalize E12 tail telemetry before comparing samples: record (A) `RESERVE_ENTRY -> FINAL_BATON`, (B) `FINAL_BATON -> END`, and (C) `RESERVE_ENTRY -> END` separately. Do not compare a C-duration against an older B-duration as if they were the same metric. For LW26 the authoritative timestamps yield A=22s, B=31s, C=53s. This is evidence about the 240s baseline, not proof of a fixed runtime ceiling.

Interpret a live reserve sample using the following frozen rule:
- `SAFE_FINALIZATION`: final baton, sole scheduler mutation, and END all commit after reserve entry.
- `RESERVE_TOO_SMALL`: execution terminates or loses continuation state before those three steps complete.
- `RESERVE_CONSERVATIVE`: safe finalization occurs and observed finalization tail is materially below the available reserve; this is evidence for a later controlled repeat, not authority to shrink within the same run.
- `PACKAGE_OVERRUN`: a package admitted before cutoff completes after the cutoff. Preserve the observation; do not relabel it as reserve failure unless finalization is lost.

Package-boundary clock checks are preferred over per-action polling because finalization risk changes meaningfully at package admission boundaries while per-action checks add control overhead without a demonstrated safety gain. If a package class later demonstrates a tail capable of consuming the reserve by itself, add class-specific admission evidence rather than globally polling every action.

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

For E12 reserve trials additionally record: `RESERVE_CUTOFF_SECONDS`, last admitted package boundary elapsed, reserve-entry elapsed, final-baton server time when available, END server time, observed finalization-tail seconds, `PACKAGE_OVERRUN`, and whether exact unfinished useful work was preserved.

Per package retain package units when meaningful, density, downstream consequences, SELECTED_BY, persistence mode, and validation result.

## Promotion evidence
LW24 demonstrated 11 substantive packages in one invocation without package-complete early exit and with one final scheduler mutation. LW25 independently repeated same-invocation refill across multiple substantive packages using the combined boundary from package 1, and exposed/hardened cold-recovery stale-NEXT handling. Within tested relay conditions, auto-refill is therefore the default invocation work-loop. This does not promote filler, unbounded single-package size, or unsafe replay.

## Rollback / adverse evidence
Reject or narrow auto-refill if it causes duplicate side effects, stale-authority overwrite, lost recovery state, extra scheduler mutations, material quality regression, counter inflation after crash, or systematic creation of low-value work. If cold recovery from the combined record cannot identify last validated package + exact next package + cumulative counters, restore richer boundary fields; do not add redundant package-end records by default. Runtime saturation is not a failure; record `REFILL_SATURATED_RUNTIME` with exact recovery state.
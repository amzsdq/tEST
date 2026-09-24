# Relay Research Program v0.7

Status: ACTIVE — work-shaping, bounded persistence routing, same-invocation auto-refill promoted; E12 finalization reserve optimizing
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that keeps a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, remains recoverable after missed wakes, and avoids duplicate execution?

## Experiment families
E1 RRULE self-shift; E2 minimum lead-time; E3 mutation stress; E4 provisional/final relay; E5 missed-wake recovery; E6 cross-automation wake; E7 duplicate authority; E8 durable cold-resume; E9 useful-work/package shaping; E10 persistence-boundary optimization; E11 same-invocation auto-refill; E12 invocation-tail/finalization reserve.

## Metrics
Primary: continuation success, missed intended wake rate, duplicate substantive execution, dispatch delay, useful-work duty cycle, recovery latency, semantic useful outputs per invocation.
Secondary: scheduler mutations per useful-work minute, bootstrap/control overhead, artifact I/O per semantic output, stale-state reconciliation, packages completed per invocation, refill success rate, finalization success under long refill chains.

## Promotion principle
Repeated evidence is required. One favorable trace is directional only. Claims must be scoped to the layer actually tested. Wall time is telemetry and never independently promotes a work-shaping mechanism.

## Canonical current pointer / cold-start fast path
Routine recovery uses Issue #1 compact tail. Broaden only for ambiguity/reconciliation or substantive artifact work. No second mutable current-state mirror by default.

## E9 — Long useful-work / package capacity
LW15–LW18 established a tested 30–36 eligible-unit operating range for semantic capacity+density. This is per-package guidance, not an invocation cap or wall-time guarantee. VALUE_GATED_TARGET_SELECTION is the default selector after independent LW19/LW20 positive samples.

## E10 — Persistence-boundary optimization
FULL_CHAIN is mandatory when later decisions depend on newly persisted reality, policy/source-of-truth is mutated, or representation drift is material. THIN_ELIGIBLE is promoted for reconstructible audit/decision work with named durable inputs and zero omitted-boundary defects in LW21/LW22. Source reads remain artifact I/O.

## E11 — Same-invocation auto-refill
Status: PROMOTED DEFAULT after independent LW24 and LW25 multi-package samples.

Primary invariant: `PACKAGE_COMPLETE != TURN_COMPLETE`. A completed package triggers parent-goal reassessment and immediate same-invocation refill while useful work remains. Valid stop conditions are PROGRAM_COMPLETE, genuine external blocker with no independent work, runtime/tool/safety constraint, or evidence-based NO_USEFUL_WORK_REMAINS. Exactly one scheduler mutation remains at actual invocation end. `NEXT_PACKAGE` is a cold-revalidated recovery pointer, not an unconditional command.

## E12 — Invocation-tail / finalization reserve
Auto-refill can consume the invocation too close to finalization, so E12 controls only admission of NEW substantive packages. Elapsed time is a safety signal, never a work quota.

LW26 and LW27 independently used a predeclared 240-second new-package cutoff and safely committed final baton + sole scheduler mutation + END. Normalized A/B/C tails were 22/31/53s and 13/21/34s. Thus 240s is `CONSERVATIVE_REPEAT_CONFIRMED`, not a required minimum.

LW28 tested the predeclared 250-second cutoff and safely finalized with A/B/C=11/26/37s. Its last package was admitted at +224s and reserve entry occurred at +267s, giving a 43s observed admission-to-next-boundary exposure and `PACKAGE_OVERRUN=YES`. This is `DIRECTIONAL_SAFE_WITH_PACKAGE_OVERRUN`, not promotion. LW29 repeats 250s unchanged.

### E12 frozen constraints
- GitHub-server timestamps are the WORKED clock.
- Check elapsed time at substantive package admission boundaries, not every action.
- Do not sleep/pad or interrupt active validation merely to hit cutoff.
- Reserve protects exact remainder + final baton + one scheduler mutation + END.
- Normalize A=`RESERVE_ENTRY->FINAL_BATON`, B=`FINAL_BATON->END`, C=`RESERVE_ENTRY->END`.
- Use C for reserve-safety comparisons; B-like sparse historical tails are not C-equivalent.
- `PACKAGE_OVERRUN` is not failure unless continuation is lost.
- For packages admitted after +200s in LW29, observe admission elapsed and next validated-boundary elapsed. This is telemetry only; do not alter the 250s policy mid-run.
- If repeated late-package evidence shows a class can materially consume reserve, evaluate class-specific admission evidence before global per-action polling.
- Two safe independent 250s samples are required before treating 250s as tested cutoff. Adverse/ambiguous finalization restores 240s.
- Do not infer a fixed runtime ceiling from near-300s traces.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` as the first queue head, not an invocation cap. Issue #1 remains durable authority. During a live invocation the in-memory queue may refill repeatedly; only the actual end-of-turn automation mutation writes the next persisted TO-DO and schedule.
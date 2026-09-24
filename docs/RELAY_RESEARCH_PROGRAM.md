# Relay Research Program v0.6

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
Package-size trials LW15–LW18 established a tested 30–36 eligible-unit operating range for semantic capacity+density under one final scheduler mutation and practical +3m lead. LW17 warned on density; LW18 repeated 34/34 with 16 outputs=4.71/10 and promoted the range. This does not guarantee 10-minute wall time or safety above 36.

### Target-selection layer
LW19 introduced a frozen value gate: decision reach, unresolved uncertainty, falsifiability, downstream reuse. LW19 and LW20 each completed 34/34 on different candidate pools with 18 audited semantic outputs=5.29/10 versus LW18 4.71/10, without scheduler/control regression. VALUE_GATED_TARGET_SELECTION is therefore the default selector within tested conditions.

### Work-shaping invariants
- Pre-shape only eligible work; never pad.
- Later substantive targets may be result-dependent and record SELECTED_BY.
- Semantic output = validated durable rule/spec/decision with named downstream consequence; duplicate consequence counts once.
- Preserve exact remainder on saturation.
- Measure package capacity, semantic density, persistence I/O, refill count, and WORKED separately.

## E10 — Persistence-boundary optimization
Target value and persistence eligibility are separate decisions.

FULL_CHAIN is mandatory when later decisions depend on newly persisted reality, policy/source-of-truth is being mutated, or representation drift is itself material: candidate persist → fresh fetch → criteria-first review → defect-caused revision persist → fresh fetch → validation.

THIN_ELIGIBLE is promoted as a bounded default for reconstructible audit/decision work when named durable inputs are authoritative/freshly readable, exact decision fields can be reconstructed, candidate persistence adds no authority, and omission cannot hide relevant representation drift. LW21 and LW22 provided independent positive samples with zero omitted-boundary defects. Source reads remain artifact I/O and are not counted as thinning savings.

### Persistence review invariants
- `PERSISTENCE_MODE` freezes before substantive execution; only mandatory rollback after a thinning failure may change it.
- FULL_CHAIN fresh-fetch review compares persisted representation against the predeclared acceptance contract, not merely file existence.
- THIN_ELIGIBLE review names authoritative durable inputs, reconstructs exact decision fields, and reports `OMITTED_BOUNDARY_DEFECT` explicitly.
- Thin audit may discover authoritative mutation is required; that mutation escalates to FULL_CHAIN and is correct routing.
- Candidate-boundary operations avoided and necessary source-read I/O are reported separately.
- Any defect attributable specifically to an omitted candidate boundary immediately rolls back the affected thin class.

## E11 — Same-invocation auto-refill
Status: PROMOTED DEFAULT within tested P5M6 conditions after independent LW24 and LW25 multi-package samples.

Primary invariant: `PACKAGE_COMPLETE != TURN_COMPLETE`.

A completed package is a refill trigger. Reassess the parent goal and unresolved durable state immediately. If useful goal-directed work remains, derive the next concrete substantive package and execute it in the same invocation. The combined package-result/refill record is compact durable recovery state, not a scheduler mutation and not a turn ending.

Valid turn-stop conditions are limited to: PROGRAM_COMPLETE; genuine external blocker with no useful independent work; runtime/tool/safety constraint; or evidence-based NO_USEFUL_WORK_REMAINS. Completing a TO-DO, artifact, package, checkpoint, semantic-output quota, or scheduler preparation is not a stop condition.

### E11 promoted invariants
- Never sleep, pad, repeat converged analysis, fabricate defects, or create low-value artifacts to lengthen elapsed time.
- Fast package completion is spare capacity and causes refill.
- Exactly one scheduler mutation remains at actual invocation end; refill boundaries do not touch the schedule.
- One compact combined result/refill record per validated package is the current recovery lower bound under Issue #1 authority; do not add separate package END records.
- `NEXT_PACKAGE` is a recovery pointer, not an unconditional cold-start command; revalidate it against current authority before side effects.
- Generic per-package START markers are not replay protection; unsafe effects need effect-level stable identity/receipt.
- Track packages completed, useful outputs, control I/O, refill-boundary I/O, and GitHub-server WORKED separately.

## E12 — Invocation-tail / finalization reserve
Auto-refill increases useful work but creates a new failure mode: continuing useful packages too close to an unknown runtime ceiling could prevent the single required final scheduler mutation and END marker. E12 seeks the smallest evidence-based reserve that protects continuation without turning elapsed time into a work target.

LW26 and LW27 independently used a predeclared 240-second new-package admission cutoff and both safely committed final baton + sole scheduler mutation + END. Normalized tails were LW26 A/B/C=22/31/53s and LW27=13/21/34s. Therefore 240s is `CONSERVATIVE_REPEAT_CONFIRMED` within observed conditions, not a promoted minimum.

LW28 is a separate predeclared 250-second controlled step-down. One safe 250s sample remains directional and requires repeat before promotion. Any lost continuation, `RESERVE_TOO_SMALL`, or materially ambiguous finalization margin restores 240s for the next trial.

Research constraints:
- GitHub-server timestamps remain the only WORKED clock.
- Check elapsed time at substantive package admission boundaries, not every trivial action.
- Do not sleep or pad to hit a duration.
- Tail policy reserves durable baton + one scheduler mutation + END marker.
- Record normalized A=`RESERVE_ENTRY->FINAL_BATON`, B=`FINAL_BATON->END`, C=`RESERVE_ENTRY->END`.
- `PACKAGE_OVERRUN` is recorded separately from reserve failure.
- Do not infer a fixed runtime ceiling from one near-300-second trace.
- Do not promote a smaller reserve from one favorable sample.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` near the top. It is the first queue head, not a cap on invocation work. Issue #1 remains durable authority. During a live invocation the in-memory queue may refill repeatedly; only the single actual end-of-turn automation mutation writes the next persisted TO-DO and schedule.
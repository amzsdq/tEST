# Relay Research Program v0.4

Status: ACTIVE — work-shaping defaults promoted; bounded persistence routing promoted; same-invocation auto-refill under test
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that keeps a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, remains recoverable after missed wakes, and avoids duplicate execution?

## Experiment families
E1 RRULE self-shift; E2 minimum lead-time; E3 mutation stress; E4 provisional/final relay; E5 missed-wake recovery; E6 cross-automation wake; E7 duplicate authority; E8 durable cold-resume; E9 useful-work/package shaping; E10 persistence-boundary optimization; E11 same-invocation auto-refill.

## Metrics
Primary: continuation success, missed intended wake rate, duplicate substantive execution, dispatch delay, useful-work duty cycle, recovery latency, semantic useful outputs per invocation.
Secondary: scheduler mutations per useful-work minute, bootstrap/control overhead, artifact I/O per semantic output, stale-state reconciliation, packages completed per invocation, refill success rate.

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
Primary invariant: `PACKAGE_COMPLETE != TURN_COMPLETE`.

A completed package is a refill trigger. Reassess the parent goal and unresolved durable state immediately. If useful goal-directed work remains, derive the next concrete substantive package and execute it in the same invocation. A refill boundary is a compact durable recovery checkpoint, not a scheduler mutation and not a turn ending.

Valid turn-stop conditions are limited to: PROGRAM_COMPLETE; genuine external blocker with no useful independent work; runtime/tool/safety constraint; or evidence-based NO_USEFUL_WORK_REMAINS. Completing a TO-DO, artifact, package, checkpoint, semantic-output quota, or scheduler preparation is not a stop condition.

### E11 anti-gaming / validation
- Never sleep, pad, repeat converged analysis, fabricate defects, or create low-value artifacts to lengthen elapsed time.
- Fast package completion is spare capacity and should cause refill.
- Exactly one scheduler mutation remains at actual invocation end; refill boundaries do not touch the schedule.
- A valid first sample must show at least one completed package followed by a second substantive package in the same invocation when useful work remains.
- Track packages completed, useful outputs, control I/O, refill-boundary I/O, and GitHub-server WORKED separately.
- Promotion requires repeat evidence; one successful multi-package invocation is directional only.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` near the top. It is the first queue head, not a cap on invocation work. Issue #1 remains durable authority. During a live invocation the in-memory queue may refill repeatedly; only the single actual end-of-turn automation mutation writes the next persisted TO-DO and schedule.
# Relay Research Program v0.2

Status: ACTIVE — LW15 large-package capacity trial, fresh-fetch reviewed
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that keeps a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, remains recoverable after missed wakes, and avoids duplicate execution?

## Experiment families
E1 RRULE self-shift; E2 minimum lead-time; E3 mutation stress; E4 provisional/final relay; E5 missed-wake recovery; E6 cross-automation wake; E7 duplicate authority; E8 durable cold-resume; E9 useful-work/package shaping.

## Metrics
Primary: continuation success, missed intended wake rate, duplicate substantive execution, dispatch delay, useful-work duty cycle, recovery latency, semantic useful outputs per invocation.
Secondary: scheduler mutations per useful-work minute, bootstrap/control overhead, artifact I/O per semantic output, stale-state reconciliation.

## Promotion principle
Repeated evidence is required. One favorable trace is directional only. Claims must be scoped to the layer actually tested.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior.

## Canonical current pointer / cold-start fast path
Routine recovery uses Issue #1 compact tail. Broaden only for ambiguity/reconciliation or substantive artifact work. No second mutable current-state mirror by default.

## E9 — Long useful-work / package capacity

### Research question
Is short WORKED partly caused by a package acceptance boundary that is too small, such that a much larger package of independently useful work yields materially more semantic output before normal termination?

### Baseline definition
The small-package baseline is the recent P5M3 family (LW9-LW13): top-of-prompt pointer, one final scheduler mutation, +3m default lead, GitHub START/END clock, and roughly 5-6 substantive units. Persist-review-revise samples are useful context but differ in artifact-I/O shape; comparisons must state whether they address capacity, efficiency, or duration.

### LW15-A — first large-package sample
Primary variable: `PACKAGE_SIZE`.

Predeclare roughly 12-15 eligible substantive units spanning TWO downstream artifacts plus cross-artifact synthesis. Required logical stages:
1. authority/NEXT transition verification;
2. artifact eligibility selection;
3-7. Artifact A evidence → candidate persist → fresh-fetch review → defect-caused revision → fresh-fetch validation;
8. A-result-dependent selection of B's unresolved question;
9-12. Artifact B evidence → candidate persist → fresh-fetch review → defect-caused revision/fresh-fetch validation;
13. cross-artifact synthesis;
14. capacity/efficiency comparison;
15. durable baton/exact continuation pointer.

### Acceptance
Large-package execution passes only when all eligible units complete or a genuine runtime/blocker/safety boundary is reached and exact remainder is persisted.

`CAPACITY_GAIN` requires materially more semantic/downstream value than the small-package baseline while scheduler/control policy remains unchanged. Raw artifact I/O may rise as a consequence of more useful units, so report it separately and normalize per semantic output. No padding, waiting, fake defects, redundant reads, or low-value artifacts.

### Contamination rule
If a protocol/document edit is necessary *because* the large-package experiment exposes a missing measurement rule, record that edit as a semantic output of LW15 but mark per-unit efficiency attribution as contaminated. Capacity attribution remains valid only if no scheduler/control mechanism changes. Never hide such contamination merely to preserve comparability.

### Saturation
If runtime/turn limits interrupt a useful package, label `SATURATED`, persist `UNITS_REMAINING` exactly, and make the next TO-DO begin with the remainder. This is evidence that package capacity exceeds one invocation, not failure if continuation is correct.

### Measurements
Use GitHub START/END `created_at` only for WORKED. Record units planned/done/remaining, semantic outputs/downstream decisions, artifacts changed, artifact I/O raw + normalized, scheduler/control I/O, package completion/early-stop reason, and next-wake continuation.

### Repetition requirement
LW15-A alone cannot promote package size. LW15-B must use a similarly large package on different eligible work with the same scheduler/control policy. Promotion requires both samples to show capacity gain. If only WALL_TIME rises, reject the claim. If semantic capacity rises but normalized I/O becomes poor, retain large-package sizing while separately optimizing artifact boundaries.

### Failure interpretation
- `CAPACITY_GAIN`: more useful semantic output under fixed scheduler/control policy.
- `SATURATED`: eligible work remains at runtime boundary; exact continuation persisted.
- `NO_GAIN`: package enlarged but useful semantic output does not materially increase.
- `NON_COMPARABLE`: unrelated control/mechanism change prevents capacity attribution.

If two large packages show NO_GAIN, investigate a higher-level turn-termination/runtime constraint rather than adding more package units.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` near the top. It is replace-only hot-path execution state; Issue #1 remains durable authority. The single end-of-turn automation mutation writes both next schedule and next TO-DO.
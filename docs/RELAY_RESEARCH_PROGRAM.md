# Relay Research Program v0.3

Status: ACTIVE — work-shaping defaults promoted through LW20; persistence-boundary optimization under repeat test
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that keeps a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, remains recoverable after missed wakes, and avoids duplicate execution?

## Experiment families
E1 RRULE self-shift; E2 minimum lead-time; E3 mutation stress; E4 provisional/final relay; E5 missed-wake recovery; E6 cross-automation wake; E7 duplicate authority; E8 durable cold-resume; E9 useful-work/package shaping; E10 persistence-boundary optimization.

## Metrics
Primary: continuation success, missed intended wake rate, duplicate substantive execution, dispatch delay, useful-work duty cycle, recovery latency, semantic useful outputs per invocation.
Secondary: scheduler mutations per useful-work minute, bootstrap/control overhead, artifact I/O per semantic output, stale-state reconciliation.

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
- Measure package capacity, semantic density, persistence I/O, and WORKED separately.

## E10 — Persistence-boundary optimization
Target value and persistence eligibility are separate decisions.

FULL_CHAIN is mandatory when later decisions depend on newly persisted reality, policy/source-of-truth is being mutated, or representation drift is itself material: candidate persist → fresh fetch → criteria-first review → defect-caused revision persist → fresh fetch → validation.

THIN_ELIGIBLE is a bounded candidate class for reconstructible audit/decision work when named durable inputs are already authoritative/freshly readable, exact decision fields can be reconstructed, candidate persistence adds no authority, and omission cannot hide relevant representation drift. Source reads remain artifact I/O and are not counted as thinning savings.

LW21 supplied one positive bounded sample: two thin targets had OMITTED_BOUNDARY_DEFECT=0 while a FULL_CHAIN policy artifact fresh-fetch caught a real regression. LW22 repeats on different thin targets before broader default promotion. Any defect attributable to an omitted persistence boundary immediately restores FULL_CHAIN for that target class.

### Persistence review invariants
- `PERSISTENCE_MODE` freezes before substantive execution; only a mandatory rollback after a thinning failure may change it.
- FULL_CHAIN fresh-fetch review must compare persisted representation against the predeclared acceptance contract, not merely confirm file existence.
- THIN_ELIGIBLE review must name authoritative durable inputs, reconstruct the exact decision fields from them, and report `OMITTED_BOUNDARY_DEFECT` explicitly.
- Candidate-boundary operations avoided and necessary source-read I/O are reported separately; source reads never count as savings.
- A thin result cannot mutate the authoritative source it is auditing. If the decision requires source mutation, route that mutation through FULL_CHAIN.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` near the top. It is replace-only hot-path execution state; Issue #1 remains durable authority. The single end-of-turn automation mutation writes both next schedule and next TO-DO.
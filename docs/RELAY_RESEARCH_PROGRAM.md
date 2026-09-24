# Relay Research Program v0.2-candidate

Status: ACTIVE — LW15 large-package capacity trial
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that keeps a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, remains recoverable after missed wakes, and avoids duplicate execution?

## Established experiment families
E1 RRULE self-shift baseline; E2 minimum lead-time; E3 repeated mutation stress; E4 provisional/final relay; E5 missed-wake recovery; E6 cross-automation wake; E7 duplicate authority; E8 durable cold-resume; E9 useful-work/package shaping.

## Metrics
Primary: continuation success, missed intended wake rate, duplicate substantive execution, dispatch delay, useful-work duty cycle, recovery latency, and semantic useful outputs per invocation.
Secondary: scheduler mutations per useful-work minute, bootstrap/control overhead, artifact I/O per semantic output, stale-state reconciliation.

## Promotion principle
Repeated evidence is required. One favorable trace is directional only. A mechanism must preserve recovery/authority and beat simpler alternatives for the layer being claimed.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior. Durable reconstruction, at-least-once-safe wake handling, stable identity, exclusive authority, authoritative completion, recovery horizon, and durable fallback remain benchmark principles.

## Canonical current pointer / cold-start fast path
Routine clean-success recovery uses Issue #1 compact tail. Broaden to ledger/docs only for ambiguity, boundary, reconciliation, or when the active substantive package needs those artifacts. Do not maintain a second mutable current-state mirror by default.

## E9 — Long useful-work / package capacity

### Research question
Is short WORKED primarily caused by a package acceptance boundary that is too small, such that a much larger package of independently useful work yields materially more semantic output before normal turn termination?

### Historical small-package baseline
Earlier LW trials used roughly 4-6 substantive units. They improved structure but remained short in wall-clock terms. Persist→fresh-fetch→review→revise chains increased useful persisted work, but the package itself still ended after one small coherent production cycle.

### LW15 — Large package capacity
Primary variable: `PACKAGE_SIZE`.

Predeclare roughly 12-15 substantive units spanning TWO eligible downstream artifacts plus a cross-artifact synthesis. The package must contain:
1. authority/NEXT verification;
2. two artifact selections that independently pass the eligibility gate;
3. Artifact A baseline criteria/evidence;
4. A candidate persistence;
5. A fresh-fetch adversarial review;
6. A defect-caused revision;
7. A fresh-fetch validation;
8. A result-dependent choice of Artifact B question;
9. B criteria/evidence;
10. B candidate persistence;
11. B fresh-fetch review;
12. B defect-caused revision and validation;
13. cross-artifact synthesis;
14. capacity/efficiency comparison;
15. durable baton and exact continuation pointer.

### Acceptance
A LW15 sample succeeds as a **large-package execution** only when all eligible units complete or a genuine runtime/blocker/safety boundary is reached and the exact remainder is persisted.

A LW15 sample supports **CAPACITY_GAIN** only when:
- semantic outputs/downstream value materially exceed the small-package baseline;
- scheduler mutation policy and lead-time policy remain unchanged;
- no padding, synthetic waiting, fake defects, redundant reads, or low-value artifacts are used;
- added artifact I/O is attributable to useful package units and is reported separately.

Do not infer reasoning depth from elapsed time. Do not target a number of minutes by waiting.

### Saturation
If runtime/turn limits interrupt a still-useful large package, label `SATURATED`, record `UNITS_REMAINING` exactly, and make the next top-of-prompt TO-DO begin with that remainder. Saturation is evidence that package capacity exceeds one invocation; it is not package failure if durable continuation is correct.

### Measurements
Use GitHub START_MARKER/END_MARKER `created_at` only for WORKED. Record:
- units planned/done/remaining;
- semantic outputs and downstream decisions;
- artifacts changed;
- artifact I/O raw and normalized per semantic output;
- scheduler/control I/O;
- package completion/early-stop reason;
- next-wake continuation result.

### Comparison sequence
1. LW15-A: first 12-15-unit large-package sample.
2. LW15-B: repeat a similarly sized package on different eligible work while preserving scheduler/control policy.
3. If both show capacity gain, promote large-package shaping as the default package-sizing rule, while separately optimizing per-unit I/O.
4. If packages still collapse with no semantic gain, reject size alone and investigate a higher-level turn-termination/runtime constraint.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` near the top of the automation prompt. It is replace-only hot-path state; Issue #1 remains durable authority. End-of-turn scheduler update also replaces the next TO-DO in the same single automation mutation.
# LW11 Transformation-Heavy Package

## Purpose
Test whether pre-shaped work that transforms evidence into durable artifacts produces more useful contiguous work than retrieval/classification-heavy packages, without adding scheduler/control writes.

## Comparison matrix

| Work class | Typical operation | Durable output | Expected useful-work depth | Control overhead | LW10 implication |
|---|---|---|---|---|---|
| Retrieval-only | fetch/read existing evidence | none or citation | low | low | compresses quickly |
| Evidence-to-decision | compare evidence and choose next action | decision + rationale | medium | low | useful but still compressible |
| Durable artifact production | synthesize evidence into reusable matrix/spec/protocol | reusable artifact | high | low if batched | best candidate |
| Control overhead | checkpoints/scheduler writes/status churn | operational metadata | low | high | avoid |

## Selected mechanism
**Dependent durable-artifact pipeline.** Each unit must consume the prior unit's output and materially extend a reusable research artifact. The mechanism is selected because it increases transformation depth without adding waits or control writes.

## Acceptance criteria
1. One package contains 5-6 substantive units.
2. At least 3 transitions are genuinely result-dependent.
3. At least 4 non-redundant evidence-to-decision outputs are produced.
4. At least 2 durable sections/artifacts are created or materially revised.
5. No synthetic waiting, padding, repeated summaries, or mid-turn scheduler/control writes.
6. Exactly one normal automation update at turn end.
7. WORKED is measured only from GitHub START_MARKER/END_MARKER created_at.

## Failure criteria
- Package collapses into retrieval/classification with no reusable transformation.
- Later units could have been fully specified without prior outputs.
- Added elapsed time comes primarily from control I/O.
- Useful outputs do not improve over LW9/LW10.

## Output 1 — Work-shaping rule
For long-work experiments, package size alone is insufficient. A candidate package should maximize **transformation depth**: evidence must be converted into a reusable artifact or discriminating decision, and later units should consume those transformed outputs.

## Output 2 — Measurement rule
Compare experiments on two axes rather than WORKED alone:
- useful durable outputs per turn;
- GitHub-server WORKED with scheduler/control write count held constant.

A longer turn is not an improvement if the added duration is control overhead. A shorter turn can still win if it produces more reusable output; the long-work project should seek increases in both useful output and contiguous WORKED where possible.

## Output 3 — Adversarial review
The first mechanism still has a loophole: declaring several headings or decisions does not prove substantial transformation. A model can generate a matrix, criteria, and conclusions in one compressed reasoning burst. Therefore `number of units` and `number of sections` are weak proxies for work depth.

A stronger package must have **revision pressure**. A later stage must inspect an earlier durable output, identify concrete defects against explicit criteria, and modify that same artifact. This creates a dependency that cannot be satisfied merely by relabeling parallel thoughts as sequential units.

## Output 4 — Validated production protocol
Use one coherent artifact and move it through five stages:
1. **Evidence extraction:** collect only evidence required for the artifact.
2. **Construction:** build a substantive model/specification from that evidence.
3. **Adversarial review:** identify at least three concrete defects, unsupported assumptions, or missing cases in the constructed artifact.
4. **Revision:** materially edit the artifact to resolve the review findings.
5. **Validation:** test the revised artifact against explicit acceptance criteria and record unresolved failures.

Required dependency: stages 3-5 must operate on the actual persisted output of the preceding stage. Merely predicting what the preceding stage would say does not satisfy the protocol.

## Output 5 — Next discriminating test design
Run **LW12-COHERENT-ARTIFACT-REVISION-01**. Keep the promoted dynamic TODO pointer, scheduler lead-time policy, and one-final-write rule fixed. Choose one existing relay research artifact that is useful enough to improve. Execute evidence extraction → construction/revision baseline → adversarial review → revision → validation in one invocation. Acceptance requires >=3 review defects, >=2 material revisions caused by those defects, a final validation verdict, no filler/waits, and GitHub-server WORKED measurement. Compare both durable-output quality and WORKED with LW9-LW11.

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

## Output 3 — Next discriminating test design
If LW11 remains short despite durable transformation, test a **single coherent production task** that requires editing one substantial artifact through sequential stages: evidence extraction → model/spec construction → adversarial review → revision → validation. Hold TODO pointer, scheduler lead time, and one-write rule fixed.

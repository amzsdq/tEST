# LW11/LW12 Transformation-Heavy Long-Work Protocol

## Purpose
Test whether one persisted artifact moving through evidence → construction → adversarial review → material revision → validation yields deeper useful contiguous work than retrieval-heavy or section-count packages, without adding scheduler/control writes.

## Evidence baseline
Observed progression:
- LW9 dynamic TODO improved hot-start continuity but completed in 31s.
- LW10 result-dependent lookup chain completed in 36s; dependency alone remained compressible.
- LW11 artifact transformation/review completed in 49s; useful durable output increased, but headings/unit counts could still be generated in one reasoning burst.

The working hypothesis is therefore not `more units = longer work`. It is: **persisted-output revision pressure can create genuine sequential work because later stages must inspect and change an actual earlier artifact.**

## Operational protocol candidate
A package uses one named artifact and exactly these semantic stages (tool calls may vary):
1. Evidence baseline — identify the artifact's decision purpose, current defects, and evidence required to improve it.
2. Candidate persistence — materially revise/build the artifact and persist the candidate before review.
3. Independent adversarial review — re-read the persisted candidate and record >=3 defects tied to explicit acceptance criteria.
4. Review-caused revision — modify the same artifact to resolve >=2 recorded defects; each edit names the defect it resolves.
5. Validation — re-read the revised persisted artifact and issue PASS/RETEST/REJECT against the acceptance criteria.
6. Measurement/decision — compare useful durable output and GitHub-server WORKED with prior experiments while scheduler mutation count remains one.

## Acceptance criteria
- One coherent artifact is named before construction.
- Candidate is persisted before adversarial review.
- Review operates on fetched persisted candidate, not an in-memory prediction.
- >=3 concrete defects are recorded. A defect must identify location/claim, failure mode, and required correction.
- >=2 material edits are explicitly traceable to recorded defects.
- Revised artifact is persisted before validation and fetched again for validation.
- Final verdict is evidence-backed PASS/RETEST/REJECT.
- No sleep, padding, repeated summary, synthetic checkpoint, or mid-turn scheduler mutation.
- Exactly one normal automation update at turn end.
- WORKED uses only GitHub START_MARKER/END_MARKER created_at.

## Failure criteria
- Review is written before the candidate is persisted/re-read.
- Defects are generic style complaints with no operational consequence.
- Revision merely appends a review section without changing the protocol under test.
- Validation relies on the intended revision rather than the fetched persisted revision.
- Added duration is mostly control I/O or redundant reads.
- Durable output quality does not improve despite extra stages.

## Measurement
Record: candidate commit, review defects, defect→edit mapping, revised commit, validation verdict, useful durable outputs, scheduler writes, START/END server timestamps, WORKED.

Compare on both axes:
1. useful durable outputs / decision quality;
2. contiguous WORKED with scheduler/control writes held constant.

## Candidate limitation to test
The protocol may still overfit to document editing: persistence/re-fetch itself can add I/O without increasing reasoning depth. LW12 must therefore distinguish **review-caused semantic changes** from time spent merely performing GitHub writes/reads. If semantic improvement is weak, reject this mechanism even if WORKED increases.

# LW11/LW12 Transformation-Heavy Long-Work Protocol

## Purpose
Test whether one persisted artifact moving through evidence → construction → adversarial review → material revision → validation yields deeper useful contiguous work than retrieval-heavy or section-count packages, without adding scheduler/control writes.

## Evidence baseline
Observed progression:
- LW9 dynamic TODO improved hot-start continuity but completed in 31s.
- LW10 result-dependent lookup chain completed in 36s; dependency alone remained compressible.
- LW11 artifact transformation/review completed in 49s; useful durable output increased, but headings/unit counts could still be generated in one reasoning burst.

Working hypothesis: **persisted-output revision pressure can create genuine sequential work because later stages inspect and change an actual earlier artifact.** More units alone are not evidence of deeper work.

## Artifact eligibility
Use this protocol only when all are true:
- the artifact will materially influence a later relay decision/experiment;
- at least one substantive uncertainty or defect is plausible before review;
- semantic revision is possible in the current turn;
- the artifact is not being created solely to manufacture elapsed time.
If these conditions fail, choose direct evidence-to-decision work instead.

## Operational protocol
Stages are semantic dependencies, not quotas. Skip a stage only when its output is demonstrably unnecessary; never invent defects or edits to satisfy a count.
1. Evidence baseline — identify decision purpose, current requirements, and only the evidence needed to improve the named artifact.
2. Candidate persistence — materially revise/build the artifact and persist it before review.
3. Adversarial review — freshly fetch the persisted candidate, then record concrete operational defects against acceptance criteria.
4. Review-caused revision — modify the same artifact to resolve material recorded defects; map each edit to its triggering defect.
5. Validation — freshly fetch the revised artifact and test the actual persisted text against acceptance criteria.
6. Measurement/decision — compare semantic gain and WORKED with prior experiments while scheduler mutation count remains one.

## Review independence boundary
A review counts only if it is based on a fresh fetch after candidate persistence. It must not reuse an unpublished in-memory draft as its review target. For every defect record:
- TARGET: exact rule/claim/section;
- FAILURE_MODE: concrete way it can reduce useful work, reliability, or measurement validity;
- REQUIRED_CHANGE: observable semantic correction.

## Acceptance criteria
- One eligible coherent artifact is named before construction.
- Candidate is persisted and freshly fetched before review.
- Review finds real operational defects; >=3 is a test target, not permission to fabricate weak defects.
- >=2 material edits are required for LW12 promotion and are explicitly traceable to review defects.
- Revised artifact is persisted and freshly fetched before validation.
- Final verdict is evidence-backed PASS/RETEST/REJECT.
- No sleep, padding, repeated summary, synthetic checkpoint, or mid-turn scheduler mutation.
- Exactly one normal automation update at turn end.
- WORKED uses only GitHub START_MARKER/END_MARKER created_at.

## LW12 adversarial review of candidate 0e1e164
D1 — TARGET: `exactly these semantic stages`. FAILURE_MODE: turns stages into quotas and can manufacture work after useful work converges. REQUIRED_CHANGE: stages become dependency gates with explicit no-busywork/skip semantics.

D2 — TARGET: `Independent adversarial review`. FAILURE_MODE: independence was undefined; the model could claim independence while reviewing its in-memory intended draft rather than persisted reality. REQUIRED_CHANGE: require a fresh post-persistence fetch and structured TARGET/FAILURE_MODE/REQUIRED_CHANGE records.

D3 — TARGET: Measurement section. FAILURE_MODE: increased WORKED could come from GitHub persistence/re-fetch latency rather than deeper semantic transformation, producing a false promotion. REQUIRED_CHANGE: record semantic changes separately from control/artifact I/O and require semantic gain for promotion.

D4 — TARGET: artifact selection. FAILURE_MODE: no eligibility gate prevented creation/editing of low-value documents solely because they take longer. REQUIRED_CHANGE: require downstream decision value and plausible substantive uncertainty before using this mechanism.

## Defect → revision mapping
- D1 resolved by replacing exact-stage quota language with semantic dependency/skip rules.
- D2 resolved by the fresh-fetch review boundary and structured defect schema.
- D3 resolved by the measurement decomposition and promotion rule below.
- D4 resolved by `Artifact eligibility`.

## Measurement decomposition
Record separately:
- SEMANTIC_OUTPUTS: concrete rules/decisions/spec changes that survive review;
- DEFECTS_FOUND / MATERIAL_DEFECTS_RESOLVED;
- ARTIFACT_IO: candidate write, candidate fetch, revision write, validation fetch;
- CONTROL_IO: Issue baton/markers and scheduler writes;
- WORKED: GitHub START_MARKER→END_MARKER.

Promotion requires semantic output quality to improve, not merely WORKED. If WORKED rises while semantic gain is weak or the extra time is predominantly persistence/re-fetch overhead, REJECT as a long-work mechanism. If semantic quality improves but duration evidence remains ambiguous, RETEST with the same I/O shape rather than adding controls.

## Failure criteria
- Review precedes candidate persistence/fresh fetch.
- Defects are generic style complaints with no operational consequence.
- Revision merely appends commentary without changing the protocol under test.
- Validation relies on intended rather than freshly fetched persisted revision.
- Artifact fails eligibility or work continues after useful convergence.
- Added duration is mostly I/O with weak semantic gain.

## LW12 validation target
PASS requires: eligible artifact; fresh-fetch review; >=3 concrete defects; >=2 material defect-caused revisions; fresh-fetch validation; semantic quality improvement; one normal scheduler mutation; no filler. Otherwise RETEST/REJECT according to whether the mechanism remains discriminating.

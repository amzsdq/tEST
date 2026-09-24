# Persisted-Output Transformation Protocol

## Purpose
Use persisted artifact boundaries when they make later work consume actual earlier outputs rather than an imagined in-memory draft. This is a semantic-quality primitive, not a wall-clock padding technique and not a mandatory wrapper around every large-package unit.

## Evidence baseline
- LW9 top-of-prompt TO-DO improved hot-start continuity but remained short.
- LW10 dependency language alone was compressible.
- LW11/LW12 showed persist → fresh fetch → review → defect-caused revision → fresh fetch validation can expose material defects.
- LW15/LW16 showed larger pre-shaped packages increase semantic capacity when every added unit is independently valuable.
- At larger scales, unconditional persistence chains can dominate artifact I/O; therefore package size and persistence-boundary density must be measured separately.

## Artifact eligibility gate
Use a persisted chain only when all are true:
1. downstream decision value;
2. substantive uncertainty or plausible material defect;
3. revisionability in the current turn;
4. persistence value — reviewing persisted reality is meaningfully safer than reviewing intended state.

If any condition fails, use direct evidence-to-decision work. Never create or rewrite a document merely to consume time or satisfy a unit quota.

## Canonical chain
1. Evidence baseline + explicit acceptance/failure criteria.
2. Candidate persistence.
3. Fresh-fetch review of the exact persisted candidate.
4. Structured real defects: TARGET / FAILURE_MODE / REQUIRED_CHANGE.
5. Defect-caused revision persistence.
6. Fresh-fetch validation: PASS / RETEST / REJECT.

Zero defects is valid. Weak style preferences without downstream consequence do not count.

## Adaptive persistence budget
Persistence is justified by corrections, not by ceremony.

For each artifact chain record:
- MATERIAL_DEFECTS_FOUND;
- MATERIAL_DEFECTS_RESOLVED;
- ARTIFACT_IO_RAW;
- SEMANTIC_OUTPUTS;
- `CORRECTION_YIELD = MATERIAL_DEFECTS_RESOLVED / ARTIFACT_IO_RAW`;
- whether a direct evidence-to-decision path plausibly would have produced the same validated decision.

Decision rule:
- RETAIN full persist/fetch/review/revise/fetch when it repeatedly catches material defects or protects a state boundary whose mismatch would change downstream action.
- THIN the chain when fresh-fetch review repeatedly produces zero material corrections and persisted-state mismatch risk is low; use one persisted validation boundary instead of two where safe.
- DEMOTE for a work class when direct evidence-to-decision produces equal semantic quality/reliability with lower artifact I/O.

Do not thin scheduler/recovery evidence merely to optimize document I/O; this rule applies to semantic artifact production, not to evidence needed for authority or external side-effect safety.

## Large-package composition
Multiple artifact chains may be composed when later targets genuinely depend on earlier validated results. Each claimed transition records:
`SELECTED_BY=<prior validated result> -> <later target>`.

A later target that was substantively preselected does not count as result-dependent capacity. Synthesis counts only when it changes a future decision.

## Measurement decomposition
Record separately:
- SEMANTIC_OUTPUTS and downstream consumers;
- SEMANTIC_OUTPUTS_PER_10_UNITS;
- DOWNSTREAM_DECISIONS_CHANGED;
- DEFECTS_FOUND / MATERIAL_DEFECTS_RESOLVED;
- ARTIFACT_IO_RAW;
- ARTIFACT_IO_PER_SEMANTIC_OUTPUT;
- CORRECTION_YIELD;
- CONTROL_IO;
- WORKED from GitHub markers;
- UNITS_PLANNED / DONE / REMAINING;
- SATURATED.

## Interpretation rules
- More WORKED with weak semantic gain is not promotion.
- More semantic outputs with unchanged control policy is capacity evidence.
- Package-size scaling and persisted-output transformation are separate variables.
- If semantic-output density stays stable but artifact I/O per output rises sharply, optimize persistence boundaries before increasing control complexity.
- If density itself falls, stop scaling package size until weak units are removed or better substantive targets exist.

## Failure criteria
REJECT/NON_COMPARABLE when:
- review uses unpublished/in-memory state while claiming persisted review;
- result-dependent target was actually preselected;
- defects are fabricated;
- revision does not correct target semantics;
- validation skips the persisted revision;
- redundant I/O or low-value artifacts are added for elapsed time;
- eligible remainder is lost at handoff.

## Promotion and demotion
Promote the full persisted-output protocol for a work class only when repeated samples show semantic/downstream-value or correction-yield gain worth its artifact I/O. Otherwise thin or demote it while preserving the large-package eligibility and exact-handoff rules.
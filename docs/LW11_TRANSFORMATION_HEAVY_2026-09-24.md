# Persisted-Output Transformation Protocol

## Purpose
Use persisted artifact boundaries when they make later work consume actual earlier outputs rather than imagined in-memory state. This is a semantic-quality primitive, not wall-clock padding and not a mandatory wrapper around every high-value target.

## Artifact eligibility gate
Use a persisted chain only when all are true: downstream decision value, substantive uncertainty/plausible material defect, current-turn revisionability, and persistence value. A high target-selection score does NOT override this gate. If persistence value fails, perform direct evidence-to-decision work and count only validated semantic consequences; never create a document merely to satisfy package or persistence shape.

## Canonical full chain
1. Evidence baseline + explicit acceptance/failure criteria.
2. Candidate persistence.
3. Fresh-fetch review of exact persisted candidate.
4. Structured real defects: TARGET / FAILURE_MODE / REQUIRED_CHANGE.
5. Defect-caused revision persistence.
6. Fresh-fetch validation: PASS / RETEST / REJECT.
Zero defects is valid. Weak style preferences without downstream consequence do not count.

## Semantic-output audit contract
A counted output must be durable, validated, and decision-bearing:
`OUTPUT_ID`, `DURABLE_CHANGE`, `DOWNSTREAM_CONSEQUENCE`, `VALIDATED_BY`.
Duplicate downstream consequences count once. Summaries/evidence restatement/style/read-write bookkeeping count zero.

## Value-gated target-selection interaction
Target selection and persistence selection are separate gates:
1. Score substantive candidate before selection using the frozen value gate (decision reach, unresolved uncertainty, falsifiability, downstream reuse).
2. If target is selected, apply artifact eligibility independently.
3. `HIGH_VALUE + PERSISTENCE_ELIGIBLE` -> full persisted-output chain baseline.
4. `HIGH_VALUE + PERSISTENCE_INELIGIBLE` -> direct evidence-to-decision path; record `PERSISTENCE_SKIP_REASON`; this is not a failed target.
5. `LOW_VALUE` -> reject target regardless of persistence convenience.
6. Never increase a value score because a document is easy to edit, and never persist solely because the target score is high.

This separation prevents value gating from turning persistence into ceremony and prevents persistence convenience from biasing target selection.

## Adaptive persistence budget
Persistence is justified by corrections or state-boundary risk. Record MATERIAL_DEFECTS_FOUND/RESOLVED, ARTIFACT_IO_RAW, SEMANTIC_OUTPUTS, `CORRECTION_YIELD = MATERIAL_DEFECTS_RESOLVED / ARTIFACT_IO_RAW`. Thinning is a separate controlled non-inferiority variable; never silently vary it during target-selection comparison. Never thin authority, scheduler/recovery, or external-side-effect evidence merely to optimize document I/O.

## Result dependency
Each claimed transition records `SELECTED_BY=<prior validated result> -> <later target/focus>`. Pre-scoring a candidate identity does not invalidate dependency if its substantive focus remains unresolved until prior validation; precomputing the later edit does.

## Value adjudication
Raw semantic-output count is the default density numerator. A lower-count sample may claim value override only by recording the exact baseline output dominated, materially larger named downstream consequence, and observable future evidence that would falsify dominance. Value override never changes raw count.

## Measurement decomposition
Record SEMANTIC_OUTPUTS/output IDs, SEMANTIC_OUTPUTS_PER_10_UNITS, DOWNSTREAM_DECISIONS_CHANGED, valid VALUE_OVERRIDE if any, DEFECTS_FOUND/RESOLVED, ARTIFACT_IO_RAW, ARTIFACT_IO_PER_SEMANTIC_OUTPUT, CORRECTION_YIELD, CONTROL_IO, WORKED, UNITS_PLANNED/DONE/REMAINING, SATURATED, TARGET_SCORE, and PERSISTENCE_SKIP_REASON where applicable.

## Failure criteria
REJECT/NON_COMPARABLE when review uses unpublished state while claiming persisted review; result-dependent focus was precomputed; defects are fabricated; semantic outputs lack named consequences; scores are changed after results; value override is subjective/unfalsifiable; high scores force ceremonial persistence; redundant I/O/low-value artifacts are added for elapsed time; or eligible remainder is lost.

## Promotion/demotion
Promote full persistence for a work class only when repeated samples show semantic/downstream-value or correction-yield gain worth its I/O. Promote value-gated target selection separately through controlled density/value comparison. Neither mechanism's success implies the other is mandatory.
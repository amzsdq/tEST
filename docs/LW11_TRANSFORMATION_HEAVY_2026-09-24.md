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
A counted output must be durable, validated, and decision-bearing: `OUTPUT_ID`, `DURABLE_CHANGE`, `DOWNSTREAM_CONSEQUENCE`, `VALIDATED_BY`. Duplicate downstream consequences count once. Summaries/evidence restatement/style/read-write bookkeeping count zero.

## Value-gated target-selection interaction
Target selection and persistence selection are separate gates:
1. Score substantive candidate before selection using the frozen value gate.
2. If selected, apply artifact eligibility independently.
3. `HIGH_VALUE + PERSISTENCE_ELIGIBLE` -> full persisted-output chain baseline.
4. `HIGH_VALUE + PERSISTENCE_INELIGIBLE` -> direct evidence-to-decision path; record `PERSISTENCE_SKIP_REASON`; this is not a failed target.
5. `LOW_VALUE` -> reject target regardless of persistence convenience.
6. Never increase a value score because a document is easy to edit, and never persist solely because the target score is high.

## S fresh-fetch review
TARGET=causal isolation; FAILURE_MODE=value score could implicitly authorize persistence and confound target-selection with I/O policy; REQUIRED_CHANGE=separate target and persistence gates. RESOLVED.
TARGET=dependency audit; FAILURE_MODE=pre-scored candidate identity could be confused with precomputed substantive focus; REQUIRED_CHANGE=identity may be scored early but focus/edit remains unresolved until SELECTED_BY. RESOLVED.
TARGET=quota pressure; FAILURE_MODE=high-value but persistence-ineligible target could trigger ceremonial artifact creation; REQUIRED_CHANGE=direct path plus PERSISTENCE_SKIP_REASON. RESOLVED.
TARGET=promotion leakage; FAILURE_MODE=success of one mechanism could promote the other; REQUIRED_CHANGE=separate promotion/demotion evidence. RESOLVED.

S_VALIDATION=PASS. Value gating can be tested while keeping persistence policy causally separate; this preserves LW19's one-variable comparison and gives future thinning experiments a clean boundary.

## Adaptive persistence budget
Persistence is justified by corrections or state-boundary risk. Record MATERIAL_DEFECTS_FOUND/RESOLVED, ARTIFACT_IO_RAW, SEMANTIC_OUTPUTS, `CORRECTION_YIELD = MATERIAL_DEFECTS_RESOLVED / ARTIFACT_IO_RAW`. Thinning is a separate controlled non-inferiority variable; never silently vary it during target-selection comparison. Never thin authority, scheduler/recovery, or external-side-effect evidence merely to optimize document I/O.

## Result dependency
Each claimed transition records `SELECTED_BY=<prior validated result> -> <later target/focus>`. Pre-scoring candidate identity does not invalidate dependency if substantive focus remains unresolved until prior validation; precomputing later edit does.

## Value adjudication
Raw semantic-output count is default density numerator. Lower-count value override requires exact baseline output dominated, materially larger named downstream consequence, and observable future evidence that would falsify dominance. Value override never changes raw count.

## Measurement decomposition
Record semantic outputs/output IDs, density, downstream decisions, valid override if any, defects, artifact I/O, I/O/output, correction yield, control I/O, WORKED, units, saturation, target score, and persistence skip reason.

## Failure criteria
REJECT/NON_COMPARABLE when review uses unpublished state while claiming persisted review; result-dependent focus was precomputed; defects are fabricated; outputs lack named consequences; scores change after results; override is subjective; high scores force ceremonial persistence; redundant I/O/low-value artifacts are added; or remainder is lost.

## Promotion/demotion
Promote full persistence for a work class only when repeated samples show semantic/downstream-value or correction-yield gain worth its I/O. Promote value-gated target selection separately through controlled density/value comparison. Neither mechanism's success implies the other is mandatory.
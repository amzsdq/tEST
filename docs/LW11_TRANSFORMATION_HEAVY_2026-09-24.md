# Persisted-Output Transformation Protocol

## Purpose
Use persisted artifact boundaries when they make later work consume actual earlier outputs rather than imagined in-memory state. This is a semantic-quality primitive, not wall-clock padding and not a mandatory wrapper around every large-package unit.

## Evidence baseline
- LW9 top-of-prompt TO-DO improved hot-start continuity but remained short.
- LW10 dependency language alone was compressible.
- LW11/LW12 showed persist -> fresh fetch -> review -> defect-caused revision -> fresh-fetch validation can expose material defects.
- LW15/LW16 showed larger pre-shaped packages increase semantic capacity when every added unit is independently valuable.
- LW17 completed 34 eligible units but exposed a density boundary; semantic-output counting now needs auditable downstream consequences rather than free-form counts.

## Artifact eligibility gate
Use a persisted chain only when all are true: downstream decision value, substantive uncertainty/plausible material defect, current-turn revisionability, and persistence value. If any fails, use direct evidence-to-decision work. Never manufacture a document or rewrite merely to satisfy a unit quota.

## Canonical full chain
1. Evidence baseline + explicit acceptance/failure criteria.
2. Candidate persistence.
3. Fresh-fetch review of the exact persisted candidate.
4. Structured real defects: TARGET / FAILURE_MODE / REQUIRED_CHANGE.
5. Defect-caused revision persistence.
6. Fresh-fetch validation: PASS / RETEST / REJECT.

Zero defects is valid. Weak style preferences without downstream consequence do not count.

## Semantic-output audit contract
A counted semantic output must be durable, validated, and decision-bearing. Record it as:
- `OUTPUT_ID=<stable local id>`
- `DURABLE_CHANGE=<rule/spec/decision changed>`
- `DOWNSTREAM_CONSEQUENCE=<named future experiment/prompt/recovery decision changed>`
- `VALIDATED_BY=<fresh-fetch validation or named evidence boundary>`

Two formulations that drive the same downstream consequence count once unless each independently changes a different named decision. Summaries, evidence restatement, stylistic edits, reads/writes, and control bookkeeping count zero.

A package-level synthesis counts only when it changes a named future decision not already counted by its component outputs. This prevents aggregation prose from inflating semantic density.

## Adaptive persistence budget
Persistence is justified by corrections or state-boundary risk, not ceremony. For each chain record MATERIAL_DEFECTS_FOUND/RESOLVED, ARTIFACT_IO_RAW, SEMANTIC_OUTPUTS, and `CORRECTION_YIELD = MATERIAL_DEFECTS_RESOLVED / ARTIFACT_IO_RAW`.

The full chain is the safe baseline for eligible artifact work. A thinner chain is a separate candidate variable. It may be tested only after comparable full-chain samples show low correction yield and low persisted-state mismatch risk. A thinning trial holds package size, scheduler/control policy, acceptance criteria, and substantive target class constant and requires repeated non-inferiority.

Never thin authority, scheduler/recovery, or external-side-effect evidence merely to optimize document I/O.

## Large-package composition
Multiple artifact chains may be composed when later targets genuinely depend on earlier validated results. Each claimed transition records `SELECTED_BY=<prior validated result> -> <later target>`. The later substantive target must remain unresolved until prior validation. A preselected target does not count as dependency evidence.

## Density guardrail
For the frozen LW18 repeat, the guardrail is 4.13 counted semantic outputs per 10 actual eligible units. Density is computed from actual UNITS_DONE. Below-guardrail results are DENSITY_DEGRADED unless higher-value adjudication names the specific output, materially larger downstream consequence, and reason raw count understates value. Wall time cannot override density.

## Measurement decomposition
Record SEMANTIC_OUTPUTS and output IDs, SEMANTIC_OUTPUTS_PER_10_UNITS, DOWNSTREAM_DECISIONS_CHANGED, DEFECTS_FOUND/RESOLVED, ARTIFACT_IO_RAW, ARTIFACT_IO_PER_SEMANTIC_OUTPUT, CORRECTION_YIELD, CONTROL_IO, WORKED, UNITS_PLANNED/DONE/REMAINING, and SATURATED.

## Interpretation rules
- More WORKED with weak semantic gain is not promotion.
- More semantic outputs with unchanged control policy is capacity evidence.
- Package-size scaling and persisted-output transformation are separate variables.
- Rising artifact I/O per output suggests a future controlled thinning experiment; it does not authorize skipping validation boundaries.
- Falling semantic-output density means stop scale-up until weak units are removed or better targets exist.

## Failure criteria
REJECT/NON_COMPARABLE when review uses unpublished state while claiming persisted review; a result-dependent target was preselected; defects are fabricated; revision does not correct target semantics; validation skips persisted revision; semantic outputs lack named downstream consequences; redundant I/O/low-value artifacts are added for elapsed time; or eligible remainder is lost at handoff.

## Promotion and demotion
Promote the full protocol for a work class when repeated samples show semantic/downstream-value or correction-yield gain worth its I/O. Demote/thin only through a controlled non-inferiority experiment, never from intuition or a single zero-defect sample.
# Relay Optimization Convergence Protocol v0.4

Status: LW21 PERSISTENCE-MODE CANDIDATE

## Objective
Converge to the smallest relay policy that maximizes semantic useful work while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state. Longer wall-clock time is diagnostic only.

## Evidence classes
- SEMANTIC_OUTPUT — validated rule/spec/decision with named downstream consequence.
- ARTIFACT_IO — persistence/fetch required by a real dependency or review boundary.
- CONTROL_IO — scheduler mutations, markers, baton/checkpoint writes, verification-only control reads.
- WALL_TIME — GitHub-server END_MARKER.created_at - START_MARKER.created_at.

## Controlled convergence
Freeze baseline; change one primary variable; repeat samples; separate WRITE_OK/STATE_OK/WAKE_OK/WORK_OK; measure semantic outputs independently from artifact/control I/O and WALL_TIME.

## Experiment eligibility gate
Every added work unit must have downstream value, substantive uncertainty/real correction need, and a discriminating result. Reject units created only to enlarge a package.

## Causal layers
Treat package size, target ranking, persistence mode, semantic counting, scheduler/control, and lead-time as distinct variables. A claim about one layer is non-comparable if another layer changes without explicit normalization.

## Persistence-mode gate
Target value and persistence eligibility are separate. Use FULL_CHAIN when later decisions depend on a newly persisted representation or persisted reality is itself under test. Use THIN_ELIGIBLE only when named durable source evidence is already authoritative, the decision can be reconstructed from it, and candidate persistence adds no authority. Any material defect attributable to an omitted persistence boundary rejects thinning for that target class and restores FULL_CHAIN.

FULL_CHAIN candidate boundary: candidate persist -> fresh fetch -> criteria-first review -> defect-caused revision persist -> fresh fetch -> validation.
THIN_ELIGIBLE: fresh durable-source evidence -> semantic review/decision -> validate reconstructibility; no ceremonial candidate copy. Necessary source reads remain ARTIFACT_IO and are never counted as savings.

## Package-capacity experiment
Large-package trials pre-shape independently valuable work, preserve actual result dependencies, keep scheduler policy unchanged, and prohibit sleep/redundant summaries/redundant reads/fake defects/low-value artifacts. Record units, semantic outputs, artifact I/O raw and normalized, control I/O, server-clock WORKED, completion/saturation, and exact remainder.

30–36 eligible-unit scale is promoted for semantic capacity+density under tested P5M4 conditions. This is not a 10-minute wall-time guarantee.

## Promotion / rollback
Scheduler/control promotion requires repeated WAKE_OK/WORK_OK and no duplicate-authority violation. Work shaping requires repeated semantic/downstream gain under unchanged control policy. Persistence thinning requires no omitted-boundary defect, non-inferior semantic/downstream quality, and materially lower candidate-boundary I/O. WALL_TIME alone never promotes.

Rollback immediately on duplicate substantive side effects, lost recurring fallback, stale authority overwrite, unrecoverable durable state, or a material defect shown to be hidden by an omitted persistence boundary.

## Decision record
Record CURRENT_CANDIDATE, PRIMARY_VARIABLE, COMPARABILITY, LEAD_TIME, SCHEDULER_WRITES, UNITS, SEMANTIC_OUTPUTS, ARTIFACTS_CHANGED, PERSISTENCE_MODE/REASON, ARTIFACT_IO_RAW/NORMALIZED, CONTROL_IO, WORKED, EVIDENCE, DECISION, NEXT.

## Current long-work research rule
Dynamic top-of-prompt TO-DO is hot-path execution state; Issue #1 remains durable authority. Value-gated target selection ranks eligible work. Persistence mode is separately gated. Judge package size by eligible semantic capacity/downstream value and persistence thinning by quality-preserving I/O reduction; do not infer reasoning depth from elapsed time.
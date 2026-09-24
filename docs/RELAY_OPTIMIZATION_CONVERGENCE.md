# Relay Optimization Convergence Protocol v0.4

Status: LW21 FRESH-FETCH REVIEWED

## Objective
Converge to the smallest relay policy that maximizes semantic useful work while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state. Longer wall-clock time is diagnostic only.

## Evidence classes
- SEMANTIC_OUTPUT — validated rule/spec/decision with named downstream consequence.
- ARTIFACT_IO — persistence/fetch required by a real dependency or review boundary.
- CONTROL_IO — scheduler mutations, markers, baton/checkpoint writes, verification-only control reads.
- WALL_TIME — GitHub-server END_MARKER.created_at - START_MARKER.created_at.

## Comparable-sample contract
A comparison is valid only when samples hold constant, or explicitly normalize, scheduler mutation count, marker/baton shape, materially relevant artifact I/O, lead-time policy, and acceptance semantics. Package-size trials may intentionally increase useful units and resulting artifact I/O, but claims are then limited to capacity/useful-output gain, not reasoning depth or per-unit efficiency.

## Controlled convergence
Freeze baseline; change one primary variable; repeat samples; separate WRITE_OK/STATE_OK/WAKE_OK/WORK_OK; measure semantic outputs independently from artifact/control I/O and WALL_TIME.

## Experiment eligibility gate
Every added work unit must have downstream value, substantive uncertainty/real correction need, and a discriminating result. Reject units created only to enlarge a package.

## Causal layers
Treat package size, target ranking, persistence mode, semantic counting, scheduler/control, and lead-time as distinct variables. A claim about one layer is NON_COMPARABLE if another layer changes without explicit normalization.

## Persist-review-revise baseline
For an eligible durable artifact: build/revise -> persist -> fresh fetch -> criteria-first review -> record real defects as TARGET / FAILURE_MODE / REQUIRED_CHANGE -> defect-mapped revision -> persist/fresh fetch -> PASS/RETEST/REJECT. Review may legitimately return zero defects.

## Persistence-mode gate — LW21
Target value and persistence eligibility are separate. FULL_CHAIN applies when later decisions depend on a newly persisted representation, source-of-truth mutation is being made, or persisted reality is itself under test. THIN_ELIGIBLE applies only when named durable source evidence is already authoritative and freshly readable, the exact decision can be reconstructed from named fields, candidate persistence adds no authority, and omission cannot hide representation drift relevant to the decision.

FULL_CHAIN candidate boundary: candidate persist -> fresh fetch -> criteria-first review -> defect-caused revision persist -> fresh fetch -> validation.
THIN_ELIGIBLE: fresh durable-source evidence -> semantic review/decision -> explicit reconstructibility validation; no ceremonial candidate copy. Necessary source reads remain ARTIFACT_IO and are never counted as savings.

Any material defect attributable to an omitted persistence boundary rejects thinning for that target class and restores FULL_CHAIN. Persistence mode is frozen before substantive target execution except mandatory rollback after such failure.

## Package-capacity experiment
Large-package trials pre-shape independently valuable work, preserve actual result dependencies, keep scheduler policy unchanged, and prohibit sleep/redundant summaries/redundant reads/fake defects/low-value artifacts. Record UNITS_PLANNED/DONE/REMAINING, semantic outputs/downstream consequences, artifacts changed, ARTIFACT_IO raw/normalized, CONTROL_IO, server-clock WORKED, PACKAGE_COMPLETE, SATURATED, and exact remainder.

Capacity outcomes: CAPACITY_GAIN, SATURATED, NO_GAIN, NON_COMPARABLE. Completing one artifact is not package completion while eligible predeclared work remains. 30–36 eligible-unit scale is promoted for semantic capacity+density under tested P5M4 conditions; no 10-minute guarantee or safety claim beyond tested scale follows.

## Promotion / rollback
- Scheduler/control: repeated WAKE_OK/WORK_OK, no duplicate-authority violation, relevant recovery evidence.
- Work shaping: repeated semantic/downstream-value gain under unchanged scheduler/control policy.
- Persistence thinning: >=2 thin-eligible targets with no omitted-boundary defect, non-inferior semantic/downstream quality, and materially lower candidate-boundary I/O; source reads are excluded from claimed savings.
- WALL_TIME alone never promotes. One adverse test may reject; one success never establishes a general rule.

Rollback immediately on duplicate substantive side effects, lost recurring fallback, stale authority overwrite, unrecoverable durable state, or a material defect shown to be hidden by an omitted persistence boundary.

## LW21 B2 fresh-fetch review
TARGET=baseline preservation; FAILURE_MODE=v0.4 candidate compressed away the explicit comparable-sample contract and persist-review-revise defect schema from v0.3; REQUIRED_CHANGE=restore those invariants before accepting persistence-mode changes. RESOLVED.
TARGET=thin safety; FAILURE_MODE='durable source exists' alone could permit thinning despite representation-sensitive decisions; REQUIRED_CHANGE=four-part reconstructibility test plus rollback. RESOLVED.
TARGET=I/O accounting; FAILURE_MODE=source reads could be mislabeled as thinning savings; REQUIRED_CHANGE=count necessary source reads as ARTIFACT_IO and compare candidate-boundary I/O separately. RESOLVED.

B2_VALIDATION=PASS_AFTER_REGRESSION_CORRECTION. FULL_CHAIN caught a real regression in the candidate itself, supporting retention of FULL_CHAIN for policy-definition/source-of-truth mutation classes.

## Decision record
Record CURRENT_CANDIDATE, PRIMARY_VARIABLE, COMPARABILITY, LEAD_TIME, SCHEDULER_WRITES, UNITS, SEMANTIC_OUTPUTS, ARTIFACTS_CHANGED, PERSISTENCE_MODE/REASON, MATERIAL_CORRECTIONS, OMITTED_BOUNDARY_DEFECT, ARTIFACT_IO_RAW/NORMALIZED, CONTROL_IO, WORKED, EVIDENCE, DECISION, NEXT.

## Current long-work research rule
Dynamic top-of-prompt TO-DO is hot-path execution state; Issue #1 remains durable authority. Value-gated target selection ranks eligible work. Persistence mode is separately gated. Judge package size by eligible semantic capacity/downstream value and persistence thinning by quality-preserving candidate-boundary I/O reduction; do not infer reasoning depth from elapsed time.
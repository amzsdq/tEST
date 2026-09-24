# Relay Optimization Convergence Protocol v0.5

Status: P5M6 AUTO-REFILL ACTIVE

## Objective
Converge to the smallest relay policy that maximizes semantic useful work while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state. Longer wall-clock time is diagnostic only; fast completion should expose spare capacity for more useful work.

## Evidence classes
- SEMANTIC_OUTPUT — validated rule/spec/decision with named downstream consequence.
- ARTIFACT_IO — persistence/fetch required by a real dependency or review boundary.
- CONTROL_IO — scheduler mutations, markers, baton/checkpoint writes, verification-only control reads.
- REFILL_IO — compact same-invocation recovery checkpoints between substantive packages; tracked separately from scheduler mutations.
- WALL_TIME — GitHub-server END_MARKER.created_at - START_MARKER.created_at.

## Comparable-sample contract
A comparison is valid only when samples hold constant, or explicitly normalize, scheduler mutation count, marker/baton shape, materially relevant artifact I/O, lead-time policy, and acceptance semantics. Package-size trials may intentionally increase useful units and resulting artifact I/O, but claims are then limited to capacity/useful-output gain. Auto-refill trials additionally change packages-per-invocation; compare invocation-level useful output and control overhead rather than pretending package-level wall time is unchanged.

## Controlled convergence
Freeze baseline; change one primary variable; repeat samples; separate WRITE_OK/STATE_OK/WAKE_OK/WORK_OK; measure semantic outputs independently from artifact/control/refill I/O and WALL_TIME.

## Experiment eligibility gate
Every added work unit must have downstream value, substantive uncertainty/real correction need, and a discriminating result. Reject units created only to enlarge a package or keep an invocation alive.

## Causal layers
Treat package size, packages-per-invocation/refill, target ranking, persistence mode, semantic counting, scheduler/control, and lead-time as distinct variables. A claim about one layer is NON_COMPARABLE if another layer changes without explicit normalization.

## Persist-review-revise baseline
For an eligible durable artifact: build/revise -> persist -> fresh fetch -> criteria-first review -> record real defects as TARGET / FAILURE_MODE / REQUIRED_CHANGE -> defect-mapped revision -> persist/fresh fetch -> PASS/RETEST/REJECT. Review may legitimately return zero defects.

## Persistence-mode gate
Target value and persistence eligibility are separate. FULL_CHAIN applies when later decisions depend on a newly persisted representation, source-of-truth mutation is being made, or persisted reality is itself under test. THIN_ELIGIBLE is a promoted bounded default only when named durable source evidence is authoritative/freshly readable, the exact decision can be reconstructed from named fields, candidate persistence adds no authority, and omission cannot hide relevant representation drift.

FULL_CHAIN candidate boundary: candidate persist -> fresh fetch -> criteria-first review -> defect-caused revision persist -> fresh fetch -> validation.
THIN_ELIGIBLE: fresh durable-source evidence -> semantic review/decision -> explicit reconstructibility validation; no ceremonial candidate copy. Necessary source reads remain ARTIFACT_IO and never count as savings.

A thin audit may conclude that authoritative mutation is required; mutation then escalates to FULL_CHAIN. Any material defect attributable specifically to an omitted candidate boundary rolls back thinning for that target class.

## Package-capacity experiment
Large-package trials pre-shape independently valuable work, preserve actual result dependencies, keep scheduler policy unchanged, and prohibit sleep/redundant summaries/redundant reads/fake defects/low-value artifacts. Record UNITS_PLANNED/DONE/REMAINING, semantic outputs/downstream consequences, artifacts changed, ARTIFACT_IO, CONTROL_IO, server-clock WORKED, PACKAGE_COMPLETE, SATURATED, and exact remainder.

30–36 eligible-unit scale is promoted for semantic capacity+density under tested conditions. This is a package-shape result, not an invocation-end rule and not a wall-time guarantee.

## Same-invocation auto-refill experiment
`PACKAGE_COMPLETE != TURN_COMPLETE`.

A completed package triggers immediate parent-goal reassessment. If useful non-redundant work remains, derive and execute the next substantive package in the SAME invocation. Persist a compact REFILL_BOUNDARY containing package result, cumulative useful outputs, and next package; do not touch the scheduler at refill boundaries.

Valid invocation stop: PROGRAM_COMPLETE, genuine external blocker with no useful independent work, runtime/tool/safety limit, or evidence-based NO_USEFUL_WORK_REMAINS. TO-DO exhaustion, package completion, artifact completion, checkpoint creation, semantic-output quota, or scheduler preparation are not stop conditions.

Auto-refill outcomes: REFILL_GAIN, REFILL_NO_GAIN, REFILL_SATURATED_RUNTIME, REFILL_INVALID_PADDING, NON_COMPARABLE. First-sample validity requires package N completion followed by substantive package N+1 in the same invocation when useful work remains. Promotion requires repeated multi-package evidence under one final scheduler mutation.

## Promotion / rollback
- Scheduler/control: repeated WAKE_OK/WORK_OK, no duplicate-authority violation, relevant recovery evidence.
- Work shaping: repeated semantic/downstream-value gain under unchanged scheduler/control policy.
- Persistence thinning: repeated thin-eligible targets with no omitted-boundary defect, non-inferior semantic/downstream quality, and lower candidate-boundary I/O.
- Auto-refill: repeated invocations with >=2 substantive packages when work remains, no padding, one final scheduler mutation, and increased invocation-level useful output without safety/recovery regression.
- WALL_TIME alone never promotes. One adverse test may reject; one success never establishes a general rule.

Rollback immediately on duplicate substantive side effects, lost recurring fallback, stale authority overwrite, unrecoverable durable state, a material defect hidden by omitted persistence boundary, or refill behavior that manufactures low-value work instead of following the parent goal.

## Decision record
Record CURRENT_CANDIDATE, PRIMARY_VARIABLE, COMPARABILITY, LEAD_TIME, SCHEDULER_WRITES, PACKAGES_COMPLETED, REFILL_BOUNDARIES, UNITS, SEMANTIC_OUTPUTS, ARTIFACTS_CHANGED, PERSISTENCE_MODE/REASON, MATERIAL_CORRECTIONS, OMITTED_BOUNDARY_DEFECT, ARTIFACT_IO, REFILL_IO, CONTROL_IO, WORKED, EVIDENCE, DECISION, STOP_REASON, NEXT.

## Current long-work research rule
Dynamic top-of-prompt TO-DO is the first queue head, not an invocation cap; Issue #1 remains durable authority. Value-gated target selection ranks eligible work. Persistence mode is separately gated. Package completion causes refill while useful work remains. Judge package size by semantic capacity/downstream value, persistence thinning by quality-preserving candidate-boundary I/O reduction, and auto-refill by invocation-level useful output/control overhead. Do not infer reasoning depth from elapsed time.
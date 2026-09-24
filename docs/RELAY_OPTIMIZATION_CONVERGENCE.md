# Relay Optimization Convergence Protocol v0.3

Status: LW15 FRESH-FETCH REVIEWED

## Objective
Converge to the smallest relay policy that maximizes **semantic useful work** while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state. Longer wall-clock time is diagnostic only.

## Evidence classes
- **SEMANTIC_OUTPUT** — new decision, validated finding, corrected artifact, discriminating test, or operational rule that changes downstream action.
- **ARTIFACT_IO** — persistence/fetch required by a real dependency or review boundary.
- **CONTROL_IO** — scheduler mutations, markers, baton/checkpoint writes, verification-only reads.
- **WALL_TIME** — GitHub-server END_MARKER.created_at - START_MARKER.created_at.

## Comparable-sample contract
A duration/useful-work comparison is valid only when samples hold constant, or explicitly normalize, scheduler mutation count, marker/baton shape, artifact persistence/fetch shape, lead-time policy, and acceptance semantics. Otherwise report **NON_COMPARABLE**.

### Package-size attribution exception
A package-size trial intentionally changes the number of useful units, so raw artifact I/O and acceptance count may rise as consequences of the primary variable. Attribution to `PACKAGE_SIZE` is allowed only if:
1. scheduler/control policy and lead-time remain fixed;
2. each added unit independently passes the eligibility gate;
3. artifact I/O is reported both raw and per semantic output;
4. no new control mechanism is introduced;
5. the conclusion is limited to **capacity/useful-output gain**, not reasoning depth or per-unit efficiency.

Thus LW15 may be comparable for *capacity* while non-comparable for per-unit duration.

## Controlled convergence
Freeze baseline; change one primary variable; repeat samples; separate WRITE_OK/STATE_OK/WAKE_OK/WORK_OK; measure semantic outputs independently from artifact/control I/O and WALL_TIME.

## Experiment eligibility gate
Every added work unit must have:
1. downstream value;
2. substantive uncertainty or a real correction/decision need;
3. a discriminating result.
Reject units created only to enlarge a package.

## Persist-review-revise protocol
For an eligible durable artifact: build/revise → persist → fresh fetch → criteria-first review → record real defects as `TARGET / FAILURE_MODE / REQUIRED_CHANGE` → defect-mapped revision → persist/fresh fetch → PASS/RETEST/REJECT. Review may legitimately return zero defects.

## Package-capacity experiment
Package size is a distinct work-shaping variable. A small package can terminate correctly while safe valuable work remains outside its acceptance boundary.

Large-package trials must pre-shape independently valuable work, use multiple real artifacts/questions when justified, preserve actual result dependencies, keep scheduler policy unchanged, and prohibit sleep/redundant summaries/redundant reads/fake defects/low-value artifacts.

Record:
- `UNITS_PLANNED`, `UNITS_DONE`, `UNITS_REMAINING`;
- `SEMANTIC_OUTPUTS` and downstream consequences;
- `ARTIFACTS_CHANGED`;
- `ARTIFACT_IO_RAW` and `ARTIFACT_IO_PER_SEMANTIC_OUTPUT`;
- `CONTROL_IO`;
- server-clock `WORKED`;
- `PACKAGE_COMPLETE` and exact remaining unit when incomplete.

### Capacity/saturation interpretation
- **CAPACITY_GAIN** — larger eligible package produces materially more semantic output/downstream value with unchanged scheduler/control policy.
- **SATURATED** — runtime/turn boundary stops execution while eligible safe units remain; exact remainder is handed off.
- **NO_GAIN** — larger package completes but useful semantic output does not materially exceed smaller-package baseline.
- **NON_COMPARABLE** — an unrelated control/mechanism change prevents attribution.

A target such as “10-minute-class” describes intended workload capacity only. Never wait or add work solely to hit a clock target.

### Large-package stop rule
Completion means all eligible predeclared units are complete or a genuine blocker/runtime/safety boundary is reached. Completing one artifact, review, or decision is not package completion. If saturation occurs, preserve the remainder rather than shrinking the package after the fact.

## Optimization order
A scheduler reliability → B mutation count → C recovery → D useful-work duty cycle/work shaping.

## Promotion rule
- Scheduler/control: repeated WAKE_OK/WORK_OK, no duplicate-authority violation, relevant recovery evidence.
- Work shaping: at least two samples appropriate to the claimed effect. For package capacity, require two large-package samples showing semantic/downstream-value gain with unchanged scheduler/control policy; compare normalized I/O as a secondary efficiency metric.
- Protocol/document: fresh-fetch validation plus demonstrated downstream use or a discriminating test enabled by revision.

WALL_TIME alone never promotes. One adverse test may reject; one successful sample never establishes a general rule.

## Rollback rule
Rollback immediately on duplicate substantive side effects, lost recurring fallback, stale authority overwrite, or unrecoverable durable state.

## Decision record
```text
CURRENT_CANDIDATE=<version>
PRIMARY_VARIABLE=<one variable>
COMPARABILITY=<capacity/per-unit scopes + reason>
LEAD_TIME=<duration>
SCHEDULER_WRITES_PER_WAKE=<n>
UNITS_PLANNED=<n>
UNITS_DONE=<n>
UNITS_REMAINING=<exact remainder>
SEMANTIC_OUTPUTS=<count + downstream value>
ARTIFACTS_CHANGED=<list>
ARTIFACT_IO_RAW=<reads/writes>
ARTIFACT_IO_PER_SEMANTIC_OUTPUT=<normalized>
CONTROL_IO=<scheduler/marker/baton operations>
WORKED=<GitHub server delta>
WORK_OK=<yes/no>
EVIDENCE=<results>
DECISION=<PROMOTE/RETEST/REJECT>
NEXT_DISCRIMINATING_TEST=<single test>
```

## Current long-work research rule
Dynamic top-of-prompt TO-DO is hot-path execution state; Issue #1 remains durable authority. Package size is now an explicit primary variable. Judge it by eligible semantic capacity and downstream value under fixed scheduler/control policy, with normalized artifact I/O reported separately; do not infer reasoning depth from elapsed time.
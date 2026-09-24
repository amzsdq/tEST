# Relay Optimization Convergence Protocol v0.3-candidate

Status: LW15 CANDIDATE — pending fresh-fetch adversarial review

## Objective
Converge to the smallest relay policy that maximizes **semantic useful work** while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state.

The target is neither fewest instructions nor longest wall-clock time. A change wins only when evidence shows better useful output/reliability for equal or lower control cost.

## Evidence classes
Every experiment separates:
- **SEMANTIC_OUTPUT** — a new decision, validated finding, corrected artifact, discriminating test, or operational rule that changes what should happen next.
- **ARTIFACT_IO** — persistence/fetch required to create a real dependency or review boundary.
- **CONTROL_IO** — scheduler mutations, markers, baton/checkpoint writes, verification-only reads.
- **WALL_TIME** — GitHub-server END_MARKER.created_at - START_MARKER.created_at; telemetry only.

Longer WALL_TIME without additional SEMANTIC_OUTPUT is not improvement. ARTIFACT_IO is justified only when it creates a real dependency/review boundary.

## Comparable-sample contract
A duration/useful-work comparison is valid only when samples hold constant, or explicitly normalize, scheduler mutation count, marker/baton shape, artifact persistence/fetch shape, lead-time policy, and package acceptance threshold. Otherwise report **NON_COMPARABLE**.

## Controlled convergence
1. Freeze exact baseline prompt/protocol and record the current candidate.
2. Change one primary variable; keep unrelated controls constant.
3. Use repeated samples. One PASS is weak evidence; include an adverse/boundary test before production promotion when relevant.
4. Separate WRITE_OK / STATE_OK / WAKE_OK / WORK_OK.
5. Record semantic outputs/downstream value independently from ARTIFACT_IO, CONTROL_IO, and WALL_TIME.

## Experiment eligibility gate
Before work amplification require downstream value, substantive uncertainty, and a discriminating comparison. Never invent defects or low-value documents merely to create stages.

## Persist-review-revise protocol
Use only when an eligible durable artifact matters downstream.
1. Build/materially revise candidate from necessary evidence.
2. Persist candidate.
3. Freshly fetch persisted candidate before review.
4. Record each real defect as `TARGET / FAILURE_MODE / REQUIRED_CHANGE`.
5. Map each material revision to one or more defects.
6. Persist and freshly fetch revision.
7. Validate against explicit acceptance criteria and issue PASS/RETEST/REJECT.

Review begins from explicit criteria after fresh fetch and may return zero defects.

## Package-capacity experiment
Package size is a distinct work-shaping variable. A small package can terminate correctly yet leave safe useful work unattempted because the acceptance boundary itself is too near.

For a large-package trial:
- pre-shape enough **independently valuable** work to exceed the prior package's semantic capacity;
- use multiple real artifacts/questions when one artifact cannot supply enough legitimate work;
- require later units to consume actual earlier results where dependencies exist;
- keep scheduler mutation policy unchanged;
- prohibit sleep, repeated summaries, redundant reads, fake defects, or low-value artifacts;
- record `UNITS_PLANNED`, `UNITS_DONE`, `SEMANTIC_OUTPUTS`, `ARTIFACTS_CHANGED`, `ARTIFACT_IO`, `CONTROL_IO`, and server-clock `WORKED`.

### Capacity/saturation interpretation
A larger package supports the package-size hypothesis only when it produces **more semantic outputs or downstream value** before termination, not merely more tool calls or longer WALL_TIME.

Interpret outcomes as:
- **CAPACITY_GAIN** — materially larger package yields more useful semantic output with no extra scheduler/control cost.
- **SATURATED** — substantial safe useful units remain but the turn terminates or runtime limits prevent completion; persist the exact remaining units for continuation.
- **NO_GAIN** — larger package completes but semantic value does not materially exceed the smaller baseline.
- **NON_COMPARABLE** — material control/I/O changes prevent attribution to package size.

Do not require a target number of minutes. A ten-minute-class package is a workload-sizing hypothesis, not a waiting requirement.

## Optimization order
Phase A scheduler reliability; Phase B mutation count; Phase C recovery; Phase D useful-work duty cycle and work shaping.

## Promotion rule
- Scheduler/control promotion: repeated WAKE_OK/WORK_OK, no duplicate-authority violation, recovery evidence where behavior changes.
- Work-shaping promotion: at least two comparable samples showing semantic-output/downstream-value gain without extra control cost; WALL_TIME alone is insufficient.
- Protocol/document promotion: fresh-fetch validation plus demonstrated downstream use or a discriminating test enabled by the revision.

A single adverse test may reject; one successful sample never establishes a general production rule.

## Rollback rule
Rollback immediately on duplicate substantive side effects, lost recurring fallback, stale authority overwrite, or unrecoverable durable state.

## Decision record
```text
CURRENT_CANDIDATE=<prompt/protocol version>
PRIMARY_VARIABLE=<one variable>
COMPARABILITY=<COMPARABLE/NON_COMPARABLE + reason>
LEAD_TIME=<duration>
SCHEDULER_WRITES_PER_WAKE=<n>
UNITS_PLANNED=<n>
UNITS_DONE=<n>
SEMANTIC_OUTPUTS=<count + downstream value>
ARTIFACTS_CHANGED=<list>
ARTIFACT_IO=<substantive reads/writes>
CONTROL_IO=<scheduler/marker/baton operations>
WORKED=<GitHub server delta>
WORK_OK=<yes/no>
KNOWN_FAILURES=<list>
EVIDENCE=<comparable samples/results>
DECISION=<PROMOTE/RETEST/REJECT>
NEXT_DISCRIMINATING_TEST=<single test>
```

## Current long-work research rule
Dynamic top-of-prompt TO-DO is a hot-path execution pointer; Issue #1 remains durable authority. Pre-shaped packages count only when stages have genuine useful value; persisted boundaries count only when they create real dependency/review value. Package size is now explicitly testable as a primary variable: compare useful semantic capacity, not elapsed time alone.
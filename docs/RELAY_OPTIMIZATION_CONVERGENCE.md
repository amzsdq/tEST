# Relay Optimization Convergence Protocol v0.2

Status: ACTIVE / LW13 VALIDATED REVISION

## Objective
Converge to the smallest relay policy that maximizes **semantic useful work** while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state.

The target is not fewest instructions or longest wall-clock time. A change wins only when evidence shows better useful output/reliability for equal or lower control cost.

## Evidence classes
Every experiment must separate:
- **SEMANTIC_OUTPUT** — a new decision, validated finding, corrected artifact, discriminating test, or operational rule that changes what should happen next.
- **ARTIFACT_IO** — persistence/fetch required to create a real dependency or review boundary.
- **CONTROL_IO** — scheduler mutations, markers, baton/checkpoint writes, verification-only reads.
- **WALL_TIME** — GitHub-server END_MARKER.created_at - START_MARKER.created_at; telemetry only.

Longer WALL_TIME without additional SEMANTIC_OUTPUT is not improvement. ARTIFACT_IO is justified only when it creates a real dependency/review boundary, not to inflate duration.

## Comparable-sample contract
A duration/useful-work comparison is valid only when the samples hold constant, or explicitly normalize, all of:
- scheduler mutation count;
- marker/baton control shape;
- artifact persistence/fetch shape;
- lead-time policy;
- package acceptance threshold.

If these differ materially, report the comparison as **NON_COMPARABLE** rather than attributing a WORKED delta to semantic depth.

## Controlled convergence
1. Freeze exact baseline prompt/protocol and record the current candidate.
2. Change one primary variable; keep unrelated controls constant.
3. Use repeated samples. One PASS is weak evidence; include an adverse/boundary test before production promotion when the mechanism can fail under adversity.
4. Separate end-to-end success layers:
   - WRITE_OK — update accepted.
   - STATE_OK — intended recurrence/enabled state persisted.
   - WAKE_OK — intended invocation occurred.
   - WORK_OK — correct authority/checkpoint resumed without duplicate substantive side effects.
5. Record semantic outputs/downstream value independently from ARTIFACT_IO, CONTROL_IO, and WALL_TIME.

## Experiment eligibility gate
Before running a work-amplification experiment, require all three:
1. **Downstream value:** output can change a later decision, prompt, test, or operational artifact.
2. **Substantive uncertainty:** a real defect/question exists; never invent defects or low-value documents to create stages.
3. **Discriminating comparison:** success/failure can distinguish the mechanism from the baseline.

If any gate fails, do not run the experiment merely to collect duration.

## Persist-review-revise protocol
Use only when an eligible durable artifact already matters downstream.
1. Build/materially revise candidate from necessary evidence.
2. Persist candidate.
3. Freshly fetch persisted candidate before review; review fetched representation, not pre-write draft.
4. Record each real defect as `TARGET / FAILURE_MODE / REQUIRED_CHANGE`.
5. Map each material revision to one or more defects.
6. Persist and freshly fetch revision.
7. Validate against explicit acceptance criteria and issue PASS/RETEST/REJECT.

### Review independence
A review is independent enough for this protocol only if it is performed **after fresh fetch** and begins from explicit acceptance/failure criteria rather than from the intended edits. The reviewer must be willing to return zero defects; a minimum defect quota is a validation target only when real defects exist, never permission to fabricate them.

## Optimization order
### Phase A — Scheduler reliability
Find minimum lead time with acceptable repeated wake delivery.
### Phase B — Mutation count
Compare control-plane write counts; equivalent reliability means fewer writes win.
### Phase C — Recovery
Inject missed wake, stale durable due, premature turn end, and duplicate actor attempts. Reject candidates that cannot recover from durable state.
### Phase D — Useful-work duty cycle
Reduce diagnostics, redundant metadata checks, repeated policy text, scheduler mutations, and unnecessary repository I/O. Then test work-shaping mechanisms by semantic output, not elapsed time alone.

## Promotion rule
Promotion requires evidence appropriate to the claimed layer:
- **Scheduler/control promotion:** repeated WAKE_OK/WORK_OK, no duplicate-authority violation, and recovery evidence where recovery behavior changes.
- **Work-shaping promotion:** at least two comparable samples showing semantic-output/downstream-value gain without extra control cost; WALL_TIME may support diagnosis but is never sufficient.
- **Protocol/document promotion:** fresh-fetch validation against explicit criteria plus demonstrated downstream use or a discriminating test enabled by the revision.

A single adverse test may reject a candidate. A single successful sample does not establish a general production rule.

## Rollback rule
Rollback immediately when duplicate substantive side effects occur, recurring fallback is lost, stale state can overwrite newer authority, or failure cannot be recovered from durable state.

## Decision record
```text
CURRENT_CANDIDATE=<prompt/protocol version>
PRIMARY_VARIABLE=<one variable>
COMPARABILITY=<COMPARABLE/NON_COMPARABLE + reason>
LEAD_TIME=<duration>
SCHEDULER_WRITES_PER_WAKE=<n>
SEMANTIC_OUTPUTS=<count + downstream value>
ARTIFACT_IO=<reads/writes required by substantive dependency>
CONTROL_IO=<scheduler/marker/baton operations>
WORKED=<GitHub server delta>
WORK_OK=<yes/no>
KNOWN_FAILURES=<list>
EVIDENCE=<comparable samples/results>
DECISION=<PROMOTE/RETEST/REJECT>
NEXT_DISCRIMINATING_TEST=<single test>
```

## Current long-work research rule
Dynamic top-of-prompt TODO is a hot-path execution pointer; Issue #1 remains durable authority. Pre-shaped packages count only when stages have genuine result dependencies. Persist-review-revise remains a candidate work-shaping mechanism until repeated **comparable** samples show semantic gain; do not universalize it from elapsed-time growth alone.

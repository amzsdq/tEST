# Relay Optimization Convergence Protocol v0.2-candidate

Status: ACTIVE / LW13 REVIEW CANDIDATE

## Objective
Converge to the smallest relay policy that maximizes **semantic useful work** while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state.

The target is not fewest instructions or longest wall-clock time. A change wins only when evidence shows better useful output/reliability for equal or lower control cost.

## Evidence classes
Every experiment must separate:
- **SEMANTIC_OUTPUT** — a new decision, validated finding, corrected artifact, discriminating test, or operational rule that changes what should happen next.
- **ARTIFACT_IO** — persistence/fetch required to make a real dependency or review boundary observable.
- **CONTROL_IO** — scheduler mutations, markers, baton/checkpoint writes, verification-only reads.
- **WALL_TIME** — GitHub-server END_MARKER.created_at - START_MARKER.created_at; telemetry only.

Longer WALL_TIME without additional SEMANTIC_OUTPUT is not improvement. ARTIFACT_IO is justified only when it creates a real dependency/review boundary, not to inflate duration.

## Controlled convergence
1. **Freeze a baseline.** Record exact prompt/protocol version and current candidate.
2. **Change one primary variable.** Keep scheduler lead time, mutation count, and unrelated prompt controls constant unless they are the variable under test.
3. **Use repeated samples.** One PASS is weak evidence. Repeat the candidate and include an adverse/boundary test before promotion when practical.
4. **Separate end-to-end success layers:**
   - WRITE_OK — update accepted.
   - STATE_OK — intended recurrence/enabled state persisted.
   - WAKE_OK — intended invocation occurred.
   - WORK_OK — correct authority/checkpoint resumed without duplicate substantive side effects.
5. **Separate useful-work quality from duration.** Record semantic outputs and their downstream decision value independently from artifact/control I/O and WALL_TIME.

## Experiment eligibility gate
Before running a work-amplification experiment, require all three:
1. **Downstream value:** its output can change a later decision, prompt, test, or operational artifact.
2. **Substantive uncertainty:** a real defect/question exists; do not invent defects or low-value documents to create stages.
3. **Discriminating comparison:** success/failure can distinguish the candidate mechanism from the current baseline.

If any gate fails, do not run the experiment merely to collect duration.

## Persist-review-revise protocol
Use this only when an eligible durable artifact already matters downstream.
1. Build/materially revise candidate from necessary evidence.
2. Persist candidate.
3. Freshly fetch the persisted candidate before review; review the fetched representation, not the pre-write draft.
4. Record each real defect as `TARGET / FAILURE_MODE / REQUIRED_CHANGE`.
5. Map each material revision to one or more defects.
6. Persist and freshly fetch the revision.
7. Validate against explicit acceptance criteria and issue PASS/RETEST/REJECT.

## Optimization order
### Phase A — Scheduler reliability
Find minimum lead time with acceptable repeated wake delivery.
### Phase B — Mutation count
Compare control-plane write counts; if reliability is equivalent, fewer writes win.
### Phase C — Recovery
Inject missed wake, stale durable due, premature turn end, and duplicate actor attempts. Reject candidates that cannot recover from durable state.
### Phase D — Useful-work duty cycle
Reduce diagnostic messages, redundant metadata checks, repeated policy text, scheduler mutations, and unnecessary repository I/O. Then test work-shaping mechanisms by semantic output, not elapsed time alone.

## Promotion rule
Promote only when the candidate has:
- repeated WORK_OK/WAKE_OK appropriate to the tested layer;
- no duplicate-authority violation;
- recovery evidence where the candidate affects recovery;
- semantic output/reliability gain or lower overhead versus baseline;
- no duration gain attributable only to extra ARTIFACT_IO or CONTROL_IO.

For work-shaping mechanisms, at least two comparable samples are required before promotion unless a single adverse test falsifies the candidate.

## Rollback rule
Rollback immediately when duplicate substantive side effects occur, recurring fallback is lost, stale state can overwrite newer authority, or failure cannot be recovered from durable state.

## Decision record
```text
CURRENT_CANDIDATE=<prompt/protocol version>
PRIMARY_VARIABLE=<one variable>
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
Dynamic top-of-prompt TODO is a hot-path execution pointer; Issue #1 remains durable authority. Pre-shaped packages may increase useful work only when stages have genuine result dependencies. Persist-review-revise is a candidate mechanism, not yet a universal requirement: it must demonstrate repeatable semantic gain under comparable artifact/control I/O before promotion.

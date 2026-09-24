# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M4 — Large TO-DO package candidate

State: EXPERIMENTAL
Parent: P5M3 dynamic TO-DO pointer
Primary variable: PACKAGE_SIZE
Rollback: P5M3

### Intent
P5M3 showed that a concrete top-of-prompt TO-DO pointer reduces startup reconstruction, but 5–6 unit packages remained highly compressible. P5M4 tests whether a materially larger package increases semantic capacity per invocation without adding scheduler/control mutations.

### Hot-path contract
- Keep `TO-DO LIST FOR THIS TURN` near the top and replace it at each continuing turn.
- Issue #1 remains authoritative durable state; the TO-DO is a hot-path execution pointer.
- Normal continuation uses the same automation and exactly one final scheduler mutation.
- Preserve recurring `RRULE:FREQ=HOURLY`; default next lead remains current Asia/Seoul time +3 minutes unless another lead trial is explicitly active.
- START/END GitHub server timestamps remain the only WORKED clock.

### Large-package contract
A large package normally contains 12–15 independently valuable substantive units and must not be shrunk merely because an early unit completes. Eligible units must contribute at least one of: evidence acquisition required by a later decision, material artifact production/revision, adversarial validation, defect-caused correction, or cross-artifact synthesis that changes a future decision.

A qualifying two-artifact package uses this shape when appropriate:
1. choose Artifact C with downstream value and real semantic uncertainty;
2. define C acceptance/failure criteria from necessary evidence;
3. materially revise/build C and persist candidate;
4. fresh-fetch C and criteria-first review it;
5. record only real defects as TARGET / FAILURE_MODE / REQUIRED_CHANGE;
6. revise C only for material findings, persist/fresh-fetch, validate;
7. use C's actual result to choose Artifact D's unresolved question;
8. gather only D evidence selected by C;
9. define D criteria and materially revise/build D;
10. persist/fresh-fetch/review D;
11. revise D for material findings, persist/fresh-fetch, validate;
12. synthesize C+D into >=5 non-redundant evidence-to-decision outputs;
13. compare semantic capacity, artifact I/O, control I/O, and WORKED with smaller-package baselines;
14. persist exact baton/NEXT;
15. replace next TO-DO and perform the one final scheduler update.

### Non-padding rule
Never increase package size with sleep, repeated summaries, redundant fetches, fabricated defects, synthetic checkpoints, or low-value artifacts. If runtime/blocker/safety stops execution while eligible useful units remain, record SATURATED plus exact UNITS_REMAINING and carry them first into the next TO-DO.

### Measurement
Record:
- UNITS_PLANNED / UNITS_DONE / UNITS_REMAINING
- PACKAGE_COMPLETE
- SEMANTIC_OUTPUTS
- ARTIFACTS_CHANGED
- ARTIFACT_IO_RAW
- ARTIFACT_IO_PER_SEMANTIC_OUTPUT
- CONTROL_IO
- WORKED from GitHub server markers

PACKAGE_SIZE is a semantic-capacity variable, not a claim about reasoning depth. Wall time alone never promotes it. Promotion requires repeated large-package samples showing materially greater useful/downstream output while scheduler/control policy stays unchanged.

### Recovery
If prompt TO-DO and Issue #1 disagree, Issue #1 wins. If a large package cannot be completed, the durable baton must name exact remaining units and immediate next action rather than a vague research topic.

---

## P4V11 — GitHub server timestamp work-duration source of truth

State: APPLIED
Parent: P4V10
Primary variable: work-duration time source only
Rollback: P4V10

- Append unique START_MARKER immediately before substantive work and matching END_MARKER after all substantive work and the allowed final scheduler update.
- `WORKED = END_MARKER.created_at - START_MARKER.created_at` using GitHub server timestamps only.
- Model/local time strings are display-only; missing/ambiguous marker pair means WORKED=UNKNOWN.

## Promoted P4 hot-path invariants retained by P5M4

- Same automation identity; no new automation for normal continuation.
- One final recurring RRULE scheduler write on the normal path.
- Issue #1 compact tail is sufficient for routine bootstrap; broader documents are cold-path unless ambiguity, boundary, anomaly, prompt change, rollback, or substantive package evidence requires them.
- Wake, scheduler write/state, and useful work remain distinct observations.
- Routine clean success may omit redundant positive fields when their meaning is reconstructable; anomaly/recovery evidence remains explicit.
- Simplicity is preferred only after recovery and duplicate-safety equivalence is established.

## Historical note
Earlier P0–P4 variants established the single-final-write recurring path, compact Issue evidence, Issue-tail bootstrap, conditional verification, positive-field omission, jitter telemetry, and GitHub-server WORKED clock. Their detailed historical evidence remains in Issue #1 and the experiment ledger; this registry keeps the currently relevant prompt semantics compact.
# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| P1-10M-01 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | +73s vs intended due | NO observed | n/a | research state restored and trial evaluated | low | PASS | Intended due 11:44:02 KST; automation turn observed at 11:45:15 KST. |
| P1-10M-02 | P0R/P1 path | lead time | 10m class | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Issue evidence: intended 11:57:00; runtime context 11:56:14. |
| P1-10M-03 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Third consecutive +10m-class continuation. |
| P1-5M-01 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | First +5m continuation. |
| P1-5M-02 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Second +5m continuation. |
| P1-5M-03 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Third +5m continuation. |
| P1-3M-01 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | First +3m continuation. |
| P1-3M-02 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored; trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Reconciled from Issue #1. |
| P1-3M-03 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | third identical +3m sample | low | PASS_WITH_TIMING_ANOMALY | Issue #1 records +3m class reaching 3/3 end-to-end continuation. |
| P1-2M-01 | P0R/P1 path | lead time | 2m | 1 | YES | YES | NO near wake | YES after fallback | n/a | NO observed | YES | hourly RRULE cold recovery | low | MISSED_NEAR_OCCURRENCE + RECOVERY_PASS | First +2m sample missed fast continuation; recurring fallback recovered. |
| P1-2M-02 | P0R/P1 path | lead time | 2m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | n/a | durable state restored | low | PASS_WITH_TIMING_ANOMALY | Mixed +2m evidence; not suitable as reliable default. |
| P1-3M-04 | P0R/P1 path | lead time | 3m | 1 | YES | YES | YES | YES | non-authoritative | NO observed | prior E5 evidence | boundary confirmation | low | PASS | +3m retained as leading minimum practical default. |
| P2-3M-01 | P0R/P2 path | provisional fallback presence | 3m final | 2 | YES | YES | YES | YES | non-authoritative | NO observed | no incremental benefit | normal-path comparison | higher than P1 | PASS_BUT_REJECTED | Added one scheduler mutation without demonstrated recovery/correctness gain over P1. |
| E8-P1-COLD-01 | P0R/P1 path | omit final fast rearm after durable checkpoint | hourly fallback | 0 after checkpoint | n/a | YES | YES | YES | ~59m recovery | NO observed | YES | cold resume from GitHub | low | RECOVERY_PASS | Existing hourly RRULE recovered without P2 provisional write. |
| E7-AUTHORITY | P0R/P1 path | duplicate authority/recovery | 3m fixed | 1 | n/a | YES | YES | YES | n/a | 0 | YES | atomic claim/recovery research | research-only | PASS_WITH_CONSTRAINT | Immutable epoch fencing + create-if-absent claim; external effects still require idempotency/reconciliation. |
| E8-MINIMAL-CHECKPOINT | P0R/P1 path | checkpoint schema | 3m fixed | 1 | YES | YES | YES | YES | n/a | 0 | YES | repeated interruption/resume | low | PASS | Minimal schema promoted: operation_id + immutable epoch/claim fence + executable next_action; fence-removal adverse test failed safely. |
| TEMPLATE | P0 | baseline | 1m | 6 | - | - | - | - | - | - | - | - | - | PENDING | Historical stress fixture, not an active production candidate. |

## Reconciliation note — 2026-09-22 17:22 KST

Issue #1 is authoritative for completed controlled trials. P2, E7 and E8 are no longer unresolved:
- P2 works but loses to P1 on parsimony.
- E8/P1 cold recovery proves the existing hourly recurrence can recover without a provisional scheduler write.
- E7 converged on immutable epoch fencing + atomic create-if-absent authority, with destination idempotency/reconciliation required for ambiguous external effects.
- E8 converged on the three-field minimal durable checkpoint `{operation_id, immutable epoch/claim fence, executable next_action}` with repeated resume success and a fence-removal adverse test.

Current candidate:

```text
CURRENT_CANDIDATE=P0R/P1 single-final-write path
LEAD_TIME=+3m
SCHEDULER_WRITES_PER_WAKE=1
RECURRENCE=RRULE:FREQ=HOURLY
CHECKPOINT={operation_id, immutable epoch/claim fence, executable next_action}
AUTHORITY=immutable epoch + atomic create-if-absent claim
KNOWN_FAILURES=+2m mixed reliability; arbitrary external non-idempotent effects cannot be exactly-once without destination support
RECOVERY_EVIDENCE=P1-2M-01 and E8-P1-COLD-01
NEXT_DISCRIMINATING_TEST=P4-VERIFY-FREQUENCY-01
```

## P4-VERIFY-FREQUENCY-01 design

Phase A/B/C evidence is sufficient to begin duty-cycle simplification. The next single primary variable is **final live-metadata verification frequency**. Scheduler path, +3m lead, RRULE recurrence, durable checkpoint and authority rules remain fixed.

Hypothesis: update success plus next-turn end-to-end WAKE_OK/WORK_OK may make unconditional same-turn post-write metadata verification redundant on the normal path. Because the current P0R prompt hard-requires verification, this turn only records the experiment design. A prompt-version change must be registered before executing the omission trial.

Success criterion for a future omission trial: scheduler update accepted; next intended wake occurs; correct checkpoint resumes; RRULE recurrence remains observable on the following turn; no duplicate work. Failure/rollback trigger: lost recurrence, wrong DTSTART behavior that cannot recover, or ambiguous scheduler state requiring same-turn verification.

## Result vocabulary

- PASS: end-to-end intended behavior observed
- WRITE_FAIL: scheduler update rejected
- STATE_MISMATCH: stored scheduler state differs from requested state
- MISSED_NEAR_OCCURRENCE: requested near-term occurrence did not invoke
- DUPLICATE_EXECUTION: more than one actor performed substantive work
- RECOVERY_PASS: injected failure recovered from durable state
- RECOVERY_FAIL: durable recovery did not restore correct continuation
- INCONCLUSIVE: observation insufficient to distinguish hypotheses

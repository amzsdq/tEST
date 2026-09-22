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
| P4-VFY-01-A | P4V0 | omit unconditional post-write live read | 3m class | 1 | YES | YES via update return | YES | YES | +10s | NO observed | inherited unchanged P1/E8 path | state restore + research | lower | PASS | First clean intended-due end-to-end omission sample. |
| P4-VFY-01-B | P4V0 | omit unconditional post-write live read | 3m class | 1 | YES | YES via update return | YES | YES | +108s | NO observed | inherited unchanged P1/E8 path | state restore + research | lower | PASS | Second clean intended-due sample. |
| P4-VFY-01-C | P4V0 | omit unconditional post-write live read | 3m class | 1 | YES | YES via update return | YES | YES | +141s | NO observed | inherited unchanged P1/E8 path | state restore + research | lower | PASS | Third clean intended-due sample. |
| P4-VFY-EARLY-01 | P4V0 | verification frequency | 3m class | 1 | YES | YES via update return | INCONCLUSIVE | YES | -146s | NO observed | n/a | anomaly classification | lower | TIMING_ANOMALY | Early invocation cannot be attributed to verification omission. |
| P4-VFY-EARLY-02 | P4V0 | verification frequency | 3m class | 1 | YES | YES via update return | INCONCLUSIVE | YES | -173s | NO observed | n/a | replicated anomaly + evidence-transfer analysis | lower | TIMING_ANOMALY | Replicates early-dispatch class; does not discriminate read-after-write policy. |
| P4-LOG-01-A | P4V2 | routine durable logging fan-out | 3m class | 1 | YES | YES via update return | YES | YES | non-authoritative | NO observed | inherited unchanged P1/E8 path | Issue-only routine evidence + next-turn reconstruction | lower | PASS | SAMPLE-1 evidence existed only in Issue #1 and was reconstructed exactly on SAMPLE-2. |
| P4-LOG-01-B | P4V2 | routine durable logging fan-out | 3m class | 1 | YES | YES via update return | YES | YES | non-authoritative | NO observed | inherited unchanged P1/E8 path | second Issue-only sample + boundary reconciliation | lower | PASS | SAMPLE-2 plus SAMPLE-1 ordering/status/NEXT were recoverable from unchanged ledger + Issue stream. |
| TEMPLATE | P0 | baseline | 1m | 6 | - | - | - | - | - | - | - | - | - | PENDING | Historical stress fixture, not an active production candidate. |

## Reconciliation note — 2026-09-22 19:21 KST

P4V2 logging fan-out is provisionally promoted on top of the existing P1/P4 path. Routine non-boundary success evidence may be appended to Issue #1 only; EXPERIMENT_LEDGER is updated at sample-set completion, promotion/rejection/rollback, or explicit reconciliation checkpoints.

Evidence:
- SAMPLE-1 was written only to Issue #1 while the ledger remained unchanged;
- SAMPLE-2 reconstructed SAMPLE-1 ordering, result, WRITE_OK/STATE_OK/WAKE_OK/WORK_OK, duplicate observation, and NEXT without ambiguity;
- at this boundary both samples were reconciled into this ledger without observed evidence loss;
- scheduler, +3m lead, checkpoint, authority, verification, and recovery mechanics were unchanged.

```text
CURRENT_CANDIDATE=P4V2 on P1 single-final-write path
LEAD_TIME=+3m class
SCHEDULER_WRITES_PER_WAKE=1
RECURRENCE=RRULE:FREQ=HOURLY
CHECKPOINT={operation_id, immutable epoch/claim fence, executable next_action}
AUTHORITY=immutable epoch + atomic create-if-absent claim
VERIFICATION=normal-path update-return validation; live read only on ambiguity/failure/reconciliation
BOOTSTRAP=EXPERIMENT_LEDGER + Issue #1 first; conditional canonical fallback
ROUTINE_LOGGING=Issue #1 only; ledger at boundaries/reconciliation
KNOWN_FAILURES=+2m mixed reliability; dispatch timestamp anomalies; arbitrary external non-idempotent effects require destination support
RECOVERY_EVIDENCE=P1-2M-01 and E8-P1-COLD-01
NEXT_DISCRIMINATING_TEST=select one further duty-cycle/control-overhead simplification; keep scheduler, +3m lead, checkpoint, authority, verification, bootstrap, and logging fixed
```

## Result vocabulary

- PASS: end-to-end intended behavior observed
- WRITE_FAIL: scheduler update rejected
- STATE_MISMATCH: stored scheduler state differs from requested state
- MISSED_NEAR_OCCURRENCE: requested near-term occurrence did not invoke
- DUPLICATE_EXECUTION: more than one actor performed substantive work
- RECOVERY_PASS: injected failure recovered from durable state
- RECOVERY_FAIL: durable recovery did not restore correct continuation
- INCONCLUSIVE: observation insufficient to distinguish hypotheses

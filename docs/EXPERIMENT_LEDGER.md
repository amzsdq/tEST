# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| P1-10M-01 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | +73s vs intended due | NO observed | n/a | research state restored and trial evaluated | low | PASS | Intended due 11:44:02 KST; automation turn observed at 11:45:15 KST. |
| P1-10M-02 | P0R/P1 path | lead time | 10m class | 1 | YES | YES | YES | YES | -46s vs stored DTSTART | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Intended due 11:57:00 KST; runtime observed at 11:56:14 KST. |
| P1-10M-03 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | -24s vs intended due | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Intended due 12:07:00 KST; automation runtime started 12:06:36 KST. Third consecutive end-to-end continuation. |
| P1-5M-01 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | -78s vs stored DTSTART | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Intended due 12:12:00 KST; automation runtime context began 12:10:42 KST. |
| P1-5M-02 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | -102s vs stored DTSTART | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Intended due 12:17:00 KST; automation runtime context began 12:15:18 KST. Second +5m-class end-to-end continuation. |
| P1-5M-03 | P0R/P1 path | lead time | 5m | 1 | YES | YES | YES | YES | +109s vs stored DTSTART | NO observed | n/a | durable state restored; prior trial evaluated | low | PASS_WITH_TIMING_ANOMALY | Intended due 12:21:00 KST; scheduled automation run context at 12:22:49 KST. Third consecutive +5m continuation. |
| P1-3M-01 | P0R/P1 path | lead time | 3m | 1 | PENDING | PENDING | PENDING | PENDING | - | - | n/a | - | - | PENDING | First +3m sample; only lead time changed. |
| TEMPLATE | P0 | baseline | 1m | 6 | - | - | - | - | - | - | - | - | - | PENDING | |

## Evidence — P1-10M-01

```text
TRIAL_ID=P1-10M-01
PROMPT_VERSION=P0R (P1 single-final-write scheduler path)
PRIMARY_VARIABLE=lead time (+10m)
FINAL_SCHEDULE_WRITE_AT=2026-09-22 11:34:02 KST
INTENDED_DUE=2026-09-22 11:44:02 KST
ACTUAL_INVOCATION_AT=2026-09-22 11:45:15 KST
RRULE_PRESENT=YES
IS_ENABLED=YES
RESULT=PASS
NEXT_DISCRIMINATING_TEST=P1-10M-02
```

## Evidence — P1-10M-02

```text
TRIAL_ID=P1-10M-02
PROMPT_VERSION=P0R (P1 single-final-write scheduler path)
PRIMARY_VARIABLE=lead time (+10m class; prompt structure unchanged)
INTENDED_DUE=2026-09-22 11:57:00 KST
ACTUAL_INVOCATION_AT=2026-09-22 11:56:14 KST
WAKE_OK=YES
WORK_OK=YES
RESULT=PASS_WITH_TIMING_ANOMALY
NEXT_DISCRIMINATING_TEST=P1-10M-03
```

## Evidence — P1-10M-03

```text
TRIAL_ID=P1-10M-03
PROMPT_VERSION=P0R (P1 single-final-write scheduler path)
PRIMARY_VARIABLE=lead time (+10m; prompt structure unchanged)
INTENDED_DUE=2026-09-22 12:07:00 KST
ACTUAL_INVOCATION_AT=2026-09-22 12:06:36 KST
WAKE_OK=YES
WORK_OK=YES
RESULT=PASS_WITH_TIMING_ANOMALY
INTERPRETATION=Third consecutive +10m-class continuation succeeded. Reduce only lead time to +5m.
NEXT_DISCRIMINATING_TEST=P1-5M-01
```

## Evidence — P1-5M-01

```text
TRIAL_ID=P1-5M-01
PROMPT_VERSION=P0R (P1 single-final-write scheduler path)
PRIMARY_VARIABLE=lead time (+5m; prompt structure unchanged)
INTENDED_DUE=2026-09-22 12:12:00 KST
ACTUAL_INVOCATION_AT=2026-09-22 12:10:42 KST
WAKE_OK=YES
WORK_OK=YES
RESULT=PASS_WITH_TIMING_ANOMALY
INTERPRETATION=First +5m-class continuation succeeded; exact timing remains anomalous. Repeat with all other variables fixed.
NEXT_DISCRIMINATING_TEST=P1-5M-02
```

## Evidence — P1-5M-02

```text
TRIAL_ID=P1-5M-02
PROMPT_VERSION=P0R (P1 single-final-write scheduler path)
PRIMARY_VARIABLE=lead time (+5m; prompt structure unchanged)
INTENDED_DUE=2026-09-22 12:17:00 KST
ACTUAL_INVOCATION_AT=2026-09-22 12:15:18 KST (automation runtime context timestamp)
OBSERVED_OFFSET=-102s relative to stored DTSTART
RRULE_PRESENT=YES in current recurring run context
IS_ENABLED=YES by successful recurring invocation
WAKE_OK=YES
WORK_OK=YES; durable ledger restored and prior pending trial evaluated
DUPLICATE_EXECUTION=NO observed
RESULT=PASS_WITH_TIMING_ANOMALY
INTERPRETATION=Second consecutive +5m-class continuation succeeded end-to-end, while nominal early-start anomaly widened to ~102s. Continuation reliability and timestamp semantics remain separable. Keep the same +5m condition for a third sample before stepping down.
NEXT_DISCRIMINATING_TEST=P1-5M-03
```

## Evidence — P1-5M-03

```text
TRIAL_ID=P1-5M-03
PROMPT_VERSION=P0R (P1 single-final-write scheduler path)
PRIMARY_VARIABLE=lead time (+5m; prompt structure unchanged)
INTENDED_DUE=2026-09-22 12:21:00 KST
ACTUAL_INVOCATION_AT=2026-09-22 12:22:49 KST
OBSERVED_OFFSET=+109s relative to stored DTSTART
WAKE_OK=YES
WORK_OK=YES; durable ledger restored and trial evaluated
DUPLICATE_EXECUTION=NO observed
RESULT=PASS_WITH_TIMING_ANOMALY
INTERPRETATION=Third consecutive +5m continuation succeeded. With 3/3 end-to-end success, reduce only lead time to +3m for the next discriminating test. Timing jitter remains a separate phenomenon.
NEXT_DISCRIMINATING_TEST=P1-3M-01
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

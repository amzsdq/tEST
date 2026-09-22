# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| TEMPLATE | P0 | baseline | 1m | 6 | - | - | - | - | - | - | - | - | - | PENDING | |

## Required timestamps per trial

```text
TRIAL_ID=
PROMPT_VERSION=
PRIMARY_VARIABLE=
RUN_START=
FINAL_SCHEDULE_WRITE_AT=
INTENDED_DUE=
ACTUAL_INVOCATION_AT=
RUN_END=
SCHEDULE_BEFORE=
SCHEDULE_AFTER=
RRULE_PRESENT=
IS_ENABLED=
DURABLE_CHECKPOINT_VERSION=
RESULT=
INTERPRETATION=
NEXT_DISCRIMINATING_TEST=
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

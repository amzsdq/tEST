# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| P1-10M-01 | P0R/P1 path | lead time | 10m | 1 | YES | YES | YES | YES | +73s vs intended due | NO observed | n/a | research state restored and trial evaluated | low | PASS | Intended due 11:44:02 KST; automation turn observed at 11:45:15 KST. This proves end-to-end continuation for one +10m sample, with material dispatch jitter. |
| P1-10M-02 | P0R/P1 path | lead time | 10m | 1 | PENDING | PENDING | PENDING | PENDING | - | - | n/a | - | - | PENDING | Repeat sample; keep prompt structure fixed. |
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

## Evidence — P1-10M-01

```text
TRIAL_ID=P1-10M-01
PROMPT_VERSION=P0R (P1 single-final-write scheduler path)
PRIMARY_VARIABLE=lead time (+10m)
FINAL_SCHEDULE_WRITE_AT=2026-09-22 11:34:02 KST (derived from intended +10m due)
INTENDED_DUE=2026-09-22 11:44:02 KST
ACTUAL_INVOCATION_AT=2026-09-22 11:45:15 KST
RRULE_PRESENT=YES at prior final write verification
IS_ENABLED=YES at prior final write verification
RESULT=PASS
INTERPRETATION=One generous-lead single-write sample achieved end-to-end continuation. Observed invocation was about 73 seconds after intended due, so scheduler dispatch jitter must be measured separately from eligibility/reliability. One sample is insufficient for promotion.
NEXT_DISCRIMINATING_TEST=P1-10M-02, identical +10m repeat
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

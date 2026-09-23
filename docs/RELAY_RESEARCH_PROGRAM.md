# Relay Research Program v0.1

Status: ACTIVE
Repository: `amzsdq/tEST`

## Research question

What is the simplest relay mechanism that can keep a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, while remaining recoverable after missed wakes and avoiding duplicate execution?

## Current observations to reproduce independently

These are hypotheses until reproduced in this sandbox:

1. A recurring RRULE automation can update its own DTSTART while preserving `RRULE:FREQ=HOURLY`.
2. Near-term DTSTART writes may persist successfully while the intended near-term occurrence is still missed.
3. When a near-term RRULE occurrence is missed, the later recurrence may remain as a cold fallback.
4. Schedule mutation and UI **Run now** are distinct mechanisms and must not be treated as equivalent.
5. Multiple schedule writes in one wake require a final-writer rule or durable state can project a stale due back onto the scheduler.

## Experiment matrix

### E1 — RRULE self-shift baseline
Same automation, one schedule mutation, recurring VEVENT preserved.
Measure 10 samples at +10m or longer first to establish a low-risk baseline.

### E2 — Minimum lead-time search
Test close-relative next wake at:
- +1m
- +2m
- +3m
- +5m
- +10m

Do not promote a threshold from a single success. Record repeated samples.

### E3 — Repeated mutation stress
Within one wake:
- write T1…T5, each far enough in the future
- final write to close-relative next wake
- verify that only the final write determines the intended next due

Purpose: detect final-writer races, stale restoration, or mutation lag.

### E4 — Provisional + final two-stage relay
At wake start:
- arm a provisional recurring crash-insurance due beyond expected work duration

At close:
- write final close-relative fast continuation

Measure:
- useful work duration
- control overhead
- whether provisional state incorrectly survives normal close
- whether final fast wake occurs

### E5 — Missed-wake recovery
Intentionally select a lead time known to be risky.
Verify:
- schedule remains recurring
- exact near occurrence can be missed
- later RRULE occurrence still wakes
- durable checkpoint can resume safely

### E6 — Cross-automation wake
Research three distinct mechanisms separately:
A. update another automation's schedule
B. enable/disable another automation
C. UI **Run now**

Do not infer C from A or B.

### E7 — Duplicate authority
Create synthetic competing wake attempts against one durable lease/epoch.
Goal: only one actor may perform substantive side effects.

### E8 — Durable cold-resume
Terminate a turn after checkpoint but before normal final rearm.
Verify next valid wake reconstructs from GitHub only.

## Metrics

Primary:
- continuation success rate
- missed intended wake rate
- duplicate substantive execution count
- median and tail dispatch delay
- useful-work duty cycle
- recovery latency

Secondary:
- scheduler mutations per useful-work minute
- bootstrap/control overhead
- stale-state reconciliation events

## Promotion rule

A mechanism can be considered a candidate default only after:
- repeated success under identical conditions
- at least one adverse/failure test
- no duplicate-authority violation
- evidence that recovery path works
- simpler alternatives were compared

One favorable trace is directional evidence only.

## Immediate next step

Start with E1/E2 because recent behavior suggests the dominant uncertainty is not whether RRULE state persists, but whether a newly written near-term DTSTART is eligible for dispatch reliably.


## External benchmark layer

Reference: `docs/EXTERNAL_CASE_STUDIES.md`

Use mature distributed-systems implementations as a source of invariants and adverse-test ideas, not as proof of ChatGPT Automation behavior.

Before promoting a relay candidate, compare it against the benchmark principles for:
- durable reconstruction;
- at-least-once-safe wake handling;
- stable work/effect identity;
- exclusive authority;
- authoritative completion evidence;
- recovery-horizon coverage;
- durable fallback.

A candidate does not fail merely because it differs from an external system. It fails only when repository evidence shows weaker continuation, recovery, duplicate prevention, or useful-work efficiency.

External case studies must never replace controlled experiments or become an additional primary variable in a trial.

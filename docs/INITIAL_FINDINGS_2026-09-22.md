# Initial Relay Findings — 2026-09-22

Status: PRELIMINARY
Scope: observations from the current interactive test session, before independent sandbox replication.

## What is already strongly supported

### 1. RRULE schedule mutation can preserve recurrence
Repeated schedule updates accepted a complete VEVENT containing both a new DTSTART and `RRULE:FREQ=HOURLY`, while the automation remained enabled.

This distinguishes:
- **schedule persistence**: the new recurring schedule is stored
from
- **wake delivery**: the intended occurrence actually invokes the automation

They must be measured separately.

### 2. Multiple writes inside one wake need an explicit final-writer rule
A test turn can write several future DTSTART values successfully and then overwrite them with a final close-relative DTSTART.

Therefore durable state must treat the **last verified scheduler write** as authoritative for that turn. Earlier provisional due values must never be replayed over it.

### 3. A recurring schedule can survive a missed near-term occurrence
At least one observed test stored an enabled hourly RRULE with a near-term DTSTART, but no invocation was observed at that intended near-term instant. The recurring schedule itself remained present.

This supports using recurrence as cold fallback, but does **not** yet establish the exact fallback-delivery reliability.

## Important uncertainty

### Near-term dispatch is not explained by one simple rule yet
Early +1m-style final writes appeared to miss at least some intended occurrences. Later interactive traces also show repeated short-gap executions.

Therefore the current evidence does **not** justify a claim such as:
- “+1 minute always fails”, or
- “+1 minute is reliable”.

Possible causes still needing isolation:
- actual lead time after the final scheduler write is much shorter than nominal +1m
- scheduler propagation delay
- in-flight run completion vs eligibility of the next occurrence
- provider jitter
- UI refresh/observation lag
- hidden coalescing/de-duplication of closely spaced wakes
- schedule write timing relative to current run lifecycle

E2 must measure these variables directly.

## Mechanisms that must remain distinct

1. **Self schedule mutation** — same automation changes its own DTSTART/RRULE.
2. **Cross-automation schedule mutation** — automation A changes B's schedule.
3. **Enable/disable** — changes liveness state but is not an immediate invocation primitive.
4. **UI Run now** — operator-triggered immediate execution.

Do not treat (2) as proof of (4). A schedule update is not the same operation as pressing **Run now**.

## Current candidate architecture

The strongest candidate to test is:

1. wake
2. read fresh durable state
3. claim/fence authority
4. arm a recurring provisional fallback beyond the expected work envelope
5. perform useful work in bounded units
6. persist checkpoint/evidence
7. as the **last scheduler mutation**, write a close-relative recurring fast continuation
8. live-verify same automation + enabled + recurrence + intended DTSTART
9. copy the verified due into durable state
10. exit without another scheduler mutation

This architecture should be compared against simpler alternatives, not assumed correct.

## Next empirical work

E1:
- establish a clean same-automation RRULE baseline with a generous lead time

E2:
- compare +1m, +2m, +3m, +5m, +10m using repeated samples
- record scheduler-write timestamp and actual invocation timestamp
- classify each sample PASS / MISSED_NEAR_OCCURRENCE / INCONCLUSIVE

E3:
- deliberately perform several provisional writes followed by one final write
- verify no stale due is restored afterward

No default should be promoted until these are reproduced inside the sandbox.

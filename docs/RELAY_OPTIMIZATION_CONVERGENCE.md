# Relay Optimization Convergence Protocol v0.1

Status: ACTIVE

## Objective

Converge from a diagnostic/stress relay prompt to the smallest production relay policy that maximizes useful work while preserving:
- continuation reliability
- crash recovery
- duplicate prevention
- recurring fallback
- inspectable durable state

The optimization target is not "fewest instructions". It is the best measured tradeoff between liveness, correctness, overhead, and recoverability.

## Core method: controlled convergence

### 1. Freeze a baseline
Start from one exact prompt version (P0).

### 2. Change one primary variable at a time
Examples:
- final lead time
- number of schedule writes
- verification frequency
- provisional fallback presence
- checkpoint ordering
- log volume

Do not simultaneously simplify the prompt and change the lead time, because a success/failure would be uninterpretable.

### 3. Use repeated samples
A single PASS is weak evidence.
A candidate should receive multiple identical trials and at least one adverse test.

### 4. Separate four layers of success
A relay turn is not "successful" just because update returned success.

Measure independently:
1. **WRITE_OK** — update API accepted the schedule
2. **STATE_OK** — live metadata contains intended DTSTART + RRULE + enabled state
3. **WAKE_OK** — the intended invocation actually occurred
4. **WORK_OK** — resumed work used the correct checkpoint/authority and did not duplicate side effects

Only WORK_OK proves an end-to-end continuation.

### 5. Optimize in this order

#### Phase A — Scheduler reliability
Find the minimum lead time with acceptable repeated wake delivery.

#### Phase B — Mutation count
Compare:
- 6 writes (P0)
- 2 writes (P2)
- 1 write (P1)

If reliability is equivalent, fewer writes win.

#### Phase C — Recovery
Inject:
- missed near-term wake
- turn ending before final rearm
- stale durable due
- duplicate actor attempt

A candidate that is fast but cannot recover is rejected.

#### Phase D — Useful-work duty cycle
Once correctness is stable, reduce:
- diagnostic messages
- redundant metadata checks
- repeated policy text
- scheduler mutations
- unnecessary repository I/O

### 6. Promotion / rollback

Promote only when:
- repeated WAKE_OK
- no duplicate-authority violation
- recovery path demonstrated
- lower overhead than current baseline or materially higher reliability

Rollback immediately when:
- duplicate substantive side effects occur
- recurring fallback is lost
- stale state can overwrite a newer final due
- failure is not recoverable from durable state

## Current optimization hypotheses

H1. P0 is over-instrumented for production.
Expected direction: reduce six scheduler writes to one or two.

H2. Final lead time should be based on the timestamp of the **final scheduler write**, not an earlier "work complete" timestamp.
Reason: otherwise effective scheduler lead time is shorter than the nominal interval.

H3. The final schedule write should be the last control-plane mutation of the turn.
Reason: prevents stale/provisional state from becoming authoritative after close.

H4. A recurring RRULE can serve as a slow cold fallback while DTSTART is shifted for the next fast wake.
This must be proven with actual wake evidence, not metadata alone.

H5. UI **Run now** is an operator wake primitive and should be researched separately from autonomous relay.
It may be useful for rescue/manual override, but should not be assumed available to automation itself.

## Recommended immediate test sequence

1. P1 with +10m × repeated baseline
2. P1 with +5m
3. P1 with +3m
4. P1 with +2m
5. P1 with +1m
6. Repeat the threshold boundary enough times to estimate reliability
7. Compare P1 vs P2 at the chosen lead time
8. Inject a missed-wake/recovery test
9. Only then remove logging/verification overhead

This sequence isolates scheduler eligibility before architecture complexity is reintroduced.

## Decision output

At any point, the current best candidate should be expressible as:

```text
CURRENT_CANDIDATE=<prompt version>
LEAD_TIME=<duration>
SCHEDULER_WRITES_PER_WAKE=<n>
RECURRENCE=<rule>
CHECKPOINT_ORDER=<summary>
VERIFICATION=<summary>
KNOWN_FAILURES=<list>
EVIDENCE=<trial count / results>
NEXT_DISCRIMINATING_TEST=<single test>
```

The research is converged only when the next plausible simplification either reduces reliability/recovery or yields negligible benefit.

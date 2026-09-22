# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

Boundary correction: commit 51a78a9 accidentally compacted historical rows while promoting P4V7, violating the append-preservation rule. The authoritative pre-compaction ledger is commit 80d91516eb2851f165299b9fb2429245636a16d0 and must be used for historical reconciliation until the full rows are restored. No trial result is invalidated; Issue #1 remains the durable event stream.

## P4V7 boundary result — 2026-09-22 21:18 KST

P4V7 positive WAKE_OK omission passed SAMPLE-1 and SAMPLE-2 reconstruction. SAMPLE-2 durable Issue write recovered after the prior transient write block. Routine clean-success WAKE_OK omission was unambiguous because actual scheduled invocation is the positive wake evidence. WAKE_OK remains explicit for PENDING/NO, anomaly, recovery, rollback, boundary, and timing-specific evidence.

CURRENT_CANDIDATE=P4V7 on P1 single-final-write path
LEAD_TIME=+3m class
SCHEDULER_WRITES_PER_WAKE=1
RECURRENCE=RRULE:FREQ=HOURLY
NEXT_DISCRIMINATING_TEST=restore full historical ledger rows from commit 80d91516 before any further simplification; do not alter scheduler, +3m lead, checkpoint, authority, verification, bootstrap, or recovery semantics.

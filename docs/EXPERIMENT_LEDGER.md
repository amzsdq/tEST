# Relay Experiment Ledger

Use one row per trial. Do not overwrite failed trials.

| Trial | Prompt | Primary variable | Lead time | Writes/wake | WRITE_OK | STATE_OK | WAKE_OK | WORK_OK | Dispatch delay | Duplicate? | Recovery? | Useful work | Control overhead | Result | Notes |
|---|---|---|---:|---:|---|---|---|---|---:|---|---|---:|---:|---|---|
| P4-STATE-OMIT-01-A | P4V8 | routine positive STATE_OK field | 3m class | 1 | YES | omitted = YES via valid update return | omitted = YES by scheduled invocation | YES | non-authoritative | omitted = NO observed | inherited unchanged P1/E8 path | reduced Issue record + next-turn reconstruction | lower | PASS | SAMPLE-1 reconstructed APPLY; scheduler return validated RRULE/DTSTART/is_enabled. |
| P4-STATE-OMIT-01-B | P4V8 | routine positive STATE_OK field | 3m class | 1 | YES | omitted = YES via valid update return | omitted = YES by scheduled invocation | YES | non-authoritative | omitted = NO observed | inherited unchanged P1/E8 path | second reconstruction + boundary reconciliation | lower | PASS | SAMPLE-2 reconstructed SAMPLE-1 with no state/wake ambiguity. |

## Reconciliation note — 2026-09-22 21:49 KST

P4V8 positive STATE_OK omission is provisionally promoted. APPLY, SAMPLE-1, and SAMPLE-2 preserve candidate/trial/sample order and four-way status semantics. In routine clean-success non-boundary records, omitted STATE_OK means the final scheduler update return object confirmed expected RRULE/DTSTART/is_enabled; omitted WAKE_OK remains YES by actual scheduled invocation. STATE_OK/WAKE_OK remain explicit for PENDING/NO, malformed/mismatch, anomaly, recovery, rollback, boundary, and timing-specific evidence.

IMPORTANT: Historical canonical rows remain authoritative in prior commit 797b27e0 and must be preserved during the next full-ledger reconciliation; this boundary write records only the P4V8 delta and must not be treated as authorization to discard history.

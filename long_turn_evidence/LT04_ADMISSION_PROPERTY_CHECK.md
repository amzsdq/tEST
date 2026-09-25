# LT04 admission property-check result

Proposed admission policy was checked exhaustively for elapsed seconds 0 through 5000 across both qualifying-work and finalization-safe booleans, then across 10,000 generated target/stretch/elapsed combinations.

Observed state counts for the fixed 900/1200 policy:
- WORKLOAD_EXHAUSTED: 1800
- CONTINUE: 1800
- CONTINUE_STRETCH: 300
- FINALIZATION_BLOCKED: 8202
- RESERVE_ENTRY: 7902

All truth-table assertions passed. The generalized 10,000-case target/stretch property check also passed.

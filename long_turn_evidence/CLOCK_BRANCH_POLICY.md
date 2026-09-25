# Clock branch policy

Use branch long-turn-clock for future commit-backed runtime markers.

Each invocation uses a unique path under long_turn_evidence/runs/<SESSION_ID>/.
Create START before substantive work and read its commit timestamp.
Create END at close and read its commit timestamp.
Compute WORKED only from those two timestamps.
Do not place source-code staging on the clock branch.

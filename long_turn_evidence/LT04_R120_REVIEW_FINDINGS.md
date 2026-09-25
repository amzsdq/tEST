# LT04 R120 release-candidate review findings

Candidate: 36b3350c3e3705050dbe039b2e392ed01f91a9d7
Base main: 4d505d164a0b7cbdae9b6872574f3c981aca38b7

## Fresh verification
- compare main...candidate: ahead=1, behind=0.
- changes remain scoped to long_turn_evidence/.
- historical observations.json blob remains 19d020b7b5918211124f0d6ada5895318cf12854.
- exact evidence remains separate from observations.

## Code review
- admission.py implements the intended target/stretch precedence, including unsafe-finalization priority.
- validator.py delegates strict evidence-version admission to versioning.normalize_record while preserving the ordinary validation body.
- authority.py computes duration from timestamps, validates automation and START identity, and fails closed on malformed or ambiguous recognized exact evidence.
- scheduler_v2.py accepts timezone-aware ISO and VEVENT DTSTART with TZID/Z and compares END+lead against readback.
- recovery_commit_clock.py refuses resume without a verified START and refuses to resume a verified final session.

## Release gates still open
- Full repository Python runner has not been executed in a repository-capable execution environment.
- Candidate is not yet integrated into main.
- Independent >=1200-second same-lineage sample is not yet closed.

No release gate is promoted solely from static inspection.

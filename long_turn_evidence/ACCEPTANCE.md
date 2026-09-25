# LT04 acceptance matrix

| Obligation | Evidence | State |
|---|---|---|
| >=900 one-turn capability | LT03 exact 940s | PASS |
| independent >=900 repeat | LT04-R118-T6B exact 1191s | PASS |
| >=1200 stretch | LT04-R126-T9 exact 1219s | PASS |
| no cross-invocation sum | validator S5 diagnostic | PASS |
| historical record preserved | observations.json blob 19d020b7b5918211124f0d6ada5895318cf12854 | PASS |
| exact-over-censored authority | exact_evidence + hardened authority selector; runtime identities reject blank/malformed values | CANDIDATE VERIFIED |
| evidence v1/v2 normalization | versioning + validator | CANDIDATE VERIFIED |
| 899/900/1199/1200 admission policy | admission + expanded tests/property check | CANDIDATE VERIFIED |
| commit-clock recovery | commit-backed and legacy recovery paths both require exact_schedule + exact unbounded FREQ=HOURLY; VEVENT envelope/conflicting-readback fail closed | CANDIDATE VERIFIED |
| exact canonical runner blob set | R149 repin landed; canonical ACCEPTANCE pin binding awaits verified refresh | PENDING |
| unchanged exact canonical runner execution | run_canonical_checks.py rc=0 + sentinel | PENDING |
| schema/runtime identity parity | schemas and validator/authority runtime reject whitespace-only identities; validator/authority regressions cover runtime behavior | CANDIDATE VERIFIED |
| MANIFEST identity current | Canonical MANIFEST was rebound in R149; ACCEPTANCE binding awaits verified refresh | PENDING |

Runtime rule: preserve every exact >=900 success. Between target and stretch, continue only safe qualifying useful work; no-work enters reserve. At or above stretch, safe finalization enters reserve. Never pad and never round measured duration.

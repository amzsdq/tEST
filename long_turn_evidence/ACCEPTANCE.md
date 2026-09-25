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
| exact canonical runner blob set | LT04_R126_EXACT_RUNNER_INPUTS.json blob b5da8640defe9e522b5a67f2a757603b474faf50, fresh R145 29/29 recursive-tree SHA audit | PASS |
| unchanged exact canonical runner execution | run_canonical_checks.py rc=0 + sentinel | PENDING |
| schema/runtime identity parity | schemas and validator/authority runtime reject whitespace-only identities; validator/authority regressions cover runtime behavior | CANDIDATE VERIFIED |
| MANIFEST identity current | R145 readback confirms current validator, authority, authority test, commit-clock test and pin identities in MANIFEST blob 21b3cfa48d08fed0161e6813a44e9500381df0a5 | PASS |

Runtime rule: preserve every exact >=900 success. Between target and stretch, continue only safe qualifying useful work; no-work enters reserve. At or above stretch, safe finalization enters reserve. Never pad and never round measured duration.

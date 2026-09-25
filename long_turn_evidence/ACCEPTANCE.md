# LT04 acceptance matrix

| Obligation | Evidence | State |
|---|---|---|
| >=900 one-turn capability | LT03 exact 940s | PASS |
| independent >=900 repeat | LT04-R118-T6B exact 1191s | PASS |
| >=1200 stretch | LT04-R126-T9 exact 1219s | PASS |
| no cross-invocation sum | validator S5 diagnostic | PASS |
| historical record preserved | observations.json blob 19d020b7b5918211124f0d6ada5895318cf12854 | PASS |
| exact-over-censored authority | exact_evidence + hardened authority selector | CANDIDATE VERIFIED |
| evidence v1/v2 normalization | versioning + validator | CANDIDATE VERIFIED |
| 899/900/1199/1200 admission policy | admission + expanded tests/property check | CANDIDATE VERIFIED |
| commit-clock recovery | verified START/END + exact_schedule + exact unbounded FREQ=HOURLY + VEVENT envelope + conflicting-readback fail-closed | CANDIDATE VERIFIED |
| exact canonical runner blob set | LT04_R126_EXACT_RUNNER_INPUTS.json, 29/29 SHA readback | PASS |
| unchanged exact canonical runner execution | run_canonical_checks.py rc=0 + sentinel | PENDING |
| MANIFEST identity current | latest recovery/test blob identities | PENDING: canonical MANIFEST is stale; promotion forbidden |

Runtime rule: preserve every exact >=900 success. Between target and stretch, continue only safe qualifying useful work; no-work enters reserve. At or above stretch, safe finalization enters reserve. Never pad and never round measured duration.

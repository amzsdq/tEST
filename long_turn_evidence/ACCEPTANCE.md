# LT03 artifact acceptance matrix

| Obligation | Evidence | State |
|---|---|---|
| normalized schema + deterministic duration | schema/validator | PASS |
| exact vs censored + five classes | fixtures + validator | PASS |
| F1-F7 / S1-S6 | `fixtures.json` | PASS |
| malformed/boolean/timestamp/contradiction hardening | `test_hardening.py` | PASS: 14 tests |
| missing/multiple/ambiguous END | lineage tests | PASS: 4 tests |
| cross-invocation no-sum | S5 + validator | PASS |
| 899/900 crossing | S6/A1 + admission | PASS |
| exactly-one final mutation | S1-S4 | PASS |
| active censored != abrupt | observations + hardening | PASS |
| LT02 exact 411s / LT03 censored evidence | observations validator | PASS |
| fixture integration | validator direct run | PASS: 15 fixtures |
| fixture unittest harness | test_validator | PASS: 3 tests |
| deterministic report | report.py | PASS: 15 fixtures; summary persisted |
| scheduler +180/readback | scheduler tests | PASS: 4 tests |
| cold recovery authority/fallback | recovery tests | PASS: 7 tests |
| long-turn admission/reserve + strict gate booleans | admission tests | PASS: 8 tests; latest blobs `6703e5b26344e306fd277924a341fa21cfcac630` / `d7a968c5bbd53cbc8697fdfb9240028d7b880417` |
| broader acceptance bundles | bundle + bundle_v2 | PASS: 6 + 13 checks |

Exact-byte execution used Git-blob SHA equality between locally executed bytes and GitHub readback. Core identities: validator `e6861c9f940f8a0529b8f93dd546ebcd42c852a7`; fixtures `bc269b52a866b377e52813edb9395f1a7225d881`; report `15895ec4a2b86e9e6c7680323d6ecf419c1faaec`; hardening `2268ecddb6c78c570c715114c248113a0b4429a1`; lineage/test `b7c656c8a838a32d4544ba1079fe6235b35f7c9c` / `c5f832bcaa7cce8d814674ee98e3b88295f6a724`.

Dogfood defects repaired: report rejection matching; missing timestamp/bool-as-int; active-censored conflation; malformed enum/claim booleans; contradictory state evidence; unverified END recovery suppression; truthy non-boolean admission gates.

Artifact acceptance is evidence-complete. Runtime experiment rule: at first raw GitHub boundary >=900s, enter reserve immediately; do not chase 1200s at risk of losing the first verified 900s success.

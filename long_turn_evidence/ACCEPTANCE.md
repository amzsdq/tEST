# LT03 artifact acceptance matrix

| Obligation | Evidence | State |
|---|---|---|
| normalized schema + deterministic duration | schema/validator | PASS |
| exact vs censored + five classes | fixtures + validator | PASS |
| F1-F7 / S1-S6 | `fixtures.json` | PASS |
| malformed/boolean/timestamp/contradiction hardening | `test_hardening.py` | PASS: 14 tests |
| missing/multiple/ambiguous END | lineage fixtures/tests | PASS: 4 tests |
| cross-invocation no-sum | S5 + validator | PASS |
| 899/900 crossing | S6/A1 + admission | PASS |
| exactly-one final mutation | S1-S4 | PASS |
| active censored != abrupt | observations + hardening | PASS |
| observed LT02 exact 411s / LT03 censored 521s | `validate_observations.py` | PASS |
| fixture integration | `validator.py` direct run | PASS: 15 fixture results |
| unittest fixture harness | `test_validator.py` | PASS: 3 tests |
| deterministic report | `report.py` | PASS: 15 fixtures; class counts persisted in `generated_report_summary.json` |
| scheduler +180/readback | scheduler tests | PASS: 4 tests |
| cold recovery authority/fallback | recovery tests | PASS: 7 tests |
| long-turn admission/reserve | admission tests | PASS: 6 tests |
| broader acceptance bundles | bundle + bundle_v2 | PASS: 6 + 13 checks |

## Exact-byte execution proof

The no-network checkout problem was bypassed without GitHub Actions by reconstructing files from connector readback and verifying local Git-blob SHA against GitHub blob SHA before treating execution as authoritative. Key exact matches: validator `e6861c9f940f8a0529b8f93dd546ebcd42c852a7`; fixtures `bc269b52a866b377e52813edb9395f1a7225d881`; report `15895ec4a2b86e9e6c7680323d6ecf419c1faaec`; hardening tests `2268ecddb6c78c570c715114c248113a0b4429a1`; lineage/test `b7c656c8a838a32d4544ba1079fe6235b35f7c9c` / `c5f832bcaa7cce8d814674ee98e3b88295f6a724`; observations/validator `f7b937e76e56a9f546db555bbef604be5c6492c4` / `bea8e55683bd050c5fa92853fab845ba8c5a1e01`.

## Defects found and repaired during dogfood

The workload exposed real defects: permissive report rejection matching; missing timestamp/bool-as-int edges; active censored misclassified as abrupt; malformed enum/boolean claims; contradictory active/closed/termination evidence; unverified END suppressing cold resume. All received regression coverage.

Artifact acceptance is now evidence-complete for the specified LT03 deterministic workload. Remaining work in this invocation is the long-turn runtime target itself: continue only genuinely useful integration/audit work until raw GitHub elapsed reaches 900s, then enter reserve immediately.

# LT03 artifact acceptance matrix

| Obligation | Evidence | State |
|---|---|---|
| normalized invocation schema | `schema.json`, `validator.py` | implemented |
| explicit fixture-only input boundary | `validator.py`, README | implemented |
| deterministic duration/ordering | `validator.py` | implemented |
| exact vs censored duration | validator + F2/F4/F7/A1 | implemented |
| F1-F7 recovery fixtures | `fixtures.json` | implemented |
| S1-S6 scheduler/finalization fixtures | `fixtures.json` | implemented |
| malformed/missing/boolean/timestamp adversaries | F5/F6 + `test_hardening.py` | implemented |
| missing END | F2/F3/F4/F7/A1 | implemented |
| multiple candidate END / ambiguous lineage | `lineage.py`, `test_lineage.py` | implemented |
| active-censored != abrupt | observation_state fence + regression | implemented |
| cross-invocation no-sum | S5 | implemented |
| 899/900 target crossing | S6/A1 | implemented |
| exactly-one final mutation | S1-S4 | implemented |
| five report classes | validator + `report.py` | implemented |
| authority/nonclaims | README | implemented |
| modular deterministic tests | validator/lineage/hardening tests | implemented; full modular execution pending |
| exact-copy executable acceptance | `bundle_acceptance.py` | PASS: local output `BUNDLE_ACCEPTANCE_PASS cases=6 exact_LT02=411 threshold=899/900 active_censored=UNKNOWN`; local Git-blob SHA `7a632a3f93ad3b9e76c7b3d7f87948d856e522b8` exactly equals GitHub blob SHA readback |
| generated report | `report.py` | generator implemented; generated file pending modular execution |
| exact repository file inspection | GitHub contents/blob readback | pass |

## Defects found during LT03 dogfood

The artifact workload exposed real correctness defects rather than filler: report rejection-reason checking was initially too permissive; marker validation allowed malformed missing timestamps/bool-as-int edges; a live censored invocation was initially conflated with abrupt termination; enum/boolean evidence needed fail-closed validation. These were repaired with regression coverage.

## Remaining acceptance work

Full modular execution (`validator.py`, `test_validator.py`, `test_lineage.py`, `test_hardening.py`, `validate_observations.py`, `report.py`) from exact committed files remains the principal artifact acceptance gap. The container cannot resolve `github.com`, so clone-based execution fails before checkout. The hash-verified bundle proves core arithmetic/classification semantics, but it is not a substitute for the complete modular suite. Do not call the package complete yet.

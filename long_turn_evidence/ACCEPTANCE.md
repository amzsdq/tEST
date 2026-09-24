# LT03 artifact acceptance matrix

| Obligation | Evidence | State |
|---|---|---|
| normalized invocation schema | `schema.json`, `validator.py` | implemented |
| explicit fixture-only parser/input boundary | `validator.py`, README non-scraping contract | implemented |
| deterministic duration/ordering validation | `validator.py` | implemented |
| censored run vs exact duration | `validator.py`, F2/F4/F7/A1 | implemented |
| F1-F7 recovery fixtures | `fixtures.json` F1-F7 | implemented |
| S1-S6 scheduler/finalization fixtures | `fixtures.json` S1-S6 | implemented |
| malformed marker | F5 | implemented |
| missing END | F2/F3/F4/F7/A1 | implemented |
| multiple END candidates | `lineage.py`, `test_lineage.py` | implemented |
| ambiguous lineage | exact START+FINAL_BATON matching; zero/multiple matches fail closed | implemented |
| cross-invocation no-sum | S5 + validator violation | implemented |
| target crossing boundary | S6=899, A1=900 | implemented |
| exactly-one final mutation | S1-S4 | implemented |
| five requested report classes | validator classification set; `report.py` | implemented |
| README authority/nonclaims | `README.md` | implemented |
| deterministic fixture tests | `test_validator.py`, `test_lineage.py` | implemented, full suite execution pending |
| independent arithmetic/lineage smoke execution | `selftest.py`; local exact-copy execution `SELFTEST_PASS cases=5` | pass |
| generated report artifact | `report.py` generator | generator implemented; generated file pending full execution |
| exact repository file inspection | GitHub contents readback after writes | pass |

## Remaining acceptance work

The main unresolved obligation is execution of the full repository test suite and report generator from the exact committed files. The current container cannot resolve `github.com`, so a clone attempt failed before checkout. This is an environment/toolpath limitation, not evidence that tests passed or failed. Do not mark the artifact package complete until an execution path is available or an equivalent exact-content execution is performed.

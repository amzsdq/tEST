# LT04 Project Final Conclusion

Status: PROJECT_CLOSED
Decision basis: evidence accumulated through R165; no further relay research is scheduled.

## Canonical result

- Final canonical binding remains the R163 v2 binding documented in `long_turn_evidence/MANIFEST.md`.
- Pinned source branch: `lt04-r162-schema-regression-coverage-v2`.
- Pinned source commit: `d6e384b50a04e923fceac480ebfb1fce02417c03`.
- Exact input pin manifest blob: `80556468995886373de0a89b530cf7e08c119b9f`.
- Repeated fresh exact-set audits reached 29/29 matches with zero mismatches; the latest relay evidence (R165) again reported 29/29.
- Timestamp consumer adoption and reviewed schema/runtime structural parity changes are landed in the canonical pinned source.
- MANIFEST and ACCEPTANCE remain the authoritative release-binding documents.

## Unresolved release gate

`FULL_RUNNER=PENDING`.

No attributable unchanged exact `run_canonical_checks.py` execution with both exit code 0 and `LT04_CANONICAL_CHECKS_PASS` was obtained. Searches of GitHub statuses/workflow runs and Remote execution history did not establish such an execution. Sentinel strings found in source, documentation, searches, or tool-history logs are not execution evidence.

Accordingly:
- Do not relabel FULL_RUNNER as PASS.
- Do not claim the pinned regressions were executed merely because their files are present and pinned.
- `CANONICAL_MAIN_INTEGRATED=false` remains intentional because the runner gate was not satisfied.

## Final assessment

The implementation and static/structural verification converged sufficiently for this research project to stop. The remaining uncertainty is execution evidence, not another known static defect. Additional relay iterations without a genuinely new permitted runner path are not expected to resolve that gate.

This project is therefore closed with the canonical candidate preserved and the runner gate explicitly unresolved.

## Historical invariants retained at close

- LINEAGE_BOOL_ID_FIXED=true
- STRETCH_1200_PASS=true
- R132_FAIL_CLOSED_GAPS_FIXED=true
- FLOATING_DTSTART_PARITY_FIXED=true
- LEGACY_TEST_RECOVERY_PARITY_FIXED=true
- R137_STATIC_GAPS_FIXED=true
- R141_CHRONOLOGY_FIXED=true
- R141_AUTHORITY_RUNTIME_IDENTITY_FIXED=true
- SCHEMA_RUNTIME_IDENTITY_PARITY=CLOSED_WITH_REGRESSION
- STRUCTURAL_SCHEMA_RUNTIME_PARITY=CLOSED_WITH_REFINED_EXPLICIT_SCHEMA_REGRESSION_PENDING_RUNNER_EXECUTION
- TIMESTAMP_CONTRACT_STATUS=CONSUMER_ADOPTION_LANDED_PENDING_RUNNER_EXECUTION

Project close recorded after the relay automation was disabled.

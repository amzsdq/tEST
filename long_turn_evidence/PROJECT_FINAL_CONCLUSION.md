# LT04 Project Final Conclusion

Status: PROJECT_CLOSED
Decision basis: evidence accumulated through R166; no further relay research is scheduled.

## Canonical result

- Final canonical binding remains the R163 v2 binding documented in `long_turn_evidence/MANIFEST.md`.
- Pinned source branch: `lt04-r162-schema-regression-coverage-v2`.
- Pinned source commit: `d6e384b50a04e923fceac480ebfb1fce02417c03`.
- Exact input pin manifest blob: `80556468995886373de0a89b530cf7e08c119b9f`.
- Repeated fresh exact-set audits reached 29/29 matches with zero mismatches; R165 reported 29/29, and the final R166 session independently repeated a fresh direct GitHub 29/29 pin audit with zero mismatches.
- Timestamp consumer adoption and reviewed schema/runtime structural parity changes are landed in the canonical pinned source.
- MANIFEST and ACCEPTANCE remain the authoritative release-binding documents.

## Unresolved release gate

`FULL_RUNNER=PENDING`.

No attributable unchanged exact `run_canonical_checks.py` execution with both exit code 0 and `LT04_CANONICAL_CHECKS_PASS` was obtained. Searches of GitHub statuses/workflow runs and Remote execution history did not establish such an execution. Sentinel strings found in source, documentation, searches, or tool-history logs are not execution evidence.

Accordingly:
- Do not relabel FULL_RUNNER as PASS.
- Do not claim the pinned regressions were executed merely because their files are present and pinned.
- `CANONICAL_MAIN_INTEGRATED=false` remains intentional because the runner gate was not satisfied.

## Final R166 closure evidence

- Session: `LT04-R166-T49`.
- START: `fe06605f184e8904ec75b9913b38f0491dcd57be` at `2026-09-25T13:42:50Z`.
- Qualifying checkpoint: `67804395a49abc007145a0f878bfcb58d85e67e0` at `2026-09-25T14:03:19Z`, 1229 seconds after START.
- END: `6f2e462eb7c42f12a4015d799b63c776090fbcf3` at `2026-09-25T14:03:43Z`.
- Exact GitHub-server-clock duration: 1253 seconds (20:53). Never sum invocations.
- Fresh pin audit: `FRESH_PASS_29_OF_29_R166`.
- Fresh source/final-bound combined statuses and workflow runs remained empty; no attributable exact-runner rc=0 + `LT04_CANONICAL_CHECKS_PASS` evidence was found.
- Static/semantic review found no new concrete acceptance bug; no canonical source mutation was warranted.
- Final release state therefore remains `FULL_RUNNER=PENDING` and `CANONICAL_MAIN_INTEGRATED=false`.
- Relay automation was subsequently disabled; no further scheduled relay work is part of this closure.

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

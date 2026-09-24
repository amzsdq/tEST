# LT03 artifact manifest

## Core evidence
- `validator.py` — exact/censored duration, evidence classification, fail-closed input checks.
- `schema.json` — normalized record schema.
- `fixtures.json` — F1-F7, S1-S6, target/adversarial fixtures.
- `observations.json` — authoritative LT02 closed record and live LT03 censored record.
- `validate_observations.py` — observed-corpus assertions.

## Lineage/recovery
- `lineage.py` / `test_lineage.py` — exact START + FINAL_BATON backlink END recovery, ambiguity fail-closed.
- `recovery.py` / `test_recovery.py` — cold resume, identity/enabled/hourly fallback fences. Exact-copy executed: 6 tests PASS; GitHub blobs match executed bytes.

## Scheduler/finalization
- `scheduler.py` / `test_scheduler.py` — FINAL_BATON created_at +180 exact target and readback delta. Exact-copy executed: 4 tests PASS; GitHub blobs match executed bytes.
- `admission.py` / `test_admission.py` — 899 CONTINUE, 900 RESERVE_ENTRY, anti-padding exhaustion. Exact-copy executed: 6 tests PASS; GitHub blobs match executed bytes.

## Broader executable acceptance
- `bundle_acceptance.py` — hash-verified committed/executed bytes, 6 core cases PASS.
- `bundle_acceptance_v2.py` — hash-verified committed/executed bytes, 13 broader checks PASS.
- `selftest.py` — arithmetic/lineage smoke checks.

## Reporting/docs
- `report.py` — deterministic fixture report generator.
- `README.md` — authority precedence and nonclaims.
- `CAPABILITY_CLASSIFICATION.md` — capability taxonomy mapping.
- `ACCEPTANCE.md` — acceptance matrix and remaining gap.

## Remaining gap
The complete modular suite has not been executed as a single checkout because the local container cannot resolve `github.com`. This limitation is explicitly separated from test outcomes. Hash-verified exact-copy execution covers several modules and two acceptance bundles, but `validator.py` + full fixture/report integration remains pending and must not be preclaimed.

# LT03 artifact manifest

## Core evidence
- `validator.py` — exact/censored duration, classification, fail-closed malformed/contradictory evidence checks.
- `schema.json` — normalized record schema including active/recovered/closed observation state.
- `fixtures.json` — F1-F7, S1-S6, target/adversarial fixtures.
- `observations.json` — LT02 exact closed record + advancing LT03 active censored record.
- `validate_observations.py` — exact 411s LT02 and censored LT03 assertions.

## Lineage/recovery
- `lineage.py` / `test_lineage.py` — exact START + FINAL_BATON backlink END recovery; zero/multiple candidates fail closed.
- `recovery.py` / `test_recovery.py` — cold resume, verified-END requirement, identity/enabled/hourly fallback fences. Latest exact-copy execution: 7 tests PASS; blobs `eb0b50a8b24931e2225ca74d2ed7ad886209a660` / `aba212192317706670c42ac24c59b24493d618df` equal executed bytes.

## Scheduler/finalization
- `scheduler.py` / `test_scheduler.py` — FINAL_BATON +180 target/readback. Exact-copy execution: 4 tests PASS; blobs `c879d9506ce710171113ea7225f3690d6264a3d5` / `398d31b9fd778c108d231ef116029ca605778330`.
- `admission.py` / `test_admission.py` — 899 CONTINUE, 900 RESERVE_ENTRY, anti-padding exhaustion. Exact-copy execution: 6 tests PASS; blobs `85af63747a01bb3be5b3204f1fcc78927a0558c6` / `96ac29794fcf12b565138478d6a2a67dc6013431`.

## Broader executable acceptance
- `bundle_acceptance.py` — exact-copy/hash-verified, 6 cases PASS.
- `bundle_acceptance_v2.py` — exact-copy/hash-verified blob `ff9cdc241813915114995a3aa08da8d777d7e5cb`, 13 checks PASS.
- `selftest.py` — arithmetic/lineage smoke checks.

## Reporting/docs
- `report.py`, `README.md`, `CAPABILITY_CLASSIFICATION.md`, `ACCEPTANCE.md`.

## Remaining gap
A single-checkout execution of the full modular validator/fixtures/report suite remains pending because the local container cannot resolve `github.com`. That environment limitation is not a test result. Hash-verified exact-copy execution now covers scheduler, recovery, admission, and two acceptance bundles; the full `validator.py` + fixture/report integration must still not be preclaimed.

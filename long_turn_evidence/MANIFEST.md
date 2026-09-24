# LT03 artifact manifest

## Core evidence
- `validator.py` + `schema.json` — normalized exact/censored evidence model and fail-closed validation.
- `fixtures.json` — F1-F7, S1-S6, target/adversarial cases.
- `observations.json` / `validate_observations.py` — LT02 exact 411s and LT03 active censored evidence.

## Executed exact-byte suite
All listed byte identities were checked using Git blob SHA before accepting local execution as evidence.
- validator direct fixture run: 15 fixture results PASS; validator blob `e6861c9f940f8a0529b8f93dd546ebcd42c852a7`; fixtures blob `bc269b52a866b377e52813edb9395f1a7225d881`.
- `test_validator.py`: 3 tests PASS, blob `f6f23844c59f059a7c81afd41eb81aa690178e09`.
- `test_lineage.py`: 4 tests PASS; lineage/test blobs `b7c656c8a838a32d4544ba1079fe6235b35f7c9c` / `c5f832bcaa7cce8d814674ee98e3b88295f6a724`.
- `test_hardening.py`: 14 tests PASS, blob `2268ecddb6c78c570c715114c248113a0b4429a1`.
- `validate_observations.py`: PASS; observations/script blobs `f7b937e76e56a9f546db555bbef604be5c6492c4` / `bea8e55683bd050c5fa92853fab845ba8c5a1e01`.
- `report.py`: PASS over 15 fixtures; report blob `15895ec4a2b86e9e6c7680323d6ecf419c1faaec`; summary persisted in `generated_report_summary.json`.
- scheduler: 4 tests PASS; recovery: 7 tests PASS; admission/reserve: 6 tests PASS.
- acceptance bundles: 6 and 13 checks PASS with committed/executed byte equality.

## Docs
`README.md`, `CAPABILITY_CLASSIFICATION.md`, `ACCEPTANCE.md`, and generated report summary document authority, nonclaims, capability mapping, and acceptance evidence.

## Status
The specified deterministic artifact acceptance workload is complete. The original clone path remains unavailable due container DNS, but it is no longer an acceptance blocker because exact committed bytes were reconstructed, hash-verified against GitHub blobs, and executed locally. Remaining LT03 work is only the invocation-duration experiment and safe finalization once the GitHub START-relative 900s threshold is crossed.

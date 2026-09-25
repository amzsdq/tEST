# Long-turn evidence: LT04 migration note

Canonical candidate policy now distinguishes the useful-work stretch interval: below 900 seconds qualifying work continues; from 900 through 1199 seconds safe qualifying work returns `CONTINUE_STRETCH`; at 1200+ safe finalization returns `RESERVE_ENTRY`. No-work never pads.

Evidence versioning: missing `evidence_version` normalizes to legacy v1; explicit v1/v2 are supported; bool/non-integer/unsupported versions are rejected. `schema.json` is a contract artifact, while runtime semantics are enforced by `versioning.py` + `validator.py`. Deprecated `cross_invocation_sum_seconds` remains visible but is still rejected with `CROSS_INVOCATION_SUM_FORBIDDEN`.

Historical `observations.json` is immutable evidence. Later exact same-lineage START/END evidence lives in `exact_evidence.json` and is selected by `authority.py` only after identity/source/timestamp validation.

Verified runtime evidence: LT03 exact 940s PASS. LT04 independent repeat 1191s PASS for >=900 and short by 9s for the 1200 stretch; never round it to 1200.

Run at minimum: `test_admission.py`, `test_validator.py`, `test_hardening.py`, `test_versioning.py`, `test_authority.py`, `test_authority_fallback.py`, `validate_observations_v2.py`, `test_scheduler_v2.py`, and `test_recovery_commit_clock.py`.

# Long-turn invocation evidence validator

This directory contains deterministic LT03/LT04 evidence and runtime-policy artifacts.

## Authority

1. Recognized GitHub START/END `created_at` values are the exact WORKED clock.
2. A durable boundary without END is only a censored lower bound.
3. Later recognized exact same-lineage evidence may supersede a historical censored observation for authority selection without rewriting history.
4. Missing END never licenses cross-invocation summing.
5. Runtime/toolpath causal classes remain hypotheses unless independently established.

## Evidence version migration

`evidence_version` is optional. Missing version normalizes to legacy v1. Explicit versions 1 and 2 are supported. Boolean, non-integer, and unsupported versions are rejected before ordinary validation.

`schema.json` is a contract artifact; runtime enforcement is `versioning.normalize_record` plus `validator.validate`. Deprecated `cross_invocation_sum_seconds` remains shape-visible for compatibility but is semantically forbidden and still produces `CROSS_INVOCATION_SUM_FORBIDDEN`.

## Historical and later-exact evidence

`observations.json` remains immutable historical evidence. `exact_evidence.json` stores later exact evidence. `authority.py` validates invocation, automation, START identity, source, marker shape, timestamp ordering, and ambiguity before selecting exact evidence.

LT03 therefore retains its historical 833-second censored lower bound while separately selecting recognized exact START/END evidence of 940 seconds.

## Admission policy

- elapsed < target: qualifying => `CONTINUE`; no-work => `WORKLOAD_EXHAUSTED`.
- target <= elapsed < stretch: unsafe => `FINALIZATION_BLOCKED`; safe+qualifying => `CONTINUE_STRETCH`; safe+no-work => `RESERVE_ENTRY`.
- elapsed >= stretch: unsafe => `FINALIZATION_BLOCKED`; safe => `RESERVE_ENTRY`.
- Stretch admits useful work only; never padding.

Boundary coverage is 899/900/1199/1200 plus strict input validation.

## Run

`python3 long_turn_evidence/validator.py`
`python3 long_turn_evidence/test_validator.py`
`python3 long_turn_evidence/test_lineage.py`
`python3 long_turn_evidence/test_hardening.py`
`python3 long_turn_evidence/test_admission.py`
`python3 long_turn_evidence/test_versioning.py`
`python3 long_turn_evidence/test_authority.py`
`python3 long_turn_evidence/test_authority_fallback.py`
`python3 long_turn_evidence/validate_observations.py`
`python3 long_turn_evidence/test_scheduler_v2.py`
`python3 long_turn_evidence/test_recovery_commit_clock.py`
`python3 long_turn_evidence/report.py`

## Runtime evidence

LT03 exact WORKED=940s proves the >=900 target. LT04-R118-T6B independently measured WORKED=1191s, independently repeating >=900 but remaining 9 seconds short of the 1200 stretch. Never round 1191 to 1200.

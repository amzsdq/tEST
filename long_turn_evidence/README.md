# Long-turn invocation evidence validator

This directory contains deterministic LT03/LT04 evidence and runtime-policy artifacts.

## Authority

Recognized GitHub START/END `created_at` values are the exact WORKED clock. A durable boundary without END is only a censored lower bound. Later recognized exact same-lineage evidence may supersede a historical censored observation for authority selection without rewriting that historical record. Missing END never licenses cross-invocation summing.

## Evidence versions

`evidence_version` is optional. Missing version normalizes to legacy v1. Explicit v1/v2 are supported; bool, non-integer, and unsupported versions are rejected before ordinary validation.

`schema.json` is a contract artifact. Runtime semantics are enforced by `versioning.normalize_record` plus `validator.validate`. Deprecated `cross_invocation_sum_seconds` remains shape-visible but is semantically forbidden and produces `CROSS_INVOCATION_SUM_FORBIDDEN`.

## Historical vs exact evidence

`observations.json` remains historical evidence. `exact_evidence.json` and `exact_evidence.schema.json` define later exact evidence. `authority.py` validates evidence ID, invocation, automation, START identity, source, marker shape, timestamp ordering, and ambiguity before exact evidence wins.

LT03 keeps its historical 833-second censored lower bound while canonical observation validation separately selects recognized exact START/END evidence of 940 seconds.

## Admission

- elapsed < target: qualifying => `CONTINUE`; no-work => `WORKLOAD_EXHAUSTED`.
- target <= elapsed < stretch: unsafe => `FINALIZATION_BLOCKED`; safe+qualifying => `CONTINUE_STRETCH`; safe+no-work => `RESERVE_ENTRY`.
- elapsed >= stretch: unsafe => `FINALIZATION_BLOCKED`; safe => `RESERVE_ENTRY`.
- Stretch is useful work only; never padding.

Boundary coverage: 899/900/1199/1200 plus strict type and relationship checks.

## Runtime helpers

`scheduler_v2.py` computes END+180 and verifies either ISO timestamps or live VEVENT DTSTART readback, including TZID schedules; duplicate or spoofed DTSTART fields fail closed. `recovery_commit_clock.py` requires a verified START before cold resume, distinguishes unverified/verified END, validates automation authority, and requires exactly one unbounded `FREQ=HOURLY` RRULE; parameterized rules such as COUNT/UNTIL/INTERVAL, spoofed frequencies, or multiple RRULE lines fail closed because they can truncate or alter relay liveness.

## Run

Canonical fail-fast suite:
`python3 long_turn_evidence/run_canonical_checks.py`

Individual checks:
`python3 long_turn_evidence/validator.py`
`python3 long_turn_evidence/test_validator.py`
`python3 long_turn_evidence/test_lineage.py`
`python3 long_turn_evidence/test_hardening.py`
`python3 long_turn_evidence/test_admission.py`
`python3 long_turn_evidence/test_versioning.py`
`python3 long_turn_evidence/test_schema_contract.py`
`python3 long_turn_evidence/test_authority.py`
`python3 long_turn_evidence/test_authority_fallback.py`
`python3 long_turn_evidence/validate_observations.py`
`python3 long_turn_evidence/test_scheduler.py`
`python3 long_turn_evidence/test_scheduler_v2.py`
`python3 long_turn_evidence/test_recovery.py`
`python3 long_turn_evidence/test_recovery_commit_clock.py`
`python3 long_turn_evidence/report.py`

## Runtime evidence

LT03 exact WORKED=940s proves >=900. LT04-R118-T6B independently measured WORKED=1191s, repeating >=900 but remaining exactly 9 seconds short of 1200. Never round 1191 to 1200.

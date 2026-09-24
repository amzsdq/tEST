# Long-turn invocation evidence validator

This directory is the deterministic artifact workload for LT03. It is independent of private/session data and does not scrape GitHub; inputs are explicit records.

## Authority precedence

1. Raw GitHub `created_at` on recognized START and matching END is the only exact WORKED clock.
2. A durable boundary without END establishes only a **censored lower bound**. It is never an exact kill time.
3. FINAL_BATON + matching END + exactly one final scheduler mutation is the accepted voluntary-final signature.
4. Missing END never licenses summing another invocation. One-turn success is one lineage only.
5. A currently active censored observation is not an abrupt termination. `observation_state=active` remains `UNKNOWN` until closure/recovery evidence exists.
6. Runtime/toolpath candidate classes are causal hypotheses, not provider root-cause declarations.

## Normalized record

Required: `invocation_id`, `automation_id`, `start`, `scheduler_mutation_count`. Optional: `end`, `last_durable_boundary`, `final_baton`, `finalization_signature`, `observation_state`, `termination_evidence`, target/claim fields. Markers require positive integer IDs and offset-aware ISO-8601 `created_at`.

## Classification

- `VOLUNTARY_FINAL`: END + finalization signature + FINAL_BATON + exactly one scheduler mutation.
- `ABRUPT_NONFINAL`: recovered/non-active censored lineage with no stronger explicit cause evidence.
- `TOOLPATH_LOSS_CANDIDATE`: censored lineage plus explicit toolpath-loss evidence.
- `PLATFORM_RUNTIME_KILL_CANDIDATE`: censored lineage plus explicit runtime-kill evidence.
- `UNKNOWN`: insufficient evidence, including a still-active censored observation.

## Safety/nonclaims

The validator does not infer exact duration for censored runs, combine invocations, infer platform root cause from silence, validate scheduler provider delivery by itself, or equate elapsed time with useful work.

## Run

`python3 long_turn_evidence/validator.py`
`python3 long_turn_evidence/test_validator.py`
`python3 long_turn_evidence/test_lineage.py`
`python3 long_turn_evidence/test_hardening.py`
`python3 long_turn_evidence/validate_observations.py`
`python3 long_turn_evidence/report.py`

Fixtures cover normal completion, censored recovery, tool/runtime candidates, malformed IDs/timestamps, impossible ordering, one-final-mutation violations, missing baton, cross-invocation summing, multiple END candidates, and 899/900-second target boundaries.

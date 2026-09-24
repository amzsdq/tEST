# Long-turn invocation evidence validator

This directory is the deterministic artifact workload for LT03. It is intentionally independent of private/session data and does not scrape GitHub. Fixtures contain explicit synthetic records shaped like durable relay evidence.

## Authority precedence

1. Raw GitHub `created_at` on the recognized invocation START and matching END is the only exact WORKED clock.
2. A durable boundary without END establishes only a **censored lower bound**: the invocation survived at least until that boundary. It is not an exact kill time.
3. FINAL_BATON + matching END + exactly one final scheduler mutation is the accepted voluntary-final signature.
4. Missing END never licenses summing time from another invocation. One-turn success must be proved inside one lineage.
5. Classification is weaker than causal proof. `PLATFORM_RUNTIME_KILL_CANDIDATE` and `TOOLPATH_LOSS_CANDIDATE` are hypotheses supported by explicit termination evidence, not declarations of provider root cause.

## Normalized record

Required fields: `invocation_id`, `automation_id`, `start`, `scheduler_mutation_count`. Optional evidence includes `end`, `last_durable_boundary`, `final_baton`, `finalization_signature`, `termination_evidence`, and target/claim fields. Markers use positive integer IDs plus offset-aware ISO-8601 `created_at`.

## Classification

- `VOLUNTARY_FINAL`: END + finalization signature + FINAL_BATON + exactly one scheduler mutation.
- `ABRUPT_NONFINAL`: no END, a durable post-START boundary, and no stronger explicit cause evidence.
- `TOOLPATH_LOSS_CANDIDATE`: censored run plus explicit toolpath-loss evidence.
- `PLATFORM_RUNTIME_KILL_CANDIDATE`: censored run plus explicit runtime-kill evidence.
- `UNKNOWN`: evidence does not satisfy a stronger deterministic class.

## Safety/nonclaims

The validator does not infer exact duration for censored runs, does not combine invocations, does not infer platform root cause from silence, does not validate scheduler provider delivery by itself, and does not treat elapsed time as useful-work evidence. It only checks explicit evidence relationships supplied to it.

## Run

`python3 long_turn_evidence/validator.py`

Every fixture is self-checking through its `expected` object. A mismatch raises. Fixtures include normal completion, censored recovery, tool/runtime candidates, malformed IDs, impossible timestamp ordering, one-final-mutation violations, missing baton, cross-invocation summing, and the 899/900-second target boundary.

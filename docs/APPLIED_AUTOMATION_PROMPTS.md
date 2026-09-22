# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version every relay prompt actually tested so experiment results can be tied to an exact control policy.

> Security note: runtime-specific automation IDs are replaced with placeholders in this public repository. The tested logic and schedule semantics are preserved.

---

## P4V1 — Ledger+Issue-first bootstrap trial

State: REGISTERED EXPERIMENTAL VARIANT
Parent: P4V0
Trial: `P4-BOOTSTRAP-READSET-01`
Primary variable: normal-path bootstrap repository read-set only
Rollback: P4V0

### Semantic diff from P4V0

Exactly one control-policy variable changes:

- **P4V0:** every wake reads `RELAY_RESEARCH_PROGRAM.md`, `APPLIED_AUTOMATION_PROMPTS.md`, `RELAY_OPTIMIZATION_CONVERGENCE.md`, `EXPERIMENT_LEDGER.md`, and Issue #1 before reconstructing state.
- **P4V1:** normal-path bootstrap reads `EXPERIMENT_LEDGER.md` and Issue #1 first. Read `RELAY_RESEARCH_PROGRAM.md`, `APPLIED_AUTOMATION_PROMPTS.md`, and `RELAY_OPTIMIZATION_CONVERGENCE.md` only when state is ambiguous/inconsistent, a prompt change is being prepared, promotion/rollback is being decided, or reconstruction lacks a required invariant.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 verification policy, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if ledger+Issue-first reconstruction omits or misstates CURRENT_CANDIDATE, lead-time/scheduler policy, checkpoint/authority, verification, known failures, recovery evidence, active trial, or NEXT_DISCRIMINATING_TEST, immediately restore P4V0 full canonical read-set.

### Trial interpretation

The test asks whether the reconciliation snapshot plus root issue is sufficient for correct normal-path continuation while reducing repository reads and increasing useful-work duty cycle. Correctness is primary; fewer reads alone is not a pass.

---

## P4V0 — Verification-frequency omission trial

State: PROVISIONALLY PROMOTED
Parent: P0R
Trial: `P4-VERIFY-FREQUENCY-01`
Primary variable: post-write live metadata verification frequency only
Rollback: P0R

### Semantic diff from P0R

- **P0R:** after every final scheduler write, immediately perform a separate live-metadata read and require matching automation id, `is_enabled=true`, `RRULE:FREQ=HOURLY`, and intended `DTSTART`.
- **P4V0:** omit that separate post-write live-metadata read on the normal path. Treat the scheduler update tool's successful returned object as `WRITE_OK/STATE_OK` evidence, but do not infer `WAKE_OK` until a future invocation actually occurs.

Everything else remains unchanged. Conditional live verification/reconciliation remains required for malformed update output, ambiguous reconstruction, or later inconsistency.

---

## P0R — Research-enabled RRULE relay worker (rollback baseline)

State: HISTORICAL/ROLLBACK BASELINE

Core invariants preserved across active variants:
- same automation id
- recurring `RRULE:FREQ=HOURLY`
- no one-shot or `dtstart_offset_json`
- no new automation
- substantive research each wake
- one primary variable per experiment
- WRITE_OK / STATE_OK / WAKE_OK / WORK_OK separated
- prompt semantic diff registered before application
- final scheduler write is authoritative and last scheduler mutation
- TEST contains no secrets/session state/private credentials

---

## Historical P0 stress fixture

P0 used five intermediate schedule mutations plus a final close-relative recurring wake and per-write verification. It remains only as a diagnostic repeated-mutation fixture; it is not a production candidate.

---

## Candidate convergence lineage

- P1: single final recurring RRULE write
- P2: provisional fallback + final fast continuation (tested/rejected as unnecessary extra mutation)
- P3: durable-state-first / checkpoint + authority fencing concepts
- P4: minimal production family; remove normal-path diagnostics only when evidence preserves reliability

## Prompt-version experiment rule

Every scheduler experiment records prompt version, semantic diff, scheduler writes/wake, intended lead time, intended due, actual invocation, WRITE/STATE/WAKE/WORK evidence, RRULE survival, duplicate observation, useful work, control overhead, and interpretation. Do not change prompt structure and lead time in the same experiment unless explicitly testing interaction effects.

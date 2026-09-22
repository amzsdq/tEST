# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version every relay prompt actually tested so experiment results can be tied to an exact control policy.

> Security note: runtime-specific automation IDs are replaced with placeholders in this public repository. The tested logic and schedule semantics are preserved.

---

## P4V7 — Routine positive-wake-field omission trial

State: REGISTERED EXPERIMENTAL VARIANT
Parent: P4V6
Trial: `P4-WAKE-POSITIVE-OMISSION-01`
Primary variable: routine clean-success positive `WAKE_OK` evidence only
Rollback: P4V6

### Semantic diff from P4V6

Exactly one control-policy variable changes:

- **P4V6:** routine clean-success non-boundary Issue records explicitly include `WAKE_OK=YES`.
- **P4V7:** omit `WAKE_OK` only for a routine clean-success scheduled invocation, because the current invocation itself is positive wake evidence. `WAKE_OK` remains explicit whenever it is `PENDING`/`NO`, or in anomaly, recovery, rollback, boundary, or timing-specific evidence where wake state must be independently visible.

Routine clean-success durable schema becomes `EXPERIMENT`, `SAMPLE`, `RESULT`, `WRITE_OK`, `STATE_OK`, `WORK_OK`, `NEXT`. P4V6 conditional `DUPLICATE` policy and P4V5 START/END policy are unchanged.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification, P4V2 Issue-only routine logging with boundary reconciliation, P4V4 Issue-tail-only routine bootstrap, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if the next routine wake cannot reconstruct candidate/trial/sample order/result/WRITE_OK/STATE_OK/WAKE_OK/WORK_OK/NEXT, if absence of `WAKE_OK` cannot be safely interpreted as positive wake evidence on a clean scheduled invocation, or if anomaly/recovery/boundary reconciliation loses wake-state evidence, immediately restore P4V6 routine schema with explicit `WAKE_OK=YES`.

### Trial interpretation

This tests whether a successful scheduled invocation can serve as the positive wake observation without redundantly persisting `WAKE_OK=YES`. Smaller records alone are not a pass; end-to-end continuation and boundary reconciliation must remain exact.

---

## P4V6 — Routine negative-duplicate-field omission trial

State: REGISTERED EXPERIMENTAL VARIANT
Parent: P4V5
Trial: `P4-COMPACT-DUPLICATE-NEGATIVE-01`
Primary variable: routine clean-success non-boundary Issue compact evidence fields only
Rollback: P4V5

### Semantic diff from P4V5

Exactly one control-policy variable changes:

- **P4V5:** every routine clean-success non-boundary Issue record includes `DUPLICATE=NO observed`.
- **P4V6:** omit `DUPLICATE` only when the observation is the routine negative case (no duplicate/anomaly). `DUPLICATE` remains explicit whenever a duplicate is observed or duplicate state is relevant to anomaly, recovery, rollback, boundary, or timing-specific evidence.

Routine clean-success durable schema becomes `EXPERIMENT`, `SAMPLE`, `RESULT`, `WRITE_OK`, `STATE_OK`, `WAKE_OK`, `WORK_OK`, `NEXT`. START/END policy from P4V5 is unchanged. ANOMALY/ROLLBACK and non-negative DUPLICATE evidence remain conditional fields.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification policy, P4V2 Issue-only routine logging with boundary reconciliation, P4V4 Issue-tail-only routine bootstrap, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if the next routine wake cannot reconstruct candidate/trial/sample order/result/status tuple/NEXT or cannot safely infer the clean-path duplicate-negative state from the absence of `DUPLICATE`, or if a later anomaly/recovery/boundary reconciliation loses duplicate evidence, immediately restore P4V5 routine schema with explicit `DUPLICATE=NO observed`.

### Trial interpretation

This tests whether an invariant-negative field can be represented by absence on clean paths without reducing duplicate-prevention observability. Smaller records alone are not a pass; end-to-end continuation and boundary reconciliation must remain exact.

---

## P4V5 — Routine compact timing-field reduction trial

State: PROVISIONALLY PROMOTED
Parent: P4V4
Trial: `P4-COMPACT-TIMING-FIELDS-01`
Primary variable: routine non-boundary Issue compact evidence fields only
Rollback: P4V4

### Semantic diff from P4V4

Exactly one control-policy variable changes:

- **P4V4:** routine successful Issue records include `START` and `END` alongside continuation-state fields.
- **P4V5:** routine clean-success non-boundary Issue records omit `START` and `END`. Timing fields remain available/required for boundary, anomaly, rollback, or timing-specific experiments. User-facing completion still reports START/END/DURATION.

Routine durable schema becomes `EXPERIMENT`, `SAMPLE`, `RESULT`, `WRITE_OK`, `STATE_OK`, `WAKE_OK`, `WORK_OK`, `DUPLICATE`, `NEXT`, with `ANOMALY`/`ROLLBACK` only when non-empty.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification policy, P4V2 Issue-only routine logging with ledger-at-boundary reconciliation, P4V3 compact evidence semantics, P4V4 Issue-tail-only routine bootstrap, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if the next routine wake cannot reconstruct candidate/trial/sample order/result/status tuple/duplicate/NEXT from the reduced Issue record, if loss of START/END prevents required anomaly/recovery/reconciliation analysis, or if boundary reconciliation disagrees, immediately restore P4V4 routine schema with START/END.

### Trial interpretation

This tests whether routine durable timestamps are redundant when scheduler/wake timing is not the active variable. Smaller records alone are not a pass; continuation and later reconciliation must remain exact.

---

## P4V4 — Issue-tail-only routine bootstrap trial

State: PROVISIONALLY PROMOTED
Parent: P4V3
Trial: `P4-BOOTSTRAP-SINGLE-SOURCE-01`
Primary variable: routine clean-success bootstrap read-source count only
Rollback: P4V3

### Semantic diff from P4V3

Exactly one control-policy variable changes:

- **P4V3:** normal-path bootstrap reads `EXPERIMENT_LEDGER.md` and Issue #1 first.
- **P4V4:** a routine clean-success continuation reads the latest Issue #1 state/comments first and may reconstruct directly from the compact Issue tail without a mandatory `EXPERIMENT_LEDGER.md` read. `EXPERIMENT_LEDGER.md` remains mandatory at sample-set completion/reconciliation boundaries and whenever state is ambiguous/inconsistent, promotion/rejection/rollback is being decided, prompt/invariant recovery is required, or Issue-tail reconstruction is insufficient.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification policy, P4V2 Issue-only routine logging with ledger-at-boundary reconciliation, P4V3 compact routine Issue schema, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if Issue-tail-only routine bootstrap cannot reconstruct CURRENT_CANDIDATE, active trial/sample identity and order, result, WRITE_OK/STATE_OK/WAKE_OK/WORK_OK, duplicate observation, NEXT, or any required invariant; or if boundary reconciliation disagrees with Issue-tail reconstruction, immediately restore P4V3 ledger+Issue-first bootstrap behavior.

### Trial interpretation

The test asks whether one routine repository read source can be removed without reducing continuation correctness. Fewer reads alone is not a pass; end-to-end wake plus later boundary reconciliation must preserve the same state.

---

## P4V3 — Compact routine Issue evidence trial

State: PROVISIONALLY PROMOTED
Parent: P4V2
Trial: `P4-ISSUE-COMPACT-01`
Primary variable: routine Issue evidence shape/verbosity only
Rollback: P4V2

### Semantic diff from P4V2

Exactly one control-policy variable changes:

- **P4V2:** routine non-boundary successful turns append durable Issue #1 evidence without a required compact representation.
- **P4V3:** the same one Issue #1 append is retained, but routine success evidence uses a fixed compact record containing only `EXPERIMENT`, `SAMPLE`, `START`, `END`, `RESULT`, `WRITE_OK`, `STATE_OK`, `WAKE_OK`, `WORK_OK`, `DUPLICATE`, and `NEXT`; add `ANOMALY` or `ROLLBACK` only when non-empty.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification policy, P4V1 ledger+Issue-first bootstrap, P4V2 Issue-only routine logging with ledger-at-boundary reconciliation, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if the next turn cannot reconstruct sample identity/order, result, WRITE_OK/STATE_OK/WAKE_OK/WORK_OK, duplicate observation, and NEXT from the compact record plus unchanged ledger, or if a needed anomaly/rollback fact is lost, immediately restore P4V2 prose-capable Issue evidence.

### Trial interpretation

The test asks whether evidence representation can be reduced without reducing continuation/reconciliation correctness. Smaller comments alone are not a pass.

---

## P4V2 — Issue-first routine logging fan-out trial

State: PROVISIONALLY PROMOTED
Parent: P4V1
Trial: `P4-LOG-FANOUT-01`
Primary variable: normal-path durable logging fan-out/frequency only
Rollback: P4V1

### Semantic diff from P4V1

- **P4V1:** routine successful turns may persist substantially overlapping per-turn evidence to both Issue #1 and canonical ledger/docs.
- **P4V2:** routine non-boundary successful turns append per-turn evidence to Issue #1 only. Canonical `EXPERIMENT_LEDGER.md` mutation is deferred to a trial boundary: sample-set completion, promotion/rejection/rollback, or explicit reconciliation checkpoint.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification policy, P4V1 ledger+Issue-first bootstrap read-set, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if Issue-only routine evidence cannot reconstruct sample ordering/result/WRITE_OK/STATE_OK/WAKE_OK/WORK_OK/duplicate observation/NEXT test at the next boundary, or deferred ledger reconciliation loses evidence, immediately restore P4V1 routine logging behavior.

### Trial interpretation

The test asks whether canonical write fan-out can be reduced without reducing durable evidence quality or reconstruction correctness. Fewer writes alone is not a pass.

---

## P4V1 — Ledger+Issue-first bootstrap trial

State: PROVISIONALLY PROMOTED
Parent: P4V0
Trial: `P4-BOOTSTRAP-READSET-01`
Primary variable: normal-path bootstrap repository read-set only
Rollback: P4V0

### Semantic diff from P4V0

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

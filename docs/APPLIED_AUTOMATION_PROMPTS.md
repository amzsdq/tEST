## P4V11 — GitHub server timestamp work-duration source of truth

State: APPLIED
Parent: P4V10
Primary variable: work-duration time source only
Rollback: P4V10

### Semantic diff from P4V10

- **P4V10:** work start/end could be reported as model-written time strings in chat/evidence.
- **P4V11:** work-duration judgment MUST use GitHub server timestamps only.
- At actual work start, append a distinct `START_MARKER` Issue #1 comment.
- At actual work end, append a distinct `END_MARKER` Issue #1 comment.
- The authoritative duration is:

```text
WORK_DURATION Source of Truth =
GitHub server comment timestamps
```

```text
WORKED =
END_MARKER.created_at
-
START_MARKER.created_at
```

- Model-written START/END/time strings are display-only metadata and MUST NOT participate in work-duration judgment, thresholding, promotion/rejection, or utilization metrics.
- If either marker or its GitHub `created_at` is unavailable/ambiguous, WORKED is UNKNOWN; do not estimate it from model text or local clock.
- START_MARKER and END_MARKER must belong to the same execution turn and be uniquely identifiable.

Everything else is frozen from P4V10: same automation id, recurring `RRULE:FREQ=HOURLY`, no one-shot schedule, same scheduler mutation policy, same state/evidence rules, same jitter telemetry, same experiment discipline.

---

# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version every relay prompt actually tested so experiment results can be tied to an exact control policy.

> Security note: runtime-specific automation IDs are replaced with placeholders in this public repository. The tested logic and schedule semantics are preserved.

---

## P4V10 — Wake-jitter telemetry instrumentation

State: REGISTERED OBSERVABILITY VARIANT
Parent: P4V9
Trial: `P4-WAKE-JITTER-TELEMETRY-01`
Primary variable: wake-timing telemetry only
Rollback: P4V9

### Semantic diff from P4V9

Exactly one operational variable changes:

- **P4V9:** relay continuation and evidence are evaluated without a mandatory accumulated wake-jitter series.
- **P4V10:** preserve all P4V9 relay behavior, schema semantics, scheduler path, lead-time policy, and rollback rules, while adding observational wake-jitter telemetry. No scheduler decision may be changed because of the telemetry until a later separately registered experiment.

For each actual automation invocation, before the final scheduler mutation:
- read the same automation's pre-update scheduled DTSTART and actual last-run/invocation time when available;
- define signed `JITTER_SEC = ACTUAL_RUN - SCHEDULED_FOR` (positive = late, negative = early);
- append a compact jitter sample to Issue #1;
- maintain running `N`, signed mean, mean absolute jitter, population standard deviation, minimum, and maximum using the previous aggregate;
- every 10 accepted samples, additionally calculate median and P95 from the accepted jitter sample set.

Manual/user-triggered turns or turns without a trustworthy matching scheduled DTSTART/actual-run pair are not accepted as jitter samples and must be marked `JITTER_SAMPLE=SKIP` rather than guessed.

Telemetry must remain append-only evidence. Do not rewrite the historical ledger merely to store routine jitter samples. Timing telemetry is observational and does not count as a second experimental PRIMARY_VARIABLE.

Everything else is frozen from P4V9: same automation id, single final recurring RRULE write, current promoted +3m-class lead policy, `RRULE:FREQ=HOURLY`, `is_enabled=true`, no new automation, P4V9 positive-field absence semantics, issue-tail bootstrap, substantive-work requirement, and existing recovery rules.

### Initial metric contract

```
TELEMETRY=WAKE_JITTER_V1
SCHEDULED_FOR=<timestamp>
ACTUAL_RUN=<timestamp>
JITTER_SEC=<signed seconds>
N=<accepted sample count>
MEAN_SIGNED_SEC=<running mean>
MEAN_ABS_SEC=<running mean absolute jitter>
STDDEV_SEC=<population stddev>
MIN_SEC=<minimum signed jitter>
MAX_SEC=<maximum signed jitter>
P50_SEC=<every 10 samples only>
P95_SEC=<every 10 samples only>
```

---

## P4V9 — Routine positive-write-field omission trial

State: REGISTERED EXPERIMENTAL VARIANT
Parent: P4V8
Trial: `P4-WRITE-POSITIVE-OMISSION-01`
Primary variable: routine clean-success positive `WRITE_OK` evidence only
Rollback: P4V8

### Semantic diff from P4V8

Exactly one control-policy variable changes:

- **P4V8:** routine clean-success non-boundary Issue records explicitly include `WRITE_OK=YES`.
- **P4V9:** omit `WRITE_OK` only when the final scheduler update returns a valid success object and the same object satisfies the existing P4V8 positive `STATE_OK` contract. `WRITE_OK` remains logically evaluated and remains explicit whenever it is `PENDING`/`NO`, the update fails, the return is malformed/mismatched, or in anomaly, recovery, rollback, boundary, or timing-specific evidence.

Routine clean-success durable schema becomes `EXPERIMENT`, `SAMPLE`, `RESULT`, `WORK_OK`, `NEXT`. P4V8 positive-state omission, P4V7 positive-wake omission, and P4V6 conditional duplicate policy remain unchanged.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification, P4V2 Issue-only routine logging with boundary reconciliation, P4V4 Issue-tail-only routine bootstrap, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if a subsequent routine wake cannot reconstruct candidate/trial/sample order/result/WRITE_OK/STATE_OK/WAKE_OK/WORK_OK/NEXT, if absence of `WRITE_OK` cannot be safely interpreted as a successful scheduler write on a clean valid scheduler update, or if anomaly/recovery/boundary reconciliation loses scheduler-write evidence, immediately restore P4V8 routine schema with explicit `WRITE_OK=YES`.

### Trial interpretation

This tests whether a valid scheduler update return can serve simultaneously as positive write and state evidence without redundantly persisting `WRITE_OK=YES`. Smaller records alone are not a pass; end-to-end continuation and boundary reconciliation must remain exact.

---

## P4V8 — Routine positive-state-field omission trial

State: REGISTERED EXPERIMENTAL VARIANT
Parent: P4V7
Trial: `P4-STATE-POSITIVE-OMISSION-01`
Primary variable: routine clean-success positive `STATE_OK` evidence only
Rollback: P4V7

### Semantic diff from P4V7

Exactly one control-policy variable changes:

- **P4V7:** routine clean-success non-boundary Issue records explicitly include `STATE_OK=YES`.
- **P4V8:** omit `STATE_OK` only when the final scheduler update return object itself confirms the expected recurring RRULE, intended DTSTART, and `is_enabled=true`. `STATE_OK` remains logically evaluated and remains explicit whenever it is `PENDING`/`NO`, the return is malformed/mismatched, or in anomaly, recovery, rollback, boundary, or timing-specific evidence.

Routine clean-success durable schema becomes `EXPERIMENT`, `SAMPLE`, `RESULT`, `WRITE_OK`, `WORK_OK`, `NEXT`. P4V7 positive-wake omission and P4V6 conditional duplicate policy remain unchanged.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification, P4V2 Issue-only routine logging with boundary reconciliation, P4V4 Issue-tail-only routine bootstrap, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

Failure/rollback rule: if a subsequent routine wake cannot reconstruct candidate/trial/sample order/result/WRITE_OK/STATE_OK/WAKE_OK/WORK_OK/NEXT, if absence of `STATE_OK` cannot be safely interpreted as positive state evidence on a clean successful scheduler update, or if anomaly/recovery/boundary reconciliation loses scheduler-state evidence, immediately restore P4V7 routine schema with explicit `STATE_OK=YES`.

### Trial interpretation

This tests whether the successful scheduler update return object can serve as positive state evidence without redundantly persisting `STATE_OK=YES`. Smaller records alone are not a pass; end-to-end continuation and boundary reconciliation must remain exact.

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

- **P4V2:** routine non-boundary successful turns append durable Issue #1 evidence without a required compact representation.
- **P4V3:** the same one Issue #1 append is retained, but routine success evidence uses a fixed compact record containing only `EXPERIMENT`, `SAMPLE`, `START`, `END`, `RESULT`, `WRITE_OK`, `STATE_OK`, `WAKE_OK`, `WORK_OK`, `DUPLICATE`, and `NEXT`; add `ANOMALY` or `ROLLBACK` only when non-empty.

Everything else is frozen: same automation, P1 single-final-write scheduler path, +3m-class lead policy, `RRULE:FREQ=HOURLY`, P4V0 conditional verification policy, P4V1 ledger+Issue-first bootstrap read-set, P4V2 Issue-only routine logging with ledger-at-boundary reconciliation, checkpoint/authority/recovery rules, substantive-work requirement, and no new automation.

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


---

## P5M1 — Minimal relay + long-work package trial

State: ACTIVE EXPERIMENTAL CANDIDATE
Parent: P4V11
Primary variables are separated by phase:
- Relay core: structural simplification only.
- Long-work experiment: WORK_PACKAGE completion gate only.
Rollback: P4V11

### Why P5M1 exists

P4V11 accumulated many anomaly/ABA/reconciliation rules. Those findings remain in the repository, but they are no longer carried in the hot prompt unless a matching failure is actually observed. The current dominant problem is short useful-work turns, not loss of recurring scheduler state.

### Relay core retained

1. Reuse exactly one automation id.
2. Keep a complete recurring VEVENT with `RRULE:FREQ=HOURLY` and `is_enabled=true`.
3. Never use one-shot DTSTART-only scheduling or `dtstart_offset_json`.
4. Perform exactly one final scheduler mutation per normal turn.
5. Compute FINAL_NEXT immediately before that final write; default class is current time +3 minutes unless a lead-time experiment is explicitly active.
6. Issue #1 is the routine durable baton. Read only its compact tail on clean continuation.
7. GitHub START_MARKER/END_MARKER server `created_at` remains the only work-duration authority. If unavailable, WORKED=UNKNOWN.
8. Do not modify R, RRuleR, or RRuleRO. Do not persist secrets/session/private URLs.

Everything else from P4V11 becomes cold-path knowledge: use it only when a matching anomaly, ambiguity, rollback, or explicit recovery experiment requires it.

### Long-work hypothesis LW1 — Sized work package + early-stop gate

Hypothesis: abstract instructions such as "work for 10-14 minutes" are weak. A concrete pre-sized work package with multiple acceptance criteria will produce longer useful turns.

Each invocation reconstructs or creates exactly one WORK_PACKAGE containing 4-6 substantive units. The package should be sized so that a competent worker would normally need roughly 8-12 minutes of real tool/reasoning work, but elapsed time is not estimated by the model for scoring.

EARLY_STOP_GATE:
- Do not end the turn merely because one unit completed.
- Continue directly into the next unit while package work remains.
- Normal turn termination is allowed only when:
  A) all package acceptance criteria are satisfied;
  B) a genuine external blocker prevents further useful work;
  C) a safety/runtime constraint prevents continuing.
- A small discovery, one successful tool call, one comment, or one scheduler update is never sufficient completion by itself.

The next wake must receive the next concrete WORK_PACKAGE pointer, not a vague research topic.

### LW1 measurement

For each sample record:
- package id
- number of planned substantive units
- number completed
- package complete yes/no
- START_MARKER and END_MARKER server timestamps when available
- WORKED
- useful outputs produced
- early-stop reason if package incomplete
- scheduler write count
- continuation outcome on next wake

Promotion target: materially longer median WORKED and more useful outputs per turn without reducing continuation reliability or increasing normal scheduler writes above one.

### P5M1 hot prompt

```text
ROLE=RELAY_RESEARCH_WORKER
REPO=amzsdq/tEST
ROOT_ISSUE=1
AUTOMATION_ID=6ab15cd35698819195d49a1ae580a8c1
PROMPT_VERSION=P5M1

GOAL:
Find the simplest reliable self-renewing Automation relay, while maximizing useful work per invocation.

CORE:
- Reuse this exact AUTOMATION_ID. Never create another automation.
- Keep is_enabled=true and a complete recurring VEVENT containing RRULE:FREQ=HOURLY.
- Never use one-shot DTSTART-only scheduling or dtstart_offset_json.
- Normal path gets exactly ONE scheduler mutation, at the end.
- FINAL_NEXT is computed immediately before that write. Default: actual current Asia/Seoul time +3 minutes unless an explicit lead-time trial is active.
- Issue #1 compact tail is the routine baton. Read broader docs only for ambiguity, boundary, anomaly, prompt change, or rollback.
- START_MARKER/END_MARKER GitHub server created_at is the only WORKED clock. Missing pair => WORKED=UNKNOWN.
- Do not modify R, RRuleR, RRuleRO. Do not store secrets/session/private URLs.

WORK_PACKAGE:
- Every wake must execute one concrete package of 4-6 substantive work units with explicit acceptance criteria.
- Prefer unfinished package work over inventing a new experiment.
- Do not stop after one unit, one finding, one comment, or one successful tool call.
- Continue unit-to-unit until the package is COMPLETE, genuinely BLOCKED, or execution/runtime safety prevents further work.
- If incomplete, write an exact NEXT package pointer so the next wake can resume immediately.
- Abstract "work longer" instructions do not count as a work package.

TURN:
1. Append START_MARKER immediately before substantive work.
2. Recover latest package/result/NEXT from Issue #1 tail.
3. Execute the package continuously.
4. Append one compact result/baton record.
5. Compute FINAL_NEXT and update this same automation once with:
   BEGIN:VEVENT
   DTSTART;TZID=Asia/Seoul:<FINAL_NEXT>
   RRULE:FREQ=HOURLY
   END:VEVENT
   and is_enabled=true.
6. Append END_MARKER. Do no substantive work after END_MARKER.
7. Report START_SERVER / END_SERVER / WORKED / PACKAGE / UNITS_DONE / RESULT / NEXT.

LONG_WORK_EXPERIMENT=LW1
PRIMARY_VARIABLE=pre-sized multi-unit WORK_PACKAGE + early-stop gate.
Do not add extra scheduler writes, watchdogs, leases, queues, ABA machinery, or new durable state unless an observed failure specifically requires them.
```


---

## P5M3 — Native terminal-aware relay / Parrot replacement target

State: ACTIVE CANDIDATE
Parent: P5M2 candidate

### Problem

A UI-driven loop that sends another "continue" message whenever generation stops cannot distinguish:
- response completion,
- package completion,
- program completion.

That creates token/control overhead after useful work is already complete.

### P5M3 change

The hot path now has an explicit durable state machine:
- CONTINUE
- PROGRAM_COMPLETE
- RECOVERABLE
- PAUSED

Continuation is permitted only when durable state contains a concrete useful NEXT action.
UI inactivity, response completion, or a vague possibility of more research are not continuation evidence.

### Terminal guard

If active program acceptance criteria are satisfied and no useful NEXT remains:
1. append final completion evidence to Issue #1;
2. set the same automation is_enabled=false;
3. do not schedule another wake.

Package completion alone does not imply program completion.

### No-op suppression

Do not keep the relay alive by:
- inventing new experiments after convergence,
- repeating redundant validation for sample-count aesthetics,
- synthetic checkpoints,
- filler summaries,
- waiting/padding.

### Success criterion

The native relay replaces the Parrot-style UI loop when one start is sufficient to:
1. continue through exact durable NEXT pointers,
2. recover from ordinary failures,
3. stop itself on PROGRAM_COMPLETE,
4. avoid any external UI agent repeatedly injecting "continue".

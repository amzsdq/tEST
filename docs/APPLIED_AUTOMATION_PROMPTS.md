# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M8 — Auto-refill finalization-reserve controlled step-down

State: APPLIED / E12 250S STEP-DOWN ACTIVE
Parent: P5M7 directional finalization reserve
Primary variable: FINALIZATION_RESERVE_CUTOFF_STEPDOWN

### Contract
AUTO_REFILL remains promoted: `PACKAGE_COMPLETE != TURN_COMPLETE`. LW26 and LW27 independently used the same predeclared 240-second new-package admission cutoff and safely committed final baton + sole scheduler mutation + END. Normalized tails were LW26 A/B/C=22/31/53s and LW27=13/21/34s, so 240s is `CONSERVATIVE_REPEAT_CONFIRMED` within observed conditions.

P5M8 changes only the admission cutoff to a separately predeclared 250 seconds. External time is checked at substantive package admission boundaries only. A safe 250s sample is directional and requires repeat before promotion. Lost continuation, `RESERVE_TOO_SMALL`, or materially ambiguous finalization margin restores 240s on the next trial. `PACKAGE_OVERRUN` is tracked separately and does not equal reserve failure unless finalization is lost. Never infer a fixed runtime ceiling from one trace and never tune the cutoff within a live run.

## P5M7 — Auto-refill with directional finalization reserve

State: SUPERSEDED FOR ACTIVE TESTING / 240S REPEAT COMPLETED
Parent: promoted P5M6 same-invocation auto-refill
Primary variable: FINALIZATION_RESERVE_POLICY

### Contract
AUTO_REFILL remains default. Elapsed time is only a safety/finalization admission signal. LW26 and LW27 supplied the repeated 240-second evidence now consumed by P5M8. Normalized E12 telemetry is A=`RESERVE_ENTRY->FINAL_BATON`, B=`FINAL_BATON->END`, C=`RESERVE_ENTRY->END`.

## P5M6 — Same-invocation auto-refill

State: PROMOTED DEFAULT after independent LW24 + LW25 multi-package repeats
Parent: P5M5 value-gated work shaping with bounded persistence routing
Primary variable: AUTO_REFILL_WITHIN_SAME_TURN
Core invariant: `PACKAGE_COMPLETE != TURN_COMPLETE`

### Promoted defaults retained
- 30–36 eligible-unit pre-shaped packages are per-package capacity guidance, not an invocation cap or wall-time guarantee.
- VALUE_GATED_TARGET_SELECTION is the default target selector.
- BOUNDED THIN_ELIGIBLE routing applies to reconstructible audit/decision work; FULL_CHAIN applies to authoritative mutation, newly persisted decision evidence, or representation-dependent validation.
- Exactly one final recurring scheduler mutation and practical +3m lead.
- GitHub START/END server timestamps are the only WORKED clock.

### Auto-refill contract
A current TO-DO/package is the queue head, not an invocation cap. When a substantive package completes, immediately reassess the parent GOAL and unresolved durable state. If useful goal-directed work remains, derive the next concrete package and execute it in the SAME invocation. Persist one compact combined package-result/refill record for recovery; do not write redundant package END + refill records and do not mutate the scheduler at refill boundaries.

Valid turn-stop conditions are only PROGRAM_COMPLETE, genuine external blocker with no useful independent work, runtime/safety limit, or evidence-based exhaustion of useful work. Package completion, TO-DO exhaustion, artifact/test completion, checkpoint creation, semantic-output quota, or scheduler preparation are not stop conditions.

### Anti-gaming and recovery
Fast completion means spare capacity. Refill with useful work; never sleep, pad, repeat converged analysis, fabricate defects, split bullets artificially, or create low-value artifacts merely to increase elapsed time or package count.

`NEXT_PACKAGE` is a recovery pointer, not an unconditional cold-start command. Cold recovery revalidates current authoritative state before side effects. Generic per-package START markers are not required because attempted execution does not prove committed effects; unsafe replay targets require effect-level stable identity/receipt or an equivalently strong checkpoint.

### Promotion evidence
LW24 completed 11 substantive packages / 36 semantic outputs in one invocation with one final scheduler mutation. LW25 independently repeated 7 substantive packages / 25 semantic outputs and hardened stale-NEXT cold recovery. AUTO_REFILL is promoted within these tested conditions.

---

## P5M5 — Value-gated work shaping with bounded persistence optimization
P5M5 promoted bounded thinning after LW21 and LW22 independent positive samples with zero omitted-boundary defects, while retaining FULL_CHAIN for authoritative mutation and representation-dependent validation.

## P5M4 — Scalable Large TO-DO package evidence
P5M4 established that 30–36 eligible-unit packages can raise semantic capacity without extra scheduler mutations. LW18 promoted the range after 34/34, 16 outputs=4.71/10 under frozen counting. LW19/LW20 then promoted value-gated target selection at 5.29/10. Wall time remained non-monotonic; package size is not a duration guarantee.

## P4V11 — GitHub server timestamp work-duration source of truth
State: APPLIED
- Append unique START_MARKER immediately before substantive work and matching END_MARKER after all substantive work and allowed final scheduler update.
- `WORKED = END_MARKER.created_at - START_MARKER.created_at` using GitHub server timestamps only.
- Model/local time strings are display-only; missing/ambiguous marker pair means WORKED=UNKNOWN.

## Promoted hot-path invariants retained
- Same automation identity; no new automation for normal continuation.
- One final recurring RRULE scheduler write on normal path.
- Issue #1 compact tail is routine bootstrap; broader documents are cold-path unless substantive evidence/boundary/recovery requires them.
- Wake, scheduler write/state, useful work, semantic density, persistence cost, refill count, reserve timing, and WORKED remain distinct observations.
- Simplicity is preferred only after recovery and duplicate-safety equivalence is established.

## Historical note
Earlier P0–P4 variants established the single-final-write recurring path, compact Issue evidence, Issue-tail bootstrap, conditional verification, positive-field omission, jitter telemetry, and GitHub-server WORKED clock. Detailed historical evidence remains in Issue #1 and experiment ledger.
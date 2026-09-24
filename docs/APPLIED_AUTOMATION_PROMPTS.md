# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M7 — Auto-refill with directional finalization reserve

State: APPLIED / E12 BASELINE ACTIVE
Parent: promoted P5M6 same-invocation auto-refill
Primary variable: FINALIZATION_RESERVE_POLICY

### Contract
AUTO_REFILL remains default: `PACKAGE_COMPLETE != TURN_COMPLETE`. Elapsed time is used only as a safety/finalization admission signal. At substantive package boundaries, compare an external clock with GitHub START server time. The first E12 baseline predeclares a conservative 240-second cutoff for starting a NEW substantive package. Once reached, preserve exact remainder, write final baton, perform the sole scheduler mutation, and append END. Do not sleep, pad, or interrupt an active validation merely to hit the cutoff.

Prior successful final-baton -> END envelopes are 23s (LW24) and 25s (LW25), measured from GitHub server timestamps. They are sparse evidence, not a safe minimum. One E12 sample cannot promote or shrink the reserve.

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
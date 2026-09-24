# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M6 — Same-invocation auto-refill

State: APPLIED / FIRST MULTI-PACKAGE SAMPLE ACTIVE
Parent: P5M5 value-gated work shaping with bounded persistence routing
Primary variable: AUTO_REFILL_WITHIN_SAME_TURN
Core invariant: `PACKAGE_COMPLETE != TURN_COMPLETE`

### Promoted defaults retained
- 30–36 eligible-unit pre-shaped packages for semantic capacity+density within tested conditions; no wall-time guarantee.
- VALUE_GATED_TARGET_SELECTION as default target selector.
- BOUNDED THIN_ELIGIBLE routing for reconstructible audit/decision work; FULL_CHAIN for authoritative mutation, newly persisted decision evidence, or representation-dependent validation.
- Exactly one final recurring scheduler mutation and practical +3m lead.
- GitHub START/END server timestamps are the only WORKED clock.

### Auto-refill contract
A current TO-DO/package is the queue head, not an invocation cap. When a substantive package completes, immediately reassess the parent GOAL and unresolved durable state. If useful goal-directed work remains, derive the next concrete package and execute it in the SAME invocation. Persist a compact `REFILL_BOUNDARY` for recovery, but do not mutate the scheduler at refill boundaries.

Valid turn-stop conditions are only:
1. PROGRAM_COMPLETE — parent goal actually completed and validated.
2. GENUINE_EXTERNAL_BLOCKER — no useful independent goal-directed work can proceed.
3. RUNTIME_OR_SAFETY_LIMIT — runtime/tool/safety constraint prevents safe continuation.
4. NO_USEFUL_WORK_REMAINS — evidence-based reassessment finds no non-redundant goal-directed work.

Package completion, TO-DO exhaustion, one artifact/test completion, checkpoint creation, semantic-output quota, or scheduler preparation are explicitly not turn-stop conditions.

### Anti-gaming
Fast completion means spare capacity. Refill with useful work; never sleep, pad, repeat converged analysis, fabricate defects, split bullets artificially, or create low-value artifacts merely to increase elapsed time or package count.

### Refill durability
Each refill boundary records completed package, key result, cumulative useful outputs, and next substantive package. It is a recovery checkpoint only. The in-memory TO-DO may refill repeatedly. The persisted automation prompt/schedule changes exactly once at actual invocation end.

### Persistence router retained
Target value and persistence mode are separate gates. FULL_CHAIN fresh-fetch review tests persisted representation against predeclared criteria. THIN_ELIGIBLE requires authoritative named durable inputs, exact reconstructibility, semantic review, explicit `OMITTED_BOUNDARY_DEFECT`, and source reads counted as artifact I/O. Thin audit may decide a mutation is required; mutation then escalates to FULL_CHAIN. Any defect attributable to an omitted candidate boundary rolls back that thin class.

### First-sample validation
A valid first P5M6 sample must demonstrate at least one completed substantive package followed by a second substantive package in the same invocation while useful work remains. Track `PACKAGES_COMPLETED`, cumulative semantic outputs, refill-boundary I/O, artifact I/O, control I/O, and GitHub-server WORKED separately. One successful sample is directional only; repeat before promotion.

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
- Wake, scheduler write/state, useful work, semantic density, persistence cost, refill count, and WORKED remain distinct observations.
- Simplicity is preferred only after recovery and duplicate-safety equivalence is established.

## Historical note
Earlier P0–P4 variants established the single-final-write recurring path, compact Issue evidence, Issue-tail bootstrap, conditional verification, positive-field omission, jitter telemetry, and GitHub-server WORKED clock. Detailed historical evidence remains in Issue #1 and experiment ledger.
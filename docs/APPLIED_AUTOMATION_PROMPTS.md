# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M11 — AUTO_REFILL + bounded fixed-3 coalescing

State: APPLIED / ACTIVE
Parent: P5M10 270s cutoff repeat/value gate
Primary variables: fixed-3 package-boundary coalescing; cross-invocation receipt recovery semantics

### Active contract
- `PACKAGE_COMPLETE != TURN_COMPLETE`; current TO-DO is queue head, not invocation cap.
- VALUE_GATED_TARGET_SELECTION; bounded THIN_ELIGIBLE for reconstructible audit/decision work; FULL_CHAIN for authoritative mutation/representation-dependent validation.
- Routine recovery uses bounded Issue #1 tail retrieval; no second mutable CURRENT pointer.
- Exactly one final recurring scheduler mutation at actual invocation end; practical +3m lead.
- GitHub START/END server `created_at` is the only WORKED clock.
- 270s is the scoped TESTED new-package admission cutoff after repeated LW32/LW33 safety plus LW33 direct incremental-value evidence. 260s remains tested fallback. Do not chase a runtime ceiling without new value evidence.
- Fixed `n=3` shared-recovery-fate reconstructible groups may use one coalesced package boundary after all nodes validate. Cross-invocation recovery with no persisted node outputs is confirmed.
- A fixed-3 group containing exactly one authoritative/idempotent mutation is eligible only under `docs/COALESCING_PROTOCOL.md`: stable effect identity/canonical payload, authoritative durable receipt/result over the replay horizon, receipt reconciliation, FULL_CHAIN unchanged, and all nodes validated. Unreceipted/non-idempotent/multiple-effect groups and larger/adaptive groups remain unpromoted.
- Receipt decision surface: COMMITTED; proof-bearing AUTHORITATIVE_NOT_FOUND as retry-eligibility only; UNKNOWN otherwise. UNKNOWN never authorizes replay under the currently promoted conservative contract.
- Negative proof has a causal boundary: after any effect attempt, pre-attempt AUTHORITATIVE_NOT_FOUND cannot determine post-attempt commit status. LW40 cold-confirmed this across invocations.
- Conservative real-effect retry requires a durable attempt/intent boundary before effect emission unless target authority atomically supplies equivalent stable attempt/effect identity and reconciliation semantics. Missing receipt never proves non-execution. Generic local emission markers are not authoritative commit evidence.

### Efficiency accounting
For reconstructible fixed-3 groups, package boundaries reduce 3->1 (66.7%). For effectful groups, required receipt and any mandatory attempt/intent durability are effect-level evidence and are never counted as removable package-boundary I/O. Report package-boundary writes and total durable writes separately. A retry path with separate attempt-intent+receipt is 5 total writes baseline versus 3 coalesced (40% total reduction), while package-boundary reduction remains 66.7%.

## P5M10 — AUTO_REFILL 270s repeat/value gate

State: SUPERSEDED BY P5M11 / 270S SCOPED TESTED CUTOFF
Parent: P5M9 260s repeat

LW32 and LW33 independently finalized safely at predeclared 270s. LW33 admitted a useful package from a +264s boundary that 260s would have rejected, providing direct incremental-value evidence. 270s was therefore promoted only within current relay/finalization conditions; cutoff step-down stopped afterward.

## P5M9 — AUTO_REFILL 260s repeat

State: SUPERSEDED / 260S TESTED FALLBACK

LW30 and LW31 independently finalized safely at 260s. 260s was promoted as scoped TESTED cutoff before the separate 270s value-gated trial. Earlier unaudited semantic cumulative counters remain rejected.

## P5M8 — AUTO_REFILL 250s controlled step-down

State: HISTORICAL / 250S TESTED

LW28/LW29 independently finalized safely at 250s. This established the first tested step-down beyond the 240s conservative repeat.

## P5M7 — AUTO_REFILL directional reserve

State: HISTORICAL / 240S CONSERVATIVE_REPEAT_CONFIRMED

LW26/LW27 supplied repeated safe 240s evidence.

## P5M6 — Same-invocation AUTO_REFILL

State: PROMOTED DEFAULT
Core invariant: `PACKAGE_COMPLETE != TURN_COMPLETE`

LW24/LW25 independently established multi-package same-invocation refill with one final scheduler mutation and cold NEXT revalidation. Valid stop conditions are PROGRAM_COMPLETE, genuine external blocker with no independent useful work, runtime/safety limit, or evidence-based exhaustion of useful work. Package/checkpoint/quota completion is not a stop condition.

## P5M5 — Value-gated work shaping + bounded persistence

State: PROMOTED DEFAULT

VALUE_GATED_TARGET_SELECTION is default. THIN_ELIGIBLE applies only to reconstructible audit/decision work; FULL_CHAIN remains mandatory for authoritative mutation or representation-dependent validation.

## P5M4 — Large package shaping

State: HISTORICAL GUIDANCE

30–36 eligible units is tested per-package capacity guidance, never an invocation cap or wall-time quota. Wall time is non-monotonic and padding is forbidden.

## P4V11 — GitHub server timestamp work-duration source of truth

State: PROMOTED DEFAULT

Append unique START_MARKER immediately before substantive work and matching END_MARKER after the sole final scheduler update. `WORKED = END_MARKER.created_at - START_MARKER.created_at`. Model/local time strings are display-only; missing/ambiguous marker pair means WORKED=UNKNOWN.

## Promoted hot-path invariants retained
- Same automation identity; never create another automation for normal continuation.
- One final recurring RRULE scheduler write on normal path.
- Issue #1 compact bounded tail is routine bootstrap; broader documents are cold-path unless substantive evidence/boundary/recovery requires them.
- Wake, scheduler state, useful work, semantic density, persistence cost, refill count, reserve timing, and WORKED remain distinct observations.
- Simplicity is preferred only after recovery and duplicate-safety equivalence is established.

## Historical note
Earlier P0–P4 variants established the single-final-write recurring path, compact Issue evidence, Issue-tail bootstrap, conditional verification, positive-field omission, jitter telemetry, and GitHub-server WORKED clock. Detailed historical evidence remains in Issue #1 and experiment ledger.

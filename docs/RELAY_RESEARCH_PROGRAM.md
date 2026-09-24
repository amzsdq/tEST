# Relay Research Program v1.0

Status: ACTIVE — work-shaping, bounded persistence, AUTO_REFILL, scoped 270s admission cutoff, bounded Issue #1 tail retrieval, and fixed-3 coalescing promoted within tested classes
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that keeps a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, remains recoverable after missed wakes, and avoids duplicate execution?

## Experiment families
E1 RRULE self-shift; E2 minimum lead-time; E3 mutation stress; E4 provisional/final relay; E5 missed-wake recovery; E6 cross-automation wake; E7 duplicate authority; E8 durable cold-resume; E9 useful-work/package shaping; E10 persistence-boundary optimization; E11 same-invocation auto-refill; E12 invocation-tail/finalization reserve; E13 fixed-group package-boundary coalescing and effect-receipt recovery.

## Promotion principle
Repeated evidence is required. One favorable trace is directional only. Claims are scoped to the layer tested. Wall time is telemetry, never a work quota. Safety promotion and useful-value promotion are separate gates when a more aggressive setting increases risk/complexity.

## Canonical current pointer
Routine recovery uses the bounded Issue #1 tail, not a second mutable CURRENT mirror. Start from prior-baton inclusive `since`, paginate saturated windows, and fall back to fresh count/final-page plus successive pages when completeness is ambiguous. Authority is determined by live lineage, created ordering, and explicit corrections; `since` is update-sensitive and `updated_at` alone is not authority. Full history is forensic fallback.

## Promoted work-shaping stack
- E9: 30–36 eligible units is tested per-package capacity guidance, not invocation cap. VALUE_GATED_TARGET_SELECTION is default.
- E10: THIN_ELIGIBLE is promoted for reconstructible audit/decision work; FULL_CHAIN remains mandatory for authoritative mutation or representation-dependent validation.
- E11: AUTO_REFILL is promoted. `PACKAGE_COMPLETE != TURN_COMPLETE`; exactly one scheduler mutation occurs at actual invocation end; cold NEXT is revalidated before side effects.
- Endpoint-only boundary-document reconciliation: live pending endpoint stays in Issue #1; boundary docs are reconciled after evidence-complete classification, not inside the finalization critical path.

## E12 — Invocation-tail / finalization reserve
Elapsed time controls admission of NEW substantive packages only. It never justifies sleeping, padding, or interrupting an already-validating package.

Evidence summary:
- LW26/LW27 cutoff 240s safe; 240s conservative repeat-confirmed.
- LW28/LW29 cutoff 250s safe; 250s promoted as scoped TESTED cutoff.
- LW30/LW31 cutoff 260s safe; 260s promoted as scoped TESTED cutoff.
- LW32/LW33 cutoff 270s repeated safe. LW33 uniquely admitted useful work from a +264s boundary that 260s would have rejected, satisfying the incremental-value gate. 270s is the current scoped TESTED admission cutoff.
- Cutoff chasing stops at 270s absent new evidence that a further step-down has useful expected value. This is not a universal runtime ceiling.

### E12 frozen constraints
- GitHub server START/END timestamps are the WORKED clock.
- Check external elapsed at substantive package admission boundaries, not every action.
- Reserve protects exact remainder + final baton + one scheduler mutation + END.
- Normalize A=`RESERVE_ENTRY->FINAL_BATON`, B=`FINAL_BATON->END`, C=`RESERVE_ENTRY->END`, D=`last admitted boundary->reserve entry`.
- Cutoff controls admission, not interruption. PACKAGE_OVERRUN alone is non-adverse unless continuation is lost.
- Do not add adaptive cutoff or class-specific guards from sparse tails.
- 260s remains tested fallback if later 270s evidence becomes adverse.

## E13 — Fixed-group package-boundary coalescing
Goal: reduce durable package-boundary writes without weakening recovery/effect safety.

Promoted scope:
- fixed `n=3` shared-recovery-fate reconstructible groups: one coalesced package boundary after all nodes validate; cross-invocation cold recovery confirmed.
- fixed `n=3` containing exactly one authoritative/idempotent mutation only under `docs/COALESCING_PROTOCOL.md`: stable effect identity + canonical payload, authoritative durable receipt/result over the replay horizon, FULL_CHAIN unchanged, and receipt reconciliation before retry.

Evidence summary:
- LW34 baseline 3 boundaries/3 audited outputs vs candidate 1/3; 66.7% package-boundary reduction with equivalent recovery/remainder.
- LW35 cross-invocation reconstructible recovery with no persisted node outputs.
- LW36 independently receipted mutation cold repeat.
- LW37 unavailable receipt authority -> UNKNOWN/no replay/no COMPLETE.
- LW38 UNKNOWN later resolved by COMMITTED -> no replay; remaining validation still required.
- LW39 proof-bearing AUTHORITATIVE_NOT_FOUND -> retry eligibility only; ordinary/expired/incomplete negative evidence -> UNKNOWN.
- LW40 cold-confirmed causal consumption: after an effect attempt, old negative proof cannot determine post-attempt commit status; absent fresh authority => UNKNOWN. Follow-up crash-window analysis requires a durable pre-effect attempt/intent boundary for the conservative retry contract unless target authority atomically supplies equivalent semantics.

Scope limits:
- fixed n=3 only; no adaptive/larger groups promoted.
- unreceipted/non-idempotent and multiple-effect groups are not promoted.
- mandatory effect receipt and any mandatory pre-effect attempt/intent evidence are effect-level durability, not removable package-boundary I/O.
- a generic local emission marker is not authoritative evidence of external commit and is not added by default.

## Metrics
Primary: continuation success, duplicate substantive execution, useful-work duty cycle, recovery latency, audited semantic useful outputs per invocation (or UNKNOWN). Secondary: scheduler mutations per useful-work minute, control overhead, artifact I/O per audited semantic output, packages per invocation, refill success, finalization success, D and normalized A/B/C tails. For effectful coalescing report package-boundary writes separately from total durable writes including mandatory effect-level evidence.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` as first queue head, not invocation cap. Issue #1 remains durable authority. In-memory queue may refill repeatedly; only actual end-of-turn automation mutation writes next persisted TO-DO and schedule.

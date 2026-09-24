# Relay Research Program v0.9

Status: ACTIVE — work-shaping, bounded persistence routing, same-invocation auto-refill promoted; E12 finalization reserve optimizing
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that keeps a ChatGPT Automation workload progressing for long periods with high useful-work duty cycle, remains recoverable after missed wakes, and avoids duplicate execution?

## Experiment families
E1 RRULE self-shift; E2 minimum lead-time; E3 mutation stress; E4 provisional/final relay; E5 missed-wake recovery; E6 cross-automation wake; E7 duplicate authority; E8 durable cold-resume; E9 useful-work/package shaping; E10 persistence-boundary optimization; E11 same-invocation auto-refill; E12 invocation-tail/finalization reserve.

## Promotion principle
Repeated evidence is required. One favorable trace is directional only. Claims are scoped to the layer tested. Wall time is telemetry, never a work quota.

## Canonical current pointer
Routine recovery uses Issue #1 compact tail. Broaden only for ambiguity, reconciliation, or substantive artifact work. No second mutable current-state mirror by default.

## Promoted work-shaping stack
- E9: 30–36 eligible units is tested per-package capacity guidance, not invocation cap. VALUE_GATED_TARGET_SELECTION is default after LW19/LW20.
- E10: THIN_ELIGIBLE is promoted for reconstructible audit/decision work; FULL_CHAIN remains mandatory for authoritative mutation or representation-dependent validation.
- E11: AUTO_REFILL is promoted after LW24/LW25. `PACKAGE_COMPLETE != TURN_COMPLETE`; exactly one scheduler mutation occurs at actual invocation end; cold NEXT is revalidated before side effects.

## E12 — Invocation-tail / finalization reserve
Elapsed time controls admission of NEW substantive packages only. It never justifies sleeping, padding, or interrupting an already-validating package.

Evidence:
- LW26 cutoff 240s: A/B/C=22/31/53s, safe.
- LW27 cutoff 240s: A/B/C=13/21/34s, safe. 240s=`CONSERVATIVE_REPEAT_CONFIRMED`.
- LW28 cutoff 250s: A/B/C=11/26/37s, safe with package overrun.
- LW29 cutoff 250s: A/B/C=8/17/25s, WORKED=282s, safe with one scheduler write. Independent LW28+LW29 evidence promotes 250s as a TESTED CUTOFF within current relay/finalization conditions. Prior running semantic-output cumulative labels are not treated as audited throughput evidence.
- LW30 cutoff 260s: D=8s, A/B/C=9/13/22s, WORKED=286s, one scheduler write, continuation safe. Semantic outputs remain UNKNOWN_PENDING_AUDIT. This is directional evidence only.
- LW31: independent predeclared 260s repeat active. 260s remains unpromoted until this repeat safely commits continuation.

### E12 frozen constraints
- GitHub server START/END timestamps are the WORKED clock.
- Check external elapsed time at substantive package admission boundaries, not every action.
- Reserve protects exact remainder + final baton + one scheduler mutation + END.
- Normalize A=`RESERVE_ENTRY->FINAL_BATON`, B=`FINAL_BATON->END`, C=`RESERVE_ENTRY->END`, D=`last admitted boundary->reserve entry`.
- Cutoff controls admission, not D after admission. `PACKAGE_OVERRUN` is not failure unless continuation is lost.
- Track packages admitted after +200s by admission -> next validated-boundary exposure; telemetry does not alter the live cutoff.
- Future step-down decisions review D and C jointly; a short C cannot hide a long post-admission D.
- Do not add class-specific admission guards without repeated same-class long-tail evidence; do not add global per-action polling absent demonstrated need.
- Adverse/ambiguous 260s finalization rolls back to tested 250s. 240s remains older conservative fallback only if a shared-mode defect invalidates 250 evidence.
- Never infer a fixed runtime ceiling from near-300s traces.

## Metrics
Primary: continuation success, duplicate substantive execution, useful-work duty cycle, recovery latency, audited semantic useful outputs per invocation (or UNKNOWN). Secondary: scheduler mutations per useful-work minute, control overhead, artifact I/O per audited semantic output, packages per invocation, refill success, finalization success, D and normalized A/B/C tails.

## External benchmark layer
`docs/EXTERNAL_CASE_STUDIES.md` supplies invariants/adverse-test ideas, never proof of ChatGPT Automation behavior.

## Hot-path execution pointer
Use `TO-DO LIST FOR THIS TURN` as first queue head, not invocation cap. Issue #1 remains durable authority. In-memory queue may refill repeatedly; only actual end-of-turn automation mutation writes next persisted TO-DO and schedule.
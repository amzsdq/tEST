# Relay Optimization Convergence Protocol v0.8

Status: P5M11 AUTO_REFILL + scoped 270s cutoff + fixed-3 coalescing ACTIVE

## Objective
Converge to the smallest relay policy that maximizes semantic useful work while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state. Longer wall-clock time is diagnostic only; fast completion exposes spare capacity for more useful work.

## Evidence classes
- SEMANTIC_OUTPUT: validated rule/spec/decision with auditable OUTPUT_ID / DURABLE_CHANGE / DOWNSTREAM_CONSEQUENCE / VALIDATED_BY; otherwise UNKNOWN.
- ARTIFACT_IO: persistence/fetch required by a real dependency or review boundary.
- CONTROL_IO: scheduler mutations, markers, baton/checkpoint writes, verification-only control reads.
- EFFECT_EVIDENCE_IO: mandatory effect receipt/result and any mandatory durable attempt/intent evidence. Never count this as removable package-boundary I/O.
- WALL_TIME: GitHub-server END_MARKER.created_at - START_MARKER.created_at.
- RESERVE_TAIL: D=last admitted boundary->reserve entry; A=reserve entry->final baton; B=final baton->END; C=reserve entry->END.

## Controlled convergence
Freeze baseline; change one primary variable; repeat samples; separate WRITE_OK/STATE_OK/WAKE_OK/WORK_OK; measure semantic outputs independently from artifact/control/effect-evidence I/O and WALL_TIME. A claim about one layer is NON_COMPARABLE if another causal layer changes without normalization.

## Eligibility / anti-gaming
Every added work unit needs downstream value, substantive uncertainty, or a real correction need and a discriminating result. Reject filler, sleep, redundant summaries/reads, fake defects, or units created only to enlarge elapsed time/package count.

## Persistence / coalescing gate
FULL_CHAIN applies when authoritative mutation or representation-dependent validation is decision-relevant. THIN_ELIGIBLE applies only to reconstructible audit/decision work.

Fixed-3 package-boundary coalescing is promoted only for shared-recovery-fate work under `docs/COALESCING_PROTOCOL.md`. Compare package-boundary writes per audited output separately from total durable writes. Required effect receipt and pre-effect attempt/intent evidence are safety evidence, not coalescing overhead to erase. Larger/adaptive groups, multiple-effect groups, and unreceipted/non-idempotent effects remain unpromoted.

## Package / AUTO_REFILL rules
30–36 eligible units is per-package guidance, not invocation cap. `PACKAGE_COMPLETE != TURN_COMPLETE`: completion triggers parent-goal reassessment and same-invocation refill while useful work remains. Exactly one scheduler mutation occurs at actual invocation end. Cold NEXT is revalidated before side effects.

## E12 finalization-reserve convergence
A cutoff controls admission of a NEW substantive package only. It is not a hard interruption deadline. Promotion requires repeated safe continuation and, once risk/complexity increases, demonstrated useful-work value.

Current boundary: 240s repeated safe -> 250s tested -> 260s tested -> 270s repeated safe plus LW33 unique useful admission from +264s boundary. 270s is the scoped TESTED cutoff. 260s remains tested fallback. Cutoff chasing stops absent new value evidence; never infer a universal runtime ceiling.

## Receipt/retry convergence
For the currently promoted conservative one-mutation fixed-3 contract:
1. reconcile authoritative receipt before retry;
2. COMMITTED suppresses replay but does not skip remaining node validation;
3. proof-bearing AUTHORITATIVE_NOT_FOUND grants retry eligibility only;
4. unavailable/ambiguous/ordinary missing/expired/incomplete/drifted evidence => UNKNOWN;
5. UNKNOWN does not authorize replay;
6. any effect attempt causally consumes pre-attempt negative proof for later commit-status decisions;
7. when that causal boundary is needed for a real effect, durable attempt/intent must precede effect emission unless target authority atomically supplies equivalent semantics;
8. generic local emission markers are not authoritative proof of external commit.

A possible narrower optimization — safe same-key retry from UNKNOWN under a target authority that itself guarantees idempotent replay/result reconciliation — is hypothesis-only until independently tested. Do not weaken the promoted conservative rule from synthetic assumption alone.

## Promotion / rollback
- Scheduler/control: repeated WAKE_OK/WORK_OK, no duplicate-authority violation, relevant recovery evidence.
- Work shaping: repeated semantic/downstream-value gain under unchanged scheduler/control.
- Persistence/coalescing: same audited work graph, recovery equivalence, no weaker effect evidence, material package-boundary reduction, bounded replay exposure.
- AUTO_REFILL: repeated multi-package work when useful work remains, no padding, one final scheduler mutation.
- Reserve cutoff: repeated safe continuation plus useful incremental value when moving to a more aggressive boundary.

Rollback immediately on duplicate substantive side effects, lost recurring fallback, stale-authority overwrite, unrecoverable durable state, omitted-boundary defect, manufactured low-value refill work, unsafe receipt inference, or reserve policy that loses continuation.

## Decision record
Record PRIMARY_VARIABLE, COMPARABILITY, CUTOFF when active, SCHEDULER_WRITES, PACKAGES_COMPLETED, SEMANTIC_OUTPUTS(audited or UNKNOWN), PACKAGE_BOUNDARY_WRITES, TOTAL_DURABLE_WRITES when meaningful, WORKED, D/A/B/C when active, EVIDENCE, DECISION, STOP_REASON, NEXT.

## Current long-work rule
Dynamic TO-DO is queue head, not invocation cap. Issue #1 bounded tail remains routine durable authority. Value gate ranks work; persistence/coalescing mode is separately gated; package completion refills while useful work remains; reserve admission protects final continuation. Do not infer reasoning depth from elapsed time.

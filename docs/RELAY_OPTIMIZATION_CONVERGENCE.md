# Relay Optimization Convergence Protocol v0.6

Status: P5M9 AUTO-REFILL + E12 FINALIZATION-RESERVE OPTIMIZATION ACTIVE

## Objective
Converge to the smallest relay policy that maximizes semantic useful work while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state. Longer wall-clock time is diagnostic only; fast completion exposes spare capacity for more useful work.

## Evidence classes
- SEMANTIC_OUTPUT: validated rule/spec/decision with named downstream consequence.
- ARTIFACT_IO: persistence/fetch required by real dependency or review boundary.
- CONTROL_IO: scheduler mutations, markers, baton/checkpoint writes, verification-only control reads.
- REFILL_IO: compact same-invocation recovery checkpoints between substantive packages.
- WALL_TIME: GitHub-server END_MARKER.created_at - START_MARKER.created_at.
- RESERVE_TAIL: D=last admitted boundary->reserve entry; A=reserve entry->final baton; B=final baton->END; C=reserve entry->END.

## Controlled convergence
Freeze baseline; change one primary variable; repeat samples; separate WRITE_OK/STATE_OK/WAKE_OK/WORK_OK; measure semantic outputs independently from artifact/control/refill I/O and WALL_TIME. A claim about one layer is NON_COMPARABLE if another causal layer changes without normalization.

Causal layers include package size, packages-per-invocation/refill, target ranking, persistence mode, semantic counting, scheduler/control, lead time, and finalization-reserve admission cutoff.

## Eligibility / anti-gaming
Every added work unit needs downstream value, substantive uncertainty or real correction need, and a discriminating result. Reject filler, sleep, redundant summaries/reads, fake defects, or units created only to enlarge elapsed time/package count.

## Persistence gate
FULL_CHAIN applies when newly persisted representation is decision-relevant, source-of-truth mutation occurs, or representation drift is material. THIN_ELIGIBLE applies only to reconstructible audit/decision work with named durable evidence and no omitted-boundary defect. Source reads remain ARTIFACT_IO.

## Package / auto-refill rules
30–36 eligible units is promoted per-package semantic-capacity guidance, not invocation cap or wall-time guarantee. `PACKAGE_COMPLETE != TURN_COMPLETE`: package completion triggers immediate parent-goal reassessment and same-invocation refill while useful work remains. Exactly one scheduler mutation occurs at actual invocation end. Cold `NEXT_PACKAGE` is revalidated before side effects.

## E12 finalization-reserve convergence
A cutoff controls admission of a NEW substantive package only. It is not a hard interruption deadline and does not bound D after admission. `PACKAGE_OVERRUN` is evidence, not failure unless continuation is lost.

Frozen method:
1. predeclare cutoff before live substantive work;
2. check external time at package admission boundaries only;
3. do not tune cutoff during the run;
4. on reserve entry preserve exact remainder, write final baton, perform sole scheduler mutation, append END;
5. normalize D/A/B/C from GitHub-server evidence;
6. one safe step-down is DIRECTIONAL only;
7. promotion requires an independent repeat at the same frozen cutoff with safe continuation;
8. adverse/ambiguous step-down rolls back to the latest independently repeated safe cutoff;
9. add class-specific admission guards only after repeated same-class long-tail evidence; do not globally poll per action absent demonstrated need;
10. never infer a universal runtime ceiling from sparse near-limit traces.

Current evidence: 240s repeated safe in LW26/LW27; 250s repeated safe in LW28/LW29 and is TESTED within current conditions; 260s is active directional LW30 and requires repeat before promotion.

## Promotion / rollback
- Scheduler/control: repeated WAKE_OK/WORK_OK, no duplicate-authority violation, relevant recovery evidence.
- Work shaping: repeated semantic/downstream-value gain under unchanged scheduler/control.
- Persistence thinning: repeated thin-eligible targets, no omitted-boundary defect, non-inferior quality, lower candidate-boundary I/O.
- Auto-refill: repeated >=2 substantive packages/invocation when work remains, no padding, one final scheduler mutation, useful-output gain without recovery regression.
- Reserve cutoff: repeated safe continuation at frozen cutoff; wall time alone never promotes.

Rollback immediately on duplicate substantive side effects, lost recurring fallback, stale-authority overwrite, unrecoverable durable state, omitted-boundary defect, manufactured low-value refill work, or reserve policy that loses continuation.

## Decision record
Record PRIMARY_VARIABLE, COMPARABILITY, LEAD_TIME, CUTOFF when active, SCHEDULER_WRITES, PACKAGES_COMPLETED, UNITS, SEMANTIC_OUTPUTS, ARTIFACT_IO, REFILL_IO, CONTROL_IO, WORKED, D/A/B/C when active, PACKAGE_OVERRUN, EVIDENCE, DECISION, STOP_REASON, NEXT.

## Current long-work rule
Dynamic top-of-prompt TO-DO is first queue head, not invocation cap. Issue #1 remains durable authority. Value gate ranks eligible work; persistence mode is separately gated; package completion refills while useful work remains; reserve admission protects final continuation. Do not infer reasoning depth from elapsed time.
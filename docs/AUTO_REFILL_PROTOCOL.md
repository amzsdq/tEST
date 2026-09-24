# Same-Invocation Auto-Refill Protocol

Status: PROMOTED DEFAULT; scoped 270s finalization-reserve admission cutoff active

## Core invariant
`PACKAGE_COMPLETE != TURN_COMPLETE`. Package completion is a refill trigger, not invocation completion. Refill useful work immediately while value/safety gates pass. Normal scheduler mutation occurs exactly once at actual invocation end.

## Refill transition
After a package validates, persist one compact combined package-result/refill boundary, reassess parent GOAL, select the next value-gated substantive package, and execute it in the same invocation. Never mutate scheduler at refill boundaries.

## Valid stop conditions
PROGRAM_COMPLETE; genuine external blocker with no independent useful work; runtime/tool/safety limit; evidence-based NO_USEFUL_WORK_REMAINS. TO-DO/checkpoint/package completion is not a stop condition. Padding/sleep/redundant work is invalid.

## Eligibility and recovery
VALUE_GATED_TARGET_SELECTION remains active. THIN_ELIGIBLE is limited to reconstructible audit/decision work; authoritative mutation or representation-dependent validation remains FULL_CHAIN. Cold recovery revalidates live authority/value/persistence gates before side effects. Generic UNKNOWN never authorizes replay.

## Finalization reserve
At substantive package admission boundaries compare GitHub server time against invocation START. Current scoped TESTED new-package admission cutoff is 270s; 260s is tested fallback. The cutoff stops admission of a NEW substantive package only and never interrupts active validation. On reserve entry preserve exact remainder, append final baton, perform the sole scheduler mutation, then append END.

Evidence:
- 240s repeated safe LW26/LW27.
- 250s repeated safe LW28/LW29.
- 260s repeated safe LW30/LW31.
- 270s repeated safe LW32/LW33; LW33 admitted useful work from a +264s boundary that 260s would have rejected, satisfying the incremental-value gate. Therefore 270s is promoted only within current relay/finalization conditions. No further cutoff step-down absent new value evidence.

Telemetry remains D=last admitted boundary->reserve entry, A=reserve entry->final baton, B=final baton->END, C=reserve entry->END. Package overrun is not adverse by itself if exact continuation is preserved.

## Boundary-document authority/freshness
Live pending endpoint remains in Issue #1. Boundary documents are reconciled after evidence-complete classification, not inside the finalization critical path. Later explicit live correction/baton/evidence governs operational NEXT; fresh narrow contracts govern their scope absent later rollback; stale broad summaries cannot roll back later evidence. If a repair write is blocked, persist the exact dirty remainder in Issue authority and keep stale text non-authoritative. Do not add a second mutable CURRENT/cache pointer.

## Coalescing interaction
Fixed n=3 reconstructible shared-recovery-fate coalescing is promoted under `docs/COALESCING_PROTOCOL.md`. Effectful groups retain mandatory effect evidence. Conservative retry uses durable pre-effect attempt/intent plus authoritative receipt reconciliation. Exact-fingerprint target-native exception may omit the separate relay attempt-intent only under its full adapter/provenance contract; generic UNKNOWN retry remains forbidden.

## Invocation metrics
Record PACKAGES_COMPLETED, audited semantic outputs, PACKAGE_BOUNDARY_WRITES, RELAY_CONTROLLED_DURABLE_WRITES, GitHub-server WORKED, STOP_REASON, exact NEXT/REMAINDER, and scheduler writes. Provider-internal opaque persistence is excluded from relay-controlled write accounting.

## Semantic-output accounting
Count an output only with unique OUTPUT_ID, DURABLE_CHANGE, DOWNSTREAM_CONSEQUENCE, and VALIDATED_BY; bookkeeping/style summaries count zero.

## Rollback
Narrow/reject on duplicate effects, stale-authority overwrite, lost recovery state, extra scheduler mutations, material quality regression, counter inflation, or systematic low-value work. Runtime saturation alone is not failure when exact recovery state is preserved.
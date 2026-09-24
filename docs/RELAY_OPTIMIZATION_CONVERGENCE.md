# Relay Optimization Convergence Protocol v0.9

Status: P5M11 AUTO_REFILL + scoped 270s cutoff + fixed-3 coalescing ACTIVE

## Objective
Converge to the smallest relay policy that maximizes semantic useful work while preserving continuation reliability, crash recovery, duplicate prevention, recurring fallback, and inspectable durable state.

## Authority / freshness
Operational NEXT is governed by explicit later live Issue correction/baton/evidence. A narrow contract governs only its proven scope when version/evidence is fresh and no later live rollback conflicts. Broad summary/registry/program documents require freshness checks and cannot roll back later evidence by omission or stale text. Ambiguous same-scope freshness => UNKNOWN/no semantic mutation until broadened reconciliation. Decision-boundary repair remainder is persisted in Issue authority; do not add a second mutable CURRENT/cache pointer.

## Evidence / convergence
SEMANTIC_OUTPUT requires OUTPUT_ID / DURABLE_CHANGE / DOWNSTREAM_CONSEQUENCE / VALIDATED_BY. Separate ARTIFACT_IO, CONTROL_IO, EFFECT_EVIDENCE_IO, and WALL_TIME. Freeze baseline; change one primary variable; repeat samples; separate WRITE_OK/STATE_OK/WAKE_OK/WORK_OK. Reject filler, sleep, redundant reads, fake defects, and work created only to enlarge elapsed time.

## Persistence / coalescing
FULL_CHAIN applies when authoritative mutation or representation-dependent validation is decision-relevant. THIN_ELIGIBLE applies only to reconstructible audit/decision work. Fixed-3 package-boundary coalescing is promoted only for shared-recovery-fate work under `docs/COALESCING_PROTOCOL.md`. Required effect receipt and pre-effect attempt/intent evidence are safety evidence, not removable package-boundary overhead. Larger/adaptive groups, multiple-effect groups, and unreceipted/non-idempotent effects remain unpromoted.

## AUTO_REFILL / reserve
30–36 eligible units is per-package guidance, not invocation cap. `PACKAGE_COMPLETE != TURN_COMPLETE`; refill while useful work remains. Exactly one scheduler mutation occurs at actual invocation end. Cold NEXT is revalidated before side effects. Current admission boundary: 270s scoped TESTED cutoff; 260s tested fallback. Cutoff chasing stops absent new value evidence.

## Receipt/retry convergence
Conservative fixed-3 contract: reconcile authoritative receipt before retry; COMMITTED suppresses replay but remaining nodes still validate; proof-bearing AUTHORITATIVE_NOT_FOUND grants retry eligibility only; unavailable/ambiguous/ordinary missing/expired/incomplete/drifted evidence => UNKNOWN; UNKNOWN does not authorize replay; any effect attempt consumes pre-attempt negative proof; durable attempt/intent precedes real effect unless target authority supplies independently proven equivalent semantics; local emission markers are not authoritative external commit proof.

`TARGET_NATIVE_IDEMPOTENCY_ELIGIBLE` is PROMOTED at adapter capability level after LW42-LW48 only for an exact fresh concrete fingerprint under `docs/TARGET_NATIVE_IDEMPOTENCY_ADAPTER.md`. It is not a generic UNKNOWN-retry rule. Stable key and attempt-time fingerprint provenance must be cold-reconstructible from preexisting durable/versioned or target-native authority without a new dedicated per-attempt relay write for the modeled 3->2 write saving to remain. Pre-emission eligibility and post-emission recovery are distinct; duplicate suppression and authoritative result reconciliation are separate gates. Synthetic adapter permutation sub-line is converged absent a concrete adapter/use-case/new discriminating failure.

## Promotion / rollback
Promote only on repeated layer-appropriate evidence. Roll back on duplicate substantive side effects, lost recurring fallback, stale-authority overwrite, unrecoverable durable state, omitted-boundary defect, manufactured low-value refill work, unsafe receipt inference, or reserve policy that loses continuation.

## Current long-work rule
Dynamic TO-DO is queue head, not invocation cap. Issue #1 bounded tail remains routine durable authority. Value gate ranks work; persistence/coalescing mode is separately gated; package completion refills while useful work remains; reserve admission protects final continuation. GitHub START/END created_at is the WORKED clock.

# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

## P5M11 — AUTO_REFILL + bounded fixed-3 coalescing
State: APPLIED / ACTIVE

### Active contract
- `PACKAGE_COMPLETE != TURN_COMPLETE`; current TO-DO is queue head, not invocation cap.
- VALUE_GATED_TARGET_SELECTION; bounded persistence; bounded Issue #1 tail retrieval; no second mutable CURRENT/eligibility pointer.
- Exactly one final recurring scheduler mutation at actual invocation end; practical +3m lead.
- GitHub START/END server `created_at` is the only WORKED clock.
- 270s is the scoped TESTED new-package admission cutoff; 260s remains tested fallback.
- Fixed `n=3` shared-recovery-fate reconstructible groups may use one coalesced package boundary after all nodes validate.
- Effectful fixed-3 groups follow `docs/COALESCING_PROTOCOL.md`. Conservative retry requires durable pre-effect attempt/intent plus authoritative receipt reconciliation; generic UNKNOWN never authorizes replay.
- Adapter-level `TARGET_NATIVE_IDEMPOTENCY_ELIGIBLE` is allowed only for an exact fresh concrete fingerprint with stable cold-recoverable key, canonical payload, authority ID/scope, explicit protection horizon, authoritative result-reconciliation domain, and cold-reconstructible attempt-time fingerprint provenance. Provider-wide `idempotent=true` is insufficient.
- Pre-emission eligibility and post-emission recovery are distinct. After a possibly emitted native attempt, stale/current fingerprint drift never means no attempt; unresolved result state remains no-replay/no-COMPLETE.
- Native write-elision value is retained only when key and attempt-time provenance derive from preexisting durable/versioned or target-native authority without a new dedicated per-attempt relay write. Otherwise write-saving value is zero.
- Eligibility is derived state, not a persisted cache/pointer.

### Authority/freshness precedence
- Later explicit live Issue correction/baton/evidence governs operational NEXT.
- A narrow contract governs its scope only when freshness/version/evidence are proven and no later live rollback conflicts.
- Broad summary/registry/program documents require freshness checks and cannot roll back later evidence by omission or stale text.
- Same-scope ambiguous freshness/lineage => UNKNOWN/no semantic mutation. Missing fields in an otherwise nonconflicting broad document are not negative evidence.
- Blocked repair persists an exact repair remainder in Issue authority; it never promotes stale text.

### Efficiency accounting
Reconstructible fixed-3 package boundaries reduce 3->1 (66.7%). Mandatory effect evidence is not removable package-boundary I/O. Conservative effectful coalescing uses group boundary + attempt-intent + receipt/result = 3 relay-controlled records for the coalesced attempt; an eligible native exception can use group boundary + authoritative result/reconciliation = 2, saving exactly one relay-controlled durable write. Provider-internal persistence is excluded.

## Retained historical guidance
- P5M10/LW32-LW33 established the scoped 270s cutoff and direct incremental value over 260s.
- P5M9 260s remains tested fallback; P5M8 250s and P5M7 240s are older tested points.
- P5M6 established same-invocation AUTO_REFILL.
- P5M5 established value-gated work shaping and bounded persistence.
- P4V11 established GitHub server timestamps as the WORKED source of truth.

## Hot-path invariants
Same automation identity; one final recurring RRULE scheduler write; Issue #1 bounded-tail bootstrap; wake/state/work/persistence metrics remain distinct; simplicity only after recovery/duplicate-safety equivalence is established.
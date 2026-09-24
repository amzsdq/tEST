# Relay Research Program v1.1

Status: ACTIVE — AUTO_REFILL, scoped 270s admission cutoff, bounded Issue #1 tail retrieval, fixed-3 coalescing, and scoped target-native idempotency exception promoted within tested classes
Repository: `amzsdq/tEST`

## Research question
What is the simplest relay mechanism that sustains high useful-work duty cycle, cold recovery, and duplicate safety while minimizing scheduler/control/persistence overhead?

## Promotion principle
Repeated evidence is required; claims remain scoped to the tested layer. Safety and value are separate gates. Wall time is telemetry, never a work quota.

## Authority and current-state recovery
Routine recovery uses bounded Issue #1 tail retrieval, not a second mutable CURRENT mirror. Later explicit live correction/baton/evidence governs operational NEXT. Fresh narrow contracts govern their scope absent later live rollback. Broad summaries/program/registry docs require freshness and cannot roll back later evidence merely by omission/stale text. Ambiguous same-scope lineage => UNKNOWN/no semantic mutation. Blocked document repair leaves an exact Issue repair remainder.

## Promoted stack
- VALUE_GATED_TARGET_SELECTION and bounded persistence.
- AUTO_REFILL: `PACKAGE_COMPLETE != TURN_COMPLETE`; one scheduler mutation only at actual invocation end.
- GitHub START/END `created_at` is the WORKED clock.
- 270s scoped TESTED new-package admission cutoff; 260s tested fallback. No cutoff chasing absent new value evidence.
- Fixed n=3 reconstructible shared-recovery-fate coalescing with one boundary after all nodes validate.
- Effectful fixed-3 coalescing under conservative receipt/retry contract in `docs/COALESCING_PROTOCOL.md`.
- Bounded Issue #1 tail retrieval; no second mutable CURRENT pointer.

## E13 — fixed-group coalescing and effect recovery
Evidence progression:
- LW34-LW35: reconstructible fixed-3 boundary reduction 3->1 and cross-invocation recovery without persisted node outputs.
- LW36-LW40: authoritative receipt recovery; UNKNOWN no-replay; proof-bearing negative evidence only as retry-eligibility; any effect attempt consumes pre-attempt negative proof; conservative real-effect retry requires durable pre-effect attempt/intent unless target authority supplies equivalent semantics.
- LW41B: durable attempt-intent -> synthetic emission -> COMMITTED receipt cold-recovered with exact identity binding and no replay.
- LW42-LW46: target-native idempotency promoted only as an adapter-level exception under exact fresh operation fingerprint; generic UNKNOWN retry remained forbidden. Duplicate suppression and authoritative original-result reconciliation are separate gates. The native exception reduces relay-controlled coalesced effect records from 3 to 2 only when stable key derives from preexisting durable identity without a new write.
- LW47-LW48: pre-emission eligibility and post-emission recovery separated. Native write-elision additionally requires cold-reconstructible attempt-time fingerprint provenance across the legitimate reconciliation horizon; missing provenance or expired/ambiguous authority => no replay/no COMPLETE. Synthetic adapter permutation sub-line converged absent a concrete adapter/use-case/new discriminating failure.
- LW49: document-authority precedence cold-confirmed against natural stale broad-document drift; stale summaries cannot roll back later scoped evidence.

Scope limits:
- fixed n=3 only; no adaptive/larger/multiple-effect groups promoted.
- provider-wide `idempotent=true` is insufficient.
- target-native eligibility is derived from concrete fingerprint, not persisted as a second mutable cache.
- generic UNKNOWN never authorizes replay.

## E12 — finalization reserve
270s is the current scoped TESTED new-package admission cutoff after repeated safe LW32/LW33 evidence and direct incremental value over 260s. 260s remains tested fallback. Cutoff controls admission only; active validation may overrun. Reserve protects exact remainder + final baton + sole scheduler mutation + END. No sleeping/padding.

## Metrics
Continuation success, duplicate execution, useful-work duty cycle, recovery latency, audited outputs, package-boundary writes, relay-controlled durable writes, scheduler mutations, refill success, and GitHub-server WORKED. Provider-internal opaque persistence is not counted as relay-controlled I/O.

## Hot-path pointer
`TO-DO LIST FOR THIS TURN` is queue head, not invocation cap. Issue #1 remains durable live authority; boundary documents are reconciled at evidence-complete decision boundaries, with exact dirty remainder persisted if repair is blocked.
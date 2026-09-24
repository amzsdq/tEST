# Target-Native Idempotency Adapter Contract

Status: PROMOTED at adapter capability level after LW42 positive cold reconstruction, LW43 adverse repeat, LW44 contract-freshness/result-domain repeat, LW45 fingerprint invalidation repeat, and LW46 independent state-machine cold reconstruction. This is not a generic UNKNOWN-retry rule.

## Purpose
A target-native idempotency contract may substitute for the relay's separate durable pre-effect attempt/intent only when it independently supplies equivalent duplicate-suppression and recovery semantics and doing so has material relay-controlled write value.

## Eligibility fingerprint
Every decision must bind to a fresh, concrete fingerprint:
- provider
- operation
- API/contract version
- authority identity
- authority scope
- stable idempotency-key derivation identity
- canonical payload equivalence rule
- explicit protection/reconciliation horizon
- authoritative result-reconciliation domain

Provider-brand-level `idempotent=true` is insufficient. Any decision-relevant stale, unverifiable, or drifted field invalidates cached eligibility until freshly re-proven. Eligibility is derived state; do not add a second mutable eligibility pointer or persistent cache merely to avoid revalidation.

## Emission policy
There are two top-level effect-emission policies.

1. `DEFAULT_CONSERVATIVE`: fingerprint false, stale, or ambiguous. Establish durable pre-effect attempt/intent before a real effect and reconcile authoritative receipt/result afterward. Generic UNKNOWN never authorizes replay.
2. `TARGET_NATIVE_EXCEPTION`: exact fresh fingerprint true, stable key cold-recoverable from preexisting durable identity without a new dedicated write, canonical payload equivalent, protection horizon valid, and authoritative result-reconciliation domain supported. A separate relay attempt-intent may be omitted; use the protected native retry/reconciliation contract and still validate remaining fixed-3 nodes before group COMPLETE.

`PROTECTED_RETRY_RESULT_UNKNOWN` is a recovery outcome inside the native branch, not a third emission policy. Duplicate suppression without authoritative result reconciliation prevents duplicate effect but does not prove COMMITTED and does not authorize group COMPLETE.

## Required behavior
`TARGET_NATIVE_IDEMPOTENCY_ELIGIBLE` requires all fingerprint fields to be fresh and stable, the key to be cold-recoverable from preexisting durable logical identity without a new dedicated pre-send persistence write, canonical payload equivalence to hold, the protection horizon to cover retry, and authoritative result reconciliation to be supported.

Generic UNKNOWN remains no-replay. Duplicate suppression and authoritative result reconciliation are separate gates. If duplicate suppression is protected but the original authoritative result cannot be reconciled, classify `PROTECTED_RETRY_RESULT_UNKNOWN`; do not infer COMMITTED and do not complete the coalesced group.

## Fail-closed matrix
- current operation/version contract cannot be freshly revalidated -> `UNKNOWN_NOT_PROTECTED`; before emission use conservative durable-attempt path.
- authority scope or idempotency semantics drift -> `NOT_ELIGIBLE` until full predicate is freshly proven.
- same key with canonical-payload drift -> `REJECT`.
- key regenerated/ephemeral -> `NOT_ELIGIBLE`.
- protection horizon unproven, pruned, or expired -> `UNKNOWN_NOT_PROTECTED`.
- duplicate suppression protected but authoritative result domain unavailable/ambiguous -> `PROTECTED_RETRY_RESULT_UNKNOWN`; no group COMPLETE.
- stable key requires a new dedicated persistence write -> `SAFETY_ELIGIBLE_BUT_NO_WRITE_SAVING`; reject/defer as write-elision optimization unless another material benefit is separately demonstrated.

Do not use conservative fallback after an already-protected native attempt as evidence that no effect occurred. Post-attempt ambiguity remains at result reconciliation until the exact attempted effect is safely resolved.

## Value accounting
For an eligible effectful fixed-3 attempt, relay-controlled durable records are modeled as:
- `DEFAULT_CONSERVATIVE`: 3 = group boundary + durable attempt-intent + authoritative receipt/result.
- `TARGET_NATIVE_EXCEPTION`: 2 = group boundary + authoritative result/reconciliation evidence.
- saving: exactly 1 relay-controlled durable record per eligible attempt.

Provider-internal opaque persistence is excluded. Never claim provider persistence disappeared. If a new dedicated key write is required, native-path relay write count returns to 3 and write-elision value is zero. Do not add persistent eligibility/cache state that consumes the saved write unless a separate material benefit is proven.

## Official-contract observations used in tests
Stripe documents replay of the first saved status/body for a given idempotency key, parameter-equivalence checking, and possible key pruning after at least 24 hours. Amazon EC2 documents client-token idempotency for supported operations, same-token/same-parameter duplicate suppression, and operation-specific Regional/Zonal scope for RunInstances; retry results may contain updated state. These differences are why result reconciliation and authority scope are explicit adapter fields rather than provider-wide assumptions.

## Evidence
- LW42: frozen positive/negative cold reconstruction; adapter-level capability promoted; generic UNKNOWN retry rejected.
- LW43: independent adverse repeat for horizon, scope, key, payload, and positive control.
- LW44: independent cold repeat for contract freshness, semantics drift, result-domain ambiguity, zero-write-saving key persistence, and positive control.
- LW45: exact fingerprint invalidation/result-domain repeat retained capability only for fresh concrete fingerprints.
- LW46: independent cold reconstruction reproduced conservative/native/result-unknown paths and 3->2 relay-controlled write model without predicate edits; promoted two emission policies and derived eligibility with no second mutable pointer.

## Scope
No real payment/cloud effect was executed in these experiments. Promotion is a contract/recovery capability classification. Real target adapters must independently validate their exact operation/version contract before use.
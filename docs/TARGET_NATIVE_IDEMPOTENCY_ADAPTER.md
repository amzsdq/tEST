# Target-Native Idempotency Adapter Contract

Status: PROMOTED at adapter capability level after LW42 positive cold reconstruction, LW43 independent adverse repeat, and LW44 contract-freshness/result-domain cold repeat. This is not a generic UNKNOWN-retry rule.

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

Provider-brand-level `idempotent=true` is insufficient. Any decision-relevant stale, unverifiable, or drifted field invalidates cached eligibility until freshly re-proven.

## Required behavior
`TARGET_NATIVE_IDEMPOTENCY_ELIGIBLE` requires all fingerprint fields to be fresh and stable, the key to be cold-recoverable from preexisting durable logical identity without a new dedicated pre-send persistence write, canonical payload equivalence to hold, the protection horizon to cover retry, and authoritative result reconciliation to be supported.

Generic UNKNOWN remains no-replay. Duplicate suppression and authoritative result reconciliation are separate gates. If duplicate suppression is protected but the original authoritative result cannot be reconciled, classify `PROTECTED_RETRY_RESULT_UNKNOWN`; do not infer COMMITTED and do not complete the coalesced group.

## Fail-closed matrix
- current operation/version contract cannot be freshly revalidated -> `UNKNOWN_NOT_PROTECTED`; use conservative durable-attempt path.
- authority scope or idempotency semantics drift -> `NOT_ELIGIBLE` until full predicate is freshly proven.
- same key with canonical-payload drift -> `REJECT`.
- key regenerated/ephemeral -> `NOT_ELIGIBLE`.
- protection horizon unproven, pruned, or expired -> `UNKNOWN_NOT_PROTECTED`.
- duplicate suppression protected but authoritative result domain unavailable/ambiguous -> `PROTECTED_RETRY_RESULT_UNKNOWN`; no group COMPLETE.
- stable key requires a new dedicated persistence write -> `SAFETY_ELIGIBLE_BUT_NO_WRITE_SAVING`; reject/defer as write-elision optimization unless another material benefit is separately demonstrated.

## Value accounting
Report relay-controlled durable writes separately from provider-internal opaque persistence. Never claim provider persistence disappeared. If target-native eligibility removes a separate relay attempt-intent write because the stable key already derives from durable identity, count that relay write saving explicitly. If a new key write is required, write-saving value is zero.

## Official-contract observations used in tests
Stripe documents replay of the first saved status/body for a given idempotency key, parameter-equivalence checking, and possible key pruning after at least 24 hours. Amazon EC2 documents client-token idempotency for supported operations, same-token/same-parameter duplicate suppression, and operation-specific Regional/Zonal scope for RunInstances; retry results may contain updated state. These differences are why result reconciliation and authority scope are explicit adapter fields rather than provider-wide assumptions.

## Evidence
- LW42: frozen positive/negative cold reconstruction; adapter-level capability promoted; generic UNKNOWN retry rejected.
- LW43: independent adverse repeat for horizon, scope, key, payload, and positive control.
- LW44: independent cold repeat for contract freshness, semantics drift, result-domain ambiguity, zero-write-saving key persistence, and positive control; all five reproduced without predicate edits.

## Scope
No real payment/cloud effect was executed in these experiments. Promotion is a contract/recovery capability classification. Real target adapters must independently validate their exact operation/version contract before use.
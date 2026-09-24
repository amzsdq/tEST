# Package-Boundary Coalescing Protocol

Status: PROMOTED for the tested fixed-3 reconstructible class and for the narrow independently-receipted mutation-containing class described below. Reconstructible cold recovery was confirmed in LW35; mutation-containing cold repeat was independently confirmed in LW36; LW37 added cross-invocation fail-closed evidence for unavailable receipt authority; LW38 confirmed UNKNOWN->COMMITTED cold recovery; LW39 confirmed proof-bearing AUTHORITATIVE_NOT_FOUND as retry-eligibility only; LW40 cold-confirmed causal consumption of pre-attempt negative proof and narrowed the real-effect contract with a durable pre-effect attempt boundary.

## Purpose
Reduce durable package-boundary I/O without weakening crash recovery or effect safety.

## Eligible class
A fixed 3-node group may use one package boundary when all nodes share recovery fate and are reconstructible audit/decision work. Recovery input must be immutable by identity/version/hash or explicitly revalidated for semantic equivalence. All nodes must validate before group COMPLETE. Temporal adjacency alone is insufficient.

A fixed 3-node group containing exactly one authoritative/idempotent mutation is eligible only under the tested receipt contract: stable effect identity bound to canonical payload; authoritative receipt/result independently durable through the full legitimate replay/reconciliation horizon; receipt reconciliation before retry; FULL_CHAIN validation strength unchanged; all three nodes share recovery fate and validate before group COMPLETE. Unreceipted/non-idempotent effects remain NOT_ELIGIBLE.

## Durable boundary
Persist one record containing `PACKAGE_GROUP_ID`, ordered `NODE_IDS`, `INPUT_IDENTITY_OR_REVALIDATION_RULE`, audited `OUTPUTS` (`OUTPUT_ID`, durable decision/change, downstream consequence, validation evidence), `RESULT`, exact `NEXT/REMAINDER`, and `TURN_COMPLETE`.

Per-node START/END/package checkpoints are not required for an eligible group. Required effect-level receipt/result evidence remains independently durable and is never removed by package-boundary coalescing.

## Recovery
Before group boundary: recover from prior authoritative baton plus stable/revalidated input and reconstruct the group. After group boundary: resume exact NEXT. A missing package boundary never proves an external effect did not occur.

Mutable input requires decision-relevant semantic-equivalence revalidation for the whole grouped surface. If it fails, the old group is stale/uncommitted and work is re-derived from current authority; do not mix input eras.

## Effect safety and receipt decision surface
Never coalesce across an unreceipted non-idempotent effect. Same effect identity with a different canonical payload is rejected. Receipt/result evidence must cover the full legitimate replay/reconciliation horizon.

- `COMMITTED`: authoritative payload-bound receipt/result proves the effect committed. Reconcile result, suppress replay, then still validate remaining group nodes before COMPLETE.
- `AUTHORITATIVE_NOT_FOUND`: retry is only `ELIGIBLE_TO_CONSIDER`, and only when effect+canonical-payload binding, authority identity/scope, lookup completeness, and retention across the full legitimate replay/reconciliation horizon are all freshly valid. It does not execute or imply an effect and does not advance group NEXT.
- `UNKNOWN`: unavailable, transiently unreachable, ambiguous, ordinary missing/404/empty without completeness proof, expired retention, incomplete authority, authority/payload drift without proven semantic equivalence, or otherwise insufficient evidence. UNKNOWN never authorizes effect replay or group COMPLETE; exact remainder stays at receipt reconciliation until safe resolution.

`AUTHORITATIVE_NOT_FOUND` has a causal validity boundary in addition to a retention horizon. Once an effect attempt occurs, the pre-attempt negative proof is stale for subsequent commit-status decisions even if its retention date has not expired. A fresh post-attempt authoritative receipt lookup is mandatory before another retry or group advancement. LW40 confirmed this rule across an invocation boundary with no persisted node outputs: proof-before-attempt plus attempt-without-post-attempt-receipt recovered as UNKNOWN, with no replay and no group/NEXT advancement.

For a real effect, causal consumption must itself survive a crash. Therefore an attempt/intent identity must be durably established before effect emission whenever recovery relies on that boundary to invalidate prior negative proof. An after-the-fact attempt marker is insufficient because a crash after effect emission but before marker persistence makes the old negative proof appear fresh. A target-specific atomic authority may substitute only if it provides equivalent stable effect/attempt identity and reconciliation semantics. This is effect-level safety evidence, not removable package-boundary I/O.

Target-specific retry state machine:
1. Revalidate effect identity + canonical payload + authority identity/scope + completeness + retention + causal freshness.
2. UNKNOWN -> block replay and retain receipt-reconciliation remainder.
3. AUTHORITATIVE_NOT_FOUND -> effect retry may be considered.
4. Before actual effect emission, durably establish the attempt/intent boundary unless an atomic target-specific authority supplies equivalent semantics.
5. Invoke the target-specific idempotent effect using the same stable effect identity/canonical payload.
6. After any effect attempt -> require fresh authoritative receipt/result. Old negative proof is consumed for commit-status purposes.
7. COMMITTED -> suppress replay, reconcile authoritative result, validate remaining fixed-3 nodes, then group COMPLETE/exact NEXT.

Crash-split behavior for the tested contract:
- before durable attempt boundary: no effect may have been emitted by this state machine; a still-valid proof-bearing AUTHORITATIVE_NOT_FOUND may retain retry eligibility;
- after durable attempt boundary / before effect or receipt: recovery is UNKNOWN until fresh target authority resolves; do not infer non-execution from absence of a receipt;
- after effect / before group boundary: COMMITTED receipt returns authoritative result and suppresses duplicate application; unavailable/ambiguous evidence remains UNKNOWN;
- after group boundary: resume exact NEXT from coalesced boundary.

## Persistence routing and efficiency
Coalescing changes package-boundary frequency, not evidence strength. THIN_ELIGIBLE reconstructible audit/decision work is the default candidate. FULL_CHAIN authoritative mutation keeps full representation-dependent validation; a later shared package boundary is allowed only under the promoted receipt contract.

An independently durable effect receipt is required effect-level evidence and is not removable package-boundary I/O. Mandatory durable attempt/intent evidence on retry paths is likewise effect-level evidence unless atomically supplied by the target authority. Report package-boundary writes and total durable writes separately, including all mandatory effect-level evidence. The simple first-attempt modeled fixed-3 mutation graph without an additional separate attempt-intent write remains baseline 3 package boundaries + 1 required receipt = 4 writes versus coalesced 1 boundary + same receipt = 2 writes. Do not reuse that 50% total-write figure for retry paths that require an additional durable attempt boundary.

## Validation failure
Any node validation failure leaves the group uncommitted. Partial conclusions are not group COMPLETE and exact NEXT/REMAINDER does not advance past the failed node. If an independently receipted effect already committed, recovery reconciles that receipt while reconstructing the otherwise uncommitted group.

## Observability and replay cost
Coalescing trades fine durable per-node progress localization for bounded replay of at most fixed 3 eligible nodes. Do not reintroduce generic durable per-node START/END solely for observability. If a failure becomes non-reconstructible or externally effectful outside the tested receipt contract, it exits the eligible class and requires target-specific durable evidence.

## Authority separation
Issue #1 compact live baton remains routine relay/recovery authority. Protocol and SHADOW/SYNTHETIC records are contract/evidence inputs and do not independently advance live NEXT. A shadow record cannot override a conflicting live baton absent explicit later authoritative correction.

## Evidence
LW34: fixed-3 baseline 3 boundaries/3 audited outputs; candidate and repeat 1/3 with equivalent recovery/exact remainder (66.7% package-boundary reduction).
LW35: true cross-invocation reconstructible recovery with no persisted node outputs.
LW36: fresh-effect cross-invocation one-mutation receipt repeat.
LW37: unavailable-authority cold differential -> UNKNOWN/no replay/no COMPLETE.
LW38: prior UNKNOWN later resolved by exact payload-bound COMMITTED receipt; no replay; remaining validation still required.
LW39: proof-bearing complete-authority/full-horizon AUTHORITATIVE_NOT_FOUND cold probe -> retry eligibility only; ordinary/expired/incomplete negative evidence -> UNKNOWN.
LW40: cross-invocation causal-consumption probe -> pre-attempt AUTHORITATIVE_NOT_FOUND became unusable for post-attempt commit status; no post-attempt receipt => UNKNOWN/no replay/no COMPLETE. Follow-up crash-window analysis requires durable attempt/intent before real effect emission unless equivalent semantics are atomic in target authority.

## Scope limit
Only fixed `n=3` shared-recovery-fate groups are promoted. Mutation-containing groups are eligible only with exactly one authoritative/idempotent mutation satisfying the full receipt contract above. Larger/adaptive batching, multiple-effect groups, unreceipted effects, and non-idempotent effects are not promoted. Do not expand scope merely for additional write savings without independent safety/value evidence.

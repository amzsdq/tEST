# Package-Boundary Coalescing Protocol

Status: PROMOTED for the tested fixed-3 reconstructible class and for the narrow independently-receipted mutation-containing class described below. Reconstructible cold recovery was confirmed in LW35; mutation-containing cold repeat was independently confirmed in LW36; LW37 added cross-invocation fail-closed evidence for unavailable receipt authority.

## Purpose
Reduce durable package-boundary I/O without weakening crash recovery or effect safety.

## Eligible class
A fixed 3-node group may use one package boundary when all nodes share recovery fate and are reconstructible audit/decision work. Recovery input must be immutable by identity/version/hash or explicitly revalidated for semantic equivalence. All nodes must validate before group COMPLETE. Temporal adjacency alone is not shared recovery fate; unrelated recovery authorities/effects must not be grouped merely to reduce writes.

A fixed 3-node group containing exactly one authoritative/idempotent mutation is also eligible only under the tested receipt contract: stable effect identity bound to the canonical payload; authoritative receipt/result independently durable through the full legitimate replay/reconciliation horizon; receipt reconciliation before retry; FULL_CHAIN validation strength unchanged; all three nodes share recovery fate and validate before group COMPLETE. Unreceipted/non-idempotent effects remain NOT_ELIGIBLE.

## Durable boundary
Persist one record containing: `PACKAGE_GROUP_ID`, ordered `NODE_IDS`, `INPUT_IDENTITY_OR_REVALIDATION_RULE`, audited `OUTPUTS` (`OUTPUT_ID`, durable decision/change, downstream consequence, validation evidence), `RESULT`, exact `NEXT/REMAINDER`, and `TURN_COMPLETE`.

Per-node START/END/package checkpoints are not required for an eligible group. Required effect-level receipt/result evidence remains independently durable and is never removed by package-boundary coalescing.

## Recovery
Before group boundary: recover from the prior authoritative baton plus stable/revalidated input and deterministically reconstruct the group. After group boundary: resume exact NEXT. A missing package boundary never proves an external effect did not occur.

LW35 cross-invocation shadow probe intentionally persisted no node outputs after conceptual N2. The next invocation reconstructed N1/N2 from frozen input identity plus this protocol, completed N3, preserved decisions/exact-remainder semantics, required no effect replay, and added no scheduler mutation.

If mutable input is used, revalidation must establish decision-relevant semantic equivalence for the whole grouped decision surface. If that fails, the old group is uncommitted/stale and work is re-derived from current authority; do not mix input eras inside one recovered group.

## Effect safety
Never coalesce across an unreceipted non-idempotent effect. For the promoted narrow mutation class, recovery looks up stable effect identity before retry and reconciles authoritative receipt/result state. Same identity with a different canonical payload is rejected. Receipt/result evidence must cover the full legitimate replay/reconciliation horizon.

Minimal receipt decision surface:
- `COMMITTED`: authoritative payload-bound receipt/result proves the effect committed; reconcile the recorded result and suppress replay.
- `AUTHORITATIVE_NOT_FOUND`: retry may be considered only when the receipt authority guarantees lookup completeness and retention across the entire legitimate replay/reconciliation horizon for that effect identity.
- `UNKNOWN`: unavailable, transiently unreachable, ambiguous, missing without completeness proof, expired, or otherwise insufficient receipt evidence. UNKNOWN never authorizes effect replay and never authorizes group COMPLETE; exact remainder stays at receipt reconciliation until authority can be re-established or a target-specific safe resolution exists.

Crash-split behavior for the tested contract:
- before effect: stable idempotency identity permits at most one committed effect for canonical payload;
- after effect / before group boundary: COMMITTED receipt returns the same authoritative result and suppresses duplicate application;
- after group boundary: resume exact NEXT from coalesced boundary.

LW35 supplied directional positive/negative evidence. LW36 independently repeated with fresh effect identity and durable receipt fixture, no persisted group-node outputs, and all three crash splits. LW37 independently exercised `RECEIPT_LOOKUP=UNAVAILABLE_TRANSIENT`, `COMMIT_STATUS=UNKNOWN`, again with no persisted group-node outputs: recovery classified UNKNOWN, did not replay the modeled effect, did not mark the group COMPLETE, and retained exact remainder at receipt reconciliation. This strengthens the scoped contract but does not broaden effect classes.

## Persistence routing
Coalescing changes package-boundary frequency, not evidence strength. THIN_ELIGIBLE reconstructible audit/decision work is the default candidate. FULL_CHAIN authoritative mutation keeps full representation-dependent validation; a later shared package boundary is allowed only under the promoted receipt contract.

An independently durable effect receipt is required effect-level evidence and is not counted as removable package-boundary I/O. For effectful groups report two denominators separately: package-boundary writes and total durable writes. In the modeled fixed-3 mutation graph, baseline is 3 package boundaries + 1 required receipt = 4 writes; coalesced is 1 boundary + the same receipt = 2 writes. Thus package-boundary reduction is 66.7% while total durable-write reduction is 50%.

## Validation failure
Any node validation failure leaves the group uncommitted. Partial node conclusions are not promoted as group COMPLETE, and exact NEXT/REMAINDER does not advance past a failed node. If an independently receipted effect already committed, recovery reconciles that receipt while reconstructing the otherwise uncommitted group.

## Observability and replay cost
Coalescing deliberately trades fine durable per-node progress localization for bounded replay of at most the fixed 3-node eligible group. Do not reintroduce generic durable per-node START/END solely for observability. Ordinary live diagnostics may be ephemeral because correctness is reconstructible from prior authority. If a failure becomes non-reconstructible or externally effectful outside the tested receipt contract, it exits the eligible class and requires target-specific durable evidence.

## Authority separation
Issue #1 compact live baton remains routine relay/recovery authority. Protocol and SHADOW/SYNTHETIC records are contract/evidence inputs and do not independently advance live NEXT. A shadow test record cannot override a conflicting live baton absent an explicit later authoritative correction.

## Evidence
LW34 fixed 3-node baseline: 3 durable package boundaries / 3 audited outputs. Candidate and independent repeat: 1 boundary / 3 audited outputs, with equivalent recovery and exact remainder. Boundary-write reduction: 66.7%.

LW35 added true cross-invocation reconstructible recovery with no persisted node outputs. LW36 independently repeated the one-mutation receipt contract with fresh effect identity and receipt. LW37 added an unavailable-authority negative cold differential proving fail-closed UNKNOWN semantics without replay or group completion.

## Scope limit
Only fixed `n=3` shared-recovery-fate groups are promoted. Reconstructible audit/decision work is eligible under stable/revalidated inputs. Mutation-containing groups are eligible only when they contain exactly one authoritative/idempotent mutation satisfying the full receipt contract above. Larger/adaptive batching, multiple-effect groups, unreceipted effects, and non-idempotent effects are not promoted. Do not expand scope merely for additional write savings without independent safety/value evidence.

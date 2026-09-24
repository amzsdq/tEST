# Package-Boundary Coalescing Protocol

Status: PROMOTED for the tested eligible reconstructible class (P5M11 / LW34), with cross-invocation cold-recovery confirmation in LW35.

## Purpose
Reduce durable package-boundary I/O without weakening crash recovery or effect safety.

## Eligible class
A fixed 3-node group may use one package boundary when all nodes share recovery fate and are reconstructible audit/decision work. Recovery input must be immutable by identity/version/hash or explicitly revalidated for semantic equivalence. All nodes must validate before group COMPLETE. Temporal adjacency alone is not shared recovery fate; unrelated recovery authorities/effects must not be grouped merely to reduce writes.

## Durable boundary
Persist one record containing: `PACKAGE_GROUP_ID`, ordered `NODE_IDS`, `INPUT_IDENTITY_OR_REVALIDATION_RULE`, audited `OUTPUTS` (`OUTPUT_ID`, durable decision/change, downstream consequence, validation evidence), `RESULT`, exact `NEXT/REMAINDER`, and `TURN_COMPLETE`.

Per-node START/END/package checkpoints are not required for this eligible class. The current fields are retained because each has a distinct recovery/audit role; byte-level field shaving does not reduce the one-record write count.

## Recovery
Before group boundary: recover from the prior authoritative baton plus stable/revalidated input and deterministically reconstruct the group. After group boundary: resume exact NEXT. A missing package boundary never proves an external effect did not occur.

LW35 cross-invocation shadow probe `LW35-COALESCE-COLD-R1` intentionally persisted no node outputs after conceptual N2. The next invocation reconstructed N1/N2 from the frozen input identity plus this protocol, completed N3, preserved the promoted decisions/exact-remainder semantics, required no effect replay, and added no scheduler mutation. This strengthens the reconstructible-class promotion beyond same-turn simulated recovery.

If mutable input is used, revalidation must establish decision-relevant semantic equivalence for the whole grouped decision surface. If that fails, the old group is uncommitted/stale and work is re-derived from current authority; do not mix input eras inside one recovered group.

## Effect safety
Never coalesce across an unreceipted non-idempotent effect. An authoritative/idempotent mutation may participate only when stable effect identity plus authoritative durable receipt/result independently survives package-boundary loss and the full legitimate replay/reconciliation horizon. Recovery reconciles that receipt before retry. If the receipt is missing, expired, or ambiguous before that horizon, the mutation is not coalescing-eligible unless equivalent authoritative result state was durably captured earlier. The receipt/idempotency authority must bind the stable effect identity to the same canonical payload or reject same-identity/different-payload reuse.

LW35 synthetic/shadow directional evidence for one independently receipted idempotent mutation passed crash splits before effect, after effect/before group boundary, and after group boundary. Negative differentials confirmed fail-closed NOT_ELIGIBLE when receipt status is ambiguous, receipt/result retention is shorter than the legitimate recovery horizon, or payload binding is not authoritative. This mutation-containing class remains DIRECTIONAL_ONLY until independently repeated; it is not yet promoted as a default eligible class.

## Persistence routing
Coalescing changes package-boundary frequency, not evidence strength. THIN_ELIGIBLE reconstructible audit/decision work is the default candidate. FULL_CHAIN authoritative mutation keeps full representation-dependent validation; a later shared package boundary is allowed only when effect identity/receipt is independently durable and explicitly reconciled.

An independently durable effect receipt is required effect-level evidence and is not counted as removable package-boundary I/O. For effectful groups report two denominators separately: package-boundary writes and total durable writes. In the modeled fixed-3 mutation graph, baseline is 3 package boundaries + 1 required receipt = 4 writes; coalesced is 1 boundary + the same receipt = 2 writes. Thus package-boundary reduction is 66.7% while total durable-write reduction is 50%.

## Validation failure
Any node validation failure leaves the group uncommitted. Partial node conclusions are not promoted as group COMPLETE, and exact NEXT/REMAINDER does not advance past a failed node. If an independently receipted effect already committed, recovery reconciles that receipt while reconstructing the otherwise uncommitted group.

## Observability and replay cost
Coalescing deliberately trades fine durable per-node progress localization for bounded replay of at most the fixed 3-node eligible group. Do not reintroduce generic durable per-node START/END solely for observability. Ordinary live diagnostics may be ephemeral because correctness is reconstructible from prior authority. If a failure becomes non-reconstructible or externally effectful, it exits the eligible class and requires target-specific durable evidence.

## Authority separation
Issue #1 compact live baton remains routine relay/recovery authority. Protocol and SHADOW/SYNTHETIC records are contract/evidence inputs and do not independently advance live NEXT. A shadow test record cannot override a conflicting live baton absent an explicit later authoritative correction.

## Evidence
LW34 fixed 3-node baseline: 3 durable package boundaries / 3 audited outputs. Candidate: 1 boundary / 3 audited outputs. Independent candidate repeat: 1 / 3. Both simulated interruption-after-node-2 recovery probes preserved semantic decisions and exact remainder with no external effect to duplicate. A live 3-node application also used 1 boundary / 3 audited outputs. Boundary-write reduction for the fixed graph: 66.7%.

LW35 added a true cross-invocation shadow recovery pass with `PERSISTED_NODE_OUTPUTS=NONE`, plus directional positive/negative receipt-contract tests for a mutation-containing group. A fresh-effect cross-invocation mutation repeat is armed for LW36; until it passes, mutation-containing groups remain directional-only.

## Scope limit
Only fixed `n=3` reconstructible shared-recovery-fate work is promoted as the default eligible class. Larger/adaptive batching is not promoted: extra write savings have not yet been shown to dominate increased replay/validation cost. Mutation-containing groups remain directional-only pending independent repeat even when they satisfy the receipt contract.

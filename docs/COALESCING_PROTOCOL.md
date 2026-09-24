# Package-Boundary Coalescing Protocol

Status: PROMOTED for the tested eligible class (P5M11 / LW34).

## Purpose
Reduce durable package-boundary I/O without weakening crash recovery or effect safety.

## Eligible class
A fixed 3-node group may use one package boundary when all nodes share recovery fate and are reconstructible audit/decision work. Recovery input must be immutable by identity/version/hash or explicitly revalidated for semantic equivalence. All nodes must validate before group COMPLETE.

## Durable boundary
Persist one record containing: `PACKAGE_GROUP_ID`, ordered `NODE_IDS`, `INPUT_IDENTITY_OR_REVALIDATION_RULE`, audited `OUTPUTS` (`OUTPUT_ID`, durable decision/change, downstream consequence, validation evidence), `RESULT`, exact `NEXT/REMAINDER`, and `TURN_COMPLETE`.

Per-node START/END/package checkpoints are not required for this eligible class.

## Recovery
Before group boundary: recover from the prior authoritative baton plus stable/revalidated input and deterministically reconstruct the group. After group boundary: resume exact NEXT. A missing package boundary never proves an external effect did not occur.

## Effect safety
Never coalesce across an unreceipted non-idempotent effect. An authoritative/idempotent mutation may participate only when stable effect identity plus authoritative durable receipt/result independently survives package-boundary loss and the recovery horizon. Recovery reconciles that receipt before retry.

## Validation failure
Any node validation failure leaves the group uncommitted. Partial node conclusions are not promoted as group COMPLETE.

## Evidence
LW34 fixed 3-node baseline: 3 durable package boundaries / 3 audited outputs. Candidate: 1 boundary / 3 audited outputs. Independent candidate repeat: 1 / 3. Both simulated interruption-after-node-2 recovery probes preserved semantic decisions and exact remainder with no external effect to duplicate. Boundary-write reduction: 66.7%.

## Scope limit
Only fixed `n=3` is promoted. Larger/adaptive batching is not promoted: extra write savings have not yet been shown to dominate increased replay/validation cost.

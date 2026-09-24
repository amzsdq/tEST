# LW21 Persistence Thinning — Controlled Candidate

Status: CANDIDATE
Primary variable: PERSISTENCE_THINNING
Frozen defaults: promoted value gate; ~34 eligible units; one final scheduler mutation; +3m lead; semantic-output contract unchanged.

## Predeclared persistence gate
FULL_CHAIN when a later decision depends on a newly persisted candidate, or when the source of truth cannot be reconstructed without observing the persisted representation.
THIN_ELIGIBLE only when source evidence is already durable, candidate persistence adds no authority, and semantic validation can be performed against the durable source/result without hiding drift.
Rollback: any material defect attributable to an omitted persist/fresh-fetch boundary => THINNING_FAILURE and restore FULL_CHAIN for that target class.

## Frozen candidate pool
Scoring uses DR/UU/F/R 0-3, eligible >=8/12, no zero DR/F, tie-break F>DR>UU>lexical ID. Target-value and persistence mode are separate decisions.

- A2=Persistence gate specification. DR3 UU3 F3 R3=12. FULL_CHAIN. Boundary: changes default persistence policy; unresolved thinning safety; falsified by omitted-boundary defect; reused across artifact work.
- B2=Convergence protocol persistence interaction. DR3 UU2 F3 R3=11. FULL_CHAIN. Boundary: changes experiment comparability; unresolved mode attribution; falsified by causal contamination; reused by future experiments.
- C2=Value-gate reconstructibility audit. DR2 UU2 F3 R3=10. THIN_ELIGIBLE. Boundary: source is already durable and freshly readable; decision is whether a second candidate copy adds authority; falsified if review cannot reconstruct score/selection rules.
- D2=Ledger reconstructibility audit. DR2 UU2 F3 R3=10. THIN_ELIGIBLE. Boundary: ledger is already durable current index; decision is whether ceremonial candidate persistence catches a material defect unavailable from source review; falsified by source/result ambiguity.
- E2=Prompt prose cleanup. DR1 UU1 F1 R1=4 REJECT_LOW_VALUE.
- F2=Formatting normalization. DR1 UU0 F1 R1=3 REJECT_LOW_VALUE.

## Candidate execution record
A2 establishes the persistence gate above. B2 is selected by A2 if the gate needs causal-isolation rules in the convergence protocol. C2/D2 are controls for reconstructible durable-source review without ceremonial candidate persistence.

## Acceptance
PROMOTE_THINNING only if >=2 FULL_CHAIN controls and >=2 THIN_ELIGIBLE targets show: no omitted-boundary defect; non-inferior semantic/downstream quality; materially lower artifact I/O for thin targets. WORKED is telemetry only.
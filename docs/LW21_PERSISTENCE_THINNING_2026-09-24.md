# LW21 Persistence Thinning — Controlled Revision

Status: REVISED_CANDIDATE
Primary variable: PERSISTENCE_THINNING
Frozen defaults: promoted value gate; target ~34 eligible units; one final scheduler mutation; +3m lead; semantic-output contract unchanged.

## Predeclared persistence gate
FULL_CHAIN when a later decision depends on a newly persisted candidate, or when source-of-truth correctness requires observing the persisted representation.
THIN_ELIGIBLE only when (1) source evidence is already durable and freshly readable, (2) candidate persistence adds no authority, (3) validation can be reconstructed from named durable inputs, and (4) omission cannot hide representation drift relevant to the decision.
Rollback: any material defect attributable to an omitted persist/fresh-fetch boundary => THINNING_FAILURE and restore FULL_CHAIN for that target class.

## Frozen value gate and candidate pool
DR/UU/F/R each 0-3; eligible >=8/12; no zero DR/F; tie-break F>DR>UU>lexical ID. Target value never determines persistence mode.

- A2 Persistence gate specification: 12/12; FULL_CHAIN. Named boundary: default persistence policy / thinning safety / omitted-boundary defect / broad reuse.
- B2 Convergence protocol persistence interaction: 11/12; FULL_CHAIN. Named boundary: experiment comparability / causal attribution / contamination / future experiments.
- C2 Value-gate reconstructibility audit: 10/12; THIN_ELIGIBLE. Named boundary: already-durable scoring contract / reconstructibility / missing-score-rule falsifier / repeated target selection.
- D2 Ledger reconstructibility audit: 10/12; THIN_ELIGIBLE. Named boundary: already-durable current index / source-result consistency / stale-boundary falsifier / repeated comparisons.
- E2 Prompt prose cleanup: 4/12 REJECT_LOW_VALUE.
- F2 Formatting normalization: 3/12 REJECT_LOW_VALUE.

## Fresh-fetch review defects and required corrections
1. TARGET=thin reconstructibility; FAILURE_MODE='durable source exists' was too weak and could hide representation-sensitive drift; REQUIRED_CHANGE=name durable inputs and require reconstruction of the exact decision-relevant fields. RESOLVED by four-part THIN_ELIGIBLE gate.
2. TARGET=I/O benefit; FAILURE_MODE='materially lower' had no threshold; REQUIRED_CHANGE=define per-target candidate-boundary I/O. RESOLVED: FULL_CHAIN candidate boundary costs 4 artifact operations (candidate write, fresh fetch, revision write, fresh fetch); THIN_ELIGIBLE target costs 0 candidate-boundary operations while source reads needed for semantic review are counted separately and are not called savings.
3. TARGET=quality comparison; FAILURE_MODE=semantic output count alone could miss lost corrections; REQUIRED_CHANGE=compare material-correction yield and explicit counterfactual boundary defects. RESOLVED: each target logs MATERIAL_CORRECTIONS and OMITTED_BOUNDARY_DEFECT; any YES rejects thinning for that class.
4. TARGET=mode gaming; FAILURE_MODE=persistence mode could be changed after seeing defects; REQUIRED_CHANGE=freeze mode before substantive target execution. RESOLVED: A2/B2 FULL_CHAIN and C2/D2 THIN_ELIGIBLE are immutable for this sample except mandatory rollback after failure.

## Execution / validation
A2 FULL_CHAIN: persisted candidate -> fresh fetch exposed 4 concrete specification defects above -> defect-caused revision persisted. MATERIAL_CORRECTIONS=4. This demonstrates FULL_CHAIN remains valuable when the artifact itself defines a new policy.
SELECTED_BY=A2_VALIDATION -> B2 focus: encode persistence as an explicit causal layer in convergence protocol so future comparisons cannot confuse target value with persistence cost.

C2 THIN_ELIGIBLE reconstructibility inputs: `docs/VALUE_GATED_TARGET_SELECTION.md` frozen score dimensions, eligibility threshold, tie-break, audit rules, acceptance boundary. Fresh source read reconstructed all decision-relevant fields without a copied candidate. MATERIAL_CORRECTIONS=0; OMITTED_BOUNDARY_DEFECT=NO; candidate-boundary ARTIFACT_IO=0. PERSISTENCE_SKIP_REASON=existing durable source is authoritative and review decision concerns reconstructibility, not a new representation.

D2 THIN_ELIGIBLE reconstructibility inputs: `docs/EXPERIMENT_LEDGER.md` canonical storage contract, frozen semantic-output contract, LW18 boundary, telemetry separation, reconciliation contract. Fresh source read exposed that compact ledger still lists LW19 ACTIVE and lacks LW20 completion, but that is a source-content reconciliation defect, not a defect hidden by omitted candidate persistence. MATERIAL_CORRECTIONS=1 (stale index); OMITTED_BOUNDARY_DEFECT=NO. This target therefore validates thinning for diagnosis but selects a future FULL_CHAIN reconciliation because changing the authoritative index requires persisted review.

## Promotion rule
PROMOTE_THINNING only for reconstructible audit/decision targets, not policy-definition or authoritative-index mutation. Require >=2 thin targets with OMITTED_BOUNDARY_DEFECT=NO, non-inferior decision quality, and zero ceremonial candidate-boundary I/O versus 4 operations per comparable FULL_CHAIN candidate boundary. Source reads remain counted as semantic evidence I/O, never misreported as savings.

## Audited semantic outputs
O1 persistence mode is a separate gate from target value -> prevents high-value score from forcing writes.
O2 four-part reconstructibility gate -> prevents thinning where persisted representation is decision-relevant.
O3 omitted-boundary defect rollback -> converts hidden drift into explicit rejection evidence.
O4 candidate-boundary I/O accounting -> savings cannot include necessary source reads.
O5 mode freeze -> prevents post-hoc classification gaming.
O6 stale-ledger finding classified as source reconciliation, not thinning failure -> next mutation must use FULL_CHAIN.

A2_VALIDATION=PASS_WITH_MATERIAL_CORRECTIONS.
C2_VALIDATION=PASS_THIN_ELIGIBLE.
D2_VALIDATION=PASS_THIN_ELIGIBLE_WITH_SOURCE_RECONCILIATION_REQUIRED.
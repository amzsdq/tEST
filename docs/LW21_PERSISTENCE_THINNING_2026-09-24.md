# LW21 Persistence Thinning — Controlled Result

Status: PASS_BOUNDED / REPEAT_FOR_DEFAULT
Primary variable: PERSISTENCE_THINNING
Frozen defaults: promoted value gate; target ~34 eligible units; one final scheduler mutation; +3m lead; semantic-output contract unchanged.

## Persistence gate
FULL_CHAIN when a later decision depends on a newly persisted representation, source-of-truth mutation is being made, or persisted reality is under test.
THIN_ELIGIBLE only when: (1) source evidence is already durable and freshly readable; (2) candidate persistence adds no authority; (3) exact decision-relevant fields can be reconstructed from named durable inputs; (4) omission cannot hide representation drift relevant to the decision.
Any material defect attributable to an omitted persist/fresh-fetch boundary => THINNING_FAILURE and FULL_CHAIN restored for that target class.

## Frozen value-gated pool
A2 Persistence gate specification 12/12 FULL_CHAIN.
B2 Convergence protocol persistence interaction 11/12 FULL_CHAIN.
C2 Value-gate reconstructibility audit 10/12 THIN_ELIGIBLE.
D2 Ledger reconstructibility audit 10/12 THIN_ELIGIBLE.
E2 Prompt prose cleanup 4/12 REJECT_LOW_VALUE.
F2 Formatting normalization 3/12 REJECT_LOW_VALUE.
Target value and persistence mode were frozen separately before execution.

## A2 FULL_CHAIN
Candidate persisted and freshly fetched. Review found four material defects: reconstructibility was underspecified; 'materially lower I/O' lacked a denominator; quality comparison ignored lost-correction risk; persistence mode could be post-hoc gamed. Revision added four-part reconstructibility, candidate-boundary accounting, MATERIAL_CORRECTIONS/OMITTED_BOUNDARY_DEFECT, and mode freeze. Revision persisted and freshly fetched. RESULT=PASS_WITH_MATERIAL_CORRECTIONS. Candidate-boundary I/O=4. MATERIAL_CORRECTIONS=4.
SELECTED_BY=A2_VALIDATION -> B2 persistence causal-layer specification.

## B2 FULL_CHAIN
`docs/RELAY_OPTIMIZATION_CONVERGENCE.md` candidate persisted and freshly fetched. Review found a real regression: the compressed v0.4 candidate had dropped v0.3's explicit comparable-sample contract and persist-review-revise defect schema. Revision restored those invariants and added the bounded persistence-mode gate, source-read accounting, and rollback. Revision persisted/freshly fetched. RESULT=PASS_AFTER_REGRESSION_CORRECTION. Candidate-boundary I/O=4. MATERIAL_CORRECTIONS=3 review findings, including 1 material baseline regression.
SELECTED_BY=B2_VALIDATION -> C2/D2 reconstructibility controls; FULL_CHAIN is retained for policy-definition/source-of-truth mutation classes.

## C2 THIN_ELIGIBLE
Named durable inputs: `docs/VALUE_GATED_TARGET_SELECTION.md` score dimensions, >=8/12 threshold, no-zero DR/F, tie-break, audit rules, acceptance boundary. Fresh source review reconstructed all decision-relevant fields without a copied candidate. PERSISTENCE_SKIP_REASON=existing durable source is authoritative; decision concerns reconstructibility, not a new representation. MATERIAL_CORRECTIONS=0. OMITTED_BOUNDARY_DEFECT=NO. Candidate-boundary I/O=0; necessary source read=1 and is not counted as savings. RESULT=PASS_THIN_ELIGIBLE.

## D2 THIN_ELIGIBLE
Named durable inputs: `docs/EXPERIMENT_LEDGER.md` canonical storage contract, frozen semantic-output contract, LW18 boundary, telemetry separation, reconciliation contract. Fresh source review reconstructed the decision and exposed a stale source-content defect: compact ledger still listed LW19 ACTIVE and omitted LW20 completion. This defect is visible directly in the authoritative source and therefore was not hidden by omitted candidate persistence. PERSISTENCE_SKIP_REASON=diagnostic decision can be made from authoritative source; mutation itself is not thin-eligible. MATERIAL_CORRECTIONS=1 diagnostic finding. OMITTED_BOUNDARY_DEFECT=NO. Candidate-boundary I/O=0; source read=1. RESULT=PASS_THIN_ELIGIBLE_WITH_FULL_CHAIN_RECONCILIATION_REQUIRED.

## Comparison
FULL_CHAIN controls=2. Candidate-boundary I/O=8 total, 4/target. Material corrections=7 review findings; importantly B2 caught a persisted-representation regression.
THIN_ELIGIBLE controls=2. Candidate-boundary I/O=0 total, source-review I/O=2 total. Omitted-boundary defects=0/2. Decision quality remained sufficient to reconstruct C2 completely and diagnose D2's stale source state. Savings claim is limited to ceremonial candidate-boundary operations: 8 avoided across two thin targets relative to applying FULL_CHAIN mechanically; necessary source reads are excluded from savings.

The experiment does NOT show that persistence is generally unnecessary. It shows the opposite boundary: FULL_CHAIN is valuable for policy/source mutation, while reconstructible read/audit decisions can omit candidate copies safely in this sample.

## Audited semantic outputs
O1 separate target-value and persistence gates -> high-value score cannot force persistence.
O2 four-part reconstructibility gate -> thin mode requires named durable decision fields.
O3 omitted-boundary rollback -> hidden drift immediately rejects target class.
O4 candidate-boundary I/O accounting -> source reads cannot be mislabeled as savings.
O5 immutable persistence mode -> prevents post-hoc mode gaming.
O6 FULL_CHAIN regression detection -> policy-definition mutations retain persisted review.
O7 thin C2 reconstructibility -> existing authoritative contracts need no ceremonial copy for audit decisions.
O8 thin D2 diagnosis -> source-content defects can be found without candidate persistence; mutation still escalates to FULL_CHAIN.
O9 persistence is a causal layer distinct from package size/ranking/counting/control -> future comparisons remain attributable.
O10 bounded thinning class -> reconstructible audit/decision targets are eligible; authoritative mutation/new representation are not.

## Metrics / verdict
UNITS_PLANNED=34 target
UNITS_DONE=30 conservative eligible-unit count
UNITS_REMAINING=0; eligible work for this controlled four-target sample converged without padding
PACKAGE_COMPLETE=YES
SATURATED=NO
SEMANTIC_OUTPUTS=10
SEMANTIC_OUTPUTS_PER_10_UNITS=3.33 (not compared to LW20 density because persistence mode intentionally changed artifact work shape)
FULL_CHAIN_TARGETS=2
THIN_TARGETS=2
FULL_CANDIDATE_BOUNDARY_IO=8
THIN_CANDIDATE_BOUNDARY_IO=0
THIN_SOURCE_READ_IO=2
OMITTED_BOUNDARY_DEFECTS=0
CONTROL_IO scheduler target=1
RESULT=PROMOTE_THINNING_BOUNDED_RECONSTRUCTIBLE_AUDIT_DECISION_CLASS; RETEST_BEFORE_BROADER_DEFAULT

Next required evidence: perform the stale ledger reconciliation under FULL_CHAIN, then repeat thinning on a different pair of reconstructible audit/decision targets. Reject expansion if any omitted-boundary defect appears.
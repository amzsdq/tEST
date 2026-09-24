# LW20 Value-Gate Repeat — Executed Record

Status: VALIDATED REPEAT
Primary variable: VALUE_GATED_TARGET_SELECTION_REPEATABILITY
Baseline held: target ~34 eligible units; frozen semantic-output contract; one scheduler mutation; +3m lead.

## Frozen gate and pre-work pool
Dimensions unchanged from LW19: DR/UU/F/R each 0–3; eligibility >=8/12; DR and F nonzero; tie-break F > DR > UU > lexical ID. Scores immutable.

| ID | Target | DR | UU | F | R | Total | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| A2 | Long useful-work workload boundary | 3 | 3 | 3 | 3 | 12 | ELIGIBLE |
| B2 | Persisted-output thinning eligibility | 3 | 3 | 3 | 3 | 12 | ELIGIBLE |
| C2 | Dispatch timing evidence boundary | 2 | 2 | 3 | 3 | 10 | ELIGIBLE |
| D2 | Cross-runtime generality contract | 3 | 3 | 3 | 2 | 11 | ELIGIBLE |
| E2 | Formatting consistency | 1 | 1 | 1 | 1 | 4 | REJECT_LOW_VALUE |
| F2 | Historical prose compression | 1 | 1 | 1 | 1 | 4 | REJECT_LOW_VALUE |

Named score boundaries were frozen before work: A2 controls the still-OPEN 10-minute/deep-work experiment family; B2 controls whether recurring persistence I/O can be removed; C2 controls whether timing offset may influence lead policy; D2 controls transfer of relay-local promotions to changed runtimes. Each has explicit observable falsification/adverse evidence; E2/F2 do not.

## A2 — long useful-work boundary
Candidate rule: package-size capacity and useful wall time are separate variables. A long-work experiment is eligible only when its work graph contains intrinsically necessary evidence acquisition, transformation, persisted validation, and result-dependent downstream decisions; target elapsed time never licenses padding.

Fresh-fetch review defects:
1. TARGET=duration attribution; FAILURE_MODE=large unit count could be treated as a proxy for deep work; REQUIRED_CHANGE=accept only GitHub START→END telemetry plus audited useful outputs, never unit count alone.
2. TARGET=termination; FAILURE_MODE=worker could stop after semantic convergence even when predeclared eligible result-dependent work remains; REQUIRED_CHANGE=carry exact eligible remainder unless runtime/safety blocks.
3. TARGET=10-minute goal; FAILURE_MODE=goal could incentivize ceremonial I/O; REQUIRED_CHANGE=10-minute observation is evidence only when density/control remain non-inferior.

Revision/validation: all three resolved. A2_VALIDATION=PASS.
SELECTED_BY=A2_VALIDATION(intrinsic-work graph identifies persistence I/O as a possible cost rather than duration objective) -> B2 focus: define evidence required before thinning persisted-output chains.

## B2 — persistence thinning boundary
Candidate rule: persistence may be thinned only when a comparable full-chain sample set shows low material correction yield and the omitted boundary is reconstructible without weakening validation.

Fresh-fetch review defects:
1. TARGET=correction yield; FAILURE_MODE="low" was undefined; REQUIRED_CHANGE=record material defects discovered only after fresh fetch per eligible chain.
2. TARGET=reconstructibility; FAILURE_MODE=direct path could hide state drift; REQUIRED_CHANGE=skip only when source-of-truth is already durable and later decision does not depend on a newly persisted candidate.
3. TARGET=rollback; FAILURE_MODE=thinning could silently persist after a miss; REQUIRED_CHANGE=any defect attributable to omitted persistence immediately restores full chain.

Revision/validation: resolved as a future controlled experiment contract; no thinning applied in LW20. B2_VALIDATION=PASS.
SELECTED_BY=B2_VALIDATION(persistence can be tested separately only if scheduler timing evidence is not conflated with state validation) -> C2 focus: bound dispatch timing evidence.

## C2 — timing evidence boundary
Candidate rule: dispatch offset is scheduler telemetry, not continuation authority. Lead-policy changes require end-to-end WAKE_OK/WORK_OK under comparable schedule state; early/late offsets alone cannot promote/demote a lead class.

Review defects resolved:
- mixed +2m evidence cannot be summarized by average offset; adverse missed-near occurrence remains first-class.
- stored DTSTART vs runtime timestamp is not the WORKED clock.
- a changed runtime/scheduler environment invalidates direct transfer without freshness check.

C2_VALIDATION=PASS.
SELECTED_BY=C2_VALIDATION(environment drift can invalidate timing/continuation interpretation) -> D2 focus: formalize cross-runtime transfer gate.

## D2 — cross-runtime transfer gate
Candidate rule: relay-local promotions transfer to a changed runtime only after checking causal fields: scheduler semantics, tool/action availability, durable-state authority, timing/dispatch behavior relevant to the mechanism, and persistence guarantees. Any material drift => historical evidence is guidance, not promotion evidence.

Review defects resolved:
- cosmetic model/version changes do not automatically invalidate evidence; only named causal-field drift matters.
- absence of observed drift is not equivalence proof; at least one adverse/replication sample is required for promotion transfer.
- rollback/demotion remains local to the changed environment unless shared causal evidence exists.

D2_VALIDATION=PASS.

## Audited semantic outputs
O20-01 / separate package capacity from duration / prevents unit-count duration claims / A2_VALIDATION
O20-02 / intrinsic-work graph eligibility / blocks padding disguised as work / A2_VALIDATION
O20-03 / exact eligible remainder rule for deep-work packages / preserves useful continuation / A2_VALIDATION
O20-04 / 10-minute evidence requires non-inferior density/control / prevents duration gaming / A2_VALIDATION
O20-05 / thinning requires measured fresh-fetch-only correction yield / creates falsifiable persistence experiment / B2_VALIDATION
O20-06 / persistence skip requires durable reconstructible source / prevents hidden state drift / B2_VALIDATION
O20-07 / omitted-boundary defect restores full chain / gives immediate rollback / B2_VALIDATION
O20-08 / dispatch offset cannot promote/demote lead class alone / protects continuation inference / C2_VALIDATION
O20-09 / adverse timing occurrence cannot be averaged away / preserves negative evidence / C2_VALIDATION
O20-10 / WORKED clock remains GitHub START→END only / prevents timestamp-role confusion / C2_VALIDATION
O20-11 / cross-runtime transfer checks named causal fields / bounds portability claims / D2_VALIDATION
O20-12 / causal drift downgrades old evidence to guidance / prevents stale promotion transfer / D2_VALIDATION
O20-13 / transfer requires adverse/replication sample / makes portability falsifiable / D2_VALIDATION
O20-14 / environment-local rollback rule / prevents unrelated global demotion / D2_VALIDATION
O20-15 / target-value and persistence gates remain independent / avoids ceremonial persistence / cross-artifact validation
O20-16 / result-dependent chain A2→B2→C2→D2 audited by SELECTED_BY / makes dependency claim testable / cross-artifact validation
O20-17 / rejected editorial candidates remain visible / prevents post-hoc candidate-pool inflation / frozen-pool validation
O20-18 / value gate repeat uses different unresolved mechanisms / tests repeatability beyond stale-document reconciliation / cross-artifact validation

## Package result
UNITS_PLANNED=34
UNITS_DONE=34
UNITS_REMAINING=0
PACKAGE_COMPLETE=YES
SATURATED=NO
SEMANTIC_OUTPUTS=18
SEMANTIC_OUTPUTS_PER_10_UNITS=5.29
REJECTED_TARGETS=2/6
SCORE_ERROR=NO
CONTROL_IO=one final scheduler mutation target
RESULT=PROMOTE_AS_DEFAULT_VALUE_GATED_TARGET_SELECTION

Comparison: LW18=4.71/10; LW19=5.29/10; LW20 repeat=5.29/10 on a different unresolved candidate pool. The repeated non-inferior >5.0 density with unchanged control policy satisfies the predeclared default-promotion criterion. Wall time remains telemetry and is not part of this promotion.
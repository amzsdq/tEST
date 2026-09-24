# Value-Gated Target Selection — LW19

Status: VALIDATED CANDIDATE for controlled comparison; not yet promoted.

## Frozen scoring gate
Score each candidate before substantive selection on four dimensions, each 0–3:
- Decision reach (DR): 0=no named downstream decision; 1=one local decision; 2=multiple near-term relay decisions; 3=changes a promoted/default mechanism or multiple experiment families.
- Unresolved uncertainty (UU): 0=settled/no material uncertainty; 1=minor bounded ambiguity; 2=material unresolved choice; 3=decision currently blocked or promotion/demotion boundary unresolved.
- Falsifiability (F): 0=subjective; 1=weak observable; 2=explicit pass/fail evidence; 3=controlled comparison or demotion trigger with observable counterevidence.
- Expected downstream reuse (R): 0=one-off prose; 1=single future use; 2=reused across repeated samples; 3=hot-path/promotion/recovery contract reused broadly.

TOTAL=DR+UU+F+R. Eligibility minimum=8/12 and no zero in DR or F. Tie-break: higher F, then DR, then UU, then lexical target ID. Dimensions/minimum/tie-break are frozen before candidate scoring and cannot be changed after density is observed.

## Candidate pool and pre-work scores
| ID | Target | DR | UU | F | R | Total | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| P | Large-package scale protocol after LW18 promotion | 3 | 2 | 3 | 3 | 11 | ELIGIBLE |
| Q | Experiment ledger/index reconciliation after LW18 | 2 | 2 | 3 | 3 | 10 | ELIGIBLE |
| R | Evidence maturity map after 30–36 promotion | 3 | 2 | 3 | 3 | 11 | ELIGIBLE |
| S | Persisted-output protocol target-selection interaction | 3 | 3 | 3 | 3 | 12 | ELIGIBLE |
| T | Applied prompt wording cleanup | 1 | 1 | 1 | 2 | 5 | REJECT_LOW_VALUE |
| U | Historical findings prose cleanup | 1 | 1 | 1 | 1 | 4 | REJECT_LOW_VALUE |

Initial target=P. Q/R/S remain eligible but their substantive focus is unresolved until selected by preceding validation; pre-scoring does not precompute edits.

## Fresh-fetch review findings and corrections
1. TARGET=selection independence; FAILURE_MODE=pre-scoring four likely winners can masquerade as result-dependent target selection; REQUIRED_CHANGE=freeze candidate identity/score but keep later substantive focus unresolved until SELECTED_BY validation. RESOLVED.
2. TARGET=score gaming; FAILURE_MODE=ordinal dimensions can be inflated post hoc without evidence; REQUIRED_CHANGE=every score >=2 must cite a named decision/evidence boundary in the turn baton, and scores are immutable for this sample. RESOLVED.
3. TARGET=value override; FAILURE_MODE=non-inferior density could be excused by vague importance claims; REQUIRED_CHANGE=override must name baseline output dominated, changed downstream decision, and observable future evidence that can falsify dominance. RESOLVED.
4. TARGET=unit quota; FAILURE_MODE=34-unit target can pressure weak work; REQUIRED_CHANGE=eligibility wins over quota; record INELIGIBLE_AFTER_REVIEW and allow 30-36 actual units, never fabricate. RESOLVED.

## Audit rules
- `SELECTED_BY=<validated result> -> <target/focus>` plus frozen gate score is mandatory for claimed dependency.
- Scores are immutable within LW19. Any discovered factual error is logged as SCORE_ERROR and makes target-selection attribution non-comparable; do not silently rescore.
- For each score dimension >=2, baton records the named decision/evidence boundary supporting it.
- Semantic output schema: OUTPUT_ID / DURABLE_CHANGE / DOWNSTREAM_CONSEQUENCE / VALIDATED_BY. Duplicate consequences count once.
- Rejected candidates stay visible. INELIGIBLE_AFTER_REVIEW stays visible.
- Eligibility wins over nominal unit count; actual 30-36 is allowed without padding.
- Package/control baseline remains full persisted-output chain, one scheduler mutation, +3m lead.

## Acceptance for LW19
Promote VALUE_GATED_TARGET_SELECTION only if raw density exceeds LW18 4.71/10 at unchanged control cost. A non-inferior-density value override is admissible only when it names (a) baseline output dominated, (b) materially changed downstream decision, and (c) observable future evidence that would falsify claimed dominance. Otherwise RETEST/REJECT.

## P validation
PASS. The gate is predeclared, rejected candidates remain auditable, result-dependent focus is protected, score mutation is prohibited, and quota gaming/value-override ambiguity are explicitly bounded.

SELECTED_BY=P_VALIDATION(score-independence + anti-gaming requirements) -> Q focus: reconcile the experiment ledger so future density/value comparisons cannot use stale LW18 ACTIVE state or ambiguous counting baseline.
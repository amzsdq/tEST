# Value-Gated Target Selection — LW19

Status: CANDIDATE under controlled test.

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

Initial highest-value substantive target=P. Q/R/S remain eligible but their substantive focus must still be selected by preceding validation; pre-scoring does not precompute their edit target.

## Audit rules
- Result-dependent selection records `SELECTED_BY=<validated result> -> <target/focus>` plus frozen score.
- A semantic output counts only as OUTPUT_ID / DURABLE_CHANGE / DOWNSTREAM_CONSEQUENCE / VALIDATED_BY.
- Duplicate downstream consequences count once.
- Rejected candidates stay visible; no post-hoc score changes.
- INELIGIBLE_AFTER_REVIEW is allowed and must remain visible.
- Package target remains 34 eligible units with the LW18 full persisted-output baseline, one scheduler mutation, +3m lead.

## Acceptance for LW19
Promote VALUE_GATED_TARGET_SELECTION only if density exceeds LW18 4.71/10, or if density is non-inferior and a falsifiable value override demonstrates materially stronger downstream consequences, without extra control cost.
# Value-Gated Target Selection

Status: PROMOTED DEFAULT within tested conditions after independent LW19/LW20 positive samples.

## Frozen scoring gate
Score each candidate before substantive selection on four dimensions, 0–3:
- Decision reach (DR): 0=no named downstream decision; 1=one local decision; 2=multiple near-term relay decisions; 3=changes a promoted/default mechanism or multiple experiment families.
- Unresolved uncertainty (UU): 0=settled; 1=minor bounded ambiguity; 2=material unresolved choice; 3=promotion/demotion boundary or decision blocked.
- Falsifiability (F): 0=subjective; 1=weak observable; 2=explicit pass/fail evidence; 3=controlled comparison/demotion trigger.
- Expected downstream reuse (R): 0=one-off prose; 1=single future use; 2=reused across samples; 3=hot-path/promotion/recovery contract reused broadly.

TOTAL=DR+UU+F+R. Eligibility minimum=8/12 and no zero in DR or F. Tie-break: higher F, then DR, then UU, then lexical target ID. Freeze dimensions/minimum/tie-break before scoring; do not change them after results are observed.

## Anti-gaming rules
- Every score >=2 cites a named decision/evidence boundary.
- Candidate score is immutable within a controlled sample; factual scoring error is logged as SCORE_ERROR and attribution becomes non-comparable rather than silently rescored.
- `SELECTED_BY=<validated prior result> -> <later target/focus>` is required for claimed result dependency.
- Pre-scoring candidate identity does not precompute later substantive edits; later focus remains result-dependent.
- Eligibility wins over nominal unit/package quota; never fabricate work to hit count.
- Rejected/INELIGIBLE candidates remain auditable.

## Semantic-output rule
Count one output only for a validated durable rule/specification/decision with a named downstream consequence. Duplicate consequences count once. Summaries, style cleanup, reads/writes, and restated evidence count zero.

## Promotion evidence
LW19 improved raw semantic density from LW18 4.71/10 to 5.29/10 under value-gated selection. LW20 independently repeated 5.29/10 on a different unresolved candidate pool with unchanged control policy. Therefore VALUE_GATED_TARGET_SELECTION is the default selector within tested conditions.

## Current interaction with auto-refill / E12
The value gate ranks substantive refill targets; it does not override persistence routing, reserve admission, or valid turn-stop conditions. Fast package completion means select another eligible target while outside reserve. Reserve entry can defer an otherwise eligible target without changing its value score. A stale documentation defect is itself eligible only when it crosses the same value threshold; do not manufacture cleanup work to keep an invocation alive.

## Rollback
Narrow/retest the gate if repeated use lowers downstream-value density, encourages score inflation, obscures result dependency, or systematically selects lower-value work than an explicit alternative under comparable control cost.
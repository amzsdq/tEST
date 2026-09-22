# E9 Historical Coverage Manifest v1

STATUS=DERIVED_AUDIT_ARTIFACT
CANONICAL_TRUTH=NO
PRIMARY_VARIABLE=historical ledger field provenance

Purpose: classify EXPERIMENT_LEDGER fields by whether they are source observations or derived/reconciliation metadata, before any attempt to demote the full ledger to a disposable report.

## Field classification

| Ledger field | Class | Regeneration rule |
|---|---|---|
| Trial | SOURCE_FACT | Recover from Issue/event trial identity. |
| Prompt | SOURCE_FACT / NORMALIZED | Prompt/version is source evidence; combined labels such as `P0R/P1 path` are normalized presentation. |
| Primary variable | DERIVED | Normalize from trial design/prompt semantic diff. |
| Lead time | SOURCE_FACT | Recover from trial/scheduler evidence where explicitly recorded. |
| Writes/wake | SOURCE_FACT / DERIVED | Explicit mutation count when recorded; otherwise derive from candidate protocol. |
| WRITE_OK | SOURCE_FACT / SCHEMA_DERIVED | Explicit failures/pending are source facts; positive omission in promoted compact schemas is derived by schema contract. |
| STATE_OK | SOURCE_FACT / SCHEMA_DERIVED | Explicit anomalies are source facts; positive omission may be derived from valid update-return contract. |
| WAKE_OK | SOURCE_FACT / SCHEMA_DERIVED | Invocation is source evidence; positive omission may be derived by clean-success schema. |
| WORK_OK | SOURCE_FACT | Substantive work/result evidence. |
| Dispatch delay | DERIVED_MEASUREMENT | Computed from timestamps; non-authoritative where timing semantics are ambiguous. |
| Duplicate? | SOURCE_FACT / SCHEMA_DERIVED | Positive observation is source fact; clean-success omission means no duplicate observed under promoted schema. |
| Recovery? | SOURCE_FACT / DERIVED_CLASSIFICATION | Recovery event is source evidence; category/summary is normalized. |
| Useful work | DERIVED_SUMMARY | Human-readable summary of source work evidence. |
| Control overhead | DERIVED | Qualitative/quantitative assessment, not raw event evidence. |
| Result | SOURCE_FACT / DECISION | Sample result is recorded evidence; promotion/rejection is a reconciliation decision. |
| Notes | DERIVED_SUMMARY | Narrative consolidation. |

## Coverage finding

Issue #1 provides append-only evidence from research bootstrap through P1 lead-time trials and later P4 compact-schema experiments. E9 also has immutable event evidence for CAS recovery. This is sufficient to reconstruct current operational state and many historical trial facts.

It is NOT yet sufficient to claim byte-for-byte or semantic regeneration of every historical ledger cell without consulting the ledger because several cells are normalized/derived (`Primary variable`, `Useful work`, `Control overhead`, narrative `Notes`) and some early records rely on historical interpretation rather than a formally versioned event schema.

## Safe architecture decision

1. Immutable/append evidence is the preferred source of truth for new observations.
2. Current-state materializations are disposable derived views.
3. EXPERIMENT_LEDGER remains a reconciliation/historical compatibility source for pre-E9 history.
4. New E9+ evidence should carry enough explicit source facts that future rows can be regenerated without mutating the historical ledger.
5. Do not full-file rewrite the ledger during concurrent relay operation; materialize a new derived report or perform a fresh-read semantic CAS only at an explicit reconciliation boundary.

RESULT=PARTIAL_COVERAGE_CONFIRMED
FULL_LEDGER_DEMOTION=NOT_YET_SAFE
NEXT=Define a versioned immutable event schema for E9+ and test one row regenerated solely from that event.
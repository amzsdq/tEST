# E9 Materialized State v1

DERIVED_VIEW=YES
CANONICAL_TRUTH=NO
REBUILD_INPUTS=Issue #1 durable event tail + events/E9-DURABLE-CONCURRENCY-01/SAMPLE-CAS-RECOVERY-1.md

CURRENT_EXPERIMENT=E9-DURABLE-CONCURRENCY-01
LAST_SAMPLE=CAS-RECOVERY-1
PROMPT_VERSION=P4V9
RESULT=PASS
WRITE_OK=YES
STATE_OK=YES
WAKE_OK=YES
WORK_OK=YES
DUPLICATE=NO observed

RECONSTRUCTION_RESULT=PASS
RECONSTRUCTION_BASIS=Issue tail independently identifies E9, CAS-RECOVERY-1, PASS and the next test; immutable event independently preserves the same experiment/sample/result and recovery semantics. No EXPERIMENT_LEDGER.md read is required to reconstruct this E9 state.

MATERIALIZATION_RULE=This file is disposable and rebuildable. Never treat it as authoritative evidence. If it conflicts with immutable event evidence, discard and regenerate it.
NEXT=Delete-or-ignore/rebuild equivalence test, then decide whether EXPERIMENT_LEDGER.md can be formally demoted to a derived historical report.

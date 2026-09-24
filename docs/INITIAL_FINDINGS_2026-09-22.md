# Relay Findings — Evidence Maturity Map

Status: LIVING EVIDENCE MAP
Origin: 2026-09-22 preliminary findings; revised during LW16 after later controlled evidence accumulated.

## Purpose

This document no longer acts as a frozen snapshot. It maps early hypotheses to their current evidence maturity so later workers do not repeatedly treat settled questions as open or provisional observations as laws.

Evidence states:
- PROMOTED: repeated relay-local evidence supports operational use.
- SUPPORTED: positive evidence exists but promotion scope is narrower than a general law.
- REJECTED_AS_DEFAULT: tested but inferior to the promoted alternative.
- OPEN: still requires discriminating evidence.

## Current promoted operating facts

### Same-automation recurring mutation — PROMOTED
A complete VEVENT preserving `RRULE:FREQ=HOURLY` can be written back to the same automation while it remains enabled. Repeated end-to-end samples established that stored schedule state and actual wake delivery must remain separate measurements.

Operational consequence: preserve recurrence on every normal final scheduler write; never infer WAKE_OK from WRITE_OK alone.

### Single final scheduler mutation — PROMOTED
Early architecture considered a provisional fallback write plus a final fast write. Controlled comparison showed the extra provisional mutation increased control overhead without demonstrated correctness/recovery gain; existing hourly recurrence already supplies cold recovery.

Operational consequence: normal path uses exactly one final scheduler mutation. Additional scheduler writes require anomaly/recovery evidence, not precaution alone.

### +3 minute continuation class — PROMOTED PRACTICAL DEFAULT
Repeated +3m samples continued end-to-end. +2m produced mixed evidence including a missed near occurrence followed by recurring recovery. Therefore +3m is the leading practical default under the tested runtime, while dispatch offset itself remains non-authoritative telemetry.

Operational consequence: do not collapse scheduler eligibility, dispatch jitter, and continuation reliability into one timing number.

### Update-return validation — PROMOTED NORMAL PATH
Routine live read-after-write verification was removed in repeated samples without loss of continuation/state reconstruction. Live verification remains an exception path for malformed returns, ambiguity, anomaly, reconciliation, or rollback.

### Issue-tail routine bootstrap — PROMOTED
Routine clean-success continuation can reconstruct active state from the compact Issue #1 tail. Ledger/canonical documents are boundary and recovery sources, not mandatory hot-path reads.

### Large pre-shaped TO-DO packages — PROMOTED FOR SEMANTIC CAPACITY
LW15-A and LW15-B independently completed 15 eligible substantive units on different artifacts while preserving one normal scheduler mutation. This establishes increased semantic capacity, not a guaranteed wall-clock duration or greater reasoning depth.

## Supported but bounded findings

### Recurrence as cold recovery — SUPPORTED
A missed near-term occurrence can leave the recurring schedule intact and a later recurring wake can restore work. This supports recurrence as a cold fallback. It does not imply a precise fallback latency guarantee.

### Durable authority — SUPPORTED WITH CONSTRAINT
Immutable epoch/fence plus atomic create-if-absent claim protects authority decisions. External side effects still require idempotency/reconciliation; authority alone does not make arbitrary effects exactly-once.

## Rejected defaults

### Provisional scheduler pre-arm on every wake — REJECTED_AS_DEFAULT
It adds a scheduler mutation without measured normal-path benefit over preserved hourly recurrence plus one final write.

### Unconditional live scheduler reread — REJECTED_AS_DEFAULT
Update-return validation is sufficient on clean normal-path samples; reread is reserved for exception/boundary cases.

### Broad repository reconstruction every wake — REJECTED_AS_DEFAULT
Compact Issue tail plus top-of-prompt TO-DO gives a cheaper hot path. Broader reads are evidence-driven.

## Open questions

1. PACKAGE_SIZE saturation: does scaling from 15 to 20–24 eligible units continue increasing semantic capacity, or does runtime saturation force exact remainder handoff?
2. Long useful-work duration: larger packages have increased measured WORKED directionally, but no evidence yet establishes a 10-minute useful-work guarantee.
3. Dispatch timing semantics: observed early/late offsets are not authoritative enough to model as a deterministic scheduler law.
4. Cross-runtime generality: findings are relay-local until reproduced under materially different runtime/provider conditions.

## Decision rule for future edits

Do not add a new mechanism merely because it is plausible. Every promoted mechanism must identify the failure it prevents, the adverse or comparative evidence supporting it, its control cost, and the condition that would demote it.

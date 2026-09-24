# Relay Findings — Evidence Maturity Map

Status: LIVING EVIDENCE MAP
Origin: 2026-09-22 preliminary findings; revised during LW16 after later controlled evidence accumulated.

## Purpose

Map early hypotheses to current evidence maturity so later workers neither reopen settled questions nor promote preliminary observations into laws.

Evidence states:
- PROMOTED: repeated relay-local evidence supports operational use inside the tested scope.
- SUPPORTED: positive evidence exists but promotion scope is narrower than a general law.
- REJECTED_AS_DEFAULT: tested but inferior to the promoted alternative on the measured objective.
- OPEN: still requires discriminating evidence.

A PROMOTED label is always scope-bound. It does not imply cross-provider or cross-runtime universality.

## Current promoted operating facts

### Same-automation recurring mutation — PROMOTED
Complete VEVENT updates preserving `RRULE:FREQ=HOURLY` repeatedly retained recurrence while the automation stayed enabled. Stored schedule state and actual wake delivery remain separate measurements.

Operational consequence: preserve recurrence on every normal final scheduler write; never infer WAKE_OK from WRITE_OK alone.
Demotion trigger: recurrence loss or state mismatch under an otherwise valid same-automation update.

### Single final scheduler mutation — PROMOTED
The provisional-fallback-plus-final-write path added control I/O without demonstrated correctness or recovery gain over preserved hourly recurrence plus one final write.

Operational consequence: normal path uses exactly one final scheduler mutation.
Exception: an observed failure mode may justify an additional write only when the extra mutation is itself the tested recovery action.
Demotion trigger: a reproducible failure that one final write cannot recover from but a specific extra write prevents.

### +3 minute continuation class — PROMOTED PRACTICAL DEFAULT
Repeated +3m samples continued end-to-end. +2m produced mixed evidence including a missed near occurrence followed by recurring recovery. +3m is therefore the leading practical default for this tested runtime; dispatch offset remains non-authoritative telemetry.

Operational consequence: do not collapse scheduler eligibility, dispatch jitter, and continuation reliability into one timing number.
Demotion trigger: repeated +3m near-occurrence misses under unchanged runtime conditions or a lower lead class demonstrating equivalent reliability with lower idle cost.

### Update-return validation — PROMOTED NORMAL PATH
Routine live read-after-write verification was removed in repeated samples without loss of continuation/state reconstruction.

Operational consequence: live verification is exception-only for malformed returns, ambiguity, anomaly, reconciliation, or rollback.
Demotion trigger: update-return success followed by reproducible persisted-state mismatch that a live read would detect before harm.

### Issue-tail routine bootstrap — PROMOTED
Routine clean-success continuation reconstructs active state from compact Issue #1 tail; ledger/canonical documents remain boundary/recovery sources.

Demotion trigger: a clean routine turn cannot reconstruct an execution-critical field from the compact tail.

### Large pre-shaped TO-DO packages — PROMOTED FOR SEMANTIC CAPACITY
LW15-A and LW15-B independently completed 15 eligible substantive units on different artifacts while preserving one normal scheduler mutation. This establishes increased semantic capacity, not a guaranteed wall-clock duration or greater reasoning depth.

Demotion trigger: repeated large packages increase nominal units but fail the eligibility gate, reduce downstream-value density, or cause unreliable continuation/remainder loss.

## Supported but bounded findings

### Recurrence as cold recovery — SUPPORTED
A missed near-term occurrence can leave recurrence intact and a later recurring wake can restore work. This supports cold fallback but does not establish a precise fallback-latency guarantee.

### Durable authority — SUPPORTED WITH CONSTRAINT
Immutable epoch/fence plus atomic create-if-absent claim protects authority decisions. External side effects still require idempotency/reconciliation; authority alone does not make arbitrary effects exactly-once.

## Rejected defaults

### Provisional scheduler pre-arm every wake — REJECTED_AS_DEFAULT
Extra scheduler mutation without measured normal-path benefit.

### Unconditional live scheduler reread — REJECTED_AS_DEFAULT
Update-return validation is sufficient on clean normal-path evidence; reread remains an exception mechanism.

### Broad repository reconstruction every wake — REJECTED_AS_DEFAULT
Compact Issue tail plus top-of-prompt TO-DO is the cheaper hot path; broader reads are evidence-driven.

## Open questions

1. PACKAGE_SIZE saturation: does 20–24 eligible-unit scaling continue increasing semantic capacity or force exact remainder handoff?
2. Long useful-work duration: larger packages increased measured WORKED directionally, but no evidence establishes a 10-minute useful-work guarantee.
3. Dispatch timing semantics: observed early/late offsets are not authoritative enough for a deterministic scheduler law.
4. Cross-runtime generality: all promoted findings remain relay-local until independently reproduced elsewhere.

## Promotion/edit contract

Every promoted mechanism must record:
1. failure or cost it addresses;
2. comparative/adverse relay-local evidence;
3. added control cost;
4. operational scope;
5. explicit demotion trigger.

A plausible mechanism without those fields stays OPEN or SUPPORTED; it is not promoted by prose confidence.

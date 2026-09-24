# Relay Findings — Evidence Maturity Map

Status: LIVING EVIDENCE MAP
Origin: 2026-09-22 preliminary findings; updated through LW16 evidence and LW17 scale-test design.

## Purpose
Map hypotheses to current evidence maturity so later workers neither reopen settled questions nor turn bounded observations into universal laws.

Evidence states: PROMOTED, SUPPORTED, REJECTED_AS_DEFAULT, OPEN. Every promotion is relay-local and scope-bound.

## Current promoted operating facts

### Same-automation recurring mutation — PROMOTED
Complete VEVENT updates preserving `RRULE:FREQ=HOURLY` repeatedly retained recurrence while enabled. Stored schedule state and actual wake delivery remain separate measurements.
Demotion: recurrence loss/state mismatch under otherwise valid same-automation update.

### Single final scheduler mutation — PROMOTED
Provisional pre-arm plus final write added control I/O without demonstrated correctness/recovery gain over preserved hourly recurrence plus one final write.
Demotion: reproducible failure prevented by a specific additional mutation.

### +3 minute continuation class — PROMOTED PRACTICAL DEFAULT
Repeated +3m samples continued end-to-end; +2m produced mixed evidence including a missed near occurrence followed by recurring recovery. Dispatch offset is non-authoritative telemetry.
Demotion: repeated +3m misses under unchanged conditions or a lower lead class with equivalent reliability and lower idle cost.

### Update-return validation — PROMOTED NORMAL PATH
Routine live reread was removed without loss of continuation/state reconstruction. Live verification remains exception-only.
Demotion: reproducible persisted-state mismatch after clean update return that reread would catch before harm.

### Issue-tail routine bootstrap — PROMOTED
Routine clean continuation reconstructs execution state from compact Issue #1 tail; broader docs remain boundary/recovery sources.
Demotion: clean routine turn cannot reconstruct an execution-critical field.

### Large pre-shaped TO-DO packages — PROMOTED FOR SEMANTIC CAPACITY THROUGH TESTED 22-UNIT SCALE
LW15-A/B independently completed 15 eligible units and LW16 completed 22/22 eligible units without saturation while preserving one scheduler mutation and +3m lead. LW16 produced 11 semantic outputs (5.0 per 10 units) with artifact I/O/output 1.09, close to LW15-B's 5.33 outputs/10 and 1.00 I/O/output. This supports capacity scaling through 22 eligible units without observed density collapse.

Scope: semantic capacity only. It does not establish a guaranteed wall-clock duration, greater reasoning depth, or arbitrary scaling beyond the tested range.
Demotion: repeated larger packages fail eligibility, lose exact remainder, increase control I/O, or materially degrade downstream-value density.

## Supported but bounded findings

### Recurrence as cold recovery — SUPPORTED
A missed near-term occurrence can leave recurrence intact and a later recurring wake can restore work; no precise fallback-latency guarantee is established.

### Durable authority — SUPPORTED WITH CONSTRAINT
Immutable epoch/fence plus atomic create-if-absent claim protects authority decisions. External side effects still require idempotency/reconciliation.

### Persisted-output review/revise chains — SUPPORTED AS QUALITY BOUNDARY
Fresh-fetch review can expose material defects and force later work to consume actual persisted state. Its I/O cost must be measured separately from package-size capacity; thinning requires a controlled non-inferiority test rather than intuition.

## Rejected defaults
- Provisional scheduler pre-arm every wake — extra scheduler mutation without measured normal-path benefit.
- Unconditional live scheduler reread — update-return validation is sufficient on clean normal path.
- Broad repository reconstruction every wake — compact Issue tail + top TO-DO is the cheaper hot path.
- Wall-clock padding — sleep/repetition/redundant I/O never counts as useful-work optimization.

## Open questions
1. PACKAGE_SIZE saturation beyond 22: LW17 probes 30–36 eligible units and semantic-output density, not just completion.
2. Long useful-work duration: larger packages increased WORKED directionally, but no evidence establishes a 10-minute guarantee; duration remains telemetry.
3. Persistence-boundary density: can artifact I/O be safely reduced for work classes with repeated zero-correction full-chain samples while preserving semantic non-inferiority?
4. Dispatch timing semantics: early/late offsets remain insufficient for deterministic scheduler law.
5. Cross-runtime generality: all findings remain relay-local until independently reproduced elsewhere.

## Promotion/edit contract
Every promoted mechanism records the failure/cost addressed, comparative/adverse relay-local evidence, added control cost, operational scope, and explicit demotion trigger. A plausible mechanism without these fields stays OPEN or SUPPORTED.
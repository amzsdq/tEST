# Relay Findings — Evidence Maturity Map

Status: LIVING EVIDENCE MAP
Origin: 2026-09-22 preliminary findings; updated through LW17 and LW18 frozen-repeat design.

## Purpose
Map hypotheses to current evidence maturity so later workers neither reopen settled questions nor turn bounded observations into universal laws. Evidence states: PROMOTED, SUPPORTED, REJECTED_AS_DEFAULT, OPEN. Every promotion is relay-local and scope-bound.

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
LW15-A/B completed 15 eligible units and LW16 completed 22/22 without saturation under one scheduler mutation/+3m lead. LW16 produced 11 semantic outputs (5.0/10 units), supporting capacity scaling through 22 without observed density collapse.

LW17 extended capacity evidence to 34/34 units with SATURATED=NO, but produced 14 outputs = 4.12/10, 0.01 below the frozen 4.13 guardrail. Therefore 34-unit capacity is SUPPORTED_WITH_DENSITY_WARNING, not promoted scale. LW18 repeats 34 under frozen counting before any larger scale-up.

Scope: semantic capacity only; no guaranteed wall-clock duration, greater reasoning depth, or arbitrary scaling beyond tested range.
Demotion: repeated larger packages fail eligibility, lose exact remainder, increase control I/O, or cross density guardrail without compensating auditable downstream value.

## Evidence freshness rule
A promotion is not timeless. Before a historical adverse sample or promotion controls a materially changed prompt/runtime/scheduler configuration, compare the fields relevant to that mechanism. If configuration drift is material, retain the evidence as historical but require fresh comparable evidence before blocking or promoting the changed candidate. Never silently discard old adverse evidence; mark its comparability.

## Supported but bounded findings

### 34-unit large-package capacity — SUPPORTED WITH DENSITY WARNING
LW17 completed 34/34 eligible units with no saturation and one scheduler mutation, proving tested execution capacity at that scale. Density 4.12/10 missed the experimental 4.13 guardrail. LW18 is the frozen repeat; >=4.13 with no saturation/remainder loss promotes the 30–36 scale, repeated <4.13 stops scale-up pending target-selection improvement unless a falsifiable value override is recorded.

### Recurrence as cold recovery — SUPPORTED
A missed near-term occurrence can leave recurrence intact and a later recurring wake can restore work; no precise fallback-latency guarantee is established.

### Durable authority — SUPPORTED WITH CONSTRAINT
Immutable epoch/fence plus atomic create-if-absent claim protects authority decisions. External side effects still require idempotency/reconciliation.

### Persisted-output review/revise chains — SUPPORTED AS QUALITY BOUNDARY
Fresh-fetch review can expose material defects and force later work to consume actual persisted state. I/O cost is separate from package-size capacity; thinning requires controlled non-inferiority evidence.

## Rejected defaults
- Provisional scheduler pre-arm every wake.
- Unconditional live scheduler reread.
- Broad repository reconstruction every wake.
- Wall-clock padding through sleep/repetition/redundant I/O.

## Open questions
1. 30–36 scale density: LW18 frozen repeat decides promotion vs stop-and-improve-target-selection.
2. Long useful-work duration: larger packages increased WORKED directionally, but no 10-minute guarantee exists.
3. Persistence-boundary density: can artifact I/O be safely reduced after repeated comparable low-correction full chains?
4. Dispatch timing semantics remain insufficient for deterministic scheduler law.
5. Cross-runtime generality remains untested.

## Promotion/edit contract
Every promoted mechanism records failure/cost addressed, comparative/adverse relay-local evidence, added control cost, operational scope, explicit demotion trigger, and evidence comparability/freshness. A plausible mechanism without these fields stays OPEN or SUPPORTED.
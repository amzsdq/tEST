# Relay Findings — Evidence Maturity Map

Status: LIVING EVIDENCE MAP
Origin: 2026-09-22 preliminary findings; updated through LW18 promotion and LW19 target-selection trial.

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

### Large pre-shaped TO-DO packages — PROMOTED FOR SEMANTIC CAPACITY AND DENSITY THROUGH 30–36 UNITS
LW15-A/B completed 15 eligible units, LW16 completed 22/22, and LW18 repeated 34/34 under the frozen counting contract with SATURATED=NO, 16 audited semantic outputs = 4.71/10, one scheduler mutation, +3m lead, and full persistence baseline. LW17's 14/34=4.12 warning was resolved by the frozen repeat rather than ignored.
Scope: semantic capacity+density under tested P5M4 conditions only; no guaranteed wall-clock duration, greater reasoning depth, or arbitrary scaling beyond 36.
Demotion: repeated 30–36 packages lose exact remainder, add control I/O, fail eligibility, or fall below the density guardrail without falsifiable compensating value.

## Evidence freshness rule
A promotion is not timeless. Before historical evidence controls a changed candidate, compare only fields capable of changing the mechanism's causal interpretation. Record `COMPARABILITY=CURRENT/DRIFTED` plus named drift fields. Drifted evidence remains historical and can guide tests, but cannot alone block/promote the changed candidate. Never silently discard adverse evidence.

## Supported but bounded findings
### Recurrence as cold recovery — SUPPORTED
A missed near-term occurrence can leave recurrence intact and a later recurring wake can restore work; no precise fallback-latency guarantee is established.

### Durable authority — SUPPORTED WITH CONSTRAINT
Immutable epoch/fence plus atomic create-if-absent claim protects authority decisions. External side effects still require idempotency/reconciliation.

### Persisted-output review/revise chains — SUPPORTED AS QUALITY BOUNDARY
Fresh-fetch review can expose material defects and force later work to consume actual persisted state. I/O cost is separate from package-size capacity; thinning requires controlled non-inferiority evidence.

## Open mechanisms
### Value-gated target selection — OPEN / LW19 ACTIVE
Hypothesis: at fixed ~34-unit package scale and unchanged persistence/control policy, predeclared scoring for decision reach, unresolved uncertainty, falsifiability, and downstream reuse can improve semantic-output density over LW18's 4.71/10 without post-hoc cherry-picking. Promotion requires controlled LW19 evidence; no current promotion is implied by plausibility.

### Long useful-work duration — OPEN
Larger packages increased useful work and reached multi-minute WORKED samples, but no 10-minute useful-work guarantee exists. Do not infer duration from unit count alone.

## R fresh-fetch review
TARGET=promotion truth; FAILURE_MODE=prior map still labeled 34-unit scale SUPPORTED_WITH_DENSITY_WARNING after LW18 had promoted it; REQUIRED_CHANGE=promote 30–36 with explicit scope/demotion. RESOLVED.
TARGET=target-selection causality; FAILURE_MODE=adding a scoring gate could be mistaken for already-proven improvement; REQUIRED_CHANGE=keep VALUE_GATED_TARGET_SELECTION OPEN until LW19 comparison completes. RESOLVED.
TARGET=duration inference; FAILURE_MODE=larger semantic capacity could be misread as a 10-minute guarantee; REQUIRED_CHANGE=retain duration as OPEN and explicitly forbid unit-count inference. RESOLVED.

R_VALIDATION=PASS. Evidence maturity now matches the canonical boundary while keeping the active target-selection mechanism and 10-minute duration question unpromoted.
SELECTED_BY=R_VALIDATION(target-selection remains open; persistence is a supported quality boundary and major I/O component) -> S focus: define how value-gated target selection interacts with persisted-output eligibility without letting high scores force ceremonial persistence.

## Rejected defaults
- Provisional scheduler pre-arm every wake.
- Unconditional live scheduler reread.
- Broad repository reconstruction every wake.
- Wall-clock padding through sleep/repetition/redundant I/O.

## Open questions
1. Can value-gated target selection improve density at fixed 30–36 scale?
2. Can artifact I/O be safely reduced after repeated comparable low-correction full chains?
3. What intrinsically useful workload reaches ~10 minutes without padding while preserving density?
4. Dispatch timing semantics remain insufficient for deterministic scheduler law.
5. Cross-runtime generality remains untested.

## Promotion/edit contract
Every promoted mechanism records failure/cost addressed, comparative/adverse relay-local evidence, added control cost, operational scope, explicit demotion trigger, and mechanism-specific evidence comparability/freshness. A plausible mechanism without these fields stays OPEN or SUPPORTED.
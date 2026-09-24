# Persisted-Output Transformation Protocol

## Purpose
Use persisted artifact boundaries to force later work to consume actual earlier outputs rather than an imagined in-memory draft. The mechanism is valuable when it improves semantic quality or decision reliability; it is not a wall-clock padding technique.

## Evidence baseline
- LW9 top-of-prompt TO-DO improved hot-start continuity but remained short.
- LW10 result-dependent lookup showed that dependency language alone is compressible.
- LW11/LW12 showed that persist → fresh fetch → review → defect-caused revision → fresh fetch validation produces useful sequential boundaries.
- LW15 showed larger pre-shaped packages can increase semantic capacity when every added unit is independently valuable.

Therefore this protocol is a **quality/dependency primitive inside eligible packages**, not a requirement that every task manufacture an artifact.

## Artifact eligibility gate
Use the chain only when all are true:
1. downstream decision value — the artifact can change a later experiment, prompt, recovery rule, or operational decision;
2. substantive uncertainty — at least one real semantic question or plausible defect exists before review;
3. revisionability — a material correction can be made in the current turn;
4. persistence value — reviewing persisted reality is meaningfully safer than reviewing an intended draft.

If any condition fails, use direct evidence-to-decision work. Never create a document merely to consume time or satisfy a unit quota.

## Canonical chain
1. Evidence baseline: state decision purpose, acceptance/failure criteria, and minimum necessary evidence.
2. Candidate persistence: materially construct/revise and persist the artifact.
3. Fresh-fetch review: fetch the persisted candidate; review that exact version against criteria.
4. Defect-caused revision: revise only material findings, with explicit defect→edit mapping.
5. Revision persistence: persist the corrected artifact.
6. Fresh-fetch validation: validate the actual persisted revision and issue PASS / RETEST / REJECT.

A stage is an eligibility-gated semantic boundary, not a quota. Zero review defects is valid when the artifact genuinely passes criteria; do not fabricate findings.

## Structured review contract
For each real defect record:
- TARGET — exact rule, claim, section, or omission;
- FAILURE_MODE — concrete operational/measurement consequence;
- REQUIRED_CHANGE — observable semantic correction.

Weak style preferences without downstream consequence do not count.

## Large-package composition
Multiple artifact chains may be composed when later targets depend on earlier validated results:

`E validation → select F question → F validation → select G question → synthesis`

Rules:
- do not precompute the substantive target of a declared result-dependent later artifact;
- every artifact independently passes the eligibility gate;
- synthesis counts only when it changes a future decision, not when it restates preceding sections;
- if runtime interrupts while eligible work remains, persist exact remaining units and resume there; do not replace them with a newly invented package.

## Measurement decomposition
Record separately:
- SEMANTIC_OUTPUTS — durable rules/decisions/spec changes surviving validation;
- DOWNSTREAM_DECISIONS_CHANGED;
- DEFECTS_FOUND / MATERIAL_DEFECTS_RESOLVED;
- ARTIFACT_IO_RAW — writes + fresh fetches;
- ARTIFACT_IO_PER_SEMANTIC_OUTPUT;
- CONTROL_IO — markers/baton/scheduler mutations;
- WORKED — GitHub START_MARKER→END_MARKER only;
- UNITS_PLANNED / DONE / REMAINING;
- SATURATED — YES only when runtime/blocker/safety interrupts while eligible units remain.

## Interpretation rules
- More WORKED with weak semantic gain is not promotion.
- More semantic outputs with unchanged control policy is evidence of capacity gain even if duration remains far below a desired wall-clock target.
- Artifact-I/O differences contaminate per-unit efficiency comparisons unless disclosed/normalized; they do not invalidate semantic-capacity comparisons when every unit is eligible.
- Package-size scaling and persisted-output transformation are separate variables: the former controls how much eligible work is pre-shaped; the latter supplies sequential validation boundaries inside suitable work.

## Failure criteria
REJECT or mark NON_COMPARABLE when:
- review uses an unpublished/in-memory draft instead of the persisted candidate;
- later result-dependent target was actually preselected;
- defects are fabricated to satisfy a count;
- revision merely appends commentary without correcting the target semantics;
- validation does not inspect the persisted revision;
- low-value artifacts or redundant I/O are added to increase elapsed time;
- work stops with eligible units remaining but no exact remainder is persisted.

## Promotion and demotion
Promote this protocol for a work class only when repeated eligible samples show semantic/downstream-value gain without extra scheduler/control cost.

Demote it for a work class when direct evidence-to-decision work produces equal semantic quality/reliability with less artifact I/O, or when persisted boundaries repeatedly add latency without causing material corrections.

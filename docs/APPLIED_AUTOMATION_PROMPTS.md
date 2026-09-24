# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M4 — Scalable Large TO-DO package candidate

State: EXPERIMENTAL / CAPACITY-PROMOTED THROUGH 22 ELIGIBLE UNITS / 34 SUPPORTED_WITH_DENSITY_WARNING
Parent: P5M3 dynamic TO-DO pointer
Primary variable: PACKAGE_SIZE
Rollback: P5M3

### Intent
P5M3 showed a concrete top-of-prompt TO-DO reduces startup reconstruction, but 5–6 unit packages remained compressible. P5M4 scales materially useful package work without adding scheduler/control mutations. LW15-A/B completed 15 eligible units, LW16 completed 22/22, and LW17 completed 34/34 with no saturation but density 4.12/10 versus frozen 4.13 guardrail. LW18 repeats 34 under frozen counting before any larger scale-up.

### Hot-path contract
- Keep `TO-DO LIST FOR THIS TURN` near the top and replace it at each continuing turn.
- Issue #1 remains authoritative durable state; TO-DO is a hot-path pointer.
- Same automation, exactly one final scheduler mutation, recurring `RRULE:FREQ=HOURLY`, +3m default lead.
- START/END GitHub server timestamps are the only WORKED clock.

### Unit eligibility gate
A unit is eligible only if omitting it removes decision-required evidence, a material durable semantic change, an independent persisted validation boundary, a defect-caused operational correction, or synthesis that changes a future experiment/prompt/recovery/promotion decision.

Bullet splitting, stylistic rewrites, repeated summaries, redundant fetches, synthetic checkpoints, fabricated defects, and low-value artifacts never create eligible units.

### Result-dependent target rule
Broad dependent stages may be named before START, but a declared later substantive target remains unresolved until preceding validation. Record `SELECTED_BY=<prior validated result> -> <later target>`. Missing mapping means no dependency credit.

### Scalable package shapes
- 12–15: normally two eligible artifact chains plus synthesis.
- 20–24: normally three chains plus synthesis.
- 30–36: normally four chains plus synthesis.

Shapes are not quotas. `NO_MORE_ELIGIBLE_WORK` is preferable to fabricated units. Runtime/blocker/safety interruption with eligible remainder is SATURATED and carries exact remainder.

### Persisted-output chain
When persistence adds decision value: evidence+criteria -> candidate persist -> fresh fetch -> criteria-first review -> real defect record -> defect-caused revision persist -> fresh fetch -> validation. Zero defects is valid; never invent defects.

### Frozen semantic-output contract for 30–36 repeat
A semantic output is one validated durable rule/spec/decision with a named downstream consequence. Log `OUTPUT_ID`, `DURABLE_CHANGE`, `DOWNSTREAM_CONSEQUENCE`, and `VALIDATED_BY`. Duplicate formulations sharing the same downstream consequence count once unless they independently alter different named decisions. Aggregation prose counts only if it changes a new named decision.

For LW18, density guardrail is frozen at 4.13 outputs per 10 actual eligible units. Raw count remains visible even if a value override is claimed. A value override must identify exact output(s), materially larger named consequence, dominated baseline output(s), and falsifiable dominance evidence; subjective quality claims are invalid.

### Saturation and exact handoff
`SATURATED=YES` only when runtime/external blocker/safety interrupts while eligible units remain. Record UNITS_DONE/REMAINING, exact artifact/stage, last validated result, and immediate next action. Next TO-DO begins with exact remainder.

### Measurement
Record UNITS_PLANNED/DONE/REMAINING, PACKAGE_COMPLETE/SATURATED, SEMANTIC_OUTPUTS plus IDs, SEMANTIC_OUTPUTS_PER_10_UNITS, DOWNSTREAM_DECISIONS_CHANGED, RESULT_DEPENDENT_TRANSITIONS, ARTIFACTS_CHANGED, ARTIFACT_IO_RAW, ARTIFACT_IO_PER_SEMANTIC_OUTPUT, CONTROL_IO, WORKED, and any valid VALUE_OVERRIDE.

Interpret separately: semantic capacity, semantic-output density, and wall time. Wall time alone never promotes. PACKAGE_SIZE remains promoted only while larger packages add eligible downstream value without extra control cost/remainder loss and without unadjudicated density degradation.

### Evidence freshness
Historical evidence remains evidence, but comparability is mechanism-specific. If materially relevant prompt/runtime/scheduler/eligibility/counting fields drift, record drift and require fresh comparable evidence before the historical result alone controls promotion/blocking.

### Recovery
If prompt TO-DO and Issue #1 disagree, Issue #1 wins. Incomplete large packages hand off exact remaining units and immediate next action.

---

## P4V11 — GitHub server timestamp work-duration source of truth

State: APPLIED
Parent: P4V10
Primary variable: work-duration time source only
Rollback: P4V10

- Append unique START_MARKER immediately before substantive work and matching END_MARKER after all substantive work and allowed final scheduler update.
- `WORKED = END_MARKER.created_at - START_MARKER.created_at` using GitHub server timestamps only.
- Model/local time strings are display-only; missing/ambiguous marker pair means WORKED=UNKNOWN.

## Promoted P4 hot-path invariants retained by P5M4
- Same automation identity; no new automation for normal continuation.
- One final recurring RRULE scheduler write on normal path.
- Issue #1 compact tail is routine bootstrap; broader documents are cold-path unless substantive evidence/boundary/recovery requires them.
- Wake, scheduler write/state, and useful work remain distinct observations.
- Simplicity is preferred only after recovery and duplicate-safety equivalence is established.

## Historical note
Earlier P0–P4 variants established the single-final-write recurring path, compact Issue evidence, Issue-tail bootstrap, conditional verification, positive-field omission, jitter telemetry, and GitHub-server WORKED clock. Detailed historical evidence remains in Issue #1 and experiment ledger.
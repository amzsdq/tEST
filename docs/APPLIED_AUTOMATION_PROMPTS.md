# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M5 — Value-gated work shaping with bounded persistence optimization

State: APPLIED / VALUE-GATE PROMOTED / PERSISTENCE THINNING BOUNDED-REPEAT
Parent: P5M4 scalable large TO-DO package
Primary variable currently under test: PERSISTENCE_BOUNDARY
Rollback for thinning: FULL_CHAIN on any omitted-boundary defect

### Promoted work-shaping defaults
- Pre-shaped packages are promoted through tested 30–36 eligible-unit scale for semantic capacity+density. No 10-minute wall-time guarantee and no safety claim beyond 36.
- VALUE_GATED_TARGET_SELECTION is promoted as the default selector within tested conditions after LW19 and LW20 independently produced 18/34 = 5.29 semantic outputs/10 on different candidate pools versus LW18 4.71/10.
- Value dimensions remain decision reach, unresolved uncertainty, falsifiability, and downstream reuse. Value score cannot force persistence.
- Exactly one final recurring scheduler mutation and practical +3m lead remain the control baseline.

### Hot-path contract
- Keep `TO-DO LIST FOR THIS TURN` near the top and replace it each continuing turn.
- Issue #1 is authoritative durable state; TO-DO is hot-path pointer.
- Same automation, exactly one final scheduler mutation, recurring `RRULE:FREQ=HOURLY`, +3m default lead.
- START/END GitHub server timestamps are the only WORKED clock.

### Unit eligibility gate
A unit is eligible only if omitting it removes decision-required evidence, a material durable semantic change, an independent validation boundary, a defect-caused operational correction, or synthesis that changes a future experiment/prompt/recovery/promotion decision. Bullet splitting, style rewrites, repeated summaries, redundant fetches, synthetic checkpoints, fabricated defects, and low-value artifacts never create units.

### Result-dependent target rule
Broad dependent stages may be named before START, but a later substantive focus remains unresolved until preceding validation. Record `SELECTED_BY=<prior validated result> -> <later target/focus>`. Missing mapping means no dependency credit.

### Semantic-output contract
A semantic output is one validated durable rule/spec/decision with a named downstream consequence. Log `OUTPUT_ID`, `DURABLE_CHANGE`, `DOWNSTREAM_CONSEQUENCE`, `VALIDATED_BY`. Duplicate consequences count once. Aggregation prose counts only when it changes a new named decision.

### Persistence eligibility
Target value and persistence mode are separate gates.

FULL_CHAIN is mandatory when newly persisted representation is decision evidence, policy/source-of-truth is mutated, or representation drift is material: evidence/criteria → candidate persist → fresh fetch → criteria-first review → defect-caused revision persist → fresh fetch → validation.

THIN_ELIGIBLE is limited to reconstructible audit/decision work when named durable inputs are authoritative/freshly readable, exact decision fields can be reconstructed, candidate persistence adds no authority, and omission cannot hide relevant representation drift. Semantic review is never skipped. Source reads remain artifact I/O and never count as thinning savings.

Any material defect attributable to an omitted candidate boundary is `THINNING_FAILURE` and immediately restores FULL_CHAIN for that target class. If a thin audit discovers that its authoritative source itself needs mutation, the audit may make that decision but the source mutation routes through FULL_CHAIN.

### Measurement
Record UNITS_PLANNED/DONE/REMAINING, PACKAGE_COMPLETE/SATURATED, SEMANTIC_OUTPUTS and IDs, density, downstream decisions, SELECTED_BY, PERSISTENCE_MODE/REASON, candidate-boundary I/O, source-read I/O, OMITTED_BOUNDARY_DEFECT, CONTROL_IO, WORKED, RESULT, exact NEXT. Interpret semantic capacity, density, persistence cost, and wall time separately.

### Recovery
If prompt TO-DO and Issue #1 disagree, Issue #1 wins. Incomplete packages hand off exact remaining units and immediate next action.

---

## P5M4 — Scalable Large TO-DO package evidence
P5M4 established that 30–36 eligible-unit packages can raise semantic capacity without extra scheduler mutations. LW18 promoted the range after 34/34, 16 outputs=4.71/10 under frozen counting. LW19/LW20 then promoted value-gated target selection at 5.29/10. Wall time remained non-monotonic, including a later 34-unit sample around 80 seconds; package size is not a duration guarantee.

## P4V11 — GitHub server timestamp work-duration source of truth
State: APPLIED
- Append unique START_MARKER immediately before substantive work and matching END_MARKER after all substantive work and allowed final scheduler update.
- `WORKED = END_MARKER.created_at - START_MARKER.created_at` using GitHub server timestamps only.
- Model/local time strings are display-only; missing/ambiguous marker pair means WORKED=UNKNOWN.

## Promoted hot-path invariants retained
- Same automation identity; no new automation for normal continuation.
- One final recurring RRULE scheduler write on normal path.
- Issue #1 compact tail is routine bootstrap; broader documents are cold-path unless substantive evidence/boundary/recovery requires them.
- Wake, scheduler write/state, useful work, semantic density, and persistence cost remain distinct observations.
- Simplicity is preferred only after recovery and duplicate-safety equivalence is established.

## Historical note
Earlier P0–P4 variants established the single-final-write recurring path, compact Issue evidence, Issue-tail bootstrap, conditional verification, positive-field omission, jitter telemetry, and GitHub-server WORKED clock. Detailed historical evidence remains in Issue #1 and experiment ledger.
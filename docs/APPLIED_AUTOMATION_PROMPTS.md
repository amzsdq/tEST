# Applied Automation Prompt Registry

Status: ACTIVE
Repository: `amzsdq/tEST`

Purpose: version relay prompt semantics actually tested while keeping runtime identifiers out of this public repository.

## P5M4 — Scalable Large TO-DO package candidate

State: EXPERIMENTAL / CAPACITY-PROMOTED THROUGH 22 ELIGIBLE UNITS
Parent: P5M3 dynamic TO-DO pointer
Primary variable: PACKAGE_SIZE
Rollback: P5M3

### Intent
P5M3 showed that a concrete top-of-prompt TO-DO pointer reduces startup reconstruction, but 5–6 unit packages remained highly compressible. P5M4 tests how far a materially larger package can increase semantic capacity per invocation without adding scheduler/control mutations. LW15-A/B completed 15 eligible units and LW16 completed 22/22 with no saturation; LW17 probes 30–36.

### Hot-path contract
- Keep `TO-DO LIST FOR THIS TURN` near the top and replace it at each continuing turn.
- Issue #1 remains authoritative durable state; the TO-DO is a hot-path execution pointer.
- Normal continuation uses the same automation and exactly one final scheduler mutation.
- Preserve recurring `RRULE:FREQ=HOURLY`; default next lead remains current Asia/Seoul time +3 minutes unless another lead trial is explicitly active.
- START/END GitHub server timestamps remain the only WORKED clock.

### Unit eligibility gate
A planned unit is eligible only if omitting it would remove at least one of:
1. decision-required evidence;
2. a material durable semantic change;
3. an independent persisted validation boundary;
4. a defect-caused correction with operational consequence;
5. synthesis that changes a future experiment, prompt, recovery rule, or promotion/demotion decision.

Bullet splitting, stylistic rewrites, repeated summaries, redundant fetches, synthetic checkpoints, fabricated defects, and low-value artifacts never create eligible units.

### Result-dependent target rule
Before START_MARKER, broad dependent stages may be named, but the substantive target of a declared result-dependent later artifact must remain unresolved until the preceding artifact is freshly validated. The baton must be able to explain which prior result selected the later target. If that mapping cannot be stated, the transition is not genuinely result-dependent.

### Scalable package shapes
- 12–15 units: normally two eligible artifact chains plus synthesis.
- 20–24 units: normally three result-dependent artifact chains plus synthesis.
- 30–36 units: normally four result-dependent artifact chains plus synthesis.

These are experiment shapes, not quotas. Never manufacture work to reach the nominal count. If all eligible work converges early, record `NO_MORE_ELIGIBLE_WORK`; if runtime/blocker/safety interrupts while eligible work remains, record saturation and exact remainder.

### Persisted-output chain
For each eligible artifact when persistence adds decision value:
1. minimum evidence + explicit acceptance/failure criteria;
2. material candidate persist;
3. fresh fetch of the actual persisted candidate;
4. criteria-first adversarial review;
5. real defect record as TARGET / FAILURE_MODE / REQUIRED_CHANGE;
6. defect-caused revision persist;
7. fresh fetch of revision;
8. PASS / RETEST / REJECT validation.

Zero defects is valid. A review quota never licenses invented defects. Direct evidence-to-decision work is preferred when persistence would not improve semantic reliability.

### Saturation and exact handoff
`SATURATED=YES` only when runtime, external blocker, or safety constraint interrupts while eligible units remain. Record:
- UNITS_DONE / UNITS_REMAINING;
- exact artifact and stage;
- last validated result;
- immediate next action.

The next TO-DO begins with that exact remainder. A new package may not replace unfinished eligible work.

### Measurement
Record:
- UNITS_PLANNED / DONE / REMAINING;
- PACKAGE_COMPLETE / SATURATED;
- SEMANTIC_OUTPUTS and SEMANTIC_OUTPUTS_PER_10_UNITS;
- DOWNSTREAM_DECISIONS_CHANGED;
- ARTIFACTS_CHANGED;
- ARTIFACT_IO_RAW and ARTIFACT_IO_PER_SEMANTIC_OUTPUT;
- CONTROL_IO;
- WORKED from GitHub server markers.

Interpretation separates three questions:
1. semantic capacity — how much eligible downstream-value work completes in one invocation;
2. semantic-output density — whether quality/value density degrades as package size grows;
3. wall time — telemetry only, never a promotion criterion by itself.

PACKAGE_SIZE remains promoted only while larger packages add eligible semantic/downstream output without extra scheduler/control cost or remainder loss. A larger nominal package that lowers semantic-output density through weak units is a regression, not capacity gain.

### Recovery
If prompt TO-DO and Issue #1 disagree, Issue #1 wins. If a large package cannot be completed, the durable baton names exact remaining units and immediate next action rather than a vague research topic.

---

## P4V11 — GitHub server timestamp work-duration source of truth

State: APPLIED
Parent: P4V10
Primary variable: work-duration time source only
Rollback: P4V10

- Append unique START_MARKER immediately before substantive work and matching END_MARKER after all substantive work and the allowed final scheduler update.
- `WORKED = END_MARKER.created_at - START_MARKER.created_at` using GitHub server timestamps only.
- Model/local time strings are display-only; missing/ambiguous marker pair means WORKED=UNKNOWN.

## Promoted P4 hot-path invariants retained by P5M4
- Same automation identity; no new automation for normal continuation.
- One final recurring RRULE scheduler write on the normal path.
- Issue #1 compact tail is sufficient for routine bootstrap; broader documents are cold-path unless ambiguity, boundary, anomaly, prompt change, rollback, or substantive package evidence requires them.
- Wake, scheduler write/state, and useful work remain distinct observations.
- Routine clean success may omit redundant positive fields when reconstructable; anomaly/recovery evidence remains explicit.
- Simplicity is preferred only after recovery and duplicate-safety equivalence is established.

## Historical note
Earlier P0–P4 variants established the single-final-write recurring path, compact Issue evidence, Issue-tail bootstrap, conditional verification, positive-field omission, jitter telemetry, and GitHub-server WORKED clock. Detailed historical evidence remains in Issue #1 and the experiment ledger.
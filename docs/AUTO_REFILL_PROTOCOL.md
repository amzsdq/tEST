# Same-Invocation Auto-Refill Protocol

Status: PROMOTED DEFAULT within tested P5M6+ conditions; E12 finalization-reserve optimization active

## Purpose and invariant
Use fast package completion as spare execution capacity. `PACKAGE_COMPLETE != TURN_COMPLETE`. A package is a bounded work-shaping unit; an invocation may contain many packages.

## Refill transition
After package N validates: persist one compact combined package-result/refill record; reassess parent GOAL; derive next value-gated substantive package if useful work remains; freeze persistence routing; execute N+1 immediately in the SAME invocation. The combined record replaces redundant package END + refill records. Do not mutate scheduler at refill boundaries; normal scheduler mutation occurs exactly once at actual invocation end.

## Valid stop conditions
PROGRAM_COMPLETE; genuine external blocker with no independent useful work; runtime/tool/safety limit; evidence-based NO_USEFUL_WORK_REMAINS. TO-DO/package/artifact/checkpoint/quota completion is not a stop condition.

## Eligibility and persistence
Refill never relaxes eligibility. Filler/sleep/padding/redundant work is invalid. VALUE_GATED_TARGET_SELECTION remains active. THIN_ELIGIBLE is restricted to reconstructible audit/decision work; authoritative mutation or representation-dependent validation uses FULL_CHAIN. Source reads remain artifact I/O.

## Scale
30–36 eligible units is per-package semantic-capacity guidance, not invocation cap or wall-time guarantee. Do not inflate one package merely to increase duration.

## Crash/recovery
Combined boundary records only the validated package and exact recovery pointer; never pre-claims next completion. `NEXT_PACKAGE` is a recovery pointer, not unconditional cold-start command. Cold recovery revalidates authority/value/persistence gates before side effects. Generic per-package START is not a correctness requirement; unsafe replay targets need effect-level stable identity plus authoritative receipt/status or equivalent checkpoint. Invocation START/END remain the WORKED clock.

## E12 finalization reserve
Elapsed time is a safety/admission signal only, never work quota. At substantive package admission boundaries compare external GitHub time to invocation START. A predeclared cutoff stops admission of a NEW substantive package; it does not interrupt an already-validating package. On reserve entry preserve exact remainder, write final baton, perform sole scheduler mutation, append END.

Normalize telemetry:
- D = last admitted boundary -> reserve entry (package exposure/overrun)
- A = reserve entry -> final baton
- B = final baton -> END, including scheduler mutation
- C = reserve entry -> END

Cutoff controls admission; it cannot bound D after admission. `PACKAGE_OVERRUN` is not reserve failure unless continuation is lost.

### E12 evidence
- LW26 cutoff 240s: A/B/C=22/31/53s, safe.
- LW27 cutoff 240s: A/B/C=13/21/34s, safe. 240s=`CONSERVATIVE_REPEAT_CONFIRMED`.
- LW28 cutoff 250s: A/B/C=11/26/37s, safe with overrun; last admission +224 -> reserve boundary +267 (43s exposure).
- LW29 cutoff 250s: A/B/C=8/17/25s, WORKED=282s, 33 packages / 156 conservative semantic outputs, one scheduler write, safe. Late exposures after +200s included 13s,6s,8s; edge admission +249 -> reserve +257.
- Therefore 250s is a TESTED CUTOFF within current relay/finalization conditions after independent LW28+LW29 samples. This is not a universal runtime ceiling or arbitrary-package guarantee.
- LW30 predeclares 260s as a separate directional step-down. One safe 260s sample remains directional and requires independent repeat before promotion.

### Frozen E12 rules
1. predeclare cutoff before live work;
2. package-boundary clock checks only; no per-action polling absent demonstrated need;
3. never tune cutoff within a live run;
4. do not sleep/pad or interrupt active validation to hit cutoff;
5. one safe step-down is directional; repeated same-cutoff safe continuation is required for promotion;
6. adverse/ambiguous 260s evidence rolls back to independently repeated 250s; 240s is older fallback only if shared-mode defect invalidates 250 evidence;
7. add class-specific admission guard only after repeated same-class long-tail evidence;
8. never infer a fixed runtime ceiling from sparse near-limit traces.

## Required combined package-result/refill fields
`PACKAGE`, `PACKAGE_COMPLETE=YES`, `RESULT`, `LAST_VALIDATION`, cumulative semantic/unit accounting when active, `NEXT_PACKAGE`, `SELECTED_BY`, `TURN_COMPLETE=NO`. Optional fields only when material.

## Invocation metrics
Record PACKAGES_COMPLETED, cumulative SEMANTIC_OUTPUTS, ARTIFACT_IO, REFILL_IO, CONTROL_IO, GitHub-server WORKED, STOP_REASON, exact NEXT/REMAINDER. E12 adds cutoff, last admission elapsed, reserve entry, D/A/B/C, PACKAGE_OVERRUN, continuation safety.

## Promotion evidence
LW24 demonstrated 11 substantive packages in one invocation; LW25 independently repeated multi-package refill and hardened cold stale-NEXT handling. AUTO_REFILL is therefore default within tested relay conditions. LW28+LW29 independently establish scoped 250s finalization-reserve admission evidence.

## Rollback / adverse evidence
Narrow or reject auto-refill on duplicate side effects, stale-authority overwrite, lost recovery state, extra scheduler mutations, material quality regression, counter inflation, or systematic low-value work. Runtime saturation itself is not failure if exact recovery state is preserved.
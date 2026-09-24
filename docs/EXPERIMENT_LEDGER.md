# Relay Experiment Ledger

## Canonical storage contract
Issue #1 is the canonical append-only raw experiment stream. Git history preserves prior ledger versions. This document is a compact boundary index; omission never means failed/deleted evidence.

## Promoted scheduler/recovery boundary
- One final recurring scheduler mutation is the normal control baseline.
- Practical +3m lead remains current; 2m has mixed evidence.
- Bounded Issue #1 tail is routine recovery authority; broader docs are cold-path.
- GitHub START/END `created_at` is the WORKED clock.
- Shared-automation early-wake/pre-arm is rejected under current primitives: observed runtime spread permits successor-before-release, while safe near continuation cannot be guaranteed without weakening single-owner/one-mutation invariants.

## Work-shaping / persistence boundary
| Trial | Result |
|---|---|
| LW18 | PROMOTE 30–36 eligible-unit per-package guidance |
| LW20 | PROMOTE VALUE_GATED_TARGET_SELECTION |
| LW22 | PROMOTE bounded THIN_ELIGIBLE; FULL_CHAIN retained for authoritative/representation-dependent work |
| LW24 | AUTO_REFILL directional pass |
| LW25 | PROMOTE AUTO_REFILL; cold NEXT revalidation hardened |
| LW34 | fixed-3 coalescing baseline 3 boundaries/3 outputs vs candidate 1/3; 66.7% package-boundary reduction |
| LW35 | cross-invocation reconstructible fixed-3 recovery PASS with no persisted node outputs |
| LW36 | one-mutation independently-receipted fixed-3 cold repeat PASS |
| LW37 | unavailable receipt authority -> UNKNOWN/no replay/no COMPLETE |
| LW38 | UNKNOWN->COMMITTED cold recovery PASS; remaining validation still required |
| LW39 | proof-bearing AUTHORITATIVE_NOT_FOUND -> retry eligibility only; weak/expired/incomplete negative evidence -> UNKNOWN |
| LW40 | pre-attempt negative proof causally consumed after attempt; absent fresh post-attempt receipt -> UNKNOWN/no replay/no COMPLETE; conservative real-effect retry requires durable pre-effect attempt/intent unless target authority supplies equivalent semantics |
| LW41B | durable attempt-intent -> emission -> COMMITTED cold recovery PASS; intent must precede effect emission on conservative path |
| LW42 | PROMOTE adapter-level TARGET_NATIVE_IDEMPOTENCY_ELIGIBLE under exact target contract; generic UNKNOWN retry remains forbidden |
| LW43 | adverse cold repeat retained capability; horizon/scope/key/payload negatives fail closed |
| LW44 | contract freshness and authoritative result-reconciliation domain made independent gates |
| LW45 | exact operation/version fingerprint invalidation repeat PASS; provider-wide capability rejected |
| LW46 | two emission policies cold-confirmed; native eligible path models 3->2 relay-controlled durable records when no new key write is needed |
| LW47 | pre-emission eligibility separated from post-emission recovery; attempt-time fingerprint provenance must be cold-reconstructible |
| LW48 | provenance five-case cold repeat PASS; native 3->2 retained only when key and attempt-time provenance need no new dedicated relay write; synthetic adapter sub-line converged |
| LW49 | authority/freshness precedence cold PASS; stale broad docs cannot roll back later scoped live evidence; no second CURRENT pointer |
| LW50 | shadow pre-arm timing found value but unsafe fixed start-relative offsets under observed runtime spread; live scheduler unchanged |
| LW51 | shared-automation early-wake/pre-arm formally REJECTED under current primitives; FINAL_ONLY_PLUS3 retained |
| LW52 | wrong propagated LW50 START reference recovered to unique semantic START; GitHub created_at pair corrected LW50 WORKED to 134s |
| LW53 | marker-reference integrity five-case cold PASS; exact-ID fast path plus conservative bounded semantic recovery promoted; marker ID is hint, validated GitHub identity/created_at is authority |
| LW54 | producer-boundary marker-reference validation five-case cold PASS; cheap direct identity read promoted as prevention while LW53 consumer fallback remains mandatory |
| LW55 | END-by-FINAL_BATON causal-backlink five-case cold PASS; minimal cross-invocation clock reference set promoted to PRIOR_START_ID + PRIOR_FINAL_BATON_ID; no propagated END ID required |
| LW56 | independent cold repeat PASS; recovered LW55 END from exact recognized baton backlink with no END ID, reconstructed GitHub-only WORKED=61s, one scheduler mutation and hourly recurrence intact |

## E12 finalization-reserve ledger
| Trial | Cutoff | D | A/B/C | Scheduler writes | Result |
|---|---:|---:|---|---:|---|
| LW26 | 240s | n/a | 22/31/53s | 1 | SAFE_DIRECTIONAL |
| LW27 | 240s | n/a | 13/21/34s | 1 | 240S_CONSERVATIVE_REPEAT_CONFIRMED |
| LW28 | 250s | 43s | 11/26/37s | 1 | 250S_DIRECTIONAL_SAFE |
| LW29 | 250s | 8s edge | 8/17/25s | 1 | PROMOTE_250S_TESTED |
| LW30 | 260s | 8s | 9/13/22s | 1 | 260S_DIRECTIONAL_SAFE |
| LW31 | 260s | 16s | 20/19/39s | 1 | PROMOTE_260S_TESTED |
| LW32 | 270s | 20s | 11/19/30s | 1 | 270S_DIRECTIONAL_SAFE |
| LW33 | 270s | 11s | 10/26/36s | 1 | PROMOTE_270S_SCOPED_TESTED; unique useful admission from +264s boundary |

## Current promoted boundaries
- 30–36 is per-package guidance, not invocation cap or wall-time guarantee.
- `PACKAGE_COMPLETE != TURN_COMPLETE`; same-invocation AUTO_REFILL is default while useful work remains.
- `NEXT_PACKAGE` is a recovery pointer, not an unconditional cold-start command.
- 270s is the scoped TESTED new-package admission cutoff; 260s remains tested fallback. Do not infer a universal runtime ceiling or continue cutoff chasing without new value evidence.
- Fixed n=3 coalescing is promoted only for shared-recovery-fate reconstructible groups and the narrow one-authoritative/idempotent-mutation receipt contract in `docs/COALESCING_PROTOCOL.md`.
- Unreceipted/non-idempotent, multiple-effect, larger/adaptive groups remain unpromoted.
- Required effect receipt and any mandatory pre-effect attempt/intent evidence are effect-level durability, not removable package-boundary I/O.
- Target-native exception is adapter-scoped only: exact fresh operation/version fingerprint, stable cold-recoverable key, canonical payload, valid protection horizon, authoritative result reconciliation, and cold-reconstructible attempt-time fingerprint provenance. Generic UNKNOWN retry remains forbidden.
- Native write-elision value is one relay-controlled durable record (3->2) only when neither key nor attempt-time provenance requires a new dedicated per-attempt relay write.
- Cross-invocation marker references use direct identity fetch as fast path/prevention and bounded semantic recovery on 404/mismatch. Zero/multiple candidates or START/END lineage mismatch leave WORKED UNKNOWN. No model-authored timestamp and no second marker pointer/cache.
- Minimal normal clock handoff is `PRIOR_START_ID + PRIOR_FINAL_BATON_ID`. Because END is created after the sole scheduler mutation, its ID is not propagated; the next invocation discovers exactly one recognized-schema END by exact FINAL_BATON backlink and validates START/automation/invocation lineage before using GitHub `created_at`. LW53 fallback remains available for damaged references.

## E12 telemetry contract
A=`RESERVE_ENTRY->FINAL_BATON`; B=`FINAL_BATON->END`; C=`RESERVE_ENTRY->END`; D=`last admitted boundary->reserve entry`. Cutoff controls admission, not interruption. PACKAGE_OVERRUN alone is non-adverse unless continuation is lost. Do not poll per action or sleep/pad.

## Semantic-output contract
A semantic output is one validated durable rule/specification/decision with a named downstream consequence. Summaries, stylistic edits, raw reads/writes, and restated evidence count zero. Audited counting requires OUTPUT_ID / DURABLE_CHANGE / DOWNSTREAM_CONSEQUENCE / VALIDATED_BY; otherwise report UNKNOWN.

## Reconciliation contract
Routine non-boundary evidence stays in Issue #1. Reconcile this index at sample-set completion, promotion/rejection/rollback, prompt-version boundary, or explicit evidence audit. The ledger must not become a mandatory hot-path read.

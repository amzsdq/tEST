# External Case Studies and Research Benchmarks v0.3

Status: ACTIVE REFERENCE
Repository: `amzsdq/tEST`

## Purpose
This benchmark layer extracts failure-handling invariants from mature systems and turns them into falsifiable relay tests. It is not evidence that ChatGPT Automation shares vendor semantics. Empirical evidence in this repository remains authoritative.

## Benchmark-to-experiment rule
A vendor pattern is actionable only when it yields:

```text
INVARIANT=<portable property>
APPLICABILITY=APPLICABLE|CONSTRAINED|REFERENCE_ONLY
RELAY_HYPOTHESIS=<what should hold here>
ADVERSE_TEST=<how to try to break it>
PROMOTION_EVIDENCE=<what repository evidence would justify adoption>
EVIDENCE_GRADE=OBSERVED|INFERRED|VENDOR_ONLY|NOT_RUN
```

`VENDOR_ONLY` evidence can justify the invariant but can never by itself promote relay behavior. If no discriminating adverse test or relay decision follows, classify REFERENCE_ONLY rather than forcing an experiment.

## 1. Temporal durable execution
- INVARIANT=worker/chat continuity is not required for correctness.
- APPLICABILITY=APPLICABLE to durable relay reconstruction.
- RELAY_HYPOTHESIS=a cold worker can reconstruct exact next valid action from durable state.
- ADVERSE_TEST=remove prior chat context and resume from Issue/repository state only.
- PROMOTION_EVIDENCE=multiple cold resumes recover exact package/NEXT without user repair or duplicate substantive effects.

## 2. AWS Step Functions execution guarantees
- INVARIANT=wake/transition success is not side-effect completion.
- APPLICABILITY=APPLICABLE when relay work has distinguishable scheduler/work/effect states.
- RELAY_HYPOTHESIS=WRITE_OK, scheduler STATE_OK, WAKE_OK, and WORK_OK remain separable when ambiguity matters.
- ADVERSE_TEST=successful wake with incomplete work or ambiguous external effect.
- PROMOTION_EVIDENCE=relay never upgrades wake evidence into completion and recovery selects the correct next action.

## 3. Kubernetes Lease leader election
- INVARIANT=authority and completion are separate facts.
- APPLICABILITY=CONSTRAINED; relevant only when multiple workers/takeover can contend for one logical job.
- RELAY_HYPOTHESIS=worker replacement transfers authority without assuming prior side effects.
- ADVERSE_TEST=interrupt authority holder around ambiguous side effect and reconstruct with successor.
- PROMOTION_EVIDENCE=successor neither duplicates a proven effect nor suppresses an unproven required effect.

## 4. Cloudflare Durable Objects Alarms
- INVARIANT=one mutable next wake can coexist with durable logical state; wake may require duplicate-safe handling.
- APPLICABILITY=APPLICABLE to the single-automation relay shape, not proof of ChatGPT scheduler delivery semantics.
- RELAY_HYPOTHESIS=one recurring automation plus durable baton is sufficient for continuation without per-turn automation creation.
- ADVERSE_TEST=duplicate/retry a wake and inspect substantive work identity/effects.
- PROMOTION_EVIDENCE=repeated continuation succeeds with one scheduler mutation per normal turn and duplicate wake does not create harmful duplicate work.

## 5. GitHub Actions concurrency groups
- INVARIANT=mutual exclusion is not effect identity/idempotency.
- APPLICABILITY=CONSTRAINED to designs with overlapping workers/runs.
- RELAY_HYPOTHESIS=logical package/effect identity survives worker/run replacement independently of concurrency.
- ADVERSE_TEST=replacement/retry under the same logical work id.
- PROMOTION_EVIDENCE=work identity remains stable and duplicate execution is prevented or safely idempotent.

## 6. Stripe idempotency keys
- INVARIANT=stable effect identity plus authoritative sink result is stronger than local success belief.
- APPLICABILITY=CONSTRAINED to external side effects that expose suitable identity/receipt semantics.
- RELAY_HYPOTHESIS=ambiguous retry can be resolved from durable effect identity/receipt when such a sink exists.
- ADVERSE_TEST=timeout/crash after request submission but before local acknowledgment.
- PROMOTION_EVIDENCE=recovery distinguishes already-applied from not-applied effects without duplication throughout supported recovery horizon.

## Cross-case benchmark principles
Reject or constrain a candidate that violates an applicable principle:
1. durable reconstruction;
2. wake != completion;
3. at-least-once tolerance when duplicate delivery/retry is possible;
4. stable logical work/effect identity where retries or replacement exist;
5. explicit authority where contention exists;
6. authoritative completion evidence for external effects;
7. evidence retention covers claimed recovery horizon;
8. fast path retains durable fallback;
9. concurrency control != idempotency;
10. simpler mechanism wins only after adverse testing.

## Decision scorecard
Use N/A rather than pretending every benchmark applies:

```text
DURABLE_RECONSTRUCTION=YES|NO|CONSTRAINED
WAKE_SEMANTICS=AT_LEAST_ONCE_SAFE|UNKNOWN|UNSAFE|N/A
STABLE_WORK_ID=YES|NO|N/A
STABLE_EFFECT_ID=YES|NO|N/A
EXCLUSIVE_AUTHORITY=YES|NO|N/A
AUTHORITATIVE_COMPLETION=YES|NO|N/A
RECOVERY_HORIZON_COVERED=YES|NO|UNKNOWN|N/A
FAST_PATH_HAS_DURABLE_FALLBACK=YES|NO|N/A
DUPLICATE_ADVERSE_TEST=PASS|FAIL|NOT_RUN|N/A
CRASH_ADVERSE_TEST=PASS|FAIL|NOT_RUN|N/A
MEASURED_CONTROL_IO=<value>
MEASURED_USEFUL_OUTPUT=<value>
MEASURED_CONTINUATION_RELIABILITY=<value>
EVIDENCE_GRADE=OBSERVED|INFERRED|VENDOR_ONLY|NOT_RUN
DECISION=ADOPT|RETEST|REJECT|REFERENCE_ONLY
```

### Evidence boundary
- `YES` requires repository evidence or directly observed runtime fact.
- `INFERRED` must not be presented as observed.
- `NOT_RUN` is never equivalent to PASS.
- Vendor documentation establishes only the external benchmark pattern, not ChatGPT relay behavior.

## Sources
- Temporal: https://docs.temporal.io/ ; https://docs.temporal.io/develop/worker-performance
- AWS Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html ; https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html
- Kubernetes Lease: https://kubernetes.io/docs/concepts/architecture/leases/ ; https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/
- Cloudflare Durable Objects Alarms: https://developers.cloudflare.com/durable-objects/api/alarms/ ; https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/
- GitHub Actions concurrency: https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency ; https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
- Stripe idempotency: https://docs.stripe.com/api/idempotent_requests

## Explicit non-goal
This document supplies invariants and adverse-test templates. Promotion still follows measured repository evidence and the active convergence protocol.
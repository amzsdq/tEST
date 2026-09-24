# External Case Studies and Research Benchmarks v0.2

Status: ACTIVE REFERENCE
Repository: `amzsdq/tEST`

## Purpose
This benchmark layer extracts failure-handling invariants from mature systems and turns them into falsifiable relay tests. It is not evidence that ChatGPT Automation shares vendor semantics. Empirical evidence in this repository remains authoritative.

## Benchmark-to-experiment rule
A vendor pattern is useful only when it yields all four fields below:

```text
INVARIANT=<portable property>
RELAY_HYPOTHESIS=<what should hold here>
ADVERSE_TEST=<how to try to break it>
PROMOTION_EVIDENCE=<what repository evidence would justify adoption>
```

Do not copy architecture mechanically. If a benchmark cannot produce a discriminating adverse test or decision, keep it reference-only.

## 1. Temporal durable execution
Observed pattern: workflow progress is durable rather than tied to one worker; workers can disappear and resume from history; faster paths can fall back to durable reconstruction.

Derived test:
- INVARIANT=worker/chat continuity is not required for correctness.
- RELAY_HYPOTHESIS=a cold worker can reconstruct exact next valid action from durable state.
- ADVERSE_TEST=remove prior chat context and resume from Issue/repository state only.
- PROMOTION_EVIDENCE=multiple cold resumes recover exact package/NEXT without user repair or duplicate substantive effects.

## 2. AWS Step Functions execution guarantees
Observed pattern: workflow types make execution guarantees explicit; retry semantics and side-effect safety are separate from state transition success.

Derived test:
- INVARIANT=wake/transition success is not side-effect completion.
- RELAY_HYPOTHESIS=WRITE_OK, scheduler STATE_OK, WAKE_OK, and WORK_OK can be distinguished when needed.
- ADVERSE_TEST=simulate/observe successful wake with incomplete work or ambiguous external effect.
- PROMOTION_EVIDENCE=relay never upgrades wake evidence into completion evidence and recovery selects the correct next action.

## 3. Kubernetes Lease leader election
Observed pattern: a lease grants temporary authority; expiration permits takeover; ownership does not prove prior work completion.

Derived test:
- INVARIANT=authority and completion are separate facts.
- RELAY_HYPOTHESIS=worker replacement can transfer authority without assuming prior side effects.
- ADVERSE_TEST=interrupt an authority holder around an ambiguous side effect and reconstruct with a successor.
- PROMOTION_EVIDENCE=successor neither duplicates a proven effect nor suppresses an unproven required effect.

## 4. Cloudflare Durable Objects Alarms
Observed pattern: one current alarm can point at the next durable event; alarms may be delivered at least once and handlers should be idempotent.

Derived test:
- INVARIANT=one mutable next wake can coexist with durable logical state.
- RELAY_HYPOTHESIS=one recurring automation plus durable baton is sufficient for continuation without per-turn automation creation.
- ADVERSE_TEST=duplicate/retry a wake and test whether substantive work identity prevents harmful duplication.
- PROMOTION_EVIDENCE=repeated continuation succeeds with one scheduler mutation per normal turn and duplicate wake does not create duplicate substantive effects.

## 5. GitHub Actions concurrency groups
Observed pattern: concurrency exclusion controls simultaneous runs but does not identify logical work or guarantee idempotency.

Derived test:
- INVARIANT=mutual exclusion is not effect identity.
- RELAY_HYPOTHESIS=logical package/effect identity survives worker/run replacement independently of concurrency.
- ADVERSE_TEST=allow replacement/retry under the same logical work id and inspect external effects.
- PROMOTION_EVIDENCE=work identity remains stable and duplicate execution is either prevented or safely idempotent.

## 6. Stripe idempotency keys
Observed pattern: retries sharing an idempotency key can resolve to the stored first result; safety depends on evidence retention horizon.

Derived test:
- INVARIANT=stable effect identity plus authoritative sink result is stronger than local success belief.
- RELAY_HYPOTHESIS=ambiguous retry can be resolved from durable effect identity/receipt when an external side effect exists.
- ADVERSE_TEST=timeout/crash after request submission but before local acknowledgment.
- PROMOTION_EVIDENCE=recovery can distinguish already-applied from not-applied effects without duplication throughout the supported recovery horizon.

## Cross-case benchmark principles
Reject or constrain a candidate that violates an applicable principle:
1. durable reconstruction;
2. wake != completion;
3. at-least-once tolerance;
4. stable logical work/effect identity;
5. explicit authority;
6. authoritative completion evidence;
7. evidence retention covers recovery horizon;
8. fast path retains durable fallback;
9. concurrency control != idempotency;
10. simpler mechanism wins only after adverse testing.

## Decision scorecard
For a candidate architecture or prompt mechanism, record only applicable fields:

```text
DURABLE_RECONSTRUCTION=YES|NO|CONSTRAINED
WAKE_SEMANTICS=AT_LEAST_ONCE_SAFE|UNKNOWN|UNSAFE
STABLE_WORK_ID=YES|NO
STABLE_EFFECT_ID=YES|NO|N/A
EXCLUSIVE_AUTHORITY=YES|NO|N/A
AUTHORITATIVE_COMPLETION=YES|NO|N/A
RECOVERY_HORIZON_COVERED=YES|NO|UNKNOWN|N/A
FAST_PATH_HAS_DURABLE_FALLBACK=YES|NO
DUPLICATE_ADVERSE_TEST=PASS|FAIL|NOT_RUN|N/A
CRASH_ADVERSE_TEST=PASS|FAIL|NOT_RUN|N/A
MEASURED_CONTROL_IO=<value>
MEASURED_USEFUL_OUTPUT=<value>
MEASURED_CONTINUATION_RELIABILITY=<value>
DECISION=ADOPT|RETEST|REJECT|REFERENCE_ONLY
```

### Evidence boundary
A `YES` requires repository evidence or a directly observed runtime fact. Vendor documentation can justify the benchmark invariant but cannot make a ChatGPT relay score `YES`. `NOT_RUN` remains distinct from `PASS`.

## Sources
- Temporal: https://docs.temporal.io/ ; https://docs.temporal.io/develop/worker-performance
- AWS Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html ; https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html
- Kubernetes Lease: https://kubernetes.io/docs/concepts/architecture/leases/ ; https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/
- Cloudflare Durable Objects Alarms: https://developers.cloudflare.com/durable-objects/api/alarms/ ; https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/
- GitHub Actions concurrency: https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency ; https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
- Stripe idempotency: https://docs.stripe.com/api/idempotent_requests

## Explicit non-goal
This document supplies invariants and adverse-test templates. Promotion still follows measured repository evidence and the active convergence protocol.
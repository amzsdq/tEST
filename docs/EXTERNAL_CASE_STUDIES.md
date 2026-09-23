# External Case Studies and Research Benchmarks v0.1

Status: ACTIVE REFERENCE
Repository: `amzsdq/tEST`

## Purpose

This document is a benchmark layer for the relay experiments. It is not evidence that ChatGPT Automation behaves like these systems.

Use it to:
- identify mature distributed-systems patterns worth testing;
- detect reinvention of solved primitives;
- define adverse tests and promotion criteria;
- prefer simpler mechanisms when they preserve the same safety properties.

Empirical evidence from this repository remains authoritative for ChatGPT Automation behavior.

## Case study 1 — Temporal durable execution

Observed pattern:
- workflow progress is represented durably rather than being tied to one worker process;
- workers may disappear and later resume work from persisted execution history;
- latency optimizations can fall back to a slower durable path after failure.

Relevant lesson for this repository:
- worker/chat continuity should not be required for correctness;
- durable reconstruction is more important than keeping one worker alive;
- fast continuation should be an optimization over a recoverable durable path.

Maps to:
- E8 Durable cold-resume
- checkpoint reconstruction
- disposable-worker design

Source:
- https://docs.temporal.io/
- https://docs.temporal.io/develop/worker-performance

## Case study 2 — AWS Step Functions execution guarantees

Observed pattern:
- Standard Workflows persist execution state between transitions and use an exactly-once workflow execution model unless explicit retry behavior is configured;
- Express Workflows trade stronger execution guarantees for higher-throughput at-least-once or at-most-once semantics depending on mode.

Relevant lesson:
- execution semantics must be explicit;
- non-idempotent effects require stronger authority than merely “the wake happened”;
- reliability and throughput/latency are separate axes.

Maps to:
- WRITE_OK / STATE_OK / WAKE_OK / WORK_OK separation
- E7 Duplicate authority
- side-effect receipt/idempotency research

Source:
- https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html
- https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html

## Case study 3 — Kubernetes Lease leader election

Observed pattern:
- a Lease is a lightweight durable coordination object;
- only one candidate owns leadership at a time;
- leadership expires if it is not renewed;
- another candidate may take over after failure.

Relevant lesson:
- a lease proves temporary authority, not task completion;
- lease identity and expiration must be durable and reconstructable;
- takeover must not imply that prior side effects did or did not happen.

Maps to:
- E7 Duplicate authority
- lease/epoch design
- recovery after worker disappearance

Source:
- https://kubernetes.io/docs/concepts/architecture/leases/
- https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/

## Case study 4 — Cloudflare Durable Objects Alarms

Observed pattern:
- each Durable Object has one current alarm;
- alarms are at-least-once and may be retried;
- documentation explicitly recommends idempotent alarm handlers;
- many logical scheduled events can be stored durably while one alarm points at the next due event.

Relevant lesson:
- a wake primitive should not be treated as exactly-once;
- “one mutable next wake + durable logical schedule” is a proven simplification pattern;
- duplicate-safe work is required even when the scheduler itself is durable.

Maps to:
- E2 Minimum lead-time search
- E3 final-writer behavior
- E5 Missed-wake recovery
- single recurring automation + durable state

Source:
- https://developers.cloudflare.com/durable-objects/api/alarms/
- https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/

## Case study 5 — GitHub Actions concurrency groups

Observed pattern:
- concurrency groups can restrict execution so that only one run in a group is active at a time;
- pending/cancel/queue policy is distinct from the identity of the logical work being performed.

Relevant lesson:
- concurrency exclusion is not the same thing as idempotency;
- preventing two workers from running simultaneously does not prove an external side effect occurred exactly once;
- work identity must survive worker/run replacement.

Maps to:
- E7 Duplicate authority
- stable work-item identity
- avoiding “current worker == logical job” assumptions

Source:
- https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency
- https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency

## Case study 6 — Stripe idempotency keys

Observed pattern:
- retries with the same idempotency key return the stored result of the first request;
- key retention is finite, so retry safety depends on the retention horizon;
- the idempotency key identifies one logical operation across network uncertainty.

Relevant lesson:
- stable effect identity is a first-class primitive;
- recovery correctness depends on the idempotency evidence living at least as long as the recovery horizon;
- local “I think it succeeded” state is weaker than an authoritative sink-side result.

Maps to:
- stable effect identity experiments
- receipt elimination when the sink is authoritative
- timeout/crash ambiguity tests

Source:
- https://docs.stripe.com/api/idempotent_requests

## Derived benchmark principles

A candidate relay design should be rejected or explicitly constrained if it violates any applicable principle below:

1. **Durable reconstruction** — a fresh worker can determine the next valid action without the previous worker's chat state.
2. **Wake != completion** — scheduler delivery is never treated as proof that useful work or an external side effect completed.
3. **At-least-once tolerance** — duplicate wake or retry must not create duplicate substantive side effects.
4. **Stable logical identity** — work/effect identity survives retry, worker replacement, and timing changes.
5. **Authority is explicit** — lease/ownership identifies who may act, not what has already completed.
6. **Completion evidence is authoritative** — completion comes from durable receipt/state or an authoritative idempotent sink.
7. **Recovery horizon is bounded by evidence retention** — idempotency/receipt data must outlive the longest supported recovery interval.
8. **Fast path has a slower durable fallback** — latency optimization must not remove the reconstructable path.
9. **Concurrency control is not idempotency** — both are evaluated separately when both are needed.
10. **Simpler wins only after adverse testing** — fewer states/writes are preferred only if recovery and duplicate safety remain equivalent.

## Research scorecard

For every candidate architecture, record:

```text
DURABLE_RECONSTRUCTION=YES|NO|CONSTRAINED
WAKE_SEMANTICS=AT_LEAST_ONCE_SAFE|UNKNOWN|UNSAFE
STABLE_WORK_ID=YES|NO
STABLE_EFFECT_ID=YES|NO|N/A
EXCLUSIVE_AUTHORITY=YES|NO|N/A
AUTHORITATIVE_COMPLETION=YES|NO|N/A
RECOVERY_HORIZON_COVERED=YES|NO|UNKNOWN
FAST_PATH_HAS_DURABLE_FALLBACK=YES|NO
DUPLICATE_ADVERSE_TEST=PASS|FAIL|NOT_RUN
CRASH_ADVERSE_TEST=PASS|FAIL|NOT_RUN
MEASURED_OVERHEAD=<value>
MEASURED_CONTINUATION_RELIABILITY=<value>
```

This scorecard is diagnostic, not a weighted ranking. Promotion still follows measured repository evidence and the promotion rules in `RELAY_RESEARCH_PROGRAM.md`.

## Explicit non-goal

Do not copy vendor architecture mechanically. The useful unit is the invariant or failure-handling pattern, then a controlled experiment against ChatGPT Automation.

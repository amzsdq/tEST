# Relay Research Sandbox

Repository: `amzsdq/tEST`

Purpose: isolated research on ChatGPT Automation relay/continuation mechanisms without mutating production repositories.

## Scope

Research targets:
- same-automation self-update with recurring RRULE
- minimum safe lead time between self-update and next wake
- scheduler dispatch jitter / missed-near-term occurrence behavior
- one-shot vs recurring RRULE continuity
- final-writer semantics for schedule mutation
- provisional crash-insurance wake vs final fast continuation
- cross-automation wake behavior
- UI **Run now** semantics vs schedule mutation
- duplicate/overlap prevention and authority fencing
- durable checkpoint + cold-resume behavior
- failure recovery when a scheduled occurrence is missed

## Safety boundaries

- This repository is a sandbox.
- Do not mutate `R`, `RRuleR`, or `RRuleRO` as part of experiments here.
- Never store credentials, session state, cookies, conversation URLs, private callback routes, or secrets.
- Use synthetic identifiers in public artifacts.
- Record observed facts separately from hypotheses.

## Evidence rule

Every experiment should record:
1. hypothesis
2. exact schedule form
3. intended due time
4. actual update time
5. actual invocation time when observed
6. automation enabled/recurrence state
7. result: PASS / FAIL / INCONCLUSIVE
8. interpretation and next experiment

The goal is not to make a relay appear reliable; the goal is to find the smallest mechanism that remains reliable under repeated empirical tests.

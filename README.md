# Relay Research Sandbox

Repository: `amzsdq/tEST`

Purpose: isolated research on ChatGPT Automation relay/continuation mechanisms without mutating production repositories.

## Current scope

Research targets include:
- same-automation self-update with recurring RRULE and one final scheduler mutation
- practical lead-time and scheduler dispatch jitter / missed-near-term behavior
- duplicate/overlap prevention, authority fencing, durable checkpointing, and cold recovery
- useful-work/package shaping and value-gated target selection
- bounded persistence routing (`FULL_CHAIN` vs reconstructible `THIN_ELIGIBLE`)
- same-invocation auto-refill where `PACKAGE_COMPLETE != TURN_COMPLETE`
- invocation-tail/finalization reserve so refill does not consume the opportunity to persist continuation
- semantic useful-output density, artifact/control I/O, packages per invocation, and GitHub-server WORKED telemetry as separate metrics

Historical one-shot/provisional/cross-automation/UI experiments remain evidence in Issue #1 and git history; they are not automatically current defaults.

## Safety boundaries

- This repository is a sandbox.
- Do not mutate `R`, `RRuleR`, or `RRuleRO` as part of experiments here.
- Never store credentials, session state, cookies, conversation URLs, private callback routes, or secrets.
- Use synthetic identifiers in public artifacts.
- Record observed facts separately from hypotheses.

## Evidence rule

Every experiment records the evidence appropriate to its tested layer. Scheduler trials separate write/state/wake/work evidence. Work-shaping trials separate semantic outputs from wall time. Persistence trials separate source-read I/O from candidate-boundary I/O. Auto-refill trials preserve exact recovery state. Finalization-reserve trials use GitHub server timestamps and normalized A/B/C tail telemetry.

Promotion requires repeated evidence. One favorable trace is directional only, and a result may only promote the layer actually tested. The goal is not to make a relay appear reliable; the goal is to find the smallest mechanism that remains reliable under repeated empirical tests.
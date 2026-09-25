# LT04 migration notes

The runtime validator remains authoritative; schema files are contract artifacts and are not currently executed by validator.py.

Evidence version semantics:
- missing evidence_version: legacy v1
- explicit 1: v1
- explicit 2: v2
- booleans, strings, and unsupported integers: reject
- normalization preserves deprecated cross_invocation_sum_seconds so the semantic validator can continue emitting CROSS_INVOCATION_SUM_FORBIDDEN.

LT03 history policy:
- observations.json remains unchanged and retains the 833-second censored historical record.
- exact_evidence.json stores later recognized START/END evidence separately.
- authority selection requires matching invocation, automation, and exact START marker.
- recognized exact evidence supersedes the censored record for current authority without rewriting historical evidence.

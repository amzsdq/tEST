# LT04 staged validation results

Local deterministic smoke checks against the exact staged logic passed:

- authority selector: exact LT03 duration = 940 seconds; target_crossed = true.
- historical LT03 observation remains censored with exact_duration_seconds = null and lower bound = 833 seconds.
- LT02 remains exact 411 seconds and below target.
- ambiguous duplicate exact authority fails closed.
- versioning helper: missing version maps to v1; explicit v2 accepted; boolean/string/0/3 rejected.
- normalization preserves cross_invocation_sum_seconds for downstream semantic rejection.

These are staging checks. Main-branch acceptance remains pending because safety checks blocked modifications to existing canonical source files during this invocation.

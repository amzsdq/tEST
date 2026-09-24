# Long-turn capability classification

Do not collapse a runtime sample into available/impossible.

- `DIRECT_UNAVAILABLE`: the product exposes no direct primitive for the requested behavior. This is a product-surface claim, not inferred from a short run.
- `WORKAROUND_AVAILABLE`: one-turn behavior is not directly provided but a composition of supported primitives achieves the same externally required result. Multiple invocations may qualify for a logical-session workaround, but **must not** be reported as one-turn 900s success.
- `CONSTRAINED`: the behavior is observed only under some workload/context/tool conditions, or evidence is insufficient to generalize. A verified 411s run plus no 900s run belongs here until stronger evidence arrives.
- `PHYSICALLY_IMPOSSIBLE`: reserved for repeated evidence establishing a hard execution-host/power/network/platform ceiling that makes the target physically unattainable. One censored/short sample is insufficient.
- `POLICY_BLOCKED`: technically possible but prohibited by governing policy. This must cite the policy boundary; it cannot be inferred from runtime silence.

## Mapping from validator evidence

`VOLUNTARY_FINAL` with exact duration >= target is positive one-turn capability evidence for that sample. `VOLUNTARY_FINAL` below target proves only that the sample ended below target. `ABRUPT_NONFINAL` supplies a survival lower bound, not a cause. `TOOLPATH_LOSS_CANDIDATE` and `PLATFORM_RUNTIME_KILL_CANDIDATE` remain causal hypotheses until independently discriminated. `UNKNOWN` cannot support a strong capability class.

Current LT03 prior: LT02 exact WORKED=411s demonstrates >270s operation but not 900s capability. Therefore the 15-minute target remains `CONSTRAINED / UNPROVEN`, not `PHYSICALLY_IMPOSSIBLE` and not `DIRECT_UNAVAILABLE`.

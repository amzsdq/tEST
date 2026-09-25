# Long-turn capability classification

- `DIRECT_UNAVAILABLE`: no direct product primitive.
- `WORKAROUND_AVAILABLE`: supported primitive composition achieves the required result.
- `CONSTRAINED`: observed under specific workload/context/tool conditions or not yet generalized.
- `PHYSICALLY_IMPOSSIBLE`: requires evidence of a hard physical/platform ceiling.
- `POLICY_BLOCKED`: technically possible but prohibited by governing policy.

## Current evidence

LT03 exact one-turn WORKED=940s proves the >=900-second target for that sample. LT04-R118-T6B independently measured one-turn WORKED=1191s, providing an independent >=900 repeat.

Therefore >=900 is no longer UNPROVEN. The broader capability remains `CONSTRAINED` because evidence is workload/tool-path specific, but it is neither `PHYSICALLY_IMPOSSIBLE` nor `DIRECT_UNAVAILABLE`.

The >=1200-second stretch remains unproven by the 1191-second sample. Nine missing seconds must not be rounded away.

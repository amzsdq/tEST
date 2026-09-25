# Long-turn capability classification

- `DIRECT_UNAVAILABLE`: no direct product primitive.
- `WORKAROUND_AVAILABLE`: supported primitive composition achieves the required result.
- `CONSTRAINED`: observed under specific workload/context/tool conditions or not yet generalized.
- `PHYSICALLY_IMPOSSIBLE`: requires evidence of a hard physical/platform ceiling.
- `POLICY_BLOCKED`: technically possible but prohibited by governing policy.

## Current evidence

LT03 exact one-turn WORKED=940s proves the >=900-second target for that sample. LT04-R118-T6B independently measured one-turn WORKED=1191s, providing an independent >=900 repeat.

Therefore >=900 is no longer UNPROVEN. The broader capability remains `CONSTRAINED` because evidence is workload/tool-path specific, but it is neither `PHYSICALLY_IMPOSSIBLE` nor `DIRECT_UNAVAILABLE`.

The >=1200-second stretch is now proven by LT04-R126-T9 at exactly 1219s (20:19) on one same-branch GitHub commit-clock session. This is an independent stretch PASS; it is not rounded and no invocations are summed.


## Release verification status

R126 pins the exact canonical runner dependency closure by Git blob SHA and readback, but unchanged end-to-end runner execution remains PENDING until an exact-byte execution bridge is available. Supplemental direct/property checks do not substitute for that gate. A repository-native GitHub Actions execution path was explored but workflow mutation was safety-blocked before application; readback confirmed the probe branch contains no workflow delta.

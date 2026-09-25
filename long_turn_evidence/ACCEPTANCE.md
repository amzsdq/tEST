# LT04 acceptance matrix

| Obligation | Evidence | State |
|---|---|---|
| >=900 one-turn capability | LT03 exact 940s | PASS |
| independent >=900 repeat | LT04-R118-T6B exact 1191s | PASS |
| >=1200 stretch | LT04-R126-T9 exact 1219s | PASS |
| no cross-invocation sum | validator diagnostic | PASS |
| historical record preserved | observations.json 19d020b7... | PASS |
| exact-over-censored authority | authority 8d64d694... + test c4b185e1... | CANDIDATE VERIFIED |
| exact canonical runner blob set | R162 pin bb8d5b99...; 29/29 tree audit | PASS |
| unchanged exact canonical runner execution | rc=0 + LT04_CANONICAL_CHECKS_PASS | PENDING |
| schema/runtime identity parity | schemas and runtime reject malformed identities | CANDIDATE VERIFIED |
| structural schema/runtime parity | R157 consumer package + R162 explicit schema regression coverage | CANDIDATE VERIFIED |
| canonical raw-GitHub timestamp contract | shared parser/schema + R157 consumers | CANDIDATE VERIFIED |
| MANIFEST identity current | R162 MANIFEST binds current pin/source and identities | PASS |

R162 binding note: FULL_RUNNER remains PENDING until unchanged exact runner execution succeeds. Pin/MANIFEST PASS does not imply runner execution or main integration.

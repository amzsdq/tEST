# LT04 artifact manifest

Canonical migration candidate includes admission stretch policy, evidence v1/v2 normalization, schema contract, separate exact evidence, hardened authority selection, canonical observation authority validation, generic scheduler-v2, and commit-clock recovery.

Verified runtime evidence:
- LT03: exact 940s, >=900 PASS.
- LT04-R118-T6B: exact 1191s, independent >=900 repeat PASS, 1200 stretch not yet passed.
- Historical observations.json blob remains 19d020b7b5918211124f0d6ada5895318cf12854 and is not rewritten.

Admission candidate blobs: module 54e6e7eb1a08ed9ba3ef8e84a1f1797bba773146; tests d94ebabca79fb6a0eb99f8e2b867313e853e268c.
Validator/versioning candidate blobs: validator ddb4fce0a4eba78c3f0d4af3a676cc87c0ee47b9; versioning b75eeceeae115baebb6cb41d6459b6c984d19379; schema f004e260ad08408c3e2596be84a7ddd3703edfba.
Authority candidate blob: d6d09f0781e9a37814a8cd4b9a2f73969c7edfdd.

Lineage hardening candidate blobs: lineage 14463582633e50c843bb6f78e9b074eb79365497; tests db96d77a59e8c9c483d0f62547a2eca93266b5fe.

Commit-clock recurrence hardening blobs: recovery ed81dd73cb2e7fec81610caadab03fc06c901d8b; tests 45201ea86972839bdbabdd13c6ee8b7a09fbeb11. Prefix-spoof RRULE values are fail-closed.

Scheduler-v2 DTSTART hardening blobs: scheduler f876c48a9e4f1ad587e5cff4f07eae4e8c54b6a7; tests 8d3291704bc0373c14bc89a41efcebb9690cf88b. Duplicate/spoofed DTSTART is fail-closed.
Commit-clock exact RRULE parser blobs: recovery 1475705f2a21b3d0c986c37df7cfeb71d620e3a0; tests cef6ef5bffb7d448c42a8e9af175e39c375e05b5. Duplicate/conflicting FREQ is fail-closed.

Remaining release gates are full canonical regression execution, main-branch integration/readback, and an independent >=1200 useful-work sample if qualifying work remains.

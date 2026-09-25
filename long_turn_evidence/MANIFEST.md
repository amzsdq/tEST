# LT04 artifact manifest

Canonical migration candidate includes admission stretch policy, evidence v1/v2 normalization, schema contract, separate exact evidence, hardened authority selection, canonical observation authority validation, generic scheduler-v2, and commit-clock recovery.

Verified runtime evidence:
- LT03: exact 940s, >=900 PASS.
- LT04-R118-T6B: exact 1191s, independent >=900 repeat PASS; this invocation remained 9s short of 1200.
- LT04-R126-T9: exact 1219s (20:19), independent same-branch >=1200 stretch PASS.
- Historical observations.json blob remains 19d020b7b5918211124f0d6ada5895318cf12854 and is not rewritten.

Admission candidate blobs: module 54e6e7eb1a08ed9ba3ef8e84a1f1797bba773146; tests d94ebabca79fb6a0eb99f8e2b867313e853e268c.
Validator/versioning candidate blobs: validator c9c31cfaa01747ca34070e78de410414f3a2f0eb; versioning b75eeceeae115baebb6cb41d6459b6c984d19379; schema f004e260ad08408c3e2596be84a7ddd3703edfba.
Authority candidate blob: 08a594565ec8bff195dbcc34eb8e1bb0885cfa69; tests ddc746023ecec0d5f91803254f1de498288181f0. Runtime invocation/automation/supersedes identities fail closed when missing, blank, or malformed.

Lineage hardening candidate blobs: lineage 14463582633e50c843bb6f78e9b074eb79365497; tests db96d77a59e8c9c483d0f62547a2eca93266b5fe.

Commit-clock recurrence hardening release-current blobs: recovery 6bd21ca7c32063d897e5829165fad5757f8afdf4; tests 70fd5b1e48849a1057a16b0b51de0f29f67edb1f. Verified START, exact_schedule, enabled state, and exactly one unbounded FREQ=HOURLY recurrence are required; COUNT/UNTIL/INTERVAL, prefix spoofing, conflicting representations, and malformed VEVENT readback fail closed.

Scheduler-v2 DTSTART hardening blobs: scheduler 3e6eb460435cb79ccbe5b3fa1315fa3eed074807; tests 9fd07d3ec6ee913e1893963ea1bc2cd14fa0fbf5. Duplicate/spoofed DTSTART is fail-closed.
Legacy recovery release-current blobs: recovery 7ea60695f642fb44f12fc1cafdbfa8b688c7ff10; tests 7ef058c6a41fb581625f31c41c605160dfff2c9e. Shape-valid END and durable-boundary timestamps must not precede START.
Exact canonical runner blob: e1f6cee2b42951333797d27cd7b8e12436133b19. Exact input pin manifest blob: db779b0084ec4c33879f5059683b672df7d9f10a; fresh R142 recursive-tree audit confirms 29/29 identities.

Remaining release gates are full canonical regression execution and main-branch integration/readback. The independent >=1200 useful-work sample gate is PASS via LT04-R126-T9.

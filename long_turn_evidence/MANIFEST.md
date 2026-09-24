# LT03 artifact manifest

Core: `validator.py`, `schema.json`, `fixtures.json`, `observations.json`, lineage/recovery/scheduler/admission modules, report generator, and authority/nonclaim documentation.

Exact-byte execution evidence (local Git blob SHA == GitHub blob SHA before acceptance): validator direct 15 fixtures PASS; test_validator 3 PASS; lineage 4 PASS; hardening 14 PASS; observations PASS; report PASS over 15 fixtures; scheduler 4 PASS; recovery 7 PASS; latest admission 8 PASS; acceptance bundles 6 + 13 PASS.

Latest admission bytes: module `6703e5b26344e306fd277924a341fa21cfcac630`, test `d7a968c5bbd53cbc8697fdfb9240028d7b880417`. Core validator/fixture/report bytes: `e6861c9f940f8a0529b8f93dd546ebcd42c852a7`, `bc269b52a866b377e52813edb9395f1a7225d881`, `15895ec4a2b86e9e6c7680323d6ecf419c1faaec`.

The deterministic artifact workload is complete. The original clone path remains unavailable due container DNS but is no longer an acceptance blocker because committed bytes were reconstructed from connector readback, hash-verified, and executed. Remaining LT03 work is solely runtime-threshold preservation and exact finalization after the first GitHub START-relative boundary >=900s.

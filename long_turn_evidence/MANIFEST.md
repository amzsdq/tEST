# LT04 artifact manifest

R157 canonical binding:
- pinned source branch: lt04-r157-reviewed-byte-exact
- pinned source commit: a5f942d57bdf21020db8e03216ae16910adad467
- exact input pin manifest blob: 75b23a94fd76b1d645de2eb31262cb764374deca
- fresh R157 recursive-tree audit: 29/29 exact files match the pin, zero mismatches.
- canonical runner: e1f6cee2b42951333797d27cd7b8e12436133b19.
- validator/test_hardening: f0d477c577192185efcf2fabd3b057101b5c8f29 / 306b1144c956f4c033ee3a7923f55ac308bb3f2f.
- authority/test_authority: 8d64d694caede5ca2b41a1b637e343fe1e102434 / c4b185e1cc1cc643d6fc2b764a30648b4729cd47.
- recovery/test_recovery: 26b3930ec6856efefff20b8229b1ba8c7a791e94 / b20d1965a4d9efa270933bad73b316bdc51c89c7.
- lineage/test_lineage: b016ee51787f761357649e3e1056cb1d7f30be55 / c22b97e0ad4fa93600f9ddeff118e2932033a312.
- scheduler_v2/test_scheduler_v2: 6bf4ea365700699cd3fb725844483799cbbe848b / c7dc9c6c1c7a51c1232f834c43c882313cddc950.
- schema/exact schema/schema tests: b4f71d37ce619d8939d849a036ec5906a4475485 / ad5ddcdd42bdd4513bdc9e5a42e5b862c49d14e5 / 6fb4ab280c77149e0a9172ba9766a27a753445eb.
- legacy scheduler/test_scheduler: b7f6edc9efdfe1ac03d40dcd24d47cb56224c019 / a972ff6250094f3f835ae29b96503e56f44650ee.
- commit-clock recovery/test: 6bd21ca7c32063d897e5829165fad5757f8afdf4 / b2a08a86ae8d5dd08a156089c5a15645a70c98c8.
- observations.json remains 19d020b7b5918211124f0d6ada5895318cf12854.

Verified runtime evidence remains LT03 exact 940s, LT04-R118-T6B exact 1191s, and LT04-R126-T9 exact 1219s.
R157 consumer package adopts strict canonical raw-GitHub marker timestamps and reviewed structural checks at validator, authority, recovery, and lineage boundaries while preserving broad scheduler/reference parsing.
Remaining release gates: unchanged exact canonical runner execution with rc=0 + LT04_CANONICAL_CHECKS_PASS, then main integration/readback.

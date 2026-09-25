# LT04 integration order

1. Apply the admission branch change and run the boundary matrix.
2. Integrate versioning normalization into validator while preserving its output shape.
3. Fold the staged schema delta into schema.json without making evidence_version required.
4. Keep observations.json unchanged.
5. Integrate exact_evidence.json and the authority selector.
6. Extend observation validation to assert both the historical LT03 censored record and the selected later exact 940-second authority.
7. Run authority, versioning, schema-contract, admission, validator, lineage, hardening, recovery, scheduler, observation, and report checks.
8. Synchronize README, MANIFEST, ACCEPTANCE, and capability classification.
9. Read back main-branch SHAs and regenerate the release manifest.

# Integration runbook

Before integrating, read main SHAs for every existing target file and compare them with the preserved baseline.

Apply existing-file changes serially. After each write, read the file back and verify the resulting blob SHA. Do not treat the write acknowledgement as sufficient.

After integration:
1. verify observations.json SHA is unchanged;
2. run admission boundary and edge cases;
3. run versioning and schema-contract checks;
4. run authority and observation checks;
5. run validator, lineage, hardening, scheduler, recovery, and report checks;
6. verify documentation no longer claims LT03 is unproven;
7. record integrated blob identities in the release manifest.

If an existing-file write is blocked, do not repeat it unchanged. Preserve staged work on the isolated branch and switch execution path.

#!/usr/bin/env python3
"""Run canonical deterministic LT04 checks in fail-fast order."""
import subprocess,sys
TESTS=[
 "test_admission.py",
 "test_validator.py",
 "test_lineage.py",
 "test_hardening.py",
 "test_versioning.py",
 "test_schema_contract.py",
 "test_authority.py",
 "test_authority_fallback.py",
 "validate_observations.py",
 "test_scheduler.py",
 "test_scheduler_v2.py",
 "test_recovery.py",
 "test_recovery_commit_clock.py",
]
for test in TESTS:
 result=subprocess.run([sys.executable,test],cwd="long_turn_evidence")
 if result.returncode:
  raise SystemExit(result.returncode)
for script in ["validator.py","report.py"]:
 result=subprocess.run([sys.executable,script],cwd="long_turn_evidence")
 if result.returncode:
  raise SystemExit(result.returncode)
print("LT04_CANONICAL_CHECKS_PASS")

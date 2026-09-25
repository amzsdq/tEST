#!/usr/bin/env python3
import subprocess
import sys

tests = [
    "test_authority.py",
    "test_authority_fallback.py",
    "test_versioning.py",
    "test_schema_contract.py",
    "test_scheduler_v2.py",
    "test_recovery_commit_clock.py",
]
for test in tests:
    result = subprocess.run([sys.executable, test], cwd="long_turn_evidence")
    if result.returncode != 0:
        raise SystemExit(result.returncode)
print("LT04_STAGED_CHECKS_PASS")

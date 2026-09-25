#!/usr/bin/env python3
import json
from pathlib import Path
from authority import select_authority

ROOT = Path(__file__).resolve().parent
observations = json.loads((ROOT / "observations.json").read_text())
exact_records = json.loads((ROOT / "exact_evidence.json").read_text())
rows = []
for observation in observations:
    rows.append({
        "invocation_id": observation["invocation_id"],
        "authority": select_authority(observation, exact_records),
    })
report = {"rows": rows, "history_rewritten": False}
print(json.dumps(report, indent=2, sort_keys=True))

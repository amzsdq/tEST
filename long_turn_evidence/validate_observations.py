#!/usr/bin/env python3
import json
from pathlib import Path
from validator import validate

ROOT = Path(__file__).resolve().parent
records = json.loads((ROOT / "observations.json").read_text())
results = [validate(r) for r in records]
by_id = {r["invocation_id"]: r for r in results}
lt02 = by_id["LT02-AUTO-LARGER-SUBSTANTIVE-PACKAGE-GRAPH-01"]
assert lt02["classification"] == "VOLUNTARY_FINAL"
assert lt02["exact_duration_seconds"] == 411
assert lt02["target_crossed"] is False
lt03 = by_id["LT03-DETERMINISTIC-ARTIFACT-CONTEXT-VOLUME-01"]
assert lt03["classification"] == "ABRUPT_NONFINAL"
assert lt03["exact_duration_seconds"] is None
assert lt03["censored_lower_bound_seconds"] == 135
print(json.dumps(results, indent=2, sort_keys=True))

#!/usr/bin/env python3
import json
from pathlib import Path
from validator import validate
from authority import select_authority

ROOT = Path(__file__).resolve().parent
observations = json.loads((ROOT / "observations.json").read_text())
results = [validate(record) for record in observations]
by_id = {result["invocation_id"]: result for result in results}

lt02 = by_id["LT02-AUTO-LARGER-SUBSTANTIVE-PACKAGE-GRAPH-01"]
assert lt02["classification"] == "VOLUNTARY_FINAL"
assert lt02["exact_duration_seconds"] == 411
assert lt02["target_crossed"] is False

lt03_id = "LT03-DETERMINISTIC-ARTIFACT-CONTEXT-VOLUME-01"
lt03 = by_id[lt03_id]
assert lt03["classification"] == "UNKNOWN"
assert lt03["exact_duration_seconds"] is None
assert lt03["censored_lower_bound_seconds"] == 833
assert lt03["target_crossed"] is False

lt03_observation = next(record for record in observations if record["invocation_id"] == lt03_id)
exact_records = json.loads((ROOT / "exact_evidence.json").read_text())
authority = select_authority(lt03_observation, exact_records)
assert authority["kind"] == "exact"
assert authority["exact_duration_seconds"] == 940
assert authority["target_crossed"] is True

print(json.dumps({"historical": results, "selected_lt03_authority": authority}, indent=2, sort_keys=True))

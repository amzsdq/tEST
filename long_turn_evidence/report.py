#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path
from validator import validate_fixture

ROOT = Path(__file__).resolve().parent
fixtures = json.loads((ROOT / "fixtures.json").read_text())
rows = []
for f in fixtures:
    expected_raise = f["expected"].get("raises")
    if expected_raise:
        try:
            validate_fixture(f)
        except ValueError as exc:
            if expected_raise not in str(exc):
                raise AssertionError(f"{f['id']}: expected rejection containing {expected_raise!r}, got {str(exc)!r}") from exc
            rows.append({"fixture": f["id"], "classification": "REJECTED_INPUT", "detail": str(exc)})
        else:
            raise AssertionError(f"{f['id']}: expected rejection")
    else:
        r = validate_fixture(f)
        rows.append({"fixture": f["id"], "classification": r["classification"],
                     "exact": r["exact_duration_seconds"], "lower_bound": r["censored_lower_bound_seconds"],
                     "target_crossed": r["target_crossed"], "valid": r["valid"], "violations": r["violations"]})
counts = Counter(r["classification"] for r in rows)
report = {"fixture_count": len(rows), "classification_counts": dict(sorted(counts.items())), "rows": rows,
          "nonclaims": ["censored lower bound is not exact kill time", "classification is not provider root-cause proof", "multiple invocations are never summed into one-turn success"]}
(ROOT / "generated_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps(report, indent=2, sort_keys=True))

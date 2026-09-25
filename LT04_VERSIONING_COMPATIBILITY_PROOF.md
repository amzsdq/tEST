# Evidence-version backward-compatibility proof

For every legacy record R that omits evidence_version:

1. normalize_record(R) returns (dict(R), 1).
2. dict(R) is a shallow top-level copy with the same key/value mapping as R.
3. validator.validate reads fields and nested marker objects but never mutates them.
4. The post-normalization validator body is otherwise unchanged from the legacy validator.
5. Therefore every legacy validation branch, classification, duration, violation, and output key is preserved for the same R.
6. Top-level input identity is deliberately not preserved, preventing validator-side top-level mutation from leaking to callers.
7. Explicit v1 follows the same validation body.
8. Explicit v2 follows the same validation body after strict version admission.
9. bool/non-int/unsupported evidence_version fails before ordinary validation.
10. cross_invocation_sum_seconds is not removed by normalization, so legacy S5 and v2 S5-equivalent records still reach CROSS_INVOCATION_SUM_FORBIDDEN.

This proof is complemented by test_versioning checks for legacy missing-version normalization, explicit v1/v2, invalid versions, v2 S5 rejection, nonmutation, and stable output-key shape.

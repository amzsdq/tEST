"""Evidence-version normalization with legacy-v1 compatibility."""
SUPPORTED_EVIDENCE_VERSIONS = {1, 2}

def normalize_record(record):
    if not isinstance(record, dict):
        raise ValueError("record must be object")
    normalized = dict(record)
    if "evidence_version" not in record:
        return normalized, 1
    version = record["evidence_version"]
    if isinstance(version, bool) or not isinstance(version, int):
        raise ValueError("invalid evidence_version")
    if version not in SUPPORTED_EVIDENCE_VERSIONS:
        raise ValueError("unsupported evidence_version")
    return normalized, version

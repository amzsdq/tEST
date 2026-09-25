# Long-turn evidence v2 draft

Authority order:
1. recognized START and matching END timestamps provide exact duration;
2. a durable boundary without END is only a censored lower bound;
3. later recognized exact evidence may supersede a censored historical observation for current authority without rewriting that observation;
4. invocations are never summed into one-turn success.

Versioning:
- missing evidence_version means legacy v1;
- explicit versions 1 and 2 are supported;
- invalid types and unsupported versions are rejected;
- deprecated cross-invocation sums remain visible to the semantic validator and remain forbidden;
- JSON schema files are contract artifacts; Python validation is runtime-authoritative.

Commit clock:
- clock writes omit caller-supplied dates;
- commit SHA readback supplies the authoritative timestamp;
- START and END are separate durable markers;
- OPEN_SESSION never invents END or WORKED.

Admission:
- below target: continue only useful work;
- target through pre-stretch: continue useful work when finalization is safe, otherwise block finalization;
- no useful work after target enters reserve;
- at stretch or later, safe sessions enter reserve.

Historical LT03 remains unchanged at an 833-second censored lower bound. Separate recognized exact evidence establishes 940 seconds for current authority.

# Issue #1 Bounded Tail Retrieval Protocol

Status: PROMOTED as a control-I/O optimization after independent live repeats in LW36/LW37. This changes retrieval cost only; it does not change Issue #1 authority semantics.

## Default path
1. Take the prior authoritative baton `created_at` as an inclusive `since` lower bound.
2. Fetch a bounded recent window from Issue #1.
3. Verify expected anchor/lineage and identify latest relevant live evidence.
4. If the returned window saturates its page size, paginate until the bounded window is complete before deciding authority.
5. If anchor presence, lineage, ordering, or completeness is ambiguous, fetch Issue #1 comment count and calculate the current final page.
6. Fetch that calculated page, then probe successive next pages until the first empty page. This closes the simple count->page rollover race where concurrent appends cross a page boundary after count was observed.
7. If authority lineage is still ambiguous, broaden/re-read. An empty page is a completeness observation for that read moment, not a permanent no-new-work guarantee.

## Authority guard
`since` is only a retrieval lower bound and is update-sensitive, not created-at-only. LW37 proved this strictly: shadow C was created at 09:25:32Z, lower-bound anchor D at 09:25:36Z, then C was edited at 09:25:41Z; `since=09:25:36Z` returned both C and D, with C still ordered before D. Therefore an older edited comment can re-enter a later bounded query. `updated_at`, response inclusion, or edit recency must never by itself supersede later append-only live evidence. Resolve authority from relevant live lineage, created ordering, and explicit later correction/supersession semantics. SHADOW/SYNTHETIC records never advance live NEXT.

## Cross-invocation marker references
LW53/LW54 promote a two-layer reference contract without adding a second mutable marker pointer or cache.

Producer fast path: before emitting a cross-invocation marker ID that already exists and will later be consumed for authority/recovery/WORKED joins, direct-fetch the referenced comment when that identity read is cheap and verify Issue #1 plus expected marker role/invocation identity. Emit it as a validated reference only after that check. A nonexistent ID or an existing comment with the wrong role/invocation is not a valid reference.

Consumer fallback: a propagated marker ID is a hint, not authority. Direct-fetch it first. On 404 or identity mismatch, perform bounded semantic recovery for the exact marker role plus invocation/experiment identity. Exactly one candidate may be direct-fetched and identity-validated, then used. Zero candidates => `MISSING_MARKER`; multiple plausible candidates => `AMBIGUOUS_MARKER`; individually valid START/END markers from different lineage => `PAIR_MISMATCH`. All three yield `WORKED=UNKNOWN`; never select newest/oldest heuristically.

Producer validation is an optimization, not a replacement for consumer recovery. Do not add validation writes merely to save exceptional recovery reads.

### Post-scheduler END recovery by FINAL_BATON backlink
LW55 promotes a structural simplification for the current finalization order `FINAL_BATON -> sole scheduler mutation -> END`. The END comment does not exist when the scheduler prompt is written, so requiring its ID in that prompt would force a forbidden second scheduler mutation.

The minimal cross-invocation clock reference set is therefore `PRIOR_START_ID + PRIOR_FINAL_BATON_ID`. After wake, discover the prior END by bounded semantic search for a recognized END schema carrying the exact prior baton backlink. Evidence-backed schemas are version/lineage scoped: current END records use `FINAL_BATON=<id>`; historical LW43/LW44 END records use `FINAL_BATON_COMMENT_ID=<id>`. Unknown aliases do not establish linkage.

Recovery is conservative: exactly one recognized END candidate with exact baton value plus matching START/automation/invocation lineage may be direct-fetched and its GitHub `created_at` used. A role match with a different backlink is rejected. Zero exact candidates => `MISSING_END`; multiple plausible exact candidates => `AMBIGUOUS_END`; lineage conflict => `PAIR_MISMATCH`. These yield `WORKED=UNKNOWN`; no newest/oldest heuristic is permitted. LW53 generic marker recovery remains the fallback safety net.

For work-duration accounting, only a validated matching START/END pair's GitHub `created_at` values are authoritative. Model-authored time strings are never substituted.

## Evidence
LW36 directional probe showed exact-timestamp inclusion and that busy recent windows can require pagination. LW37 independently repeated exact-anchor inclusion from the prior baton.

During LW37, Issue #1 grew from 1499 to 1503 comments, crossing the 1500-comment / 100-per-page boundary. `ceil(1503/100)=16`; page 16 recovered the current tail and page 17 was empty. This validates count/final-page recovery and demonstrates why a stale count at 1500 could otherwise miss a concurrently created page 16. The hardened fallback therefore probes beyond the calculated page until first empty.

A deliberately invalid/future `since` returned an empty set; the protocol treated that as an anchor/completeness failure and recovered through fresh count + final-page probing rather than concluding NOOP.

At current history size, a full-history connector response was itself truncated before the current tail while bounded REST reads exposed the needed evidence. Bounded retrieval is therefore both a cost optimization and an observability-reliability improvement under response-size limits.

LW50 supplied the natural marker-reference failure fixture: a propagated START ID was invalid while a unique semantic START marker existed. LW53 independently promoted conservative consumer recovery; LW54 independently reproduced producer-boundary validation while retaining the LW53 fallback. LW55 then used the natural LW54 END (`FINAL_BATON=5813937140`) plus historical LW43/LW44 `FINAL_BATON_COMMENT_ID` examples to cold-validate END recovery from the pre-scheduler baton without propagating an impossible post-scheduler END ID.

## Failure behavior
If the bounded read cannot prove tail completeness or relevant authority lineage, do not guess. Broaden the read or use the hardened count/final-page-plus-next-page fallback. The optimization fails open to more retrieval, never to weaker authority validation.

If a marker reference or END backlink cannot be uniquely recovered and identity-validated, retain `WORKED=UNKNOWN`. Missing reference metadata is not permission to infer a timestamp or marker identity.

## Non-goals
This protocol does not maintain a second mutable current-state or marker pointer, does not alter scheduler behavior, and does not change the compact live baton authority model.

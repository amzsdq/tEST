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

## Evidence
LW36 directional probe showed exact-timestamp inclusion and that busy recent windows can require pagination. LW37 independently repeated exact-anchor inclusion from the prior baton.

During LW37, Issue #1 grew from 1499 to 1503 comments, crossing the 1500-comment / 100-per-page boundary. `ceil(1503/100)=16`; page 16 recovered the current tail and page 17 was empty. This validates count/final-page recovery and demonstrates why a stale count at 1500 could otherwise miss a concurrently created page 16. The hardened fallback therefore probes beyond the calculated page until first empty.

A deliberately invalid/future `since` returned an empty set; the protocol treated that as an anchor/completeness failure and recovered through fresh count + final-page probing rather than concluding NOOP.

At current history size, a full-history connector response was itself truncated before the current tail while bounded REST reads exposed the needed evidence. Bounded retrieval is therefore both a cost optimization and an observability-reliability improvement under response-size limits.

## Failure behavior
If the bounded read cannot prove tail completeness or relevant authority lineage, do not guess. Broaden the read or use the hardened count/final-page-plus-next-page fallback. The optimization fails open to more retrieval, never to weaker authority validation.

## Non-goals
This protocol does not maintain a second mutable current-state pointer, does not alter scheduler behavior, and does not change the compact live baton format.

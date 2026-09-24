# Issue #1 Bounded Tail Retrieval Protocol

Status: PROMOTED as a control-I/O optimization after independent live repeats in LW36/LW37. This changes retrieval cost only; it does not change Issue #1 authority semantics.

## Default path
1. Take the prior authoritative baton `created_at` as an inclusive `since` lower bound.
2. Fetch a bounded recent window from Issue #1.
3. Verify that the expected anchor/lineage is present and identify the latest relevant live evidence.
4. If the returned window saturates its page size, paginate until the window is complete before deciding authority.
5. If anchor presence, lineage, ordering, or tail completeness is ambiguous, fall back to Issue #1 comment count and the calculated final page (and broaden further if required).

## Authority guard
`since` is only a retrieval lower bound. It is update-sensitive: an older comment edited after the lower bound can be re-included. Therefore `updated_at` or response recency must never by itself supersede later append-only live evidence. Resolve authority from relevant live lineage, created ordering, and explicit later correction/supersession semantics. SHADOW/SYNTHETIC records never advance live NEXT.

## Evidence
LW36 directional probe showed exact-timestamp inclusion and that busy recent windows can require pagination. LW37 independently repeated exact-anchor inclusion from the prior baton. Issue #1 reported 1499 comments; `ceil(1499/100)=15`, and page 15 returned the current tail range, validating the count/final-page fallback without a full-history scan.

LW37 edit-order differential created shadow A, then later-created B, then edited A. A bounded `since=A.created_at` read included edited A and B, but retained A before B in response order. This proves the lower-bound query can re-include edits and must not be treated as an updated-at authority ordering.

## Failure behavior
If the bounded read cannot prove tail completeness or relevant authority lineage, do not guess. Broaden the read or use count/final-page fallback. The optimization fails open to more retrieval, never to weaker authority validation.

## Non-goals
This protocol does not maintain a second mutable current-state pointer, does not alter scheduler behavior, and does not change the compact live baton format.

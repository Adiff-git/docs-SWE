# Feature Specification: Persistent Shopping Cart

**Feature Branch**: Existing `main`; no branch hook is configured and no branch was created.
**Created**: 2026-11-11
**Status**: Ready for planning — all clarification decisions confirmed; implementation follows separately.
**Input**: Attached shopping cart brief for Backend-SWE, with ProjectCV behavior as a reference.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Save and revisit purchase choices (Priority: P1)

An authenticated customer can save variants and revisit a private persistent cart with current prices.

**Why this priority**: Persistent choices provide the feature's core value.
**Independent Test**: View an empty cart, add a variant, and revisit in a later authenticated session.

**Acceptance Scenarios**:

1. **Given** no cart, **When** viewed, **Then** return empty items and zero totals without creating stored cart state (D1).
2. **Given** an eligible variant, **When** quantity 2 is added, **Then** one selected row has quantity 2 (D2).
3. **Given** an unselected row of quantity 2, **When** quantity 3 is added, **Then** exactly one row has quantity 5 and remains unselected (D2).
4. **Given** saved choices, **When** the user returns in a later valid session, **Then** quantities and selection persist, with current catalog prices.
5. **Given** another user's item or an unknown item, **When** any item mutation is attempted, **Then** both produce the same safe not-found result without changing either cart.

---

### User Story 2 - Adjust and remove choices (Priority: P1)

A customer can replace quantities, change options and remove choices without duplicate rows.

**Why this priority**: Edits must reflect the intended quantity exactly.
**Independent Test**: Seed variants of one product and exercise replacement, switching, merging and removal.

**Acceptance Scenarios**:

1. **Given** quantity 2, **When** updating quantity to 4 with the same or omitted variant, **Then** the result is 4.
2. **Given** source quantity 2 and an absent eligible target variant of the same product, **When** switching with quantity 4, **Then** retain source row identity and selection and set target quantity to 4 (D3).
3. **Given** source quantity 2 and an existing target quantity 3, **When** switching with quantity 4, **Then** one target row has quantity 7, target identity/selection persist and the source is removed (D3). Do not add the old source quantity.
4. **Given** an invalid target or excessive resulting quantity, **When** updating, **Then** neither row nor selection changes.
5. **Given** an owned item, **When** removing it, **Then** it disappears and totals recalculate on the next view; repeating removal returns not found.
6. **Given** an unavailable source, **When** switching to an eligible same-product variant, **Then** allow the switch; reject quantity updates retaining an unavailable variant (D4).

---

### User Story 3 - Select choices and understand estimates (Priority: P2)

A customer can choose eligible rows and see the current estimate for those choices.

**Why this priority**: Totals must reflect buying intent and current availability.
**Independent Test**: Compare selected, unselected and unavailable rows against independently calculated amounts.

**Acceptance Scenarios**:

1. **Given** selected rows with 2 units at 100 VND and 3 at 50 VND, **When** viewed, **Then** selected row count is 2, selected quantity 5, selected subtotal and final total both 350 VND.
2. **Given** those rows, **When** deselecting the first, **Then** its quantity remains 2 and the totals become one selected row, quantity 3 and 150 VND.
3. **Given** a selected row whose product becomes archived, **When** viewed, **Then** selected remains true, purchasable becomes false, a safe reason appears and eligible totals exclude it (D4).
4. **Given** mixed availability, **When** selecting all, **Then** eligible rows become selected and unavailable rows retain their stored selection; deselect-all clears every selection (D4).
5. **Given** an unavailable row, **When** selecting it, **Then** reject without mutation, even if it is already selected; deselection and removal succeed (D4).
6. **Given** a changed catalog price, **When** returning the cart, **Then** amounts use the current price without locking a future purchase price.

### Edge Cases

- Missing/null/empty/malformed, fractional, zero, negative and excessive quantities; exact-limit success and limit-plus-one failure, including addition/merge overflow.
- Omitted update variant retains the current variant; explicit null is rejected. Cross-product switching is rejected under D3.
- Zero price is eligible; missing, negative, fractional and non-finite prices are ineligible under whole-VND conventions.
- DRAFT/ARCHIVED transitions preserve rows and selection; republishing restores eligibility without rewriting selection.
- Empty bulk selection is a successful no-op; failed/no-op mutations do not create a missing cart (D1).
- Equal addition times use identifier tie-breaking; repeated adds/switches preserve ordering time; merges preserve target ordering (D5).
- Concurrent first-cart creation, repeated adds, edits, merges, deletion and selection must preserve FR-012.
- Missing images do not make price calculations depend on external storage.
- Physical deletion must preserve integrity and follow the approved cart-reference restriction D7 without changing unrelated deletion policies.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Provide authenticated persistent cart viewing, addition, quantity/variant update, removal, individual selection and bulk selection for one vendor.
- **FR-002**: Each user has at most one cart, each cart exactly one owner, and each row exactly one variant. A cart has at most one row per variant. Resolve identity through the existing authenticated boundary; never accept a client owner ID. Check ownership on every item operation.
- **FR-003**: Adding increments an existing row or creates one. Validate requested and resulting quantities before mutation; never silently cap them.
- **FR-004**: Updates require replacement quantity. Same-variant updates replace quantity; absent-target switches use requested quantity; existing-target switches add requested quantity to the target and atomically remove the source. Selection/same-product rules follow approved D3.
- **FR-005**: Eligibility requires an existing variant, PUBLISHED parent and present finite non-negative whole-VND price, together with any established catalog purchase restrictions. There is currently no stock quantity to validate.
- **FR-006**: Inventory capability and stock validation are deferred (Q1 A confirmed). No cart operation checks, reserves or reduces stock. Purchase eligibility reflects catalog state, not a stock guarantee.
- **FR-007**: Accept whole quantities from 1 through 1,000 inclusive per variant row (Q2 A confirmed). Both requested quantity and final added/merged quantity must satisfy this limit. Reject excessive values without capping or mutation. Calculate aggregate quantities and money exactly and reject unsupported overflow safely. The 1,000 limit is per row, not a limit on cart-wide total quantity or row count.
- **FR-008**: Retain unavailable rows with explicit purchasable=false and safe reasons. Reads do not delete rows or rewrite selections. Exclude unavailable rows from eligible selected counts and totals. Permit removal/deselection, reject selecting unavailable rows and quantity changes retaining unavailable variants; evaluate switches against target eligibility (D4).
- **FR-009**: Use current trusted prices/descriptions in responses. Eligible line subtotal is unit price times quantity. Selected subtotal sums purchasable selected rows; final total equals selected subtotal. Selected item count counts eligible rows; selected total quantity sums their units. Ineligible line subtotal is null; all aggregates are zero when no eligible rows are selected.
- **FR-010**: Return item/product/variant identifiers, product name, SKU/options, permitted image representation, valid current unit price, quantity, selected flag, purchasable flag, safe reason and applicable subtotal, plus selected row count, selected quantity, selected subtotal and final total. Do not expose hidden catalog information or private images.
- **FR-011**: Apply all confirmed policies D1–D8 for lifecycle, selection, same-product variant edits, unavailable items, ordering, authorization/HTTP, referenced-catalog deletion and concurrency verification (Q3 approved).
- **FR-012**: Concurrent accepted additions lose no increment and cannot create duplicate rows or carts. Merges are atomic; failed mutations change no state. Selection changes never overwrite quantities. Concurrent conflicts either complete in a valid serial order or return a defined conflict without partial changes; success for every competing request is not promised.
- **FR-013**: Reuse current authentication, account/session eligibility and authorization. Unknown and foreign-owned item operations have indistinguishable safe not-found results. Use existing safe application error conventions; the approved external contract is in the companion document.
- **FR-014**: Exclude vouchers, discounts, promotions, shop grouping, guest carts/merging, checkout endpoints, orders, payments, shipping fees, stock reservation and frontend implementation. Inventory capability and stock validation are deferred by confirmed Q1 A.

### Key Entities *(include if feature involves data)*

- **Cart**: One user's persistent purchase choices; an empty view is valid.
- **Cart item**: Owned row identity, variant reference, positive quantity, user selection and original addition time for ordering.
- **Product/variant**: Existing catalog identity, publication state, SKU/options, current price and permitted imagery; no stock quantity today.
- **Cart estimate**: Current eligible line amounts, selected row count/quantity and selected/final VND totals; no future purchase commitment.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All acceptance scenarios pass, including addition 2+3=5, replacement 2→4 and merge 3+4=7.
- **SC-002**: Every tested price/selection/availability combination matches independently calculated exact amounts and counts with zero rounding discrepancy.
- **SC-003**: All foreign-owner and unknown-item cases disclose zero private cart details and cause zero unauthorized changes.
- **SC-004**: Every invalid-input and failed-merge case preserves previous quantities, rows and selections completely.
- **SC-005**: Returning users recover all saved quantities and selections across sessions, except changes they explicitly made; catalog changes affect current eligibility and estimates.
- **SC-006**: All synchronized concurrent-operation test schedules preserve one cart per user, one row per variant, accepted increments and atomic outcomes.

## Assumptions

### Confirmed scope and repository evidence

The supplied brief establishes single-vendor scope and edit arithmetic. Source confirms UUID catalog IDs, SKU/options/sellingPrice, PUBLISHED public visibility and no inventory quantity. Monetary output is whole VND. Existing catalog validation permits negative values, so cart eligibility must reject them without claiming catalog already does. Bearer authentication checks current user/session state. MANAGE_WISHLIST exists; cart permission does not. See [engineering contract](contracts/engineering.md) for evidence and integration constraints.

Local ProjectCV source confirms incremental adds, replacement updates, target-plus-request merges and separate selection mutations. Its read-time cart creation, unrestricted switching, stock, shop, voucher and checkout behavior are not adopted automatically.

### Confirmed clarification decisions (2026-11-11)

- **Q1 A**: Defer inventory capability and stock validation.
- **Q2 A**: Maximum quantity is 1,000 per variant row, including resulting additions and merges. For example, 999 + 1 succeeds; 1,000 + 1 fails unchanged. A replacement of 1,000 succeeds; 1,001 fails. A merge of target 600 plus requested 400 succeeds; plus requested 401 fails with source and target unchanged.

- **Q3**: D1–D8 approved in full.

### Approved policies (Q3 confirmed 2026-11-11)

- **D1 — Lifecycle**: Create on first successful add; missing-cart reads return empty without insertion. Empty bulk selection is a no-op. Failed/no-op operations do not create a cart. Removing the last item retains an empty cart.
- **D2 — Add selection**: New rows selected; repeated addition preserves existing selection.
- **D3 — Variant edits**: Same-product switches only. Absent-target switches preserve source identity/selection; merges preserve target identity/selection. Quantity required; omitted variant retains current; explicit null and zero quantity are invalid.
- **D4 — Availability**: Keep stored selected separate from purchasable. Select-all changes eligible rows only, leaving unavailable rows unchanged; deselect-all clears all. Permit unavailable-source to eligible-target switches. Invalid price yields null unit price/subtotal. Hidden products expose only previously public identifying name/SKU/options and row identity, without hidden descriptions or imagery.
- **D5 — Listing**: Return the complete cart without pagination, ordered by original added time descending then item ID ascending. Repeated adds/switches keep original time; merges keep target time. No unconfirmed row cap or expiry policy.
- **D6 — Authorization and HTTP**: Require MANAGE_CART on all operations, assigned to existing/future USER roles; custom roles require explicit grants. Current permission changes apply on the next request. Add returns 201 for new row and 200 for merge; view/updates return 200 and delete returns 204. Exact approved inputs/errors are in the companion contract.
- **D7 — Catalog deletion**: Keep archived rows; restrict physical deletion of referenced variants/products while cart references remain, without cascading away cart data or changing unrelated relationships. There is no independent variant archive field to reuse.
- **D8 — Verification**: Include synchronized concurrency tests now for duplicate adds, increments, first-cart creation, merges and selection-versus-quantity edits. Choose transaction/locking mechanisms during planning.

### Dependencies and boundaries

Depends on catalog lookup/publication/pricing, current user/account authorization, auth sessions and publication-safe catalog/media image information. Any needed batch variant lookup must use catalog-owned boundaries. Follow constitution and established tests. These documents do not implement code, migrations, permissions, inventory or deletion-policy changes. No latency/load promise is inferred without an agreed workload; acceptance outcomes above define measurable readiness.

### Approved storage and failure-handling follow-up (2026-11-11)

Image types share one URL distribution mechanism over stored keys/references; generated URLs are never durable cart data. The cart design eliminates unnecessary request-owned image resources. Genuine cleanup cannot replace success or the original operation failure. Lock contention must roll back to a safe conflict, with timeout configured before waiting and no automatic retry. See the internal service contract for technical rules. The user limited this follow-up to shared storage implementation and cart design; cart behavior and concurrency tests remain unimplemented.

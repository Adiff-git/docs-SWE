# External HTTP Contract: Shopping Cart

2026-11-11. Approved and implemented policies D1–D8; quantity 1–1,000; inventory deferred. This is the normative HTTP contract, supplementing the repository evidence in engineering.md. No checkout endpoint exists.

## Shared rules

Base resource `/api/me/cart`. Bearer authentication must identify a currently eligible account/session with MANAGE_CART. Current grants/revocations apply on the next request. No owner ID is accepted. Requests with JSON bodies use application/json; responses use application/json, errors application/problem+json (existing ProblemDetail/ApiError with safe code where defined). Cart success/error responses are private, no-store; DELETE has no body. Authentication and authorization take precedence over MVC method/media-type validation: missing/invalid bearer returns 401; insufficient permission or a method outside the explicit allowed matchers returns 403 under deny-all. For a supported method on an authorized route, unsupported media type returns 415 ProblemDetail after security checks. No unconditional 405/415 or missing-route 404 promise overrides the existing security policy.

Unknown/foreign item IDs have the same 404 status/code/detail (`CART_ITEM_NOT_FOUND`, `Cart item not found`). Ownership is checked before resolving requested target details. New cart/item IDs are positive Long values serialized as JSON integers; variant/product UUIDs are canonical UUID strings. No pagination/sort/filter parameters are accepted. Full item ordering is addedAt descending, id ascending; addedAt is internal and need not be exposed.

## Routes

| Method/path | Body | Success |
| --- | --- | --- |
| GET /api/me/cart | None | 200 CartResponse, empty without insertion if absent |
| POST /api/me/cart/items | AddCartItemRequest | 201 CartResponse for a new row, Location `/api/me/cart/items/{id}`; 200 CartResponse for incrementing an existing row |
| PUT /api/me/cart/items/{itemId} | UpdateCartItemRequest | 200 CartResponse; identity follows source unless merge retains target |
| DELETE /api/me/cart/items/{itemId} | None | 204, no content; absent/foreign 404 |
| PUT /api/me/cart/items/{itemId}/selection | CartSelectionRequest | 200 CartResponse |
| PUT /api/me/cart/selection | CartSelectionRequest | 200 CartResponse; missing cart is empty no-op |

No standalone item GET is introduced by the Location identifier. All complete responses include the mutation's resulting cart state and current prepared catalog values. POST is not idempotent: retrying an accepted addition adds again. No idempotency-key protocol is introduced.

## Request schemas and field semantics

`AddCartItemRequest`: exactly `variantId` and `quantity`, both required. Example `{"variantId":"00000000-0000-0000-0000-000000000001","quantity":2}` (illustrative ID; use a real fixture UUID).

`UpdateCartItemRequest`: required `quantity`; optional `variantId`. Example `{"quantity":4}` replaces quantity and retains the variant. Example `{"variantId":"00000000-0000-0000-0000-000000000002","quantity":4}` switches within the same product.

`CartSelectionRequest`: exactly required `selected`. Example `{"selected":false}`.

| Input | Missing | Null | Empty/malformed/type mismatch | Valid value |
| --- | --- | --- | --- | --- |
| Add variantId | 400 | 400 | 400; nonempty canonical UUID string only | Resolve eligible target |
| Update variantId | Retain current | 400 | 400 | Retain/switch within source product |
| quantity | 400 | 400 | 400; strict integer JSON token, no strings/booleans/decimal/exponent form | 1–1000 inclusive |
| selected | 400 | 400 | 400; boolean JSON token only | true/false |
| itemId | Missing path does not match item route | Invalid literal is malformed | 400 noninteger/overflow; 404 nonpositive/unmatched identifier | Positive Long with owned lookup |

Bodies must be JSON objects. Missing body, JSON null, arrays, scalar bodies, empty object, unknown fields and duplicate keys are 400. Explicit client prices/totals/product descriptions/owner IDs are unknown fields and rejected. Nonempty body on GET/DELETE and any unsupported query parameter are 400. No coercion of `"2"`, `2.0`, `2e0`, `"true"` or `1` into accepted integer/boolean values.

## Editing and selection semantics

- New eligible variant creates a selected row. Repeated add increments quantity but preserves selection/id/time.
- Same variant (including omitted variantId) replaces quantity. A different same-product variant absent from the cart replaces source variant/quantity and preserves source id/selection/time.
- Existing-target switch results in target quantity + request quantity; source old quantity is not added. Retain target id/selection/time and remove source atomically.
- Direct quantities outside 1–1000 are 400. Valid inputs whose add/merge result exceeds 1000 are 422; no silent cap and no partial state change.
- Cross-product variant switch is 422. Hidden or missing requested target is safe 404. Published target with invalid price is 422.
- Selecting an unavailable item is 422, including if stored selected is already true. Deselecting/removing unavailable rows is allowed. Bulk select sets only eligible rows true; unavailable selections are unchanged. Bulk deselect sets all false.
- Empty-cart view/bulk selection returns zero state. Removing the last row leaves an empty cart. Repeated removal of missing item returns 404.

## CartResponse

| Field | Type | Meaning |
| --- | --- | --- |
| items | CartItemResponse[] | Complete collection including retained unavailable rows |
| selectedItemCount | Long | Number of selected AND purchasable rows |
| selectedTotalQuantity | Long | Sum of their quantities; may exceed 1000 |
| selectedSubtotal | Money | Sum of their line subtotals |
| finalTotal | Money | Same as selectedSubtotal; no fees/discounts |

`Money` reuses SellingPrice representation: `{ "amount": 350, "currency": "VND" }`; amount is an exact nonnegative arbitrary-precision integer JSON number. Clients must preserve integer precision rather than assume IEEE-754-safe values. All amounts remain whole VND.

| Item field | Type | Meaning |
| --- | --- | --- |
| id | Long | Cart item identity |
| productId | UUID string | Product identity |
| variantId | UUID string | Variant identity |
| productName | String | Current public name or prior-public snapshot if hidden |
| sku | String | Current public SKU or prior-public snapshot if hidden |
| options | Map<String,String> | Current public options or prior-public snapshot if hidden |
| primaryImageUrl | String or null | Current permitted signed primary image; hidden products always null |
| unitPrice | Money or null | Current valid nonnegative whole price; null if invalid |
| quantity | Integer | 1–1000 |
| selected | Boolean | Stored customer preference, independent of availability |
| purchasable | Boolean | Current catalog eligibility; no stock assurance |
| availabilityReason | String or null | null, PRODUCT_UNAVAILABLE or PRICE_UNAVAILABLE |
| subtotal | Money or null | Exact unitPrice × quantity if purchasable; otherwise null |

For hidden products use PRODUCT_UNAVAILABLE before price reason; preserve selected flag and exclude from all eligible aggregates. Current hidden descriptions/images are never exposed. Valid current price may be displayed on a hidden row as allowed by the approved engineering contract; it is not chargeable and subtotal remains null. Optional image can be null when absent or newly introduced after image preflight; do not perform credential resolution under cart locks to fill it. Genuine storage signing failure is a safe 503 and rolls back a mutation, not a successful partial mutation.

Empty response: `{"items":[],"selectedItemCount":0,"selectedTotalQuantity":0,"selectedSubtotal":{"amount":0,"currency":"VND"},"finalTotal":{"amount":0,"currency":"VND"}}`.

Numerical examples: rows (selected, eligible) 2×100 and 3×50 give row count 2, quantity 5, subtotal/final 350. If the first is unselected or unavailable, eligible row count 1, quantity 3, total 150. A selected unavailable row remains selected=true visibly. Prices are current estimates, not commitments.

## Errors and atomicity

| Status | Conditions |
| --- | --- |
| 400 | Shape/type/null/unknown/duplicate/path/request-quantity errors |
| 401 | Missing/invalid/expired credentials or invalidated identity/session |
| 403 | Authenticated current user lacks MANAGE_CART/current access eligibility |
| 404 | Unknown/foreign source item (identical response); missing or hidden requested target |
| 409 | Expected concurrent conflict/lock timeout/deadlock; safe retry decision left to client |
| 422 | Cross-product switch, published invalid target price, unavailable selection, final merged/add quantity limit, unsupported aggregate overflow |
| 503 | Existing catalog image signing dependency unavailable; safe message and no partial mutation |
| 500 | Unexpected fault, without internal/SQL/token disclosure |

Use descriptive custom exceptions with stable cart error codes (`INVALID_CART_REQUEST`, `CART_ITEM_NOT_FOUND`, `CART_QUANTITY_LIMIT`, `CART_VARIANT_SWITCH_INVALID`, `CART_ITEM_UNAVAILABLE`, `CART_CONFLICT`) and existing safe target/auth codes where applicable. New global error envelope is not introduced. Every rejected application mutation rolls back all database changes, including newly created carts and source deletion. Duplicate additions preserve one variant row; accepted increments cannot be lost. Concurrent conflicting operations either serialize safely or return conflict. No stock modification, stronger price snapshot, global retry or checkout guarantee.

## Shared URL distribution follow-up (2026-11-11)

Cart responses use the same ImageUrlResolver as product/avatar responses. PreparedImageUrls is resource-free; no cart closeable context or postcommit cleanup exists. Generated URLs remain transient, private and expire after 300 seconds; issuance is not an object-existence HEAD check. U2 is implemented and tested with independent contending PostgreSQL transactions, bounded safe 409 responses, rollback and pooled-connection timeout restoration.

# Shopping Cart Engineering Contract

Created 2026-11-11 and implemented under the subsequent speckit-implement authorization. Q3 confirms D1–D8; Q1 A defers inventory/stock validation; Q2 A sets quantity 1–1,000 per row, including final additions/merges. Technical contracts are in [api.md](api.md) and [internal-services.md](internal-services.md); execution evidence is in [../quickstart.md](../quickstart.md). Repository observations below describe the original planning baseline unless implementation evidence is explicitly stated.

## Verified repository and reference evidence

- `demo/src/main/java/com/example/demo/catalog/entity/Product.java` and `ProductVariant.java`: UUID keys, product status, SKU, option combinations and BigDecimal selling price; no shop relationship or inventory quantity.
- `demo/src/main/resources/db/migration/V1__create_catalog_core.sql`: whole finite NUMERIC prices, unique options per product, product-to-variant foreign key without delete cascade. Product statuses include DRAFT/PUBLISHED/ARCHIVED; no variant archive field.
- `catalog/dto/response/SellingPrice.java` and `catalog/converter/ProductCatalogConverter.java`: BigInteger amount plus currency VND. Preserve exact whole-VND representation; no fractional or fixed-width monetary arithmetic.
- `catalog/validator/CatalogDataValidator.java`: checks whole price but does not reject negative values. Cart adds the required eligibility guard, not a catalog policy rewrite.
- `catalog/dto/response/ProductSummary.java`: id/name/category/primaryImageUrl; `media/dto/response/ImageAccessResponse.java`: id/finalUrl. Reuse appropriate publication-safe representations; never persist presigned URLs.
- `common/identity/CurrentUserIdProvider` and `auth/security/SpringSecurityCurrentUserIdProvider`: current user has Long identity. Preserve current user/catalog ID contracts; new cart/item key choice belongs in planning.
- `auth/config/AuthSecurityConfiguration.java` and `auth/security/CurrentStateJwtConverter.java`: bearer access and current account/session permissions. Existing refresh/Google capabilities are dependencies, not cart additions.
- `db/migration/V10__create_wishlist_items.sql`: MANAGE_WISHLIST and USER rollout establish the naming precedent for approved MANAGE_CART.
- `common/exception/ApiExceptionHandler.java`, `GlobalExceptionHandler.java` and auth security handlers: ProblemDetail conventions. Catalog advice is package-scoped; do not assume it handles cart binding/domain failures.
- Existing specifications reviewed: catalog, user profiles, auth sessions, image storage, wishlist, catalog enhancement and email/Google auth. `.specify/memory/constitution.md` governs architecture and verification; historical delivery statements are not proof of current behavior.
- ProjectCV reference: `C:/Users/TrinhThanh/Downloads/ProjectCV/Backend/demo/src/main/java/com/example/demo/cart/service/impl/CartItemServiceImpl.java`, `CartServiceImpl.java` and `cart/converter/CartItemConverter.java`. Confirms accumulation, replacement, target+request merge and independent selection. It creates carts during reads and includes stock/multi-shop/checkout; those policies are not imported.

## Approved HTTP contract (D6)

Require valid bearer authentication, current account/session eligibility and MANAGE_CART throughout. Resolve owner from CurrentUserIdProvider. Cart responses use private no-store caching.

| Method/path | Input | Success |
| --- | --- | --- |
| GET /api/me/cart | None | 200 complete cart |
| POST /api/me/cart/items | variantId, quantity | 201 complete cart on new row; 200 complete cart on merge |
| PUT /api/me/cart/items/{itemId} | quantity; optional variantId | 200 complete cart |
| DELETE /api/me/cart/items/{itemId} | None | 204 without body |
| PUT /api/me/cart/items/{itemId}/selection | selected | 200 complete cart |
| PUT /api/me/cart/selection | selected | 200 complete cart |

POST is explicitly add-or-increment; new rows return Location identifying the item resource (no separate item GET is promised). Quantity PUT is a complete quantity update with explicitly optional variant retention. Selection PUT completely sets selection without replacing quantity.

### Field semantics

| Field | Omitted | Null | Empty/malformed/invalid type | Valid value |
| --- | --- | --- | --- | --- |
| Add variantId | 400 | 400 | 400; UUID string required | Resolve eligible target |
| Update variantId | Retain current | 400 | 400; UUID string required | Retain or same-product switch |
| Add/update quantity | 400 | 400 | 400; no strings, booleans, fractions, zero or negatives | Integer from 1 through 1,000 inclusive |
| selected | 400 | 400 | 400; no string/numeric coercion | Boolean true/false |
| itemId path | No matching route | Invalid path identifier | 400 malformed identifier | Owner-scoped lookup; unknown/foreign 404 |

Mutation JSON bodies must be objects; missing/null/malformed/empty bodies fail 400. Reject unknown or duplicate fields, including owner IDs, prices, totals and descriptions. GET/DELETE accept no nonempty body. Unsupported query options fail 400. Validate request shape before mutations and ownership before target lookup. An out-of-range input quantity is 400; an otherwise-valid addition/merge whose resulting row quantity exceeds 1,000 is 422. Never silently cap or wrap values.

### Error mapping

- 400: request binding/shape/null/value failures above.
- 401: missing/invalid/expired credentials or invalid session under existing auth policy.
- 403: valid authentication lacking MANAGE_CART or existing current-access eligibility.
- 404: identical safe result for unknown and foreign items; missing/non-public requested target variants use safe variant-not-found without revealing hidden catalog data.
- 422: known public target has invalid price, cross-product switch, unavailable-item selection, final quantity limit or unsupported aggregate overflow.
- 409: concurrent conflict unable to complete safely; no partial mutation or broad automatic retry.
- 503: existing catalog image signing dependency unavailable, preserving its current exception status; mutation rolls back.
- 500: unexpected infrastructure failure with safe ProblemDetail, never leaked internals or false success.

Use custom cart domain exceptions under existing ApplicationException conventions and centralized handling; security-chain failures remain in security handlers. Safe row reasons: PRODUCT_UNAVAILABLE or PRICE_UNAVAILABLE; purchasable rows have null reason. No stock availability reason is introduced because inventory and stock validation are deferred. Never expose hidden target catalog details through reasons.

## Response and arithmetic

Finalized in api.md: `items[]` with `id`, `productId`, `variantId`, `productName`, `sku`, `options`, `primaryImageUrl`, `unitPrice`, `quantity`, `selected`, `purchasable`, `availabilityReason`, `subtotal`; top-level `selectedItemCount`, `selectedTotalQuantity`, `selectedSubtotal`, `finalTotal`.

Money uses existing amount/currency representation, currency VND and exact arbitrary-precision whole-unit arithmetic. Aggregate quantity representation is Long, with checked intermediate calculation and safe overflow rejection. Quantity input is an integer from 1 through 1,000 inclusive; resulting additions/merges have the same per-row limit, while total cart quantity may exceed 1,000. Invalid price yields null unitPrice; ineligible subtotal is null. Valid prices can still be displayed on retained archived rows as prior public cart information, without private fields or imagery. Totals/counts are eligible-selected only and zero for empty selection.

Images are nullable, transient and publication-safe. Plan safe retention of previously public identifying name/SKU/options so public-only catalog lookup does not erase unavailable cart rows; reads must not rewrite stored snapshots. No durable temporary URLs or locked purchase price. Reuse suitable existing nested structures without exposing entities.

Responses reflect successful mutations and current catalog data used for that response; no cross-request catalog snapshot guarantee. Totals and rows use the same prepared data. Ordering follows D5; switches retain source identity except merges, which retain target identity.

## Architecture and persistence obligations

Follow constitution domain layering under `com.example.demo.cart`. Controllers delegate; service interfaces/implementations orchestrate; services use only own repositories and other domains' service boundaries; validators own business checks; converters map prepared data without queries or hidden lazy fetching. Keep dependencies acyclic and plan batched response fetching without per-item hidden queries.

Later schema work uses additive Flyway migrations and ownership/variant foreign keys, unique user-cart and cart-variant relationships, and positive/bounded quantity checks. D7 requires restricting referenced catalog deletion without altering other catalog relationships or cascading away cart records. Existing user lifecycle remains authoritative. No migration, permission grant or production change is performed by specification.

Plan FR-012 transaction/locking mechanisms against actual conflicts. Default isolation remains READ COMMITTED; no automatic SERIALIZABLE or broad retries. Document consistent conflict/lock ordering, first-cart race handling and atomic merge boundaries. Avoid holding locks across avoidable external image calls.

## Verification expectations (D8 approved)

Use approved JUnit 5, Mockito, AssertJ, MockMvc and PostgreSQL Testcontainers. Unit tests cover meaningful service/validator/calculation/conversion behavior without Spring; MVC slices verify binding, statuses and security; repository IT proves mappings/constraints; service IT proves real commit/rollback and concurrency. API/flow tests prove authenticated add/edit/select/revisit/remove with real internal dependencies. Avoid duplicating assertions across categories; follow constitution domain/layer packages, responsibility-based classes and `*Test`/`*IT` naming.

Cover empty carts, repeated additions, quantity replacement, switches with/without merge, selection preservation, removal, ownership, exact quantity limits/overflow, publication/price changes, selected totals and unchanged state after failure. D8 adds synchronized independent transactions for first creation, duplicate adds/accepted increments, merges and selection/quantity races, without timing sleeps or test-level transactions hiding production commits. External image services must not be needed for cart calculation tests.

`demo/pom.xml` configures Failsafe integration-test/verify goals. Actual Surefire/Failsafe cart discovery and test results must be verified during implementation; none is claimed here.

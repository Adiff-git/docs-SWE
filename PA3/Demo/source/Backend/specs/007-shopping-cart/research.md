# Research: Persistent Shopping Cart

Date: 2026-11-11; implementation follow-up 2026-11-12. Decisions below are resolved. Rationales capture the planning baseline; current implementation evidence is recorded in plan.md and quickstart.md. Read-only planning research examined concurrency/persistence and catalog/media integration. No dependencies or additional business scope were added.

## 1. Reuse the current backend

**Decision**: Java 25 / Spring Boot 4.1.2 modular monolith, existing Maven/JPA/PostgreSQL/Flyway/security/test stack, new cart domain.
**Rationale**: `demo/pom.xml`, the constitution and existing wishlist/user domains establish the approach. Approved Q1 defers inventory; Q2 confirms 1–1,000; Q3 confirms all D policies.
**Alternatives considered**: New framework, cache, inventory service, checkout or global refactor add unauthorized scope. No load target is invented.

## 2. Coordinate existing-cart writes on their parent

**Decision**: All cart writers acquire the same cart PESSIMISTIC_WRITE lock and fetch mutable items only afterwards. Missing-cart adds acquire UserService.getUserEntityForUpdate, recheck and create once; other missing-cart mutations never create. Use REQUIRED / READ COMMITTED and a positive configurable cart lock timeout with 5,000 ms default, set transaction-locally BEFORE the first blocking cart lock. Preserve existing UserService timeout-before-user-lock behavior; reapply cart timeout after user acquisition and before any cart lock. Each acquisition has its own bound, not a whole-request deadline. Verify rollback, 409 and pooled connection reset without automatic retries.
**Rationale**: `user/service/UserService.java`, `user/service/impl/UserServiceImpl.java` and `user/repository/UserRepository.java` already provide user locking/refresh/timeout. `user/service/impl/AddressServiceImpl.java` uses user-before-owned-child coordination. One common cart writer protocol covers add, replace, merge, delete and selections. Parent locks coordinate writers by agreement, not by magically locking child rows.
**Alternatives considered**: Lock User for every edit would serialize unrelated profile/address operations. Per-item UPSERT cannot alone handle atomic merges and bulk selections. Optimistic-only design creates avoidable conflicts; SERIALIZABLE and generic retries are not approved. Lock order is User→Cart when creating, never Cart→User. Catalog image locks follow afterwards in globally ascending UUID order.

**Implementation evidence**: A failing 105-product unit test exposed UUID.compareTo's signed-long ordering difference from PostgreSQL UUID ordering. Image-bearing product IDs are now sorted by canonical UUID string before chunking, with ORDER BY id ASC inside each database lock query. This preserves the approved global lock order across batches. Real contention tests verify timeout-before-lock, bounded 409, rollback, independent owners and pooled timeout restoration.

## 3. Batch catalog state without dropping unavailable rows

**Decision**: Add CatalogCartReadService with catalog-owned immutable DTOs and a variant-ID projection joining product. Return existence/publication/valid-price states even for hidden products, but no current hidden descriptive values. Chunk queries at 100 distinct IDs and assemble a complete response; calculate once from the prepared state.
**Rationale**: `catalog/service/ProductCatalogService.java#getProductSummaries` is capped at 100 and omits unpublished products; `getPublishedProductEntity` cannot represent unavailable retained items. At planning time ProductVariantRepository had only product-based queries; the implementation adds the cart scalar projection. Per-item getProduct loads excessive galleries and risks N+1 behavior.
**Alternatives considered**: One unbounded public summary call breaks its input contract. Treating omitted summaries as deleted cart rows violates D4. Cross-domain repository access violates constitution I. No new stock or purchase restriction was found beyond the approved catalog checks.

## 4. Retain prior public descriptions

**Decision**: Store cart-owned product ID plus public productName/SKU/options snapshots on eligible add or variant switch. Published responses use current public descriptions; hidden responses use snapshots. Reads never rewrite snapshots; mutations may refresh snapshots only from confirmed public data for the affected row.
**Rationale**: Catalog can change metadata after archival; returning newly hidden descriptive values violates D4. Cart-owned remembered values avoid a catalog-to-cart dependency. `ProductVariant` supplies SKU/options and Product supplies name, with UUID identities.
**Alternatives considered**: Reading current hidden names leaks catalog data. Omitting the row loses user choices. Full product/price/image snapshots duplicate data and could suggest a locked price. Store no price commitment or signed URL.

## 5. Publication-safe images without credential calls under cart locks

**Decision**: Catalog owns a resource-free PreparedImageUrls capability from the shared ImageUrlResolver. Cart orchestration performs owner-scoped nonlocking preflight to identify variant IDs (plus a requested add/update target); catalog checks candidate image metadata and the shared resolver captures credentials over the application-managed presigner before entering the authoritative cart transaction if images are candidates. Inside that transaction, fetch authoritative cart state, recheck publication and sign locally. No network image inspection/download is part of calculation. If preflight had no candidates and an image appears concurrently, return a safe nullable image until the next response rather than initialize credentials under locks.
**Rationale**: `ImageUrlResolver.prepare`, resource-free `PreparedImageUrls`, thin `SharedProductImageStorage` adapter and `ObjectStorageService.prepareDownloadSigner` separate potentially remote credential lookup from local signing over the application-managed presigner. Prepared capabilities own no resources. Routine avatar reads use the same resolver without HEAD; attachment/publication validation retains required object checks. A future CDN resolver can replace distribution policy without domain or database changes. `ProductCatalogServiceImpl` and `ProductRepository.lockStatusesForShare` enforce publication-safe ordered share locks. `WishlistServiceImpl.listWishlist` already uses write-capable but nonmutating transactions for this reason.
**Alternatives considered**: Calling getProductSummaries after locking cart may resolve credentials while holding its lock. Building fallible responses after commit can report failure after mutation. Read-only PostgreSQL transaction plus FOR SHARE is incompatible with the established path. Do not silently suppress signing failures: preparation failure occurs before mutation; signing failure rolls back the transaction. Narrow nullable fallback covers only absent/new image metadata, not storage failures. No durable temporary URL.

## 6. Exact amounts and strict inputs

**Decision**: BigInteger whole VND, checked Long selected quantity, Integer request/row quantities 1–1,000. Shared CartCalculator owns line/aggregate math; validator owns business checks. Use presence-aware update variant binding and cart-scoped strict Jackson 3 parsing for token types, unknown/duplicate keys and integer lexical values.
**Rationale**: `SellingPrice` and `ProductCatalogConverter` already use BigInteger/VND. `CatalogDataValidator` checks whole values but not negative values. `user/dto/request/UpdateUserRequest` demonstrates presence flags, JsonNode strictness and unknown-property rejection. Normal bean binding cannot by itself promise all approved coercion/duplicate-field rules.
**Alternatives considered**: Floating point or fixed-width money risks loss/overflow; ordinary nullable UUID cannot distinguish absent/null; global ObjectMapper changes would alter unrelated endpoints. Widen quantities before addition and reject final >1,000.

## 7. Schema, IDs and rollout

**Decision**: Long/BIGINT identity cart/item IDs by WishlistItem/Address precedent; preserve Long users and UUID variants/products. Add carts/cart_items, public descriptive snapshots, FK/unique/check/order indexes and MANAGE_CART USER grant in the next unused Flyway migration (currently V15). Referenced variants RESTRICT; cart-owned children cascade with cart deletion and existing user cleanup precedent is retained.
**Rationale**: `V10__create_wishlist_items.sql` establishes naming, user lifecycle and USER permission rollout. Approved D7 requires retained references. Existing `V3__enforce_catalog_relationships.sql` acquires catalog product locks for integrity; do not rewrite its triggers.
**Alternatives considered**: Changing all keys or prior migrations is outside scope. Cascading catalog deletion removes user choices. New variant archive fields or catalog delete APIs are unnecessary.

## 8. Errors and security

**Decision**: Add exact cart route MANAGE_CART matchers in existing bearer chain. Keep CurrentUserIdProvider/current-state token conversion, default USER-role rollout and current permission visibility. Use custom ApplicationException subtypes and existing GlobalExceptionHandler/ApiErrorFactory. Add narrow expected constraint/concurrency mappings, including deadlock SQLState 40P01, after rollback.
**Rationale**: `ApiError` extends ProblemDetail; global handling covers new cart controllers. Catalog-specific ApiExceptionHandler is controller-package scoped and is not the cart handler. ApiErrorFactory already handles 55P03/optimistic conflicts and wishlist-specific FKs, but lacks cart names/deadlock mapping.
**Alternatives considered**: A new security chain or token scheme is unnecessary. Broadly mapping every constraint failure to a business error conceals defects. Same safe 404 for unknown/foreign items and hidden/missing requested targets prevents disclosure.

## 9. Verification and tool setup

**Decision**: Use meaningful unit/MVC/repository/service/API/flow responsibilities; D8 requires synchronized real-transaction races, not timing sleeps. Mock existing image signing boundary in arithmetic tests; include separate publication/signing integration checks. Prove real commit/rollback without test-level transaction camouflage.
**Rationale**: Existing wishlist IT uses independent fixtures, injected signing failures and PostgreSQL. `application-test.properties` pool size is 2; concurrency classes override it to 6, avoid barriers while starving workers and bound future waits. Surefire/Failsafe discovery is inspected directly; actual results are in quickstart.md.
**Alternatives considered**: Omnibus tests, duplicate boundary assertions, external S3 dependency for arithmetic, or claiming Maven discovery without reports are rejected.

Bash setup was attempted exactly as requested but failed at MSYS named-object access; bundled PowerShell setup resolved FEATURE_SPEC/IMPL_PLAN/FEATURE_DIR successfully. Active feature is `specs/007-shopping-cart`; actual Git branch is `main` although setup labels BRANCH with the directory name. No hooks file exists. No AGENTS.md was found in this repository.

## Approved implementation boundary (2026-11-11)

The earlier storage-only selection is historical; the subsequent `$speckit-implement` invocation authorizes cart implementation. Cart entities/controllers/services, V15 and U2 contention tests now exist alongside the shared image refactor. URL distribution itself requires no migration. Variant/review image domains remain outside this feature.

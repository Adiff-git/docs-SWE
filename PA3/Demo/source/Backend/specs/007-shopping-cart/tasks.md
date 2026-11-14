# Tasks: Persistent Shopping Cart

**Input**: [spec.md](spec.md), [plan.md](plan.md), [research.md](research.md), [data-model.md](data-model.md), [API contract](contracts/api.md), [service contracts](contracts/internal-services.md), [engineering evidence](contracts/engineering.md), [quickstart.md](quickstart.md).
**Prerequisites**: Q1 A inventory deferred; Q2 A maximum 1,000 per row; Q3 D1–D8 approved. All requirement checklist items pass. Actual branch is main.
**Tests**: Explicitly required by the brief, constitution and D8. Write tests before corresponding implementation; after minimal types compile, prove meaningful failing assertions before fixing behavior. Missing symbols alone do not demonstrate a behavioral test failure.
**Organization**: Shared foundations, US1 (P1), US2 (P1), US3 (P2), cross-cutting verification. Task markers below track verified implementation progress; the generation notes preserve the original planning state.

## Format: `[ID] [P?] [Story] Description`

[P] means different-file work can run concurrently after the stated prerequisites. Story tasks carry [US1], [US2] or [US3]. Paths are repository-relative; resolve absolute paths for filesystem tool calls. No new dependencies, global parser changes, empty scaffolding, mechanical accessor tests, automatic commits or pushes.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the actual repository baseline without reinitializing the project.

- [X] T001 Recheck approved artifacts/constitution against current `demo/pom.xml`, `demo/src/main/resources/db/migration/` and `demo/src/main/java/com/example/demo/auth/config/AuthSecurityConfiguration.java`; record discrepancies and select the next unused migration version (currently V15) in `specs/007-shopping-cart/plan.md`, preserving inventory/checkout exclusions and existing dependency approvals.
- [X] T002 Verify Java 25, Docker and `demo/mvnw.cmd`; run baseline tests/verify through `demo/pom.xml` when infrastructure permits, inspect `demo/target/surefire-reports/` and `demo/target/failsafe-reports/`, and record actual discovery/failures or infrastructure limitations in `specs/007-shopping-cart/quickstart.md` without fixing unrelated failures or claiming unavailable checks pass.

**Checkpoint**: Migration slot, current boundaries and verification baseline are known.

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared persistence, prepared data, catalog integration and safe errors. Complete before story behavior work.

- [X] T003 Write PostgreSQL mapping/constraint tests in `demo/src/test/java/com/example/demo/cart/repository/CartRepositoryIT.java` and `demo/src/test/java/com/example/demo/cart/repository/CartItemRepositoryIT.java` for one cart/user, one row/variant, quantity 0/1/1000/1001, owned ordered reads, referenced catalog deletion RESTRICT and legitimate cart-owned cascade cleanup; keep setup independent of queries under test and use appropriate slice isolation or committed fixtures.
- [X] T004 Create next-unused `demo/src/main/resources/db/migration/V15__create_carts.sql` (change version only if T001 found collision): carts.id is "Primary key; new domain follows wishlist/address precedent" (Long/BIGINT identity), user_id is "NOT NULL, UNIQUE, FK users(id), existing user cleanup precedent ON DELETE CASCADE"; add `uk_carts_user_id` and `fk_carts_user_id` without editing applied migrations.
- [X] T005 Extend `demo/src/main/resources/db/migration/V15__create_carts.sql` with cart_items constraints quoted from data-model.md: id "Primary key, opaque external item identifier" (Long/BIGINT identity), cart_id "NOT NULL FK carts(id), ON DELETE CASCADE: true aggregate lifecycle", product_variant_id "NOT NULL FK product_variants(id), ON DELETE RESTRICT", product_id "NOT NULL FK products(id), ON DELETE RESTRICT; original product for safe snapshot rendering/switch checks", quantity "NOT NULL, CHECK BETWEEN 1 AND 1000", selected "NOT NULL; application default true only for new rows", added_at "NOT NULL; injected Clock sampled once per new row; never changed on replacement/add/merge target" (TIMESTAMPTZ), public_product_name/public_sku "NOT NULL, nonblank; previously public snapshot", public_options "NOT NULL object; copy eligible variant options; empty object allowed for an unparameterized variant" (JSONB); apply all named constraints/indexes from data-model.md and MANAGE_CART USER-role grant following V10, failing if USER is absent.
- [X] T006 Map `demo/src/main/java/com/example/demo/cart/entity/Cart.java` and `demo/src/main/java/com/example/demo/cart/entity/CartItem.java` to T004–T005 exactly: preserve Long user/cart/item and UUID catalog IDs, "NOT NULL" references, "CHECK BETWEEN 1 AND 1000" quantity, nonnull selection/Instant addition time and nonblank/object snapshots; use lazy safe JPA/Lombok, cascade only within cart, no stored money/URLs, and enforce variant-parent/productId consistency in eligible mutations rather than claiming separate FKs prove pair consistency.
- [X] T007 Implement `demo/src/main/java/com/example/demo/cart/repository/CartRepository.java` and `demo/src/main/java/com/example/demo/cart/repository/CartItemRepository.java` with owned lookup/cart PESSIMISTIC_WRITE, transaction-local positive `cart.lock-timeout-ms` (default 5000) applied inside the transaction BEFORE the first blocking cart lock query, fresh owner-scoped item/variant reads, complete projections `(added_at DESC,id ASC)` and save/delete/flush; no catalog/user repository access and no cart pagination/cap; make T003 pass.
- [X] T008 Define only foundation-ready `demo/src/main/java/com/example/demo/cart/dto/response/CartReadSeed.java` as a Lombok-based immutable `@Value` DTO class in `com.example.demo.cart.dto.response` (not a Java record; defensively copy collection/map data), `demo/src/main/java/com/example/demo/catalog/dto/response/CartVariantState.java` and `demo/src/main/java/com/example/demo/catalog/service/CatalogCartReadService.java` using the existing storage-owned PreparedImageUrls capability (no closeable cart context); fix catalog signatures and nullable-price/public-field semantics per contracts/internal-services.md without references to later cart request/response types. Defer CartService/CartTransactionService, PreparedCart and AddCartResult to T016; keep foundation compilable, copied data immutable and catalog independent of cart.
- [X] T009 Write catalog tests in `demo/src/test/java/com/example/demo/catalog/service/CatalogCartReadServiceImplTest.java` and `CatalogCartReadServiceIT.java` for mixed publication, zero/negative/fractional/invalid prices, hidden fields, >100 distinct variants/products, deduplication, preparation outside locks, globally UUID-ordered publication locks across chunks, late hiding/new-image null fallback and propagated signing failure; stub the existing storage seam without external S3 for calculation checks.
- [X] T010 Implement `demo/src/main/java/com/example/demo/catalog/service/CatalogCartReadServiceImpl.java` and variant-ID scalar batch projection in `demo/src/main/java/com/example/demo/catalog/repository/ProductVariantRepository.java`, reusing/extending `ProductImageRepository.java` and `ProductRepository.java` as needed; chunk at 100 internally, retain hidden identity/status/allowed price while withholding hidden descriptions, prepare credentials before cart transactions, sign locally after final publication checks and safely return nullable images introduced after signer-free preflight; make T009 pass without changing public catalog/wishlist behavior.
- [X] T011 Add descriptive ApplicationException subtypes in `demo/src/main/java/com/example/demo/cart/exception/InvalidCartRequestException.java`, `CartItemNotFoundException.java`, `CartQuantityLimitException.java`, `CartVariantSwitchException.java`, `CartItemUnavailableException.java` and `CartConflictException.java`; extend `demo/src/main/java/com/example/demo/common/exception/ApiErrorFactory.java` narrowly for expected cart FK/uniqueness races, 55P03/40P01/optimistic conflicts after rollback, preserving safe 401/404/409 and existing signing 503 while escaped checks remain 500; test mappings in `demo/src/test/java/com/example/demo/common/exception/ApiErrorFactoryTest.java` without generic wrapping or a new security chain.

**Checkpoint**: Shared schema, owned repositories, DTO/service contracts, catalog presentation and errors work. No business endpoint is yet claimed complete.

## Phase 3: User Story 1 — Save and revisit purchase choices (Priority: P1) — MVP

**Goal**: Private persistent viewing/addition, current prices, default selection, retained unavailable rows.
**Independent Test**: Fresh user GET returns zero state without insert; add 2 then 3 gives one selected row of 5, 201 then 200. Later session recovers quantities with current prices. Unselected fixture rows stay unselected on repeated add. Parallel accepted additions/first creation preserve invariants. Selection endpoints are not needed: seed selection states through fixtures.

### Tests for User Story 1

- [X] T012 [P] [US1] Write GET/POST MVC tests in `demo/src/test/java/com/example/demo/cart/controller/CartControllerTest.java` for empty/full response, 201+Location versus merge 200, private/no-store, bearer 401/MANAGE_CART 403, required canonical UUID/strict integer 1–1000, null/unknown/duplicate/nonobject bodies, string/decimal/exponent coercion rejection, unsupported GET body/query, authentication/authorization-first 401/403, unsupported-method 403 under deny-all and authorized supported-route media-type 415 ProblemDetail and no owner input; exercise real binding, not just setters.
- [X] T013 [P] [US1] Write facade/transaction unit tests in `demo/src/test/java/com/example/demo/cart/service/CartServiceImplTest.java` and `CartTransactionServiceImplTest.java` for owner-scoped non-authoritative preflight, no request-owned signer or cleanup on success/failure, separate proxy calls, missing-cart lock/recheck/create, no cart on failure, widened resulting quantity checks, selection/time preservation and no mandatory fallible response work after commit.
- [X] T014 [P] [US1] Write arithmetic/mapping/validator tests in `demo/src/test/java/com/example/demo/cart/calculator/CartCalculatorTest.java`, `demo/src/test/java/com/example/demo/cart/converter/CartConverterTest.java` and `demo/src/test/java/com/example/demo/cart/validator/CartValidatorTest.java` for exact zero/large whole-VND amounts, row count versus checked Long quantity, empty zero totals, null ineligible subtotal, safe snapshots/no hidden data, 999+1 success/1000+1 rejection and converters without fetching/signing; use plain unit tests without Spring.
- [X] T015 [US1] Write real read/add commit/rollback and synchronized first-creation/duplicate-add tests in `demo/src/test/java/com/example/demo/cart/service/CartServiceIT.java`; use independent committed transactions, controlled starts, bounded futures and adequate class-local pool size instead of default 2; prove accepted-increment sums, near-limit unchanged failures, bounded lock contention/409/no retry, rollback and timeout reset on pooled connection reuse with unrelated DB failures distinguished, independent users, signer rollback of new cart, archived snapshots, complete >100-product reads, ordering ties and zero GET writes.

### Implementation for User Story 1

- [X] T016 [US1] Add `demo/src/main/java/com/example/demo/cart/dto/request/AddCartItemRequest.java` with required canonical UUID variantId and strict integer quantity 1–1000; implement Lombok `demo/src/main/java/com/example/demo/cart/dto/response/CartResponse.java` and `CartItemResponse.java` with all API fields, nullable image/unitPrice/ineligible subtotal, independent selected/purchasable, Long counts/quantity and reused exact VND money shape, without exposed entities. In this same task define `demo/src/main/java/com/example/demo/cart/dto/response/PreparedCart.java` and `demo/src/main/java/com/example/demo/cart/dto/response/AddCartResult.java` as Lombok-based immutable `@Value` DTO classes in `com.example.demo.cart.dto.response` (not Java records; defensively copy collection/map data where applicable), preserving prepared-data/status responsibilities; then define `demo/src/main/java/com/example/demo/cart/service/CartService.java` and `CartTransactionService.java` for GET/add only, after their required DTOs exist. Add later-story methods only in T028 and T037.
- [X] T017 [US1] Implement cart-scoped `demo/src/main/java/com/example/demo/cart/controller/CartRequestBodyAdvice.java` and `CartRequestReader.java` using existing Jackson 3 facilities to detect duplicate keys before tree materialization, reject unknown properties/coercion/nonobject/empty/null bodies, enforce integer/canonical UUID tokens and reject unsupported GET body/query; preserve global ObjectMapper/other controllers and existing ProblemDetail handling. Add cart-path-scoped unsupported-media-type 415 mapping after successful security checks; never use body parsing or MVC handling to bypass earlier 401/403. Unsupported methods remain 403 under the existing deny-all policy; no 405 guarantee.
- [X] T018 [US1] Implement `demo/src/main/java/com/example/demo/cart/validator/CartValidator.java` owner, positive/bounded request/result quantity and purchase checks with named 1/1000 constants, widened arithmetic, PUBLISHED/nonnegative finite whole-price eligibility and safe missing/hidden target handling/reason precedence; do not add stock checks or duplicate authoritative amount math.
- [X] T019 [US1] Implement `demo/src/main/java/com/example/demo/cart/calculator/CartCalculator.java` and `demo/src/main/java/com/example/demo/cart/converter/CartConverter.java` so one prepared state drives exact BigInteger VND line values, checked Long eligible-selected counts/quantities, equal selectedSubtotal/finalTotal and pure DTO/snapshot mapping; no converter queries/signing/validation or duplicate business calculations; make T014 pass for read/add.
- [X] T020 [US1] Implement GET/add in `demo/src/main/java/com/example/demo/cart/service/impl/CartTransactionServiceImpl.java` using REQUIRED/READ COMMITTED, business-nonmutating write-capable image GET, SET LOCAL-equivalent timeout BEFORE the first blocking cart lock, common owned cart lock for writes, missing-cart UserService timeout-before-user-lock→recheck→create and no Cart→User lock, fresh child reads, public snapshot capture, new selected=true/preserved existing selection, validate before writes and prepare complete response/flush before commit without credential network calls under locks.
- [X] T021 [US1] Implement GET/add facade in `demo/src/main/java/com/example/demo/cart/service/impl/CartServiceImpl.java` without ambient transaction: owned projection preflight plus requested target, shared ImageUrlResolver.prepare() credentials capability before authoritative transaction, repeated validation in proxied transaction service and original error propagation without cart-context cleanup; empty reads avoid cart creation/signing and failures preserve database state.
- [X] T022 [US1] Implement GET `/api/me/cart` and POST `/api/me/cart/items` in `demo/src/main/java/com/example/demo/cart/controller/CartController.java` with validation/current identity, 201+Location for new row or 200 for merge and full CartResponse; ensure private/no-store success/error behavior via cart-scoped `CartRequestBodyAdvice.java` as needed, and do not expose later-story endpoints prematurely.
- [X] T023 [US1] Add exact GET/add MANAGE_CART matchers in `demo/src/main/java/com/example/demo/auth/config/AuthSecurityConfiguration.java`, preserving bearer/session/account checks and deny-all fallback (missing/invalid bearer 401; insufficient permission or unsupported method 403 before MVC/body processing); prove migration permission inheritance for existing/future USER assignments, custom-role denial and next-request grant/revoke visibility with unchanged credentials in `demo/src/test/java/com/example/demo/cart/controller/CartControllerIT.java`.
- [X] T024 [US1] Complete real GET/add HTTP integration in `demo/src/test/java/com/example/demo/cart/controller/CartControllerIT.java` for authenticated ownership/no-price-trust/current prices and revisit, add only distinct rollback/batch assertions to `demo/src/test/java/com/example/demo/cart/service/CartServiceIT.java`, make T012–T015 pass and record actual US1 discovery/counts/results in `specs/007-shopping-cart/quickstart.md`.

**Checkpoint**: Save/revisit MVP works without US2/US3 endpoints. Fixture selections already produce correct current eligible totals and unavailable rows stay visible safely.

## Phase 4: User Story 2 — Adjust and remove choices (Priority: P1)

**Goal**: Quantity replacement, same-product variant switch/merge and owned removal with atomic failures.
**Independent Test**: A=2 replacement request 4 gives 4; switching to absent B with 4 gives 4; A=2 to existing B=3 with request 4 gives B=7/source removed, preserving target identity/selection/time. Invalid target/cross-product/overflow leaves both unchanged. Delete returns 204, repeated unknown delete 404.

### Tests for User Story 2

- [X] T025 [P] [US2] Extend `demo/src/test/java/com/example/demo/cart/controller/CartControllerTest.java` for item PUT/DELETE: required quantity, omitted variant retained/explicit null rejected, strict update tokens/duplicates, 400 request bound versus 422 final bound, 200 cart/204 bodyless response, malformed path versus identical unknown/foreign 404, rejected DELETE body/query and ownership before target-detail disclosure.
- [X] T026 [P] [US2] Extend `demo/src/test/java/com/example/demo/cart/service/CartTransactionServiceImplTest.java` for replacement, absent/present target switches, target+request without old-source quantity, same-product restriction, identity/selection/time/snapshot preservation, unavailable-source→eligible-target recovery and unavailable retained-target rejection before writes; extend `CartServiceImplTest.java` only for distinct facade/preflight behavior.
- [X] T027 [US2] Extend `demo/src/test/java/com/example/demo/cart/service/CartServiceIT.java` with committed merge/removal, forced post-write rollback, identical missing/foreign failures, target 600+400 success/600+401 unchanged, synchronized merge-versus-add/two-merges/delete conflicts and last-row empty-cart retention; use independent verification transactions, not test-level rollback camouflage.

### Implementation for User Story 2

- [X] T028 [US2] Create `demo/src/main/java/com/example/demo/cart/dto/request/UpdateCartItemRequest.java` with required strict quantity 1–1000 and presence-aware variantId (omitted retain, explicit null invalid); extend `demo/src/main/java/com/example/demo/cart/controller/CartRequestReader.java` and `CartRequestBodyAdvice.java` for update/path/body/query semantics without global parser changes; define update/delete methods on `demo/src/main/java/com/example/demo/cart/service/CartService.java` and `CartTransactionService.java` now, after their input types exist and before T030 implements them.
- [X] T029 [US2] Extend `demo/src/main/java/com/example/demo/cart/validator/CartValidator.java` and `demo/src/test/java/com/example/demo/cart/validator/CartValidatorTest.java` for owned source, same-product target, required replacement quantity, target-only switch eligibility and widened final bound 1000; handle catalog invalid-price/hidden/missing targets safely without changing catalog-wide policy.
- [X] T030 [US2] Implement replacement/switch/merge/removal in `demo/src/main/java/com/example/demo/cart/service/impl/CartTransactionServiceImpl.java` and owned match/delete in `demo/src/main/java/com/example/demo/cart/repository/CartItemRepository.java`: lock cart before fresh children, validate final quantities/rows before mutation, preserve prescribed identity/selection/time, refresh snapshots only from public target, delete source atomically and build PUT response before commit; delete needs no signer and never creates cart.
- [X] T031 [US2] Extend `demo/src/main/java/com/example/demo/cart/service/impl/CartServiceImpl.java` for the update/delete signatures introduced in T028 with non-authoritative preflight, identical safe source 404, repeated ownership before target lookup, signer prep outside locks and rollback on update response failure.
- [X] T032 [US2] Add PUT `/api/me/cart/items/{itemId}` and DELETE `/api/me/cart/items/{itemId}` in `demo/src/main/java/com/example/demo/cart/controller/CartController.java` and exact MANAGE_CART matchers in `demo/src/main/java/com/example/demo/auth/config/AuthSecurityConfiguration.java`; retain complete-quantity PUT semantics, 200/204/404 contracts and existing security chain.
- [X] T033 [US2] Extend `demo/src/test/java/com/example/demo/cart/controller/CartControllerIT.java` for real owned replacement/switch/merge/delete, foreign-owner parity, unavailable-source recovery and unchanged rejected operations; run US1+US2 including T025–T027 and record actual reports in `specs/007-shopping-cart/quickstart.md`, avoiding duplicate HTTP copies of repository/concurrency tests.

**Checkpoint**: Edit/remove slice is independently testable with fixture selection states; it does not require selection endpoints.

## Phase 5: User Story 3 — Select choices and understand estimates (Priority: P2)

**Goal**: Individual/all selection with current eligibility and exact estimates, preserving quantities.
**Independent Test**: Selected eligible rows 2×100 and 3×50 give row count 2, quantity 5 and total 350. Deselect first gives count 1/quantity 3/total 150. Archive selected first: selected remains true, purchasable false and eligible total excludes it. Select-all skips unavailable flags; deselect-all clears every flag.

### Tests for User Story 3

- [X] T034 [P] [US3] Extend `demo/src/test/java/com/example/demo/cart/controller/CartControllerTest.java` for both selection PUTs: required strict boolean, rejected omitted/null/string/numeric/unknown/duplicate fields, 200 full cart, safe unknown/foreign 404, unavailable selection 422, private/no-store and MANAGE_CART on both routes.
- [X] T035 [P] [US3] Extend `demo/src/test/java/com/example/demo/cart/calculator/CartCalculatorTest.java` and `demo/src/test/java/com/example/demo/cart/validator/CartValidatorTest.java` for 350→150 examples, checked aggregate quantity >1000 across rows, selected/purchasable independence, unavailable null subtotal/reason priority, select-all skip/deselect-all clear and rejection of already-selected unavailable true; keep converter tests separate from business logic.
- [X] T036 [US3] Extend `demo/src/test/java/com/example/demo/cart/service/CartServiceIT.java` for individual/bulk mixed availability, missing-cart no-insert no-op, archive/republish/current prices with no GET writes, unchanged quantity on selection, synchronized selection-versus-quantity/add/merge and full rollback on final eligibility/signing failure; reuse deterministic worker infrastructure with independent committed checks.

### Implementation for User Story 3

- [X] T037 [US3] Create `demo/src/main/java/com/example/demo/cart/dto/request/CartSelectionRequest.java` with required Boolean selected; extend `demo/src/main/java/com/example/demo/cart/controller/CartRequestReader.java` for literal true/false only, rejecting omitted/null/coerced/duplicate/unknown fields through current Bean Validation/binding without weakening add/update parsing; add selection signatures to `demo/src/main/java/com/example/demo/cart/service/CartService.java` and `CartTransactionService.java` in this task before T038 implements them.
- [X] T038 [US3] Implement individual/bulk selection in `demo/src/main/java/com/example/demo/cart/service/impl/CartTransactionServiceImpl.java` and `demo/src/main/java/com/example/demo/cart/validator/CartValidator.java`: common cart lock, owned source, final prepared eligibility, reject unavailable true even if already selected, permit false, bulk true changes eligible rows only/preserves unavailable flags, bulk false clears all, missing bulk cart is no-op, no overwritten quantities or GET snapshot/selection writes.
- [X] T039 [US3] Extend `demo/src/main/java/com/example/demo/cart/service/impl/CartServiceImpl.java` with both selection operations whose signatures were introduced in T037 using established preflight/resource-free prepared-URL/proxy boundaries; derive all totals from the same final state via CartCalculator and preserve rollback rather than refetch after commit.
- [X] T040 [US3] Add PUT `/api/me/cart/items/{itemId}/selection` and PUT `/api/me/cart/selection` in `demo/src/main/java/com/example/demo/cart/controller/CartController.java` and exact MANAGE_CART matchers in `demo/src/main/java/com/example/demo/auth/config/AuthSecurityConfiguration.java`; preserve 200 full response, current security, strict fields, safe errors and private caching rules.
- [X] T041 [US3] Extend `demo/src/test/java/com/example/demo/cart/controller/CartControllerIT.java` with real selected totals/unavailable behavior, same-token permission visibility on selection and empty bulk no-insert; pass T034–T036 plus earlier story tests and record actual counts/results in `specs/007-shopping-cart/quickstart.md`.

**Checkpoint**: All stories work and can be acceptance-tested independently from controlled fixtures. No stock, discounts/fees, price lock, checkout or trusted client owner/amount data.

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T042 Write/pass `demo/src/test/java/com/example/demo/e2e/CartFlowIT.java` for actual existing registration/verification or provisioned account/login, empty view, add/repeated add, quantity/variant changes, selection, revisit in a later valid session and removal; use real internal auth/cart/catalog boundaries and established controlled infrastructure, never bypass authentication or label an API-only test as a full flow.
- [X] T043 Audit `demo/src/main/java/com/example/demo/cart/` and `demo/src/main/java/com/example/demo/catalog/service/CatalogCartReadServiceImpl.java` against service contracts; extend `demo/src/test/java/com/example/demo/catalog/service/CatalogCartReadServiceIT.java` and `demo/src/test/java/com/example/demo/cart/service/CartServiceIT.java` only for missing >100-product batch/global lock-order evidence, converter query absence, snapshot/image privacy, resource-free prepared URL reuse without close, credentials outside locks, final flags/totals consistency, no GET writes, narrow conflict errors and catalog deletion restriction.
- [X] T044 Run full `demo/mvnw.cmd -f demo/pom.xml test` and `verify`; inspect `demo/target/surefire-reports/` and `demo/target/failsafe-reports/` for nonzero cart/catalog/security discovery, failures/skips, schema validation and all D8 race results; record configured versus unavailable quality checks in `specs/007-shopping-cart/quickstart.md`, fixing only feature-caused failures without unapproved dependencies/plugins or weakened tests/security.
- [X] T045 Execute `specs/007-shopping-cart/quickstart.md` HTTP walkthrough using isolated fixtures and existing `compose.dev.yaml` when available; record statuses 201/200/204/400/401/403/404/409/422/503 using deterministic tests where injection is needed, exact amounts, zero-insert reads, owner protection and current permissions; no tokens/secrets, destructive volume resets or invented success when infrastructure is blocked.
- [X] T046 Reconcile actual implemented signatures/fields/migration slot and verification evidence in `specs/007-shopping-cart/contracts/api.md`, `contracts/internal-services.md`, `data-model.md`, `plan.md`, `quickstart.md` and `checklists/requirements.md`; preserve approved scope/policies and distinguish requirement readiness from delivered evidence, update `specs/007-shopping-cart/tasks.md` only as tasks complete, and leave commits/push/deployment for explicit authorization.

## Dependencies & Execution Order

### Phase dependencies

Setup T001→T002 → foundation T003–T011 → US1 T012–T024 → US2 T025–T033 → US3 T034–T041 → cross-cutting T042–T046. This is the safe default schedule; shared production files are not parallel work areas.

### Foundation dependencies

T003 defines persistence acceptance; T004→T005→T006→T007 implements/proves it. T008 fixes catalog-only shared signatures before T009 tests→T010 catalog implementation. Cart contracts are introduced incrementally: GET/add and response-dependent prepared types in T016, update/delete in T028, selection in T037; no foundation type may reference a later-story DTO. T011 finishes shared errors. Complete every foundation task before stories. Where a test is initially uncompilable because a type is new, later prove an actual behavior failure before implementing that behavior.

### User story dependencies

US1 is the first deliverable with no later-story dependency. US2 and US3 consume its read/add/transaction infrastructure. US3 has no semantic dependency on US2 variant editing/removal and can be tested from fixtures; default execution nevertheless completes US2 first because controller, validator, transaction/facade and tests share files. Cross-story parallel edits require explicit separate ownership/reconciliation rather than treating stories as conflict-free.

Within US1: T012/T013/T014 may run together after foundation; T015 defines real transaction acceptance. T016→T017 and T018→T019 establish types/logic, then T020 transactional behavior (requires both chains)→T021 facade→T022 endpoints→T023 security→T024 checkpoint. All writers use the common lock protocol from their first implementation.

Within US2: T025/T026 may run together after US1; T027 defines transaction acceptance; T028→T029→T030→T031→T032 implements the slice; T033 validates it. Within US3: T034/T035 may run together after preceding checkpoints; T036 defines transaction acceptance; T037→T038→T039→T040 implements; T041 validates. Never run same-file task edits together.

### Dependency graph

```text
Setup → Foundation → US1 (P1: save/revisit MVP)
                       ├─→ US2 (P1: edit/remove) ─┐
                       └─→ US3 (P2: selection) ───┴─→ Full-flow/regression/walkthrough
                            ↑
             default schedule waits for US2 to avoid shared-file collisions
```

## Parallel Execution Examples

### US1

After T011, write T012 MVC tests in CartControllerTest.java, T013 facade/transaction tests in CartServiceImplTest.java/CartTransactionServiceImplTest.java, and T014 validator/calculator/converter tests concurrently. They have different files and consume the documented US1 contract; T016 introduces its compilable DTOs/interfaces before implementation. Establish meaningful failing assertions once those types exist. Implementation follows; do not concurrently extend CartServiceIT.java in multiple tasks or share mutable database fixtures.

### US2

After the US1 checkpoint, T025 edits CartControllerTest.java while T026 edits service unit tests. T027 real transactions and production tasks remain sequential. No speculative parallelism across shared source files.

### US3

After the US2 checkpoint, T034 edits MVC tests while T035 edits calculator/validator tests. Once finished, proceed to T036 and implementation. Application concurrency inside a test is separate from task-authoring concurrency.

## Implementation Strategy

### MVP First (US1)

Complete setup/foundations/US1 and validate its checkpoint: persistence across sessions, default/preserved selection, duplicate merging, current pricing/hidden-row safety and simultaneous first-add/increment correctness. It is an interim deliverable, not completion of the approved feature. Reaching it does not authorize deployment or commits.

### Incremental Delivery

Add US2 edits/removal and independently validate using fixture selections. Add US3 selection/totals and races, reusing the same transaction/calculation boundaries. Finish actual authenticated flow, regressions/test discovery and quickstart evidence. Check off tasks only after the corresponding work is verified. Helpers at `demo/src/test/java/com/example/demo/fixture/cart/CartFixtures.java` or `demo/src/test/java/com/example/demo/testdata/cart/CartTestData.java` may be created within test tasks only when they remove real duplication; no empty omnibus infrastructure.

## Requirements Coverage

| Requirements/policies | Tasks |
| --- | --- |
| FR-001/002, D1 ownership/lifecycle | T003–T008, T013, T015, T020–T024, T027, T030–T033, T036, T038–T042 |
| FR-003/007, D2 add/bounds | T005–T007, T012–T020, T024, T027–T030 |
| FR-004, D3 variant semantics | T025–T033 |
| FR-005/006/008, D4 eligibility/no stock/retention | T008–T010, T014–T021, T026–T033, T035–T041 |
| FR-009/010 response/totals/images | T009–T010, T014–T024, T035–T043 |
| FR-011, D5 order/full cart | T003, T007, T009–T010, T015, T020, T043 |
| FR-013, D6 permission/status/binding/error | T005, T011–T012, T016–T017, T022–T025, T028, T032–T034, T037, T040–T045 |
| D7 catalog deletion integrity | T003–T006, T043–T044 |
| FR-012, D8 concurrency/atomicity | T007, T011, T013, T015, T020–T021, T027, T030–T031, T036, T038–T039, T043–T044 |
| FR-014 scope exclusions | T001, T043, T046 |
| SC-001–SC-006 measurable acceptance | Story checkpoints and T042–T046 |

## Generation Validation and Hooks

Generated 2026-11-11 from the resolved tasks template. Bash setup failed at MSYS NtCreateDirectoryObject access; bundled PowerShell setup succeeded and found all design documents. The invocation's trailing backslash adds no feature scope. No extensions.yml exists, so no before_tasks/after_tasks hooks are registered or dispatched. Validate syntax/IDs/story labels/file paths/dependency references as documentation; no implementation or test success is claimed by creating this list.

Generation checks passed: 46 unchecked tasks with contiguous unique IDs T001–T046; 13 US1, 9 US2, 8 US3 and 16 shared/cross-cutting. Seven [P] tasks form three different-file test-authoring groups. Every task has the required checkbox/ID, correct phase-specific story label and a concrete file path. No dangling task references, broken local document links or template placeholders were found. Only this task artifact was created during task generation; application builds/tests were not run.


## Approved Analysis Remediation (2026-11-11)

C2 resolved: CartReadSeed, PreparedCart and AddCartResult use `cart/dto/response` and package `com.example.demo.cart.dto.response` as Lombok-based immutable `@Value` DTO classes with defensive copies where applicable. Paths and conventions are synchronized with plan.md, data-model.md and contracts/internal-services.md. Responsibilities, behavior, task IDs, T008/T016 staging and HTTP contracts are unchanged. This correction originally updated design documents only. The subsequent speckit-implement invocation authorizes the runtime work tracked above.

I1 B: Introduce cart service methods/types incrementally by story, keeping foundation compilable. C1: Authentication/authorization takes precedence; invalid/missing bearer is 401, denied permissions/unsupported methods are 403 under deny-all. A permitted supported method may return 415 after security checks. U1: use shared resource-free PreparedImageUrls; remove cart-specific closeable image context/cleanup. Genuine cleanup must never replace success or the original error and must log safely. U2: set transaction-local timeout before the first blocking cart lock; preserve user-before-cart creation and user timeout before user lock. That earlier storage-only scope is historical. Cart code and contention tests are now implemented under the subsequent speckit-implement invocation.

## Implementation completion — 2026-11-12

All T001–T046 are complete. Final full verify passed 342 unit/controller and 337 integration tests (679 total), zero failures/errors/skips; JAR packaging and 15-migration schema validation passed. See quickstart.md for observed evidence, environment options and the isolated real-HTTP walkthrough. requirements.md remained read-only at 16/16 checked. No implementation hooks exist. No commits, pushes or deployment were performed; the earlier shared storage changes were preserved.

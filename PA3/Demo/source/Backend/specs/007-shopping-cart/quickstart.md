# Quickstart and Validation: Shopping Cart

The cart endpoints, source and V15 migration are implemented. Run from repository root with disposable development/test data. Observed automated execution is recorded below; the standalone Compose/curl steps are reproducible instructions, not a claim that a local deployment was modified.

## Prerequisites

Java 25, the bundled Maven wrapper, Docker for PostgreSQL Testcontainers and local Compose. Existing secrets/configuration must be supplied through local environment files, never copied into artifacts or logs. See `.env.example`, `compose.dev.yaml` and `demo/src/main/resources/application-local.properties`. Existing local registration may require enabled email verification and Mailpit confirmation; use an already provisioned active account or complete the existing registration flow. Do not invent a cart-specific login bypass.

Prepare catalog fixtures using existing catalog fixture/import facilities: one PUBLISHED product with variants A/B/C, prices whole nonnegative VND (e.g. A=100, B=50), and a second product for rejected cross-product switching. IDs must be discovered from fixture results or existing GET `/api/products` then `/api/products/{id}`, never hardcoded generated IDs. No inventory data is needed.

## Build and automated validation

PowerShell commands from repository root:

```powershell
.\demo\mvnw.cmd -f .\demo\pom.xml test
.\demo\mvnw.cmd -f .\demo\pom.xml verify
```

Docker must be available for the existing Testcontainers tests. Run the targeted cart unit/MVC group during development, then the full regression suite above:

```powershell
.\demo\mvnw.cmd -f .\demo\pom.xml '-Dtest=Cart*Test' test
.\demo\mvnw.cmd -f .\demo\pom.xml '-Dit.test=Cart*IT' verify
Get-ChildItem .\demo\target\surefire-reports\TEST-*Cart*.xml
Get-ChildItem .\demo\target\failsafe-reports\TEST-*Cart*.xml
```

Target patterns refer to planned test names; absent classes/reports mean verification is incomplete. Verify nonzero test counts, zero failures/errors and correct phase discovery. Include catalog boundary tests and current security regression coverage in the full suite. No extra quality plugin is authorized; report configured versus absent static checks honestly.

Expected responsibilities: CartValidatorTest, CartCalculatorTest, CartConverterTest, CartServiceImplTest/CartTransactionServiceImplTest where responsibilities differ, CartControllerTest, CartRepositoryIT/CartItemRepositoryIT for actual custom mappings/queries/constraints, CartServiceIT, CartControllerIT, e2e/CartFlowIT, and narrow CatalogCartReadServiceImplTest/IT. Do not create mechanical DTO/entity/delegation tests or duplicate service IT names for one responsibility.

## Start local runtime

```powershell
docker compose --env-file .env.local -f compose.dev.yaml up -d --build
```

Uses existing PostgreSQL, LocalStack/image-storage, Mailpit and backend topology; default backend port is 18081 unless overridden. Confirm Flyway applies the new migration and existing schemas still validate. No destructive volume reset is required.

Obtain credentials through the existing login flow. Keep values out of reports:

```powershell
$cartBase = 'http://localhost:18081'
$cartLoginBody = @{ identifier = $env:CART_TEST_IDENTIFIER; password = $env:CART_TEST_PASSWORD } | ConvertTo-Json
$cartLogin = Invoke-WebRequest -Method Post -Uri "$cartBase/api/auth/login" -ContentType 'application/json' -Body $cartLoginBody
$cartHeaders = @{ Authorization = [string]$cartLogin.Headers['Authorization'] }
Invoke-RestMethod -Uri "$cartBase/api/me/cart" -Headers $cartHeaders
```

Login returns the bearer token in its Authorization response header; do not assume an accessToken JSON field (TokenResponse currently holds refresh/expiry metadata). Default USER should receive MANAGE_CART through migration; custom roles require an explicit grant. This flow uses the actual current security chain.

## Manual acceptance walkthrough

Set `$cartVariantA` and `$cartVariantB` to real same-product variant UUID strings and use a fresh empty fixture user. The examples intentionally reuse the real server response item IDs.

```powershell
$cartAddBody = @{ variantId = $cartVariantA; quantity = 2 } | ConvertTo-Json
$cartView = Invoke-RestMethod -Method Post -Uri "$cartBase/api/me/cart/items" -Headers $cartHeaders -ContentType 'application/json' -Body $cartAddBody
$cartItemA = ($cartView.items | Where-Object variantId -eq $cartVariantA).id
$cartAddBody = @{ variantId = $cartVariantA; quantity = 3 } | ConvertTo-Json
$cartView = Invoke-RestMethod -Method Post -Uri "$cartBase/api/me/cart/items" -Headers $cartHeaders -ContentType 'application/json' -Body $cartAddBody
$cartView = Invoke-RestMethod -Method Put -Uri "$cartBase/api/me/cart/items/$cartItemA" -Headers $cartHeaders -ContentType 'application/json' -Body '{"quantity":4}'
$cartView = Invoke-RestMethod -Method Put -Uri "$cartBase/api/me/cart/items/$cartItemA/selection" -Headers $cartHeaders -ContentType 'application/json' -Body '{"selected":false}'
```

Expected: first add 201, repeat add 200; one A row quantities 2→5→4, selection false after final request. Use Invoke-WebRequest instead when inspecting response status/Location. Revisit GET after reauthentication and verify retained quantity/selection and Cache-Control private/no-store.

Then validate these scenarios against [api.md](contracts/api.md) and [data-model.md](data-model.md):

1. Replace A with 2. Add B with 3. Switch A→B with request quantity 4: source disappears, existing B quantity is 7, target identity and selection persist. Switching to absent C uses exactly request quantity and source identity/selection.
2. Set quantity 1000: succeeds. Request 1001: 400. Add 1 to existing 1000: 422, unchanged. Target 600 + requested merge 400 succeeds; +401 fails and preserves both rows. Aggregate quantity above 1000 across variants is valid.
3. Select/deselect individual/all rows. Verify exact row count versus quantity and 2×100 + 3×50 = 350 examples. Missing selection/null/string values fail safely.
4. Change product publication/price using a disposable fixture's committed catalog transaction (no new admin route is assumed). GET retains archived rows and snapshots, selected=true can remain, purchasable=false, no hidden image, zero eligible contribution. Republish/change price and verify current amounts without cart writes.
5. With a second authenticated user, try each source item operation against the first user's item. Compare with an unknown ID: identical safe 404, no detail disclosure or mutation. Missing bearer is 401; missing MANAGE_CART is 403. Grant/revoke the permission and verify the next request with the same valid token.
6. Delete owned row: 204/no body; repeat: 404. Last-row removal leaves an empty cart. Missing-cart GET and empty bulk selections must insert nothing.
7. Send malformed JSON, duplicate keys, unknown owner/price fields, explicit-null variant, omitted quantity, fractional/exponent/string quantities and numeric/string selection; all produce contract failures without changes. GET/DELETE body/query validation must preserve ProblemDetail. Verify security-first precedence: missing/invalid bearer yields 401, insufficient permission or unsupported methods yield 403 under deny-all, and unsupported media type on an otherwise permitted method/route yields 415 after security checks. No unconditional 405 expectation.

## Transaction, concurrency and fetch verification

These are automated integration scenarios, not timing-based manual HTTP races:

- Fresh committed fixtures; independent worker transactions; synchronized starts/controlled barriers and bounded futures. Override only concurrency test class pool size (e.g. 6) because current application-test.properties allows 2 connections. Do not wait at barriers while starving another worker's required connection.
- Parallel first adds: one cart, one row per variant; duplicate accepted adds sum exactly. Race near 1000 never commits >1000; rejected additions leave state unchanged.
- Race merge against add, two merges and selection versus quantity update. Every accepted outcome has a valid serial explanation; no lost increment, duplicate row or quantity overwrite. Distinct users should progress without a shared cart lock.
- Force failure after a target update/source delete and before commit (including signer failure) and verify both rows and newly created cart roll back from a separate transaction. No test-level transaction hides commit behavior.
- Direct PostgreSQL tests prove quantity, uniqueness and RESTRICT on referenced variants/products. Do not classify all database faults as expected 422/409.
- Test >100 cart rows across >100 products to exercise complete cart and globally ordered chunk locks. Query work grows by batches, not hidden converter/item lookups. Verify empty/hidden/missing-image cases, signing preparation before cart locks, final publication recheck, signer failure and no writes on GET. Image/storage seams are stubbed for arithmetic tests; no real S3 needed there.

## Completion evidence

Record actual Surefire/Failsafe class/count reports, full regression result, migration/schema result, synchronized-race assertions and HTTP statuses/amounts. Preserve no credentials/tokens. Document unavailable checks rather than claiming success. Use existing per-test cleanup on isolated test databases. Observed implementation evidence follows.

### Cart implementation execution — 2026-11-11/12

Final full Maven `verify`: BUILD SUCCESS at 2026-11-12 00:12:15 Asia/Saigon (4 min 53 sec). All 679 discovered tests passed with zero failures/errors/skips/flakes. Surefire ran 342 tests across 80 classes; Failsafe ran 337 tests across 79 classes. Actual executed class names were matched to XML reports, avoiding stale reports from earlier targeted invocations. failsafe-summary.xml confirms completed=337 and zero errors/failures/skips/flakes. JAR packaging succeeded, all 15 migrations applied/validated, and Hibernate schema validation passed. The separate full `test` run also passed before final verification.

Feature discovery: CartCalculatorTest (2), CartControllerTest (33), CartConverterTest (1), CartServiceImplTest (3), CartTransactionServiceImplTest (3), CartValidatorTest (8), CatalogCartReadServiceImplTest (4) and ApiErrorFactoryTest (1); CartRepositoryIT (1), CartItemRepositoryIT (8), CartServiceIT (13), CartControllerIT (6), CatalogCartReadServiceIT (3) and CartFlowIT (2). These 88 focused cases are included in the full-suite totals, not additional runs to add to 679.

Final log: demo/target/cart-verify-complete.log. XML evidence: demo/target/surefire-reports/ and demo/target/failsafe-reports/. Packaged artifact: demo/target/demo-0.0.1-SNAPSHOT.jar. git diff --check passed. All 21 local Markdown document links resolve. All 46 implementation task markers are complete; the requirements-quality checklist remains unchanged and read-only.

The subsequent speckit-implement invocation authorized the complete approved cart feature. Pre-cart baseline: Maven `test` passed 287 tests with no failures/errors/skips. The earlier 185-unit/40-IT storage results below are a separate targeted historical run, not that full baseline.

Implemented V15, all six routes, strict local JSON binding, MANAGE_CART inheritance/current permission checks, exact VND totals, public snapshots, complete ordered batch reads, parent-coordinated writes and resource-free prepared image URLs. CartReadSeed, PreparedCart and AddCartResult remain Lombok @Value classes in cart/dto/response with defensive copies. No inventory, checkout, fees, external ownership input, dependencies or build plugins were added.

Observed development failures were corrected: missing cart tables before V15; unsupported update/selection routes before implementation; Java UUID ordering inconsistent with PostgreSQL across batches; and a missing parser bean in unrelated MVC test slices. Full verification also exposed old exact migration/permission expectations. Those assertions now include V15/MANAGE_CART and retain exact authority/count checks, plus explicit USER-only upgrade grant assertions.

The HTTP walkthrough runs through CartFlowIT on a real embedded server with a random port and disposable PostgreSQL. It verifies 201 + Location, repeated-add 200, malformed quantity 400, absent bearer 401, current permission denial 403, missing removal 404, final quantity limit 422 and bodyless removal 204. Exact network totals are 4 units / 4,000 VND before deselection and zero afterwards. The internal provisioned-account flow verifies login, edits/variant switch, selection, logout/revoked old token, later login/revisit and removal. Controlled CartControllerIT cases verify HTTP 409 under a held database lock and 503 on signer failure without partial cart creation. MVC tests additionally verify strict duplicate/unknown/null/coerced tokens, security-first errors and authorized 415.

The existing Compose services were inspected read-only and remain healthy on their earlier image. They were not rebuilt, migrated or reset. The isolated walkthrough avoids changing that local dataset. No tokens or secrets are recorded here.

CartServiceIT verifies committed first creation/increments, quantity and merge bounds, unavailable-source recovery, mixed eligibility/selection, signing rollback after writes, independent lock holders, pooled timeout reset, overlapping merges/adds/deletes/selections, complete 105-row ordering and no GET writes. The 105-row GET uses at most 15 prepared statements; the catalog unit test verifies two 100-sized batches, globally PostgreSQL-ordered publication lock arguments, batched queries and nullable URLs without a prepared signer.

Validation uses the existing Java 25.0.4.1, PostgreSQL 17 and LocalStack setup. Test JVM arguments load the already installed Mockito 5.23.0 javaagent and set jdk.net.unixdomain.tmpdir to the workspace demo/target/uds directory. These are command-line environment workarounds, with no build configuration changes. Static analysis and coverage thresholds are not configured and are not claimed. Checklist requirements.md was read-only throughout implementation and remains 16/16 checked; task completion is tracked separately. No extensions.yml exists, so no implementation hooks are registered. No commits, pushes or deployment were performed.

## Follow-up validation obligations

Shared ImageUrlResolver returns resource-free PreparedImageUrls; no cart-context close is needed. CartServiceIT now holds independent cart/user locks while a competing mutation reaches its configured 200 ms transaction-local timeout. It verifies safe 409 mapping, unchanged state, subsequent successful writes and restored lock_timeout on all six borrowed pool connections. CartControllerIT independently verifies HTTP 409 without SQL disclosure. There is no automatic retry. Existing UserService retains timeout-before-user-lock behavior. Signing failure tests verify rollback of first-cart creation, source deletion/target merging and unchanged selection; preparation is asserted outside the transaction and signing inside it.

## Earlier shared storage verification — 2026-11-11 (historical)

Scope: shared image distribution/cleanup implementation plus cart design updates only. No cart runtime code or new migration exists. Final Maven invocation completed BUILD SUCCESS at 18:37 Asia/Saigon. This is targeted regression coverage, not a claim that the complete repository verify suite or future cart tests ran.

- Surefire: 185 tests across 32 report files, zero failures/errors/skips. Selected classes matched Product*Test, Media*Test, Image*Test, User*Test, Wishlist*Test, PresignedImageUrlResolverTest, ObjectStorageServiceImplTest, S3StorageConfigurationTest, StoredObjectContentTest and SharedProductImageStorageTest.
- Failsafe: 40 tests across ProductDetailApiIT (4), ProductListingApiIT (5), ImageCompletionConsistencyIT (8), ImageUploadFlowIT (3), UserImageApiIT (5) and WishlistServiceIT (15); zero failures/errors/skips. The integration tests used real disposable PostgreSQL 17 and LocalStack. Existing 14 Flyway migrations validated; no migration was added.
- Verified newly affected behavior: application presigner survives compatibility-handle close and serves multiple keys, credentials are captured once before local signing, shared five-minute URL representation, no HEAD on routine completed-image reads, retained attachment object/ownership checks, nonthrowing temporary cleanup after successful work and preservation of original business errors, actual presigned PUT/GET upload flow, catalog publication/listing and wishlist rollback behavior.
- Production/test sources compiled with Java 25.0.4.1. git diff --check passed. Actual Surefire/Failsafe XML files and failsafe-summary.xml were inspected rather than inferring discovery from the process exit.

Effective command: demo/mvnw.cmd -f demo/pom.xml with the above -Dtest/-Dit.test lists and goals `test failsafe:integration-test failsafe:verify`. No dependencies/plugins/build settings changed. On this Windows environment, a command-line -DargLine loaded the existing Mockito 5.23.0 JAR via -javaagent and set -Djdk.net.unixdomain.tmpdir to the absolute workspace demo/target/uds directory. Docker-backed tests required access outside the sandbox.

Initial attempts exposed environment failures: dynamic Mockito attachment could not open its Windows pipe, and three flow cases could not initialize Java HttpClient due to a Unix-domain loopback socket error. Startup-agent and workspace-local socket-directory options resolved those failures; the final unmodified assertions all passed. These options apply only to test JVMs, not production configuration.

Known semantic limit: issuing an image URL no longer HEAD-checks object existence on routine reads. External deletion of completed objects is discovered by the storage GET; attachment/publication checks are retained. CDN distribution is a future resolver implementation, not enabled now. Cart lock timeout order, 409 rollback, pooled-connection reset and contention tests remain documented future work by explicit user scope selection.

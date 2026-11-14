# Implementation Plan: Persistent Shopping Cart

**Branch**: `main` | **Date**: 2026-11-11 | **Spec**: [spec.md](spec.md)

**Input**: `specs/007-shopping-cart/spec.md`; Q1 inventory deferred, Q2 per-row quantity 1–1,000, Q3 D1–D8 approved.

## Summary

Add a private persistent cart to the existing domain-oriented backend. Cart-owned transactions serialize writes using the cart row; missing-cart additions use the existing user service lock and recheck before insertion. New cart/catalog DTO boundaries provide batched current eligibility/prices and safe images. Retained public metadata snapshots keep unavailable rows renderable. Exact whole-VND calculations produce eligible-selected counts and totals. Six HTTP operations reuse bearer/session security and the approved MANAGE_CART permission rollout.

Implementation authorized by the subsequent `$speckit-implement` invocation. The cart source, six routes, V15 migration and runtime tests now implement this design. The earlier storage-only scope is historical and superseded for cart execution. No dependencies/plugins, commits, pushes or deployments were added. Task completion and observed verification are recorded in tasks.md and quickstart.md.

## Technical Context

**Language/Version**: Java 25; Spring Boot parent 4.1.2 verified in `demo/pom.xml`.
**Primary Dependencies**: Existing Spring MVC/Security/Data JPA/Validation, Lombok, Jackson 3 (`tools.jackson` usage), springdoc, Flyway, AWS SDK S3. No new dependency/build plugin.
**Storage**: PostgreSQL; local Compose uses PostgreSQL 17. New carts/cart_items tables via next unused additive migration, currently V15. Existing S3/LocalStack integration signs image URLs, not durable cart data.
**Testing**: Existing JUnit 5, Mockito, AssertJ, MockMvc, PostgreSQL Testcontainers; Surefire unit/slice phase and existing Failsafe integration-test/verify goals. Actual cart discovery must be proved after implementation.
**Target Platform**: Existing Java backend/runtime and local Docker Compose; no new deployment target.
**Project Type**: Single-module backend web service (`demo/`).
**Performance Goals**: Complete-cart responses with bounded batch data retrieval; no per-row hidden queries. No approved latency, throughput or row-cap promise. Batch size 100 is an internal query bound, not pagination or a cart capacity limit.
**Constraints**: One cart/user and row/variant; 1–1,000 quantity per row; exact whole VND; current auth/session/permissions; nonmutating GET; atomic failures; retained unavailable rows; no inventory, checkout or multi-vendor functionality.
**Scale/Scope**: Six endpoints; unlimited-by-contract row count; serialized writes within one cart and independent writes across carts; checked Long aggregate quantity, BigInteger money. No new framework, cache or worker.

## Constitution Check

Gate evaluated before Phase 0 and again after Phase 1. Both PASS for this design; this does not certify existing code or future implementation.

| Principles | Pre-research check | Post-design evidence |
| --- | --- | --- |
| I–III domain layering | PASS: cart owns its persistence; catalog/user integration through interfaces | CartService/CartTransactionService and CatalogCartReadService interfaces/implementations; prepared DTOs, dedicated validator/calculator/converter; no cross-domain repository calls |
| IV–VI HTTP/errors/security | PASS: approved statuses, null/omitted rules and MANAGE_CART | contracts/api.md defines strict scoped binding, safe ProblemDetail, current identity and owner checks; no token changes |
| VII–VIII schema/entities | PASS: additive Flyway, existing ID types, lazy entity relationships | data-model.md defines Long identity cart keys by local precedent, UUID variant references, quantity/uniqueness/FK constraints and D7 RESTRICT |
| IX–X transactions/concurrency | PASS: REQUIRED/READ COMMITTED; scoped pessimistic coordination | User-before-cart only for creation; no broad retry, ordered catalog image locks, rollback before error mapping; response prepared before commit |
| XI–XII storage/time | PASS: no uploads or persisted temporary URLs | Shared resource-free prepared image URLs, local signing, publication recheck; Instant/TIMESTAMPTZ addedAt |
| XIII testing | PASS: D8 authorizes concurrency verification | Responsibility-based tests, independent transactions, actual discovery and rollback checks in quickstart.md |
| XIV–XVII tooling/scope | PASS: no dependency/plugin/CI changes, no auto-commit | Existing tools only; authorized cart implementation; no invented load or static-analysis pass claims |

**Recorded SHOULD departure**: Image-bearing cart GET uses a write-capable, business-nonmutating REQUIRED transaction because existing publication-safe signing uses PostgreSQL FOR SHARE. This follows catalog/wishlist precedent and constitution IX's readOnly preference permits a documented rationale. No business record is inserted/updated/deleted on GET. Do not mark the transaction read-only and then attempt share locks.

## Project Structure

### Documentation (this feature)

```text
specs/007-shopping-cart/
  spec.md
  plan.md
  research.md
  data-model.md
  quickstart.md
  checklists/requirements.md
  contracts/
    engineering.md
    api.md
    internal-services.md
```

`tasks.md` is deliberately not generated in this phase.

### Source Code (repository root)

Planned additions/targeted edits, not already implemented:

```text
demo/src/main/java/com/example/demo/
  cart/
    controller/CartController.java, CartRequestReader.java, CartRequestBodyAdvice.java, CartCacheFilter.java
    service/CartService.java, CartTransactionService.java
    service/impl/CartServiceImpl.java, CartTransactionServiceImpl.java
    repository/CartRepository.java, CartItemRepository.java
    entity/Cart.java, CartItem.java
    dto/request/AddCartItemRequest.java, UpdateCartItemRequest.java, CartSelectionRequest.java
    dto/response/CartResponse.java, CartItemResponse.java
    dto/response/CartReadSeed.java, PreparedCart.java, AddCartResult.java
    validator/CartValidator.java
    calculator/CartCalculator.java
    converter/CartConverter.java
    exception/ (specific ApplicationException subtypes)
  catalog/
    service/CatalogCartReadService.java, CatalogCartReadServiceImpl.java
    dto/response/CartVariantState.java
    repository/ProductVariantRepository.java (batch projection)
    repository/CartVariantView.java (scalar projection interface)
    repository/ProductImageRepository.java (reuse batch metadata)
    repository/ProductRepository.java (reuse ordered publication locks)
  auth/config/AuthSecurityConfiguration.java (cart routes/permission)
  common/exception/ApiErrorFactory.java (narrow cart/concurrency mappings)
demo/src/main/resources/db/migration/V15__create_carts.sql (confirmed next unused migration)
demo/src/test/java/com/example/demo/
  cart/{controller,service,repository,validator,calculator,converter}/
  catalog/{service,repository}/ (new boundary behavior only)
  fixture/cart/ (reusable persisted fixtures if needed)
  testdata/cart/ (fresh unit factories if needed)
  e2e/CartFlowIT.java
```

**Structure Decision**: Extend the current modular monolith. Services own orchestration; one explicit transaction service avoids self-invocation and keeps credential preparation outside cart locks. Existing catalog package uses service implementations directly in `service/`; retain that convention. No empty fixture/config/test classes solely to fill the tree.

**Prepared DTO convention (C2 resolved)**: `CartReadSeed`, `PreparedCart` and `AddCartResult` are Lombok-based immutable DTO classes in `com.example.demo.cart.dto.response`, at `demo/src/main/java/com/example/demo/cart/dto/response/`. Use Lombok `@Value` classes, not Java records, and defensively copy collection/map data where applicable. These internal prepared/result DTOs keep their existing responsibilities; their package does not make them additional HTTP response bodies. Introduce CartReadSeed in T008 and PreparedCart/AddCartResult in T016, preserving the incremental service-contract dependency order.

## Phase 0: Research Results

Completed [research.md](research.md), with delegated read-only research of concurrency/schema and catalog/image integration as requested by the planning skill. All design unknowns resolved from source and approved requirements; no unresolved clarification is left. Decisions are engineering choices within approved scope, not new business features.

## Phase 1: Design

- [data-model.md](data-model.md): cart/item fields, constraints, snapshot privacy, state transitions and migration rollout.
- [contracts/api.md](contracts/api.md): external routes, input semantics, response fields/statuses/errors and numerical examples.
- [contracts/internal-services.md](contracts/internal-services.md): service boundaries, query batching, signer lifecycle, transaction flow and concurrency ordering.
- [quickstart.md](quickstart.md): prerequisites, commands and expected validation after implementation.

Service methods and DTOs were introduced incrementally by story (I1 B). Security-first errors follow approved C1: 401 for missing/invalid bearer; 403 for denied permission/unsupported methods under deny-all; authorized supported methods can reach MVC 415. U1 uses the resource-free shared signing capability with no cart cleanup lifecycle. U2 sets transaction-local timeout before the first cart lock and retains the existing timeout-before-user-lock protocol. Runtime contention and rollback tests now exercise these requirements.

Implement request strictness locally: preserve omitted versus explicit-null update variant, reject coercion/unknown/duplicate fields without changing other controllers. Snapshot/amount preparation completes inside the transaction; do not commit a mutation and then invoke fallible mandatory response-building work.

## Verification Strategy

Unit tests cover quantity/eligibility/selection, arithmetic and safe mapping. MVC tests prove strict fields, bearer permission integration, statuses and ownership-safe errors. Repository IT proves schema constraints, owned lookups/order and D7 deletion restriction. Service IT proves real rollback and synchronized races including first-cart creation, increments near 1,000, competing merges and selection-versus-quantity changes. API integration and one actual authenticated flow prove cross-domain registration/login/cart behavior with isolated fixtures. Image calculation tests use the existing signing seam, not external S3.

Run the existing regression suite and inspect actual reports, rather than infer discovery from a successful Maven exit. Cart and shared-storage test evidence is recorded separately in quickstart.md.

**Implementation audit, 2026-11-12**: All six routes, V15, scalar ownership/reference mappings, Lombok response DTO conventions, pure converter/calculator boundaries and scoped binding are implemented. REQUIRED/READ_COMMITTED is explicit on the transaction service; positive cart.lock-timeout-ms is validated at startup. The final full verify passed 342 Surefire + 337 Failsafe tests with no failures/errors/skips, including real HTTP, rollback, contention and 105-row batch checks. No dependency/plugin/CI change or deployment was needed. See quickstart.md for exact evidence and environment options.

## Complexity Tracking

No MUST-rule violations or unapproved capabilities. The narrow readOnly SHOULD departure is documented above. No new infrastructure or dependencies. Current tooling observations: Bash setup failed at MSYS NtCreateDirectoryObject access; bundled PowerShell setup succeeded. Its BRANCH output was `007-shopping-cart` derived from feature.json, while `git branch --show-current` confirms `main`; no branch was created/switched. No extensions.yml exists, so no pre/post planning hooks apply.

## Earlier shared image refactor scope (historical)

The subsequent implement invocation supersedes the storage-only restriction below. Cart V15 and runtime code are now delivered; that earlier step itself required no migration.

Products and avatars use storage/service/ImageUrlResolver and impl/PresignedImageUrlResolver. ObjectStorageServiceImpl reuses the application S3Presigner and captures credentials before publication locks; PreparedImageUrls owns no resources. SharedProductImageStorage is a compatibility adapter, not an S3 implementation. Existing API fields, private bucket policy, 300-second GET lifetime, upload/publication lifecycle, product ordering/primary/publication rules and avatar ownership/attachment verification remain unchanged. Routine completed-image reads no longer HEAD. Temporary content cleanup is nonthrowing and safely logged. No migration, variant/review image subsystem or cart runtime code was added.

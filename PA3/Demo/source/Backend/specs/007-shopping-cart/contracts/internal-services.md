# Internal Service Contracts: Shopping Cart

These interfaces are implemented under `com.example.demo`. Catalog has no dependency on cart. The subsequent implement invocation supersedes the earlier storage-only scope.

## CartService / CartServiceImpl

Prepared/result types `CartReadSeed`, `PreparedCart` and `AddCartResult` are Lombok-based immutable `@Value` DTO classes in `com.example.demo.cart.dto.response`, under `demo/src/main/java/com/example/demo/cart/dto/response/`. Use defensive collection/map copies where applicable, not Java records or root `cart.dto` DTOs. CartReadSeed remains the internal owned-row projection, PreparedCart the fully prepared calculation/mapping data, and AddCartResult the creation/status result. This package correction changes no service responsibility, business behavior or external API schema; CartReadSeed is introduced in T008 and PreparedCart/AddCartResult in T016.

Public application facade: `getCart(Long owner)`, `addItem(Long owner, AddCartItemRequest request)`, `updateItem(Long owner, Long itemId, UpdateCartItemRequest request)`, `removeItem(Long owner, Long itemId)`, `selectItem(Long owner, Long itemId, CartSelectionRequest request)`, `selectAll(Long owner, CartSelectionRequest request)`. Returns CartResponse, except add returns AddCartResult and delete returns void. The transaction service uses the same signatures with a final nullable PreparedImageUrls argument on every response-bearing operation. Controllers obtain owner only from CurrentUserIdProvider. Types were staged through T008/T016/T028/T037. No closeable cart image context exists.

Facade owns preparation, not an ambient transaction. Before any signer initialization, validate request shape and perform owner-scoped nonlocking preflight; unauthorized/unknown source IDs must not trigger target-detail exposure or image preparation. Preflight is never authoritative: every ownership/state/quantity check runs again inside the transaction. No managed writable entities from preflight are reused in the mutation persistence context.

For response-bearing operations, use preflight owned variant IDs plus an allowed target to check catalog image candidates, then call shared ImageUrlResolver.prepare() before the authoritative transaction if needed. Missing-cart GET/bulk selection returns zero state without signing; missing source operations fail 404; deletion needs no URL capability. No CatalogCartReadService.prepareImageContext or cart-owned closeable resource is introduced. A concurrent add after an empty GET can appear on the next view; no stronger snapshot promise exists.

Invoke separate Spring-proxied CartTransactionService with the resource-free PreparedImageUrls capability from ImageUrlResolver.prepare(). No per-request presigner is constructed, no cart-specific image context exists, and no close/cleanup occurs after commit or rollback. Application-managed S3Presigner closes only at shutdown. No mandatory fallible conversion/signing/calculation after commit; preparation/signing failures still propagate before commit and mutations roll back. Genuine temporary-content cleanup must attempt deletion on both success and failure, log a safe warning without keys/paths/URLs/exception messages, and preserve the original outcome. A transport failure after commit remains an ordinary HTTP limitation, not a rollback guarantee.

## CartTransactionService / CartTransactionServiceImpl

Provides corresponding transactional operations; all transaction boundaries use REQUIRED and default READ COMMITTED. GET is business-nonmutating but write-capable for publication share locking; deletion and mutations use read-write transactions. Service invokes own repositories, UserService, CatalogCartReadService, CartValidator, CartCalculator and CartConverter.

Write protocol:

1. Inside the active transaction, FIRST set transaction-local `cart.lock-timeout-ms` (positive, default 5000), equivalent to SET LOCAL lock_timeout='5s', through the cart repository. ONLY THEN issue the first potentially blocking cart PESSIMISTIC_WRITE query; fetch mutable rows fresh after the lock. Never request a user write lock after acquiring cart. The local setting ends at commit/rollback, never use a session-wide SET. The bound applies to individual lock acquisitions, not the HTTP request duration.
2. Missing-cart addition calls existing UserService.getUserEntityForUpdate(ownerId), whose transaction-local timeout is set BEFORE its user-lock query. After acquiring user, reapply the cart timeout BEFORE rechecking/acquiring any cart lock, then lock an existing winner or create one cart. Preserve User→Cart ordering; fresh reads follow coordination. Missing-cart selection is a no-op; missing sources are 404. A genuine lock timeout rolls back and maps to safe 409 without automatic retries; unrelated database errors retain their own mappings.
3. Fetch owner-scoped rows fresh after coordination; refresh/reload if persistence context could contain stale state. Foreign and unknown source IDs map to the identical exception before target business lookup.
4. Obtain current target variant state through catalog. Validator enforces publication, whole/non-negative price, same-product switch and requested/final quantity. Widen quantities before sums. Validate merge before changing either row. No source quantity is added to a target merge.
5. Apply only intended changes. All writers use this parent coordination protocol; selection writes do not replace quantity. Snapshot refresh is limited to eligible public data for affected rows; GET never refreshes snapshots.
6. Capture final owned row seeds and batch current catalog data; prepare safe images and final publication states. A target that became unavailable before final mutation validation causes rollback; pre-existing unrelated unavailable rows remain visible. Current eligible selection for selecting one/all is determined from the final prepared state. Use the same state for flags and totals.
7. Calculate exact totals once; converter performs pure mapping. Flush and complete transaction before returning. Signing, calculation, constraints or final validation failures roll back cart creation, source removal, target updates and selections.

No blanket catalog snapshot is promised across requests or statements. Eligibility is validated against authoritative catalog state observed in this transaction; later catalog changes can make the next view unavailable without corrupting cart state. Do not lock all catalog rows solely to imply stock reservation. Image publication recheck must never produce a hidden URL.

## Cart repositories

CartRepository: nonlocking owner lookup, owner-scoped pessimistic lock lookup, positive transaction-local lock timeout, create/flush. CartItemRepository: owned source lookup, complete cart projection ordered addedAt DESC/id ASC, variant match within cart, save/delete as needed. All writes are coordinated by CartTransactionService; child SQL need not lock every row again. DB uniqueness/FKs/checks are final integrity protection, not substitutes for domain checks.

Queries capture row collections in bounded statements without lazy converter fetches. Child references use lazy mappings or explicit projections; no cross-domain repositories in cart.

## CatalogCartReadService / CatalogCartReadServiceImpl

Catalog-owned contracts, returning its own prepared DTOs:

- `getVariantStates(Collection<UUID>)`: map of existing variants with parent identity, publication and price validity/current amount, and current public descriptions only for published parents. It accepts complete sets, internally deduplicates/chunks at 100; absent IDs remain absent. Called in transaction for authoritative decisions; no hidden per-item queries.
- Nonlocking metadata preflight identifies candidate images. Call the shared `ImageUrlResolver.prepare()` outside the cart transaction/locks only when candidates exist; it returns resource-free `PreparedImageUrls`, backed by captured credentials and the application-managed signer. No custom cart preparation/cleanup abstraction or per-request S3 client, no product lock during credential initialization, no persistent URL or public object key. A future resolver can return CDN URLs without domain/database changes.
- `getCartPresentation(Collection<UUID>, PreparedImageUrls)`: batch current variant states/primary image metadata, gather all image-bearing product IDs and acquire publication share locks in globally ascending UUID order across batches of 100. Locally resolve permitted URLs using the supplied capability. Reflect final publication flags in row states; hidden products get no URL/current hidden description. Zero candidates take no image lock.

Preflight can race with cart/metadata changes. If no prepared capability exists and a new image appears during the transaction, its image is null for this response; never resolve credentials under a cart lock. A prepared capability can resolve newly observed keys locally. This nullable fallback covers missing/new metadata only; actual preparation/signing failures are not swallowed and fail before mutation or roll back it. Existing public catalog APIs/wishlist behavior remain unchanged.

Use storage-owned ImageUrlResolver/PreparedImageUrls. Existing ProductImageStorage/PreparedReadSigner are only a compatibility adapter with no-op close and no owned resource. Do not call media repositories, full gallery endpoints, object HEAD/download or resolver helpers from cart converters. A published product with invalid price can still have a public image; it remains excluded from purchasable totals.

## Validation, arithmetic, conversion and errors

CartValidator owns positive/bounded quantities, ownership, same-product rules, eligibility and selection rules; basic shape uses Bean Validation plus scoped strict token validation. CartCalculator owns only exact line/aggregate arithmetic from prepared state. CartConverter maps those prepared results and snapshots without persistence access, signing, hidden loads or duplicate arithmetic.

Domain exception examples: CartItemNotFoundException (404), InvalidCartRequestException (400), CartQuantityLimitException (422), CartVariantSwitchException (422), CartItemUnavailableException (422), CartConflictException (409). Existing catalog safe not-found may be reused for target absence/hidden state. Use existing ApplicationException base and ApiErrorFactory/GlobalExceptionHandler.

Translate expected persistence conflicts only after the failed transactional call has rolled back. Cover 55P03 lock timeout and 40P01 deadlock as 409, cart owner FK disappearance as existing identity-unavailable 401, variant/product FK race as safe target 404 or conflict according to whether the requested target disappeared, and known cart pair uniqueness race as 409. Unexpected quantity/check violations that escaped domain validation remain 500 defects rather than becoming generic business success/errors. Do not wrap every framework exception or catch-and-continue in a failed transaction. Catalog signing failures preserve existing CatalogStorageUnavailableException status (503) with safe ProblemDetail.

## Strict binding boundary

Implement a cart-controller-scoped request-body reader/message conversion path using existing Jackson 3 facilities. Reject duplicate keys before JsonNode/object materialization can discard them, then validate object shape, exact integer/boolean/string token types, unknown properties and explicit-null semantics. Populate Lombok request DTOs, including `variantIdPresent`; activate Bean Validation in controller. No global ObjectMapper or auth/profile API change. Malformed path IDs and unsupported query/body combinations use existing safe binding handling. Verify support with real MVC binding tests, not DTO setter tests alone.

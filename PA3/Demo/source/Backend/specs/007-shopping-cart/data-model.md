# Data Model: Persistent Shopping Cart

Implemented model, 2026-11-11. V15__create_carts.sql and cart/entity/Cart.java plus CartItem.java implement these fields and constraints. Cross-domain and aggregate references use scalar IDs rather than entity associations; lifecycle cascade and catalog RESTRICT are enforced by PostgreSQL. Catalog target validation enforces the variant/product pairing.

## Cart → carts

| Field | Type | Rules |
| --- | --- | --- |
| id | Long / BIGINT identity | Primary key; new domain follows wishlist/address precedent |
| userId | Long / BIGINT | NOT NULL, UNIQUE, FK users(id), existing user cleanup precedent ON DELETE CASCADE |

No mandatory createdAt/updatedAt/version field: addedAt is the relevant ordering time on items. No empty cart row is created by viewing or no-op/failed writes. Removing the last item retains its cart.

Constraint names: `uk_carts_user_id`, `fk_carts_user_id`. Unique index supplies user lookup. JPA lazy user reference, or scalar ownership representation with explicit FK migration; never expose entity graphs over HTTP.

## CartItem → cart_items

| Field | Type | Rules |
| --- | --- | --- |
| id | Long / BIGINT identity | Primary key, opaque external item identifier |
| cartId | Long / BIGINT | NOT NULL FK carts(id), ON DELETE CASCADE: true aggregate lifecycle |
| productVariantId | UUID | NOT NULL FK product_variants(id), ON DELETE RESTRICT |
| productId | UUID | NOT NULL FK products(id), ON DELETE RESTRICT; original product for safe snapshot rendering/switch checks |
| quantity | Integer / INTEGER | NOT NULL, CHECK BETWEEN 1 AND 1000 |
| selected | Boolean / BOOLEAN | NOT NULL; application default true only for new rows |
| addedAt | Instant / TIMESTAMPTZ | NOT NULL; injected Clock sampled once per new row; never changed on replacement/add/merge target |
| publicProductName | String / TEXT | NOT NULL, nonblank; previously public snapshot |
| publicSku | String / TEXT | NOT NULL, nonblank; previously public snapshot |
| publicOptions | Map<String,String> / JSONB | NOT NULL object; copy eligible variant options; empty object allowed for an unparameterized variant |

Uniqueness: `uk_cart_items_cart_id_product_variant_id`. Other constraints: `fk_cart_items_cart_id`, `fk_cart_items_product_variant_id`, `fk_cart_items_product_id`, `ck_cart_items_quantity`, `ck_cart_items_public_product_name_nonblank`, `ck_cart_items_public_sku_nonblank`, `ck_cart_items_public_options_object`.

Indexes: `idx_cart_items_cart_id_added_at_id` on `(cart_id, added_at DESC, id ASC)`, `idx_cart_items_product_variant_id` and `idx_cart_items_product_id` for reference checks. No index duplicates the variant-pair unique index unnecessarily.

Store productId because hidden response rendering and same-product source comparison must not rely on exposing hidden descriptions. Catalog returns the authoritative variant→product relation. Cart validator ensures productId equals that relation on creation/switch; no other writer may alter cart links outside the cart service protocol. Schema FKs protect reference existence; do not claim two independent FKs prove variant/product pair equality. Repository/service integration verifies pair consistency; snapshots are not an authority for target eligibility.

The implemented entities use scalar IDs, safe Lombok getters/setters and no generated entity equality/toString. PostgreSQL handles cart-owned lifecycle cascades; repository deletion removes individual items. Children load explicitly after the parent lock. Snapshot JSON uses the existing Hibernate JSON mapping; no new JSON library.

## Referenced existing entities

User identity stays Long. Product and ProductVariant identities stay UUID. Product owns publication status; variant owns SKU/options/sellingPrice. No stock/reservation or independent variant archive field is added. Catalog product/variant deletion is restricted by cart FKs; existing unrelated constraints/triggers remain untouched. Archiving products leaves cart links intact. Removing cart rows eventually releases their deletion restrictions.

## Prepared response data (not durable entities)

- `CartVariantState`: variantId, productId, published, valid current whole-VND amount or price-invalid flag, and current public name/SKU/options only if published. Do not leak current hidden descriptions.
- `CartReadSeed` (`cart/dto/response/CartReadSeed.java`): Lombok-based immutable `@Value` DTO class; owned row projection, including snapshots, after lock for writes or a single captured row read for GET.
- `PreparedCart` (`cart/dto/response/PreparedCart.java`): Lombok-based immutable `@Value` DTO class; defensive items/states/subtotals collections plus selectedItemCount, selectedTotalQuantity and exact BigInteger selectedSubtotal. Signed URLs are embedded in final CartVariantState values, without a separate image map. Ineligible IDs have no subtotal entry; the converter renders null. No lazy entity references.
- `AddCartResult` (`cart/dto/response/AddCartResult.java`): Lombok-based immutable `@Value` DTO class; created boolean, resulting itemId and complete response; determines 201/200 and Location independently of quantity.
- `CartResponse` / `CartItemResponse`: explicit external fields in contracts/api.md; quantities checked, amounts use existing SellingPrice shape.

The three prepared/result DTO paths above are relative to `demo/src/main/java/com/example/demo/`; their package is `com.example.demo.cart.dto.response`. Use classes rather than Java records, with defensive collection/map copies where applicable. Their responsibilities, calculation ownership, transaction timing and HTTP exposure remain unchanged; package placement does not add public endpoints or response fields.

No durable unitPrice, subtotal, total, purchasable or URL columns. They reflect current prepared catalog state. Invalid price maps to null; zero is valid. PRICE_UNAVAILABLE applies only when product is published but price is invalid; PRODUCT_UNAVAILABLE takes precedence for hidden/missing state. Physically missing referenced state indicates an integrity/race conflict, not permission to delete rows silently; retained row remains nonpurchasable on reads and target mutations fail safely.

## State transitions

| Operation | Required state | Transition |
| --- | --- | --- |
| View missing cart | Eligible authenticated user | Empty DTO only, no stored transition |
| Add absent variant | Published, valid price, quantity 1–1000 | Create cart if missing; create selected row with snapshot/time |
| Add existing variant | Same eligibility, resulting quantity ≤1000 | Increment quantity, preserve selected/id/time |
| Replace quantity | Owned row, eligible retained variant | Replace quantity; preserve selected/id/time |
| Switch to absent same-product variant | Owned source and eligible target | Retain source id/selection/time; replace variant, quantity, public snapshot |
| Switch to existing same-product variant | Owned source/target, eligible target, target+request ≤1000 | Target increments by request, retains selection/id/time; delete source atomically |
| Select one | Owned row and eligible target | selected=true only |
| Deselect one | Owned row; eligibility not required | selected=false only |
| Select all | Existing cart or absent no-op | Set eligible rows true; unavailable flags unchanged |
| Deselect all | Existing cart or absent no-op | Set every selected flag false |
| Remove | Owned row; eligibility not required | Delete row; retain empty cart if last |
| Product archive/draft | Existing row | No cart writes; next response unavailable, snapshot visible, selection preserved, totals exclude |
| Product republish/price change | Existing row | No cart writes; next response uses current public eligibility/prices |
| Any rejected mutation | Any | Roll back all row/cart/snapshot/selection changes |

## Calculations

For each purchasable row: subtotal = exact BigInteger current unit amount × quantity. For each selected and purchasable row, add subtotal to selectedSubtotal/finalTotal, increment selectedItemCount and add quantity using checked Long arithmetic. Ineligible subtotal=null and never contributes. Selected quantity can exceed 1000 across rows. All amounts remain VND; there is no rounding, discount, shipping or future-price guarantee.

## Migration and rollout

V15__create_carts.sql was confirmed unused and added without editing earlier migrations. It creates the tables/constraints/indexes and MANAGE_CART permission plus USER role grant, failing if USER is absent. Current-state authorization makes role grants affect existing tokens on the next request; new USER assignments inherit the same permission. Custom roles get no implicit grant.

Verify applied schema against mappings with ddl-auto=validate, plus direct PostgreSQL uniqueness/boundary/reference checks. Do not execute destructive rollback or introduce a production data deletion step. No cart data backfill is needed for this new feature.

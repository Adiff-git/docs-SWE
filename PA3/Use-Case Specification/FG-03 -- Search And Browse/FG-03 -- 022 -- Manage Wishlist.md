# **Electronics Store E-commerce Website**

# **FG-03 \-- 022 \-- Manage Wishlist**

# 

# **Version 1.1**

# **Revision History**

| Date | Version | Description | Author |
| ----- | ----- | ----- | ----- |
| 14/Nov/26 | 1.1 | PA3 specification aligned with team RUP template, Vision v1.4 and Hza static exports | Nguyễn Hoàng Gia |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

# **Table of Contents**

1\. Use-Case Name	4

1.1 Brief Description	4

2\. Flow of Events	4

2.1 Basic Flow	4

2.2 Alternative Flows	4

2.2.1 Input validation and business-rule alternatives	4

2.2.2 Additional outcomes and service failures	5

3\. Special Requirements	5

3.1 Use-case quality and integrity constraints	5

4\. Preconditions	5

4.1 Conditions that must hold	5

5\. Postconditions	5

5.1 Success and failure states	5

6\. Extension Points	5

6.1 Related use cases and scope	5

Prototype Screens	7

# **FG-03 \-- 022 \-- Manage Wishlist**

1. # **Use-Case Name**

   UC-022 — Manage Wishlist

   1. ## **Brief Description**

   An authenticated Customer saves products to a personal wishlist, views the saved products, and removes products that are no longer of interest. The System keeps the list associated with the Customer's account so it can be revisited in a later session.

   Functional group: FG-03 — Search and Browse

   Actor(s): Customer (C)

   Priority: Optional

2. # **Flow of Events**

   1. ## **Basic Flow**

   1\. The Customer opens a product card or product detail page.

   2\. The Customer selects Add to Wishlist.

   3\. The System verifies the Customer's authenticated session and validates that the product is eligible to be saved.

   4\. The System adds the product identifier to the Customer's wishlist and confirms the updated state.

   5\. The Customer opens the Wishlist page or section.

   6\. The System retrieves the wishlist belonging only to the authenticated Customer and displays the saved products with current product-card information.

   7\. The Customer selects a saved product to continue with UC-015 View Product Details, or selects Remove to delete it from the wishlist.

   8\. When the Customer removes a product, the System deletes the corresponding wishlist entry and confirms the updated list.

   2. ## **Alternative Flows**

      1. ### *Input validation and business-rule alternatives*

   A1. The product is already in the Customer's wishlist: the System keeps a single entry and does not create a duplicate.

   A2. The Customer's wishlist is empty: the System displays an empty state and provides a route back to the product catalog.

   A3. A saved product is unpublished or deleted: the System does not expose its private/unpublished details and either removes the stale entry or marks it unavailable according to the approved wishlist policy.

   A4. A saved product is out of stock or its price changes: the System displays the latest verified availability and price; the wishlist does not reserve stock or lock a price.

      2. ### *Additional outcomes and service failures*

   A5. The Customer is not authenticated or the session expires: the System requests sign-in before accessing or changing the account-specific wishlist.

   A6. The wishlist/catalog service fails or times out: the System displays a recoverable error and does not claim that an add/remove operation succeeded without Backend confirmation.

3. # **Special Requirements**

   1. ## **Use-case quality and integrity constraints**

   • Each wishlist must be private to its owning Customer. Every read, add, and remove operation must be authorized by the Backend.

   • The wishlist must not contain duplicate entries for the same product identifier.

   • Saved entries must not reserve inventory, freeze a price, or imply that a product is available for purchase.

   • Current product name, image, price, discount, and availability must be refreshed from authoritative catalog data when the list is displayed.

   • The wishlist is account-associated according to the intended Vision behavior; the exact retention policy and handling of deleted accounts require Backend confirmation.

4. # **Preconditions**

   1. ## **Conditions that must hold**

   • The Customer is authenticated.

   • The wishlist and catalog services are available, or the System can return a defined empty/error state.

   • The product is identifiable in the catalog when the Customer adds it.

5. # **Postconditions**

   1. ## **Success and failure states**

   Success:

   • The Customer's wishlist contains the added products and excludes successfully removed products.

   Failure:

   • No other Customer's wishlist is exposed or modified.

   • Wishlist operations do not change product stock, cart contents, or order records.

6. # **Extension Points**

   1. ## **Related use cases and scope**

   No formal UML extension point is defined in the current shared Use-Case Model. Related use cases:

   • UC-015 — View Product Details

   • UC-018 — View Recently Viewed Products

   • UC-023 — Manage Shopping Cart

   Scope: Vision v1.4 states that Customers can save products to a personal wishlist, revisit them, and remove saved products. No dedicated wishlist page, add-to-wishlist control, or wishlist empty state is present in the supplied Hza.zip exports. The account requirement, retention policy, and exact entry point therefore need Frontend/Backend confirmation. The flow above is a requirements-level specification, not evidence of a completed wishlist implementation.

   Performed by: Nguyễn Hoàng Gia \| Reviewed by: Pending \| Status: Draft for review

   ## **Prototype Screens**

Source: Hza(1).zip — static PDF exports. Images show sample data, not implementation or test evidence. Canonical PA3 UC identifiers take precedence over the export-local screen labels.

Prototype gap: No dedicated screen for this use case is included in Hza.zip. Basic-flow and alternative-flow screenshots remain required for the PA3 prototype requirement. No substitute screen is represented as an existing design.
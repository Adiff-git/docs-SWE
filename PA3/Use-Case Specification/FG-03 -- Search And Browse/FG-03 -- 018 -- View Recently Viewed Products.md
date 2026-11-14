# **Electronics Store E-commerce Website**

# **FG-03 \-- 018 \-- View Recently Viewed Products**

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

2.2.2 Additional outcomes and service failures	4

3\. Special Requirements	5

3.1 Use-case quality and integrity constraints	5

4\. Preconditions	5

4.1 Conditions that must hold	5

5\. Postconditions	5

5.1 Success and failure states	5

6\. Extension Points	5

6.1 Related use cases and scope	5

Prototype Screens	6

# **FG-03 \-- 018 \-- View Recently Viewed Products**

1. # **Use-Case Name**

   UC-018 — View Recently Viewed Products

   1. ## **Brief Description**

   An authenticated Customer revisits products that they previously opened. The System retrieves the Customer's own recent product-view history and displays still-published products in reverse chronological order so the Customer can return to a product without repeating the original search.

   Functional group: FG-03 — Search and Browse

   Actor(s): Customer (C)

   Priority: Optional

2. # **Flow of Events**

   1. ## **Basic Flow**

   1\. The Customer opens the storefront or account area and selects the Recently Viewed Products entry point. The exact entry point is not shown in Hza.zip and must be confirmed by Frontend.

   2\. The System verifies the Customer's authenticated session and requests recent product-view records belonging only to that Customer.

   3\. The System retrieves the associated product records and orders them from most recently viewed to least recently viewed within the configured history-retention window.

   4\. The System excludes products that are no longer published for public display and obtains current product-card fields for the remaining products.

   5\. The System displays the recent products as a list or product-card section with available names, images, current prices, and availability.

   6\. The Customer selects a product to continue with UC-015 View Product Details.

   2. ## **Alternative Flows**

      1. ### *Input validation and business-rule alternatives*

   A1. The Customer has no recorded product views within the configured retention window: the System displays an explanatory empty state and provides a route to browse the catalog.

   A2. A previously viewed product is unpublished or deleted: the System excludes it from the public list or clearly marks it unavailable, according to the approved history-display policy. It must not expose unpublished product details.

   A3. A product has incomplete current catalog fields: the System displays only verified fields and does not reuse an old price or stock value as though it were current.

      2. ### *Additional outcomes and service failures*

   A4. The Customer's session expires: the System prompts the Customer to sign in again and does not reveal the history before authentication is restored.

   A5. The history or catalog service fails or times out: the System displays a recoverable error and retry action; it does not fabricate a recent-view record or product card.

3. # **Special Requirements**

   1. ## **Use-case quality and integrity constraints**

   • The history must be scoped to the authenticated Customer. One Customer must never see another Customer's viewed-product history.

   • The System must use only permitted product-view signals and follow the team's approved consent, retention, and deletion rules.

   • The retention duration, maximum number of records, and whether history is synchronized across devices are not specified in Vision v1.4 and require team/Backend confirmation.

   • Product identity may come from history records, but price, discount, and availability must be refreshed from current catalog data before display.

   • Recently viewed history is a convenience feature; it must not reserve inventory or guarantee that a product remains available.

4. # **Preconditions**

   1. ## **Conditions that must hold**

   • The Customer is authenticated.

   • The recent-view history service and public catalog are available, or the System can return a defined empty/error state.

   • The Customer has permission to access only their own activity history.

5. # **Postconditions**

   1. ## **Success and failure states**

   Success:

   • The Customer sees their own recent published products in the configured chronological order.

   Failure:

   • No other Customer's history or unpublished product data is exposed.

   • Viewing history does not modify product, inventory, cart, or order data.

6. # **Extension Points**

   1. ## **Related use cases and scope**

   No formal UML extension point is defined in the current shared Use-Case Model. Related use cases:

   • UC-015 — View Product Details

   • UC-019 — View Homepage Recommendations

   • UC-020 — View Personalized Recommendations

   • UC-022 — Manage Wishlist

   Scope: Vision v1.4 identifies recent product views as a permitted signal for authorized recommendations, and the shared Use-Case Model assigns this use case to Customer. No dedicated Recently Viewed Products screen, history list, empty state, or history-management control is present in the supplied Hza.zip exports. The display entry point, retention period, and consent policy remain open design/Backend decisions.

   Performed by: Nguyễn Hoàng Gia \| Reviewed by: Pending \| Status: Draft for review

   ## **Prototype Screens**

Source: Hza(1).zip — static PDF exports. Images show sample data, not implementation or test evidence. Canonical PA3 UC identifiers take precedence over the export-local screen labels.

Prototype gap: No dedicated screen for this use case is included in Hza.zip. Basic-flow and alternative-flow screenshots remain required for the PA3 prototype requirement. No substitute screen is represented as an existing design.
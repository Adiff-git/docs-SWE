# **Electronics Store E-commerce Website**

# **FG-03 \-- 016 \-- Compare Products**

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

# **FG-03 \-- 016 \-- Compare Products**

1. # **Use-Case Name**

   UC-016 — Compare Products

   1. ## **Brief Description**

   A Guest or Customer selects two or three products from the same category and views their key attributes side by side to evaluate differences in price, specifications, and suitability. The System presents comparable catalog facts without inventing missing values or making an unsupported universal-best claim.

   Functional group: FG-03 — Search and Browse

   Actor(s): Guest (G), Customer (C)

   Priority: Core

2. # **Flow of Events**

   1. ## **Basic Flow**

   1\. The Guest or Customer opens a product listing or product detail page.

   2\. The Guest or Customer selects the compare action for a product. The System adds the product to a temporary comparison selection and indicates the current selection count.

   3\. The Guest or Customer selects another product from the same category.

   4\. The System validates that the selected products belong to the same category and that the comparison contains no more than three products.

   5\. When at least two valid products are selected, the Guest or Customer opens the comparison view.

   6\. The System retrieves current product and variant attributes and displays the selected products in side-by-side columns or cards.

   7\. The System aligns comparable attributes, such as price, processor/chipset, memory, storage, display, battery, and other category-relevant specifications. Missing attributes are marked as unavailable.

   8\. The Guest or Customer may remove or replace a selected product, return to the catalog, or open a product detail through UC-015.

   2. ## **Alternative Flows**

      1. ### *Input validation and business-rule alternatives*

   A1. Only one product is selected: the System keeps the selection and prompts the actor to select at least one more product before opening the comparison.

   A2. The actor attempts to add a fourth product: the System prevents the selection or requires the actor to remove one of the existing products first.

   A3. The actor selects products from different categories: the System rejects the incompatible selection and explains that products must belong to the same category.

   A4. A selected product has missing technical attributes: the System displays “Not available” for those fields and continues comparing the attributes that are present.

      2. ### *Additional outcomes and service failures*

   A5. A selected product becomes unpublished or unavailable: the System marks it as unavailable or removes it from the active comparison and does not present it as purchasable.

   A6. The comparison/catalog service fails or times out: the System displays a retry state and preserves the current selection where possible; it does not fabricate comparison values.

3. # **Special Requirements**

   1. ## **Use-case quality and integrity constraints**

   • The comparison must contain two or three products from the same category, as specified in Vision v1.4.

   • Product identifiers and variant identifiers must remain unambiguous; prices and availability must be current and traceable to catalog records.

   • Comparable technical attributes must use consistent units and labels. Non-comparable or missing fields must be explicitly marked rather than guessed.

   • The comparison view should emphasize factual differences and must not claim that one product is universally best when suitability depends on customer priorities.

   • The selection persistence period (current page, browser session, or account) and the exact compare-entry control require confirmation by the team; this specification does not assume cross-device persistence.

4. # **Preconditions**

   1. ## **Conditions that must hold**

   • The public catalog and product-detail data are reachable.

   • At least two published products from a common category are available for a successful comparison.

   • No authenticated session is required for public product comparison.

5. # **Postconditions**

   1. ## **Success and failure states**

   Success:

   • A side-by-side comparison of two or three same-category products is displayed with verified product attributes.

   Failure:

   • Invalid selections do not produce a misleading comparison.

   • No product, inventory, cart, customer, or order data is modified.

6. # **Extension Points**

   1. ## **Related use cases and scope**

   No formal UML extension point is defined in the current shared Use-Case Model. Related use cases:

   • UC-012 — Browse Product Catalog

   • UC-013 — Search Products

   • UC-014 — Filter & Sort Products

   • UC-015 — View Product Details

   • UC-020 — View Personalized Recommendations

   Scope: Vision v1.4 requires comparison of two or three products from the same category. No dedicated comparison page, compare-selection control, comparison table, or comparison empty/error state is present in the supplied Hza.zip exports. The flow above is therefore a requirements-level specification derived from Vision and the shared Use-Case Model, not a claim that the current prototype or implementation contains this feature. The compare entry point, selected-field matrix, and selection persistence must be confirmed with Frontend/Backend.

   Performed by: Nguyễn Hoàng Gia \| Reviewed by: Pending \| Status: Draft for review

   ## **Prototype Screens**

Source: Hza(1).zip — static PDF exports. Images show sample data, not implementation or test evidence. Canonical PA3 UC identifiers take precedence over the export-local screen labels.

Prototype gap: No dedicated screen for this use case is included in Hza.zip. Basic-flow and alternative-flow screenshots remain required for the PA3 prototype requirement. No substitute screen is represented as an existing design.
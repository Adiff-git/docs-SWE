# **Electronics Store E-commerce Website**

# **FG-03 \-- 020 \-- View Personalized Recommendations**

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

# **FG-03 \-- 020 \-- View Personalized Recommendations**

1. # **Use-Case Name**

   UC-020 — View Personalized Recommendations

   1. ## **Brief Description**

   An authenticated Customer requests product suggestions tailored to permitted shopping signals and expressed preferences. The System uses Backend-approved catalog data and only authorized Customer signals, such as recent searches or product views, to rank relevant published products. If personal signals or consent are unavailable, the System falls back to non-personalized suggestions.

   Functional group: FG-03 — Search and Browse

   Actor(s): Customer (C)

   Priority: Optional

2. # **Flow of Events**

   1. ## **Basic Flow**

   1\. The Customer opens a personalized-recommendation section from the storefront. The exact placement and entry point require Frontend confirmation because no dedicated frame is present in Hza.zip.

   2\. The System verifies the Customer's authenticated session and checks whether personalization is enabled and the required data-use permission is available.

   3\. The System retrieves only the permitted Customer signals and preference fields needed for recommendation generation, such as recent searches, recent product views, category interests, or an expressed budget where available.

   4\. The Recommendation service obtains eligible published product candidates and their current attributes from the authoritative Backend catalog.

   5\. The Recommendation service ranks candidates against the permitted signals and preferences. The ranking algorithm and relevance thresholds are implementation decisions and are not specified by Vision v1.4.

   6\. The System displays the recommended product cards with verified product names, images, prices, and availability, and identifies the section as personalized only when personalization was actually used.

   7\. The Customer selects a recommended product to continue with UC-015 View Product Details.

   2. ## **Alternative Flows**

      1. ### *Input validation and business-rule alternatives*

   A1. Personalization is disabled or the Customer has not granted the required permission: the System does not use personal activity signals and displays non-personalized homepage suggestions through UC-019, or explains that personalized suggestions are unavailable.

   A2. The Customer has insufficient recent activity or no usable preference data: the System uses a non-personalized fallback rather than inventing a profile or activity history.

   A3. No eligible products match the permitted constraints: the System displays an empty/limited-result state and may invite the Customer to broaden preferences; it does not fabricate products.

   A4. A recommended product becomes unpublished or unavailable: the System removes or marks the product unavailable and does not present it as purchasable.

      2. ### *Additional outcomes and service failures*

   A5. Recommendation service or catalog retrieval fails or times out: the System displays a recoverable section-level error and falls back to ordinary catalog browsing or non-personalized homepage content.

   A6. Customer session expires during the request: the System stops account-specific processing and prompts the Customer to sign in again.

3. # **Special Requirements**

   1. ## **Use-case quality and integrity constraints**

   • The recommendation service may use only Backend-approved product attributes and Customer signals that are permitted and authorized for this purpose.

   • If consent or personal history is unavailable, the System must use non-personalized suggestions; it must not infer or invent Customer activity.

   • Product names, prices, stock, specifications, and links must match authoritative catalog records. Missing attributes must not be guessed.

   • Suggestions should respect expressed budget and category preferences when those fields are available and supported.

   • The System must distinguish personalized results from curated/featured homepage content in UC-019.

   • Vision v1.4 identifies AF-01 as Gia's recommendation ownership area but explicitly states that implementation and relevance testing are planned, not complete. This specification describes intended behavior and is not evidence of a completed recommendation engine.

4. # **Preconditions**

   1. ## **Conditions that must hold**

   • The Customer is authenticated for account-specific recommendation processing.

   • The recommendation feature and catalog candidate service are available, or the System can return a defined fallback/error state.

   • The System has the required permission to use any personal signals included in the request.

5. # **Postconditions**

   1. ## **Success and failure states**

   Success:

   • The Customer sees verified product suggestions ranked using permitted personal signals and preferences, or a clearly identified non-personalized fallback.

   Failure:

   • No unauthorized Customer signal or unsupported product fact is used or exposed.

   • No product, inventory, cart, or order data is modified by viewing recommendations.

6. # **Extension Points**

   1. ## **Related use cases and scope**

   No formal UML extension point is defined in the current shared Use-Case Model. Related use cases:

   • UC-018 — View Recently Viewed Products

   • UC-019 — View Homepage Recommendations

   • UC-021 — Manage Recommendation Preferences

   • UC-015 — View Product Details

   Scope: Vision v1.4 defines AF-01 as personalized product recommendations using approved product attributes and, for authorized Customers, permitted signals such as recent searches or views. It requires fallback to non-personalized suggestions when consent or personal history is unavailable. No dedicated personalized-recommendation frame, ranking explanation, or preference-aware state is present in Hza.zip. The feature is planned and requires Backend data contracts, consent handling, and relevance testing.

   Performed by: Nguyễn Hoàng Gia \| Reviewed by: Pending \| Status: Draft for review

   ## **Prototype Screens**

Source: Hza(1).zip — static PDF exports. Images show sample data, not implementation or test evidence. Canonical PA3 UC identifiers take precedence over the export-local screen labels.

Prototype gap: No dedicated screen for this use case is included in Hza.zip. Basic-flow and alternative-flow screenshots remain required for the PA3 prototype requirement. No substitute screen is represented as an existing design.
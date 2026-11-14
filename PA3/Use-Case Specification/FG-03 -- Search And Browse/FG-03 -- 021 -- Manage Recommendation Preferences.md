# **Electronics Store E-commerce Website**

# **FG-03 \-- 021 \-- Manage Recommendation Preferences**

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

Prototype Screens	7

# **FG-03 \-- 021 \-- Manage Recommendation Preferences**

1. # **Use-Case Name**

   UC-021 — Manage Recommendation Preferences

   1. ## **Brief Description**

   An authenticated Customer manages whether permitted personal signals may be used to personalize product recommendations and, where supported by the approved product design, updates preference inputs such as interested categories or budget range. The System saves the Customer's choices and applies them to subsequent recommendation requests.

   Functional group: FG-03 — Search and Browse

   Actor(s): Customer (C)

   Priority: Optional

2. # **Flow of Events**

   1. ## **Basic Flow**

   1\. The Customer opens the recommendation-preferences entry point from the account area or recommendation section. The exact location is not present in Hza.zip and requires Frontend confirmation.

   2\. The System verifies the Customer's authenticated session and retrieves the Customer's current recommendation consent and supported preference values.

   3\. The System displays the current personalization status and the preference controls approved for the release. Vision v1.4 identifies category interests and budget as relevant recommendation preferences, but does not define the final field list or UI.

   4\. The Customer enables or disables personalized recommendations and optionally changes the supported category or budget preferences.

   5\. The System validates the submitted values and saves the Customer's preference settings.

   6\. The System confirms the saved state and uses the updated settings in subsequent UC-020 View Personalized Recommendations requests.

   2. ## **Alternative Flows**

      1. ### *Input validation and business-rule alternatives*

   A1. The Customer submits an invalid preference value (for example, a negative budget or an unsupported category): the System displays a field-level validation message and does not overwrite the last valid settings.

   A2. The Customer disables personalization: the System records the opt-out and stops using personal activity signals for subsequent personalized-recommendation requests. Generic UC-019 homepage content may remain available.

   A3. The Customer clears optional category/budget preferences: the System removes those constraints and does not invent replacement values.

      2. ### *Additional outcomes and service failures*

   A4. The Customer's session expires: the System requests sign-in and does not save account-specific preference changes.

   A5. The preference service fails or times out: the System reports that the change was not confirmed and retains the previously saved state; it must not display a success message without a confirmed save response.

3. # **Special Requirements**

   1. ## **Use-case quality and integrity constraints**

   • Personalization consent must be explicit, understandable, and changeable by the Customer.

   • When personalization is disabled, the recommendation service must not use the Customer's recent searches or views for personalized ranking.

   • Only preference fields approved by the team and supported by the Backend may be displayed or saved. The final preference schema, default values, and entry point remain open decisions.

   • Preference data must be scoped to the authenticated Customer and protected against cross-account access.

   • The System must not claim that a preference has been saved until the Backend confirms the update.

   • Retention and deletion behavior for historical activity after opt-out must be defined separately; disabling future use must not be misrepresented as deletion of previously stored data.

4. # **Preconditions**

   1. ## **Conditions that must hold**

   • The Customer is authenticated.

   • The preference service is available, or the System can return a defined error state.

   • The recommendation-preference fields and consent policy have been approved by the team.

5. # **Postconditions**

   1. ## **Success and failure states**

   Success:

   • The Customer's approved recommendation settings are saved and available to subsequent recommendation requests.

   Failure:

   • The previous saved settings remain unchanged when validation or persistence fails.

   • No other Customer's preference data is exposed or modified.

6. # **Extension Points**

   1. ## **Related use cases and scope**

   No formal UML extension point is defined in the current shared Use-Case Model. Related use cases:

   • UC-020 — View Personalized Recommendations

   • UC-019 — View Homepage Recommendations

   • UC-018 — View Recently Viewed Products

   • UC-009 — Manage Profile

   Scope: The shared Use-Case Model includes UC-021, and Vision v1.4 states that recommendations should respect expressed budget/category preferences and only use permitted personal signals. However, the supplied Hza.zip does not contain a recommendation-settings page or preference controls, and Vision v1.4 does not define a final preference schema. This specification therefore captures the minimum consent/preference behavior and marks the field list, settings location, default state, and historical-data retention policy for team confirmation.

   Performed by: Nguyễn Hoàng Gia \| Reviewed by: Pending \| Status: Draft for review

   ## **Prototype Screens**

Source: Hza(1).zip — static PDF exports. Images show sample data, not implementation or test evidence. Canonical PA3 UC identifiers take precedence over the export-local screen labels.

Prototype gap: No dedicated screen for this use case is included in Hza.zip. Basic-flow and alternative-flow screenshots remain required for the PA3 prototype requirement. No substitute screen is represented as an existing design.
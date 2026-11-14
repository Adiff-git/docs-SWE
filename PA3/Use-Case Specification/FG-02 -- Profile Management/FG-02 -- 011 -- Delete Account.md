# **Electronics Store E-commerce Website**

# **FG-02 \-- 011 \-- Delete Account**

# 

# **Version 1.1**

# **Revision History**

| Date | Version | Description | Author |
| ----- | ----- | ----- | ----- |
| 14/Nov/26 | 1.1 | PA3 specification aligned with team RUP template, Vision v1.4 and Hza static exports | Trịnh Văn Thành |
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

3\. Special Requirements	4

3.1 Use-case quality and integrity constraints	4

4\. Preconditions	5

4.1 Conditions that must hold	5

5\. Postconditions	5

5.1 Success and failure states	5

6\. Extension Points	5

6.1 Related use cases and scope	5

Prototype Screens	6

# **FG-02 \-- 011 \-- Delete Account**

1. # **Use-Case Name**

   UC-011 — Delete Account

   1. ## **Brief Description**

   A Customer requests deletion of their own account through a protected confirmation flow, subject to an approved retention and outstanding-transaction policy.

   Functional group: FG-02 — Profile Management

   Actor(s): Customer (C)

   Priority: Optional

2. # **Flow of Events**

   1. ## **Basic Flow**

   1\. The Customer opens the account-deletion entry point.

   2\. The System authenticates the Customer and explains the approved consequences and records that must be retained.

   3\. The Customer completes required recent authentication and explicitly confirms the deletion request.

   4\. The System checks ownership, outstanding-transaction restrictions and the approved deletion/retention policy.

   5\. The System applies the permitted account removal/deactivation/anonymization operation and revokes affected sessions consistently.

   6\. The System confirms the real result and displays a signed-out completion state.

   2. ## **Alternative Flows**

      1. ### *Input validation and business-rule alternatives*

   A1. Before step 3, the Customer cancels: make no change.

   A2. At step 3, recent-authentication evidence fails: deny deletion.

   A3. At step 4, pending orders/refunds or required retention prevent the requested operation: explain the restriction without pretending deletion completed.

      2. ### *Additional outcomes and service failures*

   A4. At step 4, the request targets another account: deny it.

   A5. At steps 2–5, the session expires: require sign-in and fresh confirmation.

   A6. At step 5, persistence fails or the result is uncertain: report an unconfirmed state and reconcile before retry.

3. # **Special Requirements**

   1. ## **Use-case quality and integrity constraints**

   • This is a proposed flow because no deletion screen, Backend contract or approved retention rules are supplied.

   • Deletion must not erase financial/order snapshots indiscriminately or be confused with administrator temporary locking.

   • The exact legal/business retention period, reactivation window and meaning of delete must be agreed before enabling the feature; no jurisdiction-specific policy is asserted here.

   • Never execute this operation solely from a general profile-save action.

4. # **Preconditions**

   1. ## **Conditions that must hold**

   • The Customer is authenticated and an approved account-deletion policy is configured.

5. # **Postconditions**

   1. ## **Success and failure states**

   Success:

   • Only the approved account operation is committed; sessions and retained records follow the agreed policy.

   Failure:

   • Rejected/uncertain requests are not labeled complete and do not affect another account.

6. # **Extension Points**

   1. ## **Related use cases and scope**

   No named UML extension location is verified in the supplied model tab. Related use cases: UC-009 Manage Profile; UC-003 Logout; UC-048 Manage Customer Accounts.

   Scope: Canonical Optional UC-011 is absent from Hza and the old Thành files. Requires an approved prototype and deletion/retention policy before implementation.

   Sources: Vision v1.4; shared PA3 Use-Case Model; Hza.zip static exports; earlier Thành specifications dated 11 November 2026\. Prior Backend statements have not been revalidated against repository code in this revision.

   Performed by: Trịnh Văn Thành \| Reviewed by: Pending \| Status: Draft for review

   ## **Prototype Screens**

Source: Hza(1).zip — static PDF exports. Images show sample data, not implementation or test evidence. Canonical PA3 UC identifiers take precedence over the export-local screen labels.

Prototype gap: No dedicated screen for this use case is included in Hza.zip. Basic-flow and alternative-flow screenshots remain required for the PA3 prototype requirement. No substitute screen is represented as an existing design.
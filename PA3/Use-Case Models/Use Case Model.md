# Use Case Model

**Performed By**: Nguyễn Công Kiên, Phan Thị Thanh Huyền 
 
**Reviewed By**: Nguyễn Hoàng Gia

-
**System:** Electronics Store E-Commerce Platform  

## Actors and Notation

| Actor | Role |
| --- | --- |
| Guest | Registers, logs in, and browses the public catalog. |
| Customer | Manages their account, cart, payments, and orders. |
| Administrator | Uses shared authentication and confirms manually reconciled payments. |
| Email Service | Delivers verification, recovery, and restock emails. |
| Google Identity Provider | Authenticates users through Google. |
| Payment Provider | Processes online payments and confirms results. |

Mermaid diagrams represent use cases as rounded nodes inside the system boundary and actors outside it.

- Solid line: actor participation.
- `<<include>>`: mandatory reused behavior; arrow points to the included use case.
- `<<extend>>`: conditional behavior; arrow points to the base use case.
- `Generalization`: specialization; arrow points to the general actor or use case.
- `[Optional]`: optional feature. Other numbered use cases are core.
- `SUP-01` to `SUP-04`: supplemental use cases for restock notifications, checkout item selection, fulfillment selection, and recipient details. Nodes without IDs represent supporting behavior.

## FG-01: Authentication & Authorization

```mermaid
flowchart LR
    G["Guest"]
    C["Customer"]
    A["Administrator"]
    U["Authenticated User (abstract)"]
    E["Email Service"]
    Google["Google Identity Provider"]
    C -->|Generalization| U
    A -->|Generalization| U
    subgraph SYS["E-commerce Platform — Authentication & Authorization"]
        UC001(["UC-001 Register Account"])
        UC002(["UC-002 Login"])
        UC003(["UC-003 Logout"])
        UC004(["UC-004 Verify Email"])
        UC005(["UC-005 Reset Password"])
        UC006(["UC-006 Change Password"])
        UC007(["UC-007 Login with Google [Optional]"])
        Role(["Determine Role-Appropriate Interface"])
    end
    G --- UC001
    G --- UC002
    G --- UC004
    G --- UC005
    G --- UC007
    U --- UC003
    C --- UC005
    C --- UC006
    E --- UC004
    E --- UC005
    Google --- UC007
    UC001 -.->|"<<include>>"| UC004
    UC007 -->|Generalization| UC002
    UC002 -.->|"<<include>>"| Role
```

## FG-02: User Profile & Address Management

```mermaid
flowchart LR
    C["Customer"]
    subgraph SYS["E-commerce Platform — User Profile & Address Management"]
        UC009(["UC-009 Manage Profile"])
        UC010(["UC-010 Manage Shipping Address"])
        UC011(["UC-011 Delete Account"])
    end
    C --- UC009
    C --- UC010
    C --- UC011
```

## FG-03: Search and Browse

```mermaid
flowchart LR
    G["Guest"]
    C["Customer"]
    V["«abstract»<br/>Catalog Visitor"]

    G -.->|"generalization"| V
    C -.->|"generalization"| V

    subgraph SYS["E-commerce Platform — Search and Browse"]
        UC012(["UC-012 Browse Product Catalog"])
        UC013(["UC-013 Search Products"])
        UC014(["UC-014 Filter & Sort Products"])
        UC015(["UC-015 View Product Details"])
        UC016(["UC-016 Compare Products"])
        UC017(["UC-017 View Product Promotions"])
        UC018(["UC-018 View Recently Viewed Products"])
        UC019(["UC-019 View Homepage Recommendations"])
        UC022(["UC-022 View Personalized Recommendations"])
    end

    V --- UC012
    V --- UC013
    V --- UC015
    V --- UC016
    V --- UC017

    C --- UC018
    C --- UC019
    C --- UC022

    UC014 -.->|"«extend» when filters or sorting are chosen"| UC012
    UC014 -.->|"«extend» when filters or sorting are chosen"| UC013
    UC017 -.->|"«extend» when promotions exist"| UC015
```

## FG-04: Shopping Cart

```mermaid
flowchart LR
    C["Customer"]

    subgraph SYS["E-commerce Platform — Shopping Cart"]
        UC023(["UC-023 Manage Shopping Cart"])
        UC024(["UC-024 Apply Discount Code"])
    end

    C --- UC023

    UC024 -.->|"«extend» when a code is submitted"| UC023
```

## FG-05: Checkout & Payment

```mermaid
flowchart LR
    C["Customer"]
    P["Payment Provider"]

    subgraph SYS["E-commerce Platform — Checkout & Payment"]
        UC025(["UC-025 Checkout"])
        UC026(["UC-026 Place Order"])
        UC027(["UC-027 Make Payment"])
        UC028(["UC-028 View Payment Status"])
    end

    C --- UC025
    C --- UC028
    P --- UC027

    UC026 -.->|"«extend» when the customer confirms the order"| UC025
    UC027 -.->|"«extend» when the customer pays"| UC026
```

## FG-06: Product Management
```mermaid
flowchart LR
    A["Administrator"]

    subgraph SYS["E-commerce Platform — Product Management"]
        UC030(["UC-030 View Product Sales Overview"])
        UC031(["UC-031 Manage Products"])
        UC032(["UC-032 Manage Product Categories"])
        UC033(["UC-033 Manage Product Brands"])
        UC034(["UC-034 Manage Product Variants & Prices"])
        UC035(["UC-035 Manage Product Images"])
        UC036(["UC-036 Manage Product Specifications"])
        UC037(["UC-037 Manage Product Stock"])
        UC038(["UC-038 Import Product Data"])
    end

    A --- UC030
    A --- UC031
    A --- UC032
    A --- UC033
    A --- UC037

    UC034 -.->|"«extend»"| UC031
    UC035 -.->|"«extend»"| UC031
    UC036 -.->|"«extend»"| UC031
    UC038 -.->|"«extend»"| UC031
```

## FG-07: Order Management
```mermaid
flowchart LR
    C["Customer"]
    A["Administrator"]

    subgraph SYS["E-commerce Platform — Order Management"]
        UC039(["UC-039 View Order History & Details"])
        UC040(["UC-040 Track Order Status"])
        UC041(["UC-041 Cancel Order"])
        UC042(["UC-042 Request Return"])
        UC043(["UC-043 Request Refund"])
        UC044(["UC-044 Process Customer Orders"])
    end

    C --- UC039
    A --- UC044

    UC040 -.->|"«extend»"| UC039
    UC041 -.->|"«extend»"| UC039
    UC042 -.->|"«extend»"| UC039
    UC043 -.->|"«extend»"| UC041
    UC043 -.->|"«extend»"| UC042
```

## FG-07: Wishlist & Product Reviews

```mermaid
flowchart LR
    U["«abstract»<br/>User"]
    G["Guest"]
    C["Customer"]

    G -.->|"generalization"| U
    C -.->|"generalization"| U

    subgraph SYS["E-commerce Platform — Wishlist & Product Reviews"]
        UC051(["UC-051/053 Manage Wishlist"])
        UC052(["UC-052 View Wishlist"])

        UC054(["UC-054 View Product Reviews"])
        UC055(["UC-055 Write Product Review"])
        UC056(["UC-056 Rate Product"])
        UC057(["UC-057 Edit Product Review"])
        UC058(["UC-058 Delete Product Review"])
    end

    C --- UC051
    C --- UC052

    U --- UC054
    C --- UC055
    C --- UC056
    C --- UC057
    C --- UC058

    UC055 -.->|"«extend»"| UC056
```

## FG-09: Administration
```mermaid
flowchart LR
    A["Administrator"]

    subgraph SYS["E-commerce Platform — Store Administration"]
        UC047(["UC-047 Manage Store Settings & Homepage Content"])
        UC048(["UC-048 Manage Customer Accounts"])
        UC049(["UC-049 Manage Promotions & Vouchers"])
        UC050(["UC-050 Moderate Product Reviews"])
        UC051(["UC-051 View Sales Statistics"])
    end

    A --- UC047
    A --- UC048
    A --- UC049
    A --- UC050
    A --- UC051
```

## FG-10: AI Chatbot & Shopping Automation
```mermaid
flowchart LR
    C["Customer"]

    subgraph SYS["E-commerce Platform — AI Chatbot & Shopping Automation"]
        UC052(["UC-052 Chat with AI Assistant"])
        UC053(["UC-053 Search Products Using Natural Language"])
        UC054(["UC-054 Get AI Product Recommendations"])
        UC055(["UC-055 Compare Products Using AI"])
        UC056(["UC-056 Manage Shopping Cart via AI"])
        UC057(["UC-057 Prepare Checkout via AI"])
        UC058(["UC-058 Ask AI About Order Status"])
        UC059(["UC-059 Manage AI Conversation History"])
    end

    C --- UC052

    UC053 -.->|"«extend»"| UC052
    UC054 -.->|"«extend»"| UC052
    UC055 -.->|"«extend»"| UC052
    UC056 -.->|"«extend»"| UC052
    UC057 -.->|"«extend»"| UC052
    UC058 -.->|"«extend»"| UC052
    UC059 -.->|"«extend»"| UC052
```
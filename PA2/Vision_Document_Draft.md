
# VISION DOCUMENT — THINH'S ASSIGNED SECTIONS

**Project:** Electronics Store E-Commerce Website with AI Shopping Assistance
**Team:** SWE Group 03 — Lẩu Gà Lá É  
**Version:** Review draft, 28 October 2026  
**Scope:** Seven assigned sections only; not the complete team Vision Document  
**Primary writer / Performed by:** Lê Đức Thịnh  
**Section reviewer:** Trịnh Văn Thành (**review pending**)  
**Main document reviewer:** Phan Thị Thanh Huyền (**review pending**)  
**Source of scope:** Team's PA1 Project Proposal and PA2 Week 1 Work Plan; AI-SWE architecture and API-contract documents.

> **Review note.** This document is written as **proposed product requirements**, not as a statement that AI features are already implemented. As of the review baseline, the AI repository provides FastAPI endpoints and placeholders, but no live LLM, product-retrieval tool, persistent chat sessions, or automated shopping action. Quantitative quality criteria in Section 6 are **proposed acceptance targets** to be agreed upon with the team, not measured results. Retain the seven sections below when merging them into `Vision_Document.md`; the sections assigned to Thành should remain under his ownership.

---

## 2. Positioning

### 2.1 Problem Statement

**Jira:** SWE-81  
**Performed by:** Lê Đức Thịnh  
**Reviewed by:** Trịnh Văn Thành (pending)  
**Edited by:** Lê Đức Thịnh (initial draft; further edits pending review)

Online electronics shopping presents two related problems. Customers must understand a wide range of technical specifications while choosing products that match their actual needs and budgets. At the same time, store staff must keep product information, availability, orders, and customer support consistent across the shopping process. Standard catalog pages and filters are useful, but they may not be sufficient for a customer who can describe a need in everyday language without knowing the appropriate technical parameters.

| Problem-statement element | Description |
| --- | --- |
| **The problem of** | Customers having difficulty identifying and comparing suitable electronic products, and having to switch between catalog pages, specification tables, shopping-cart operations, and support channels to complete a purchase. |
| **Affects** | Customers with limited technical knowledge; budget-conscious shoppers comparing several alternatives; returning customers checking order or stock information; and store staff who handle repetitive product and order inquiries. |
| **Whose impact is** | More time spent researching products, uncertainty about compatibility and value, abandoned shopping journeys, repeated questions to staff, and potential mistakes when choosing variants or managing carts. For the store, fragmented information and manual operations can increase customer-support workload. |
| **A successful solution would** | Provide a single web storefront where customers can browse trustworthy catalog information, compare products consistently, manage purchases, and obtain AI-assisted, context-aware guidance grounded in store data. Customers would stay in control of all consequential actions, including order confirmation and payment. |

**Business opportunity.** The proposed system combines standard e-commerce capabilities with a conversational shopping advisor that helps customers translate practical requirements (e.g., "a laptop for university within 25 million VND") into product-search criteria. Rather than replacing the normal browsing and checkout process, AI assistance should reduce unnecessary steps and make product choices easier to understand. The store can maintain a single source of truth for product and stock information through its Backend service.

**Problem boundaries.** The system is designed for a single electronics-store e-commerce operation, not a marketplace that compares inventories across unrelated merchants. The advisor must not present unverified specifications, prices, stock quantities, promotions, or delivery promises as facts. Product availability and final prices are determined by the Backend at the relevant time, especially before checkout.

### 2.2 Product Position Statement

**Jira:** SWE-82  
**Performed by:** Lê Đức Thịnh  
**Reviewed by:** Trịnh Văn Thành (pending)  
**Edited by:** Lê Đức Thịnh (initial draft; further edits pending review)

| Positioning element | Product position |
| --- | --- |
| **For** | Online shoppers seeking electronics, especially customers who value clear explanations and straightforward product selection; and store administrators responsible for catalog and order operations. |
| **Who** | Want to find reliable products within a budget, understand specifications, compare alternatives, and complete purchases without spending excessive time researching technical details. |
| **The product** | Is a browser-based electronics e-commerce platform with an integrated AI shopping assistant. |
| **That** | Provides catalog browsing and filtering, structured product details and comparison, customer-account and shopping-cart functions, checkout and order tracking, together with conversational product discovery, consultation, and selected assisted actions. |
| **Unlike** | A physical-only store or a traditional catalog-first shopping journey in which users must translate needs into filters and navigate many pages or ask staff for help. |
| **Our product** | Integrates natural-language assistance into the same storefront and uses Backend-owned catalog and account information for grounded responses, while requiring user confirmation before purchases and other sensitive actions. |

**Value proposition.** The platform should make electronics shopping more accessible without sacrificing the factual accuracy of structured catalog data. Customers can begin with either conventional search and filters or the AI Chatbox, then proceed to product pages, cart, and checkout using the same underlying product records. The design emphasizes transparent recommendations, explicit prices and availability, and customer control. Administrators retain responsibility for authoritative product data, inventory, order status, and store policies.

**Product differentiators (proposed, not yet validated):**

1. **Needs-based guidance:** Customers may describe use cases, budget constraints, and preferences in natural language; the assistant translates these into catalog-based suggestions.
2. **Explainable alternatives:** Product suggestions and comparisons refer to relevant, verifiable attributes (such as RAM, storage, battery, display, compatibility, or price) rather than unsupported marketing claims.
3. **Connected shopping journey:** The assistant can guide the user from discovery to product details and, in later phases, confirmed cart operations without inventing a separate inventory or checkout system.
4. **User-controlled automation:** For actions that affect a user's account or cart, the system shows what it intends to change; users retain final control over checkout and payment.

---

## 4. Product Overview

### 4.1 Product Perspective

**Jira:** SWE-87  
**Performed by:** Lê Đức Thịnh  
**Reviewed by:** Trịnh Văn Thành (pending)  
**Edited by:** Lê Đức Thịnh (initial draft; further edits pending review)

The product is a web-based application for an electronics retailer. It combines a **customer storefront** and an **administrator interface** with a centralized Backend and a separately deployed AI service. The system is expected to operate in modern desktop browsers such as Chrome and Firefox on Windows and Linux, with an internet connection. The initial coursework implementation should prioritize functioning core journeys before more advanced recommendation and automation features.

**Major subsystems and responsibilities**

| Subsystem | Primary responsibility | Key interactions |
| --- | --- | --- |
| **Customer frontend** | Presents the homepage, catalog, product details, comparison, login, cart, checkout, order history, and AI Chatbox. Displays validation errors and asks users to confirm actions. | Calls Backend APIs for authenticated user data and shopping operations; renders AI results delivered through the agreed integration path. |
| **Administrator frontend** | Provides catalog, stock, promotion, account, review, and order management interfaces for authorized store staff. | Calls Backend APIs subject to administrative authorization. |
| **Backend service** | Is the authoritative source for users, roles, product records, variants, prices, inventory, cart, orders, and customer activity data as permitted by policy. Handles authentication, authorization, input validation, and persistent state. | Offers agreed REST APIs to the Frontend and authorized AI service. |
| **AI service — Recommendation** | Produces candidate products according to available product metadata and, when permitted, relevant customer signals. | Requests approved catalog and behavior data through Backend contracts; returns product identifiers/scores as agreed. |
| **AI service — Shopping Agent** | Interprets conversational requests, asks clarifying questions, calls permitted tools, and prepares grounded product suggestions, comparisons, or assisted shopping steps. | Uses Backend-facing tools and an LLM provider where configured; returns safe structured outputs for presentation. |
| **External services (conditional)** | Payment gateway, email notification provider, and selected LLM provider. | Each requires separately approved credentials, contracts, availability handling, and security controls. |

**Conceptual interaction model.** Customers use a single web application, whether they browse products manually or open the AI Chatbox. According to the current AI repository's intended architecture, the Frontend communicates with the Backend, and the Backend mediates authorized calls to the AI service. The AI service does not directly access the Backend database. For any future frontend-to-AI shortcut, authentication, authorization, CORS, and API ownership must be reviewed before adopting a different architecture.

**Shared business-data principle.** A product displayed in an AI recommendation must refer to the same product identifier and authoritative record used by the storefront. The AI service can suggest or summarize a product but must not independently set prices, stock quantities, voucher eligibility, delivery fees, or order states. A final Backend recheck is required when an operation depends on inventory or pricing that may have changed since the chat response.

**Roles and permissions.** Guest shoppers may browse public catalog information and request general product advice. Logged-in customers may access their own saved information, cart, and order status according to Backend permissions. Store administrators can perform management operations through the admin interface; AI tools must not acquire administrative privileges from a customer's natural-language message.

**User-experience perspective.** The Chatbox should be reachable from core customer-facing screens, including the homepage and product-related journeys. It must not block ordinary browsing, login, cart editing, or checkout when the AI service is unavailable. Desktop is the documented initial deployment environment; responsive adaptation can be added as project capacity allows and should not be claimed complete without testing.

**Development perspective and current baseline.** The Frontend currently uses React and Vite; its main route table and layout components are in place. The AI repository uses Python, FastAPI, and HTTPX, with health, recommendation, and chat endpoints that return scaffold or placeholder responses. Therefore, the complete AI capabilities described in this Vision represent the **planned end state**, not current Sprint 2 functionality. Planned progression is: stable Frontend/Backend foundations → grounded AI MVP → integrated tool calls and personalization → safer automation and testing.

### 4.2 Assumptions and Dependencies

**Jira:** SWE-88  
**Performed by:** Lê Đức Thịnh  
**Reviewed by:** Trịnh Văn Thành (pending)  
**Edited by:** Lê Đức Thịnh (initial draft; further edits pending review)

**Assumptions**

| ID | Assumption | Consequence if not satisfied |
| --- | --- | --- |
| AS-01 | Product records contain unique, stable IDs, category, name, price, variant information, current availability, and sufficient technical attributes for search and comparison. | AI recommendations and comparisons may be incomplete or misleading; affected features must be restricted or return an explicit insufficiency notice. |
| AS-02 | The Backend team exposes documented and versioned REST APIs, with OpenAPI definitions or equivalent agreed schemas. | Frontend and AI integration will be delayed; teams should use mock data/contracts without presenting them as production APIs. |
| AS-03 | Authentication and authorization are implemented and enforced by the Backend for each account-specific request or action. | The assistant must be limited to public catalog consultation until secure account operations become available. |
| AS-04 | Customers have a functioning internet connection and can use a modern browser; desktop is the initial supported environment. | The website and AI-assisted features may not be accessible; offline functionality is outside the initial scope. |
| AS-05 | A suitable LLM provider, API access, or compatible local model can be configured within project cost and compute constraints. | The conversational agent may need to remain a mock/demo interface or use constrained rule-based behavior until a provider is approved. |
| AS-06 | The team has access to representative catalog examples and test questions covering common electronics categories and price ranges. | Quality evaluation may be inconclusive; acceptance metrics must be evaluated only after a representative test set is agreed. |
| AS-07 | Any external email, payment, or notification integration is subject to separate configuration and policy agreement. | Related actions should be disabled or clearly marked as unavailable until integrations are established. |

**Dependencies**

| ID | Dependency | Owner / interface | Affected capabilities | Mitigation or interim approach |
| --- | --- | --- | --- | --- |
| DP-01 | Catalog search, product details, category, price and availability APIs | Backend (Gia / Thành) | Product search, comparison, consultation, recommendation | Agree a minimal contract early; use labeled mock catalog responses for UI demonstrations. |
| DP-02 | Authentication, customer identity, and authorization | Backend (Thành) | Personalized suggestions; customer-specific cart and order actions | Restrict guests to public product information; enforce permissions on every Backend request. |
| DP-03 | Cart and checkout APIs and rules | Backend | Adding/replacing/removing cart items, preparing checkout | Build preview-only or confirmation-only UI until endpoints are implemented. Never promise a completed order from a chat message. |
| DP-04 | User activity and history data, consent, and retention rules | Backend + AI Recommendation (Gia) | Personalized recommendations | Start with non-personalized recommendations when consented behavior data is unavailable. |
| DP-05 | Chatbox, product cards, compare view, and shared design tokens | Frontend (Thịnh / Kiên / Huyền) | End-user access to AI capabilities | Implement UI mock states first; progressively connect to validated APIs. |
| DP-06 | LLM connection, system prompt, agent orchestration, and tool definitions | AI Shopping Agent (Thịnh) | Natural-language assistance and tool use | Deliver a minimal prompt + LLM prototype, then integrate tools after Backend contract review. |
| DP-07 | Model response quality, API rate limits, and external network reliability | AI team and chosen provider | AI response time, availability, and operational cost | Set timeouts and bounded responses; provide ordinary catalog search as a fallback. |
| DP-08 | Product/variant data synchronization | Backend and AI teams | Correct prices, stock information, recommendation eligibility | Prefer live Backend reads or clearly identified timestamps; revalidate before mutations. |

**Known constraints and open decisions.**

- The original PA1 proposal includes delivery, pickup, payment methods, restock alerts, order tracking, and AI-assisted actions; not all are mandatory for the immediate PA2 code snapshot. The Vision describes planned capabilities while the Project Plan specifies sprint-by-sprint implementation priorities.
- Direct access from the AI service to the Backend's database is out of scope of the currently documented architecture. AI must rely on authorized service APIs.
- Payment execution, submission of an order, and any high-impact or account-sensitive mutation require explicit user control and server-side validation. The assistant must not bypass checkout or simulate a successful purchase.
- Personalization is conditional on valid customer data, permitted access, and a clearly defined relevance/evaluation method. Missing data must not result in invented behavioral history.
- The Backend–AI API contract remains a proposal in the current AI repository and requires cross-team confirmation before being represented as implemented.

---
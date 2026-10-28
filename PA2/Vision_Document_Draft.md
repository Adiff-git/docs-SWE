
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

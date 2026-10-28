
# SWE GROUP 03 — PROJECT CONSTITUTION (DRAFT)

**Project:** Electronics Store E-Commerce Website with AI Shopping Assistance
**Proposed version:** 0.1.0 — Not ratified
**Draft date:** 28 October 2026
**Prepared for:** SWE Group 03 — Lẩu Gà Lá É
**Draft owner / Performed by:** Lê Đức Thịnh
**Reviewer:** Phan Thị Thanh Huyền
**Approval required from:** Team leads and project manager before adoption

> This is a **proposed cross-repository constitution** for PA2 review. It must not silently replace existing Frontend and Backend repository constitutions. Repository-level standards may be more specific, but they should not contradict approved project-wide principles. Until ratified, the PA1 Team Contract and current repository conventions remain authoritative.

## Purpose and Scope

This constitution defines shared engineering principles for the Frontend, Backend, AI, and project-documentation repositories of the electronics-store e-commerce system. It aims to maintain consistent interfaces, truthful documentation, secure handling of customer data, understandable AI behavior, reviewable changes, and traceable coursework evidence. Product scope includes customer browsing and shopping, administrator operations, and AI-assisted product discovery, comparison, recommendation, and selected customer-approved actions.

## Core Principles

### I. Single Source of Truth and Explicit API Contracts (NON-NEGOTIABLE)

- The Backend MUST own and authorize persistent business entities including users, product IDs, categories, variants, prices, inventory, carts, orders, and permissions. The AI service MUST NOT write to the Backend database directly.
- Cross-service interactions MUST use documented, agreed REST contracts or other protocols explicitly approved by the relevant leads. The team MUST NOT describe proposed endpoints as implemented.
- Frontend code MUST use a shared HTTP client; direct requests from arbitrary UI components MUST NOT bypass established API boundaries.
- Product facts shown by the AI assistant MUST originate from approved catalog data. Price, stock, product eligibility, and order state MUST be revalidated by the Backend before committing consequential actions.
- Breaking contract changes MUST be discussed with affected owners and accompanied by updated documentation or versioned schemas before integration.

**Rationale:** One authoritative source for business data prevents conflicting information among UI, AI, and Backend, and reduces integration mistakes.

### II. Security, Privacy, Authorization and User Control (NON-NEGOTIABLE)

- Credentials, API keys, payment tokens, and personal secrets MUST NOT be committed to Git or placed in source examples; use environment-based configuration and sanitized `.env.example` files.
- The Backend MUST authorize account-specific access on every applicable request. Natural-language prompts MUST NOT grant permission to read another customer's data or perform administrative operations.
- The AI assistant MUST request or display explicit user confirmation before account-affecting actions according to the approved action policy. Final order placement and payment MUST remain customer-controlled in the standard checkout process.
- Logs and AI prompts MUST minimize private customer information. Team members MUST use fabricated or sanitized data in reports and coursework examples unless explicitly authorized to use real data.
- If security, authorization, or safe output behavior is unknown, the feature MUST fail safely and communicate its limitation to the user.

**Rationale:** A helpful shopping assistant cannot be allowed to bypass conventional commerce security controls.

### III. Small, Testable, Reviewed Changes (NON-NEGOTIABLE)

- Each change MUST be associated with an appropriately scoped Jira issue or documented project task and developed on a purpose-specific branch, except where explicitly authorized by the team Git workflow.
- Production branches SHOULD be updated through a Pull Request with a reviewer other than the primary author. Authors MUST NOT mark work as Done before the change meets its agreed acceptance criteria.
- Frontend changes MUST pass configured lint and build checks; Backend and AI changes MUST pass their repository-appropriate tests, linting, and local validation. Where automated tests do not yet exist, the Pull Request MUST document reproducible manual verification steps.
- Pull Requests SHOULD remain focused on a single feature, fix, or documentation deliverable and MUST explain scope, risks, testing, and screenshots for visible UI changes when applicable.
- Known failures, incomplete paths, and placeholder behavior MUST be stated clearly. The team MUST NOT count an endpoint returning `not_implemented` as completed AI functionality.

**Rationale:** Traceable, testable contributions reduce integration conflicts and give reviewers verifiable evidence.

### IV. Clear Module Boundaries and Maintainable Code

- Frontend SHOULD separate pages/layouts from reusable components, domain features, hooks, and API access according to its existing conventions. New shared components MUST be reviewed for broad reuse and compatibility with agreed design tokens.
- Backend MUST encapsulate business rules, persistence, authorization, and validation so that other services cannot duplicate or bypass them.
- AI SHOULD separate HTTP routes, schemas, model/service orchestration, tool definitions, prompts, and Backend integration. Every Agent tool MUST declare expected parameters, access boundaries, and failure behavior.
- Modules MUST prefer clear names, small responsibilities, and explicit error paths over hidden coupling or speculative abstractions.
- Where multiple modules share code or schema contracts, the responsible leads SHOULD agree on ownership before broad refactoring.

**Rationale:** Stable boundaries allow parallel development by Backend, Frontend, and AI teams.

### V. Grounded and Evaluated AI Behavior

- AI-generated claims about store products MUST be traceable to authoritative product data or clearly labeled as general advice. Missing attributes MUST not be guessed.
- The Agent MUST separate read-only product-information tools from actions that mutate cart, order, or notification state. Every tool invocation MUST observe server-side validation and permissions.
- Evaluation MUST cover realistic shopping queries, budget constraints, product comparisons, incorrect/missing data, service outages, and prompt-injection attempts where relevant.
- The team MUST report the difference between proposed targets, measured metrics, and untested capabilities. Quality targets MAY be refined by team agreement after reproducible measurements.
- Recommendation and Agent modules MUST provide a graceful fallback to ordinary browsing when AI functionality is unavailable.

**Rationale:** Reliable AI reduces shopping uncertainty; ungrounded or unverified claims would undermine user trust.

### VI. Specification-Driven, Evidence-Based Documentation

- Teams SHOULD use Spec Kit consistently with the official PA2 instructions and approved project structure. Templates, constitutions, generated feature Markdown, screenshots, and training logs MUST be distinguishable in the submission package.
- Each completed document section MUST include truthful authorship/review information and match the current project scope. `Performed by`, `Reviewed by`, and `Edited by` fields MUST not imply a review that has not occurred.
- Files required by PA2 MUST be stored at the repository paths confirmed by the instructor/team. The current use of `.specify/` MUST be reconciled with any separate `/src` requirement before moving files.
- AI-assisted code and documentation MUST be checked by a responsible team member. Submitted logs or training evidence MUST describe real activities, not simulated or invented sessions.
- Architecture diagrams, API contracts, sprint plans, and Vision requirements SHOULD be updated together when decisions materially change.

**Rationale:** Coursework deliverables require not just files, but consistent and truthful evidence of the process.

## Development Workflow

1. **Clarify and scope.** Identify the stakeholder need, Jira issue, acceptance criteria, responsible owner, and dependencies. Avoid implementing unapproved API guesses.
2. **Specify.** For work requiring Spec Kit, produce a meaningful specification and planning artifacts according to the official course requirements, not merely empty templates.
3. **Implement in a feature branch.** Follow repository naming conventions and keep changes small. Store secrets outside the repository.
4. **Validate.** Run appropriate automated checks and manual acceptance scenarios; record failures as open work rather than claiming success.
5. **Review.** Submit a Pull Request or reviewable document; incorporate comments from the responsible lead/reviewer.
6. **Integrate and trace.** Merge or publish only after approved review; update Jira links, documentation, and reported progress to match actual work.

## Quality Gates and Definition of Done

A task is **Done** only when all applicable checks pass: documented acceptance criteria; a runnable implementation or complete deliverable; relevant tests/validation evidence; security and authorization checks where relevant; review by the designated reviewer; no unresolved blocking comments; source and documentation synchronized; and an accurate Jira status with the correct link or artifact path. A proposed design, unmerged branch, unreviewed document, or placeholder is **not** by itself a completed implementation.

## Decision-Making, Changes, and Exceptions

The team follows the PA1 Team Contract: cross-team decisions are discussed with affected members; the relevant technical lead coordinates domain-specific choices; the project manager coordinates planning and deadlines. Any exception to a NON-NEGOTIABLE principle requires documented review from the affected technical leads and must not compromise user authorization or secret handling. Constitution changes SHOULD be proposed through a Pull Request or tracked document edit, summarizing why a rule changes and which repositories are affected. This document SHOULD be reviewed at least once per Sprint and whenever an approved architecture or process change makes its guidance outdated.

## Suggested Ratification Record — TO BE COMPLETED

| Field                     | Proposed / status                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| Version                   | 0.1.0 (draft)                                                                                           |
| Ratified on               | **Not yet ratified**                                                                              |
| Prepared by               | Lê Đức Thịnh (draft for review)                                                                     |
| Documentation reviewer    | Phan Thị Thanh Huyền — **pending**                                                             |
| Technical reviewers       | Trịnh Văn Thành, Nguyễn Công Kiên, Nguyễn Hoàng Gia — **pending confirmation**           |
| Approved storage location | **To be confirmed** (`docs-SWE/PA2/` or an agreed Spec Kit artifact directory)                  |
| Alignment notes           | Verify against PA1 Team Contract, existing FE/BE constitutions, official PA2 artifact-path requirement. |

## References

- Team Contract and project work plan: [https://docs.google.com/document/d/1tGGx3s4Ofp8mLfQZ4sMy5bcDLiJNUQf-tCZLgDgTk6w/edit](https://docs.google.com/document/d/1tGGx3s4Ofp8mLfQZ4sMy5bcDLiJNUQf-tCZLgDgTk6w/edit)
- Frontend constitution: [https://github.com/Adiff-git/Frontend-SWE/blob/main/.specify/memory/constitution.md](https://github.com/Adiff-git/Frontend-SWE/blob/main/.specify/memory/constitution.md)
- Backend constitution: [https://github.com/Adiff-git/Backend-SWE/blob/main/.specify/memory/constitution.md](https://github.com/Adiff-git/Backend-SWE/blob/main/.specify/memory/constitution.md)
- Frontend conventions: [https://github.com/Adiff-git/Frontend-SWE/blob/main/docs/CONVENTIONS.md](https://github.com/Adiff-git/Frontend-SWE/blob/main/docs/CONVENTIONS.md)
- AI architecture: [https://github.com/Adiff-git/AI-SWE/blob/main/docs/architecture.md](https://github.com/Adiff-git/AI-SWE/blob/main/docs/architecture.md)
- Jira SWE-98: [https://giagia8765.atlassian.net/browse/SWE-98](https://giagia8765.atlassian.net/browse/SWE-98)

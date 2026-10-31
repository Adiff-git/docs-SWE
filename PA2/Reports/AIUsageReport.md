# **AI Usage Report \- Sprint 2 (PA2)**

*Performed by: Phan Thi Thanh Huyen*  
*Reviewed by: Trinh Van Thanh*

## **1\. AI Usage Declaration**

* **Did the team use AI tools during this sprint?** Yes.  
* **Scope of usage: AI tools assisted with document structure and language refinement, requirements and UI planning, code generation and debugging, Spec Kit workflows, product data preparation, and test suggestions. The team remains responsible for reviewing, modifying, and validating any AI-assisted outputs.**

## **2\. Detailed AI Usage Logs**

### **Member 1: Phan Thi Thanh Huyen**

#### Record 1: User Flow Specification

**Tool Name:** Google Gemini

**Version/Model:** Gemini 3.8 Flash

**Purpose:** To assist in drafting the user flow specification based on the project's functional requirements and expected user interactions.

**Prompts Provided:** Prompts describing the project requirements, expected features, and user interactions, requesting a structured user flow specification.

**AI Output Summary:** Generated a draft user flow specification outlining user journeys, navigation paths, and interactions between system features.

**Human Verification/Modifications:** The generated specification was reviewed against the project requirements. I modified and refined the proposed user flows, corrected inconsistencies, and adjusted the specification to align with the intended system behavior.

#### Record 2: Review of User Flow Specification

**Tool Name:** ChatGPT

**Purpose:** To review the draft user flow specification for completeness, logical consistency, and alignment with the project's requirements.

**Prompts Provided:** Prompts requesting a review of the user flow specification, including identifying missing steps, inconsistencies, and potential improvements.

**AI Output Summary:** Provided feedback on the specification, highlighting potential gaps, inconsistencies, and areas for improvement in the user flows and navigation logic.

**Human Verification/Modifications:** I evaluated the feedback against the project requirements and revised the specification where appropriate. Suggestions were not adopted automatically; I reviewed and determined which changes were relevant to the intended system.

#### Record 3: UI Wireframe Generation

**Tool Name:** Google Stitch (Gemini-powered)

**Purpose:** To generate initial UI wireframes based on the approved or refined user flow specification.

**Prompts Provided:** Prompts providing the user flow specification, UI requirements, and relevant design constraints, requesting wireframes that reflect the defined user journeys and system functionality.

**AI Output Summary:** Generated initial UI wireframes illustrating proposed page layouts, interface components, and navigation between screens based on the provided specification.

**Human Verification/Modifications:** The generated wireframes were reviewed against the user flow specification and project requirements. I modified layouts, adjusted UI components and navigation where necessary in Figma, and refined the designs to improve usability and consistency with the intended functionality.

### **Member 2: Trinh Van Thanh**

**Tool/model/platform:** OpenAI Codex; GPT-6.1 Sol

#### **Record 1: Backend Constitution Review**

**Access log:** 24 October 2026

**Commands used:** speckit-constitution.

**Purpose:** To review and refine the existing backend engineering principles.

**Original prompt excerpts:** “Review and refine the existing \`Backend-SWE Java Backend Constitution\` based on the findings below…”; “Review the current \`.specify/memory/constitution.md\` and perform a final, narrowly scoped refinement…”

**AI Output Summary:** Refined .specify/memory/constitution.md, including architecture, validation, persistence, security, testing, API contracts and amendment metadata.

**Human Contribution/Review:** I supplied the review requirements and requested targeted changes while preserving confirmed architectural decisions and existing HTTP contracts. I asked for field-specific update behavior to be documented explicitly.

#### **Record 2: User Profiles and Address Management**

**Access log:** 26 October 2026

**Commands used:** speckit-specify, speckit-clarify, speckit-plan, speckit-checklist, speckit-tasks, speckit-analyze and speckit-implement.

**Purpose:** To specify, plan and implement profile and address APIs.

**Original prompt excerpts:** “Write a feature specification for User Profiles and Address Management in the current single-vendor Spring Boot e-commerce project…”; “clarify the requirments about user and address features”; “A and use pessimistic locking”; “read all source specs, i have checked all of them”.

**AI Output Summary:** Generated specs/001-user-profiles-addresses artifacts and implemented controllers, services, DTOs, validation, persistence and tests.

**Human Contribution/Review:** I defined public-profile privacy, owner-only updates, field lengths and normalization; selected pessimistic locking; and confirmed that User/Address implementation should precede Authentication and Media with minimal integration contracts.

#### **Record 3: JWT Authentication and Session Lifecycle**

**Access log:** 26 October 2026

**Commands used:** speckit-specify, speckit-plan, speckit-checklist, speckit-tasks and speckit-implement.

**Purpose:** To add registration, login, JWT access tokens, refresh-token rotation and session revocation.

**Original prompt excerpts:** “Write an English specification for authentication, JWT access tokens, refresh-token rotation and authentication-session revocation in the current Spring Boot project…”;... 

**AI Output Summary:** Generated specs/002-auth-session-tokens and implemented authentication, session handling, permission/ownership checks, migrations and tests.

**Human Contribution/Review:** I retained the original User validation rules; confirmed USER/ACTIVE defaults, BCrypt strength 10, password limits, HS256 and an external signing secret; and approved Resource Server/Jose dependencies. Actual email/Google verification was deferred, with email provisionally trusted for this scope.

#### **Record 4: Image Storage and Avatar Integration**

**Access log:** 27 October 2026

**Commands used:** speckit-specify, speckit-plan, speckit-tasks, speckit-checklist, speckit-analyze and speckit-implement.

**Purpose:** To specify and implement shared image storage and avatar references.

**Original prompt excerpts:** “Specify an image storage feature for this Spring Boot project, using Amazon S3-compatible storage with LocalStack for local development and AWS S3 for production…”; “q1: B q2: A, q3: postponse simultaneous-completion test; hold object-replacement test…”.

**AI Output Summary:** Generated specs/003-image-storage and implemented upload/completion/view flows, storage adapters, avatar references and automated checks.

**Human Contribution/Review:** I answered the specification questions, clarified identical-content and metadata-only behavior during the command workflow, requested distinct adapter and orchestration tests without redundant facade tests, and kept authoritative requirements in spec.md. Deferred tests and unresolved storage behavior were not treated as independently verified results.

#### **Record 5: Product Wishlist**

**Access log:** 30 October 2026

**Commands used:** speckit-specify, speckit-plan, speckit-tasks, speckit-analyze, speckit-checklist and speckit-implement.

**Purpose:** To specify and implement permission-protected wishlist add/list/remove operations.

**Original prompt excerpts:** “Specify a product wishlist feature for the current Backend-SWE project…”; “Use PostgreSQL \`INSERT ... ON CONFLICT DO NOTHING\` for duplicate wishlist additions…”; “Do not introduce pessimistic locking for this operation…”

**AI Output Summary:** Generated specs/004-product-wishlist artifacts, a V10 migration, wishlist implementation and regression tests.

**Human Contribution/Review:** I answered the specification questions and resolved analysis findings, selecting conflict-ignore insertion and duplicate additions as successful no-ops. The test results above are Codex-reported verification, not an independent manual test run by me.

**Status:** The wishlist work was local and uncommitted on feature/wishlist when checked; no merge into main is claimed.

### **Member 3: Nguyen Cong Kien**

#### Record 1: Frontend Routing Setup and Page Structure 

**Tool Name:** Claude (Anthropic)

**Purpose:** To plan and verify the frontend routing setup for the e-commerce web application, including which pages the app needs, how to separate customer, admin, and authentication layouts, and how to organize the `src/pages/` folder under the team’s CONVENTIONS.md.

**Prompts Provided:** Questions on whether `App.jsx` is the right place for routing and whether all pages must be defined first; requests to review my proposed page list and route table; a question on what separate customer and admin “shells” mean in practice; a question on whether each page should get its own folder with a JSX and CSS file;

**AI Output Summary:** Explained that a route maps to a page rather than to a feature, so items such as product comparison, reviews and the chatbot are not necessarily pages. Described the customer, admin and auth layouts as separate wrapper components rendering `<Outlet />`. Pointed out a missing `/>` on the checkout route and inconsistent naming (`/product` vs `/products`, `/profile/order` vs `/profile/orders`). Noted that the payment step should be an order-result page rather than a payment form when a third-party gateway is used, and that reset-password, order detail and 404 pages were missing. Advised that pages should be flat files in `src/pages/` following CONVENTIONS.md. 

**Human Verification/Modifications:** I wrote the page list and route table myself and applied the suggested fixes (plural route names, `Page` suffix on component names, closing tag). I grouped the page files into `Admin`, `Auth` and `Customer` subfolders instead of keeping them flat, as I judged this clearer for the team. I located the blank-page cause by inspecting the page and found the files were empty, then added placeholders. The `/admin/product/:id` route still needs renaming to the plural form, and the order-result, order-detail and 404 pages, route protection and the temporary admin switch button in `CustomerLayout` were deferred to later work and not implemented yet.

#### Record 2: Frontend API Client Layer and Authentication Integration  

**Tool Name:** Claude (Anthropic)

**Purpose:** To understand and implement the frontend API client layer for the e-commerce web app, including token handling for the backend authentication and catalogue APIs. 

**Prompts Provided:** Asked what an API client layer is and how it differs from endpoint functions. Supplied the backend OpenAPI specs (authentication/users/addresses and product catalogue) and asked what to change in token handling and route-based behavior, and whether the specs were enough to build authentication and catalogue code in `/src/api`. Asked whether `client.js` needed changes, where `refreshSession` should live, and whether `auth.js` and catalogue files belonged in the API layer task. Then asked Claude to write the files. 

**AI Output Summary:** Explained the split between the generic client and endpoint files, and proposed a folder structure. From the specs, it is identified that the access token comes in the Authorization response header, that refresh tokens are single-use (so refreshes must not run in parallel), and that PATCH is blocked by CORS. Listed gaps in the backend contract (no password recovery, no role information, no search/filter, no price in the product list, signup accepting only username and password). Generated .env.example, `src/api/tokenStore.js`, `src/api/client.js` (ApiError with fieldErrors, auth option, shared refresh with a cross-tab lock, one retry on 401, auth-failure callback) and `src/api/auth.js` (register, login, logout, changePassword). Ran a mock-backend test script covering login, parallel refresh, reload, public requests, error parsing, network errors and failed refresh.

**Human Verification/Modifications:** I cross-checked the AI's explanations of token handling (refresh token rotation, CORS and the Authorization header) against other online sources, and asked another team member to review the generated code before using it. I did not run the code against the real backend, thus integration with the real API remains to be verified.

 **Member 4: Gia**

#### **Record 1: AI Project Constitution and Spec Kit Setup**

**Tool Name:** ChatGPT, OpenAI Codex

**Purpose:** To initialize Spec Kit and establish engineering principles for the AI repository.

**Prompts Provided:** Requests to create and refine constitution.md, define AI service boundaries, Backend integration, security, and testing standards.

**AI Output Summary:** Generated the AI project constitution and suggested improvements to architecture and development rules.

**Human Verification/Modifications:** I reviewed and refined the constitution to align with the project's architecture and requirements.

#### **Record 2: Product Dataset Preparation and Normalization**

**Tool Name:** ChatGPT, OpenAI Codex

**Purpose:** To prepare and normalize approximately 10,000 products for the e-commerce system.

**Prompts Provided:** Requests to process product data, normalize specifications, map categories, generate prices, and validate data quality.

**AI Output Summary:** Generated processing scripts, normalized datasets, category mappings, pricing policies, and validation reports.

**Human Verification/Modifications:** I reviewed the outputs, checked data consistency, and refined the normalization requirements while preserving the original dataset.

#### **Record 3: Product Catalog Import and Image Integration**

**Tool Name:** ChatGPT, OpenAI Codex

**Purpose:** To prepare product data and real images for Backend integration.

**Prompts Provided:** Requests to analyze Backend database structures, develop import utilities, process product images, and implement validation tests.

**AI Output Summary:** Generated import preparation scripts, image processing utilities, local preview functionality, and automated tests.

**Human Verification/Modifications:** I checked Backend compatibility, reviewed import and image handling behavior, and validated the generated scripts and tests.

#### **Record 4: Dataset Distribution and Docker Planning**

**Tool Name:** ChatGPT, OpenAI Codex

**Purpose:** To plan a reproducible Product Catalog setup for team members.

**Prompts Provided:** Requests to evaluate GitHub and Docker distribution, estimate storage requirements, and reduce the dataset to approximately 1,500 diverse products.

**AI Output Summary:** Proposed data distribution approaches and a workflow for downloading images and importing product data locally.

**Human Verification/Modifications:** I evaluated storage costs, setup complexity, and product diversity. Docker-based distribution remained in the planning stage.

### **Member 5: Le Duc Thinh**

#### Record 1: Vision Document Drafting and Requirements Review

Tool Name: ChatGPT (OpenAI)  
Related discussion date: 30 October 2026 — Vision Document review and template alignment. Exact AI access hour: not verified.  
Purpose: To support drafting and reviewing the Vision Document for the electronics e-commerce platform, especially the scope, stakeholder needs, and AI-supported shopping capabilities.  
Prompts Provided: Supplied the project proposal, course template, and team decisions; requested structured drafts for the Vision sections, then asked for revisions to improve clarity, consistency, and alignment with the agreed project scope.  
AI Output Summary: Proposed section drafts, reorganized descriptions of business needs and product capabilities, and identified wording that was ambiguous or inconsistent across the proposal and Vision.  
Human Verification/Modifications: I checked the drafts against the course template and team requirements, adjusted the feature scope and terminology, and coordinated the document review with teammates. The generated text was treated as a starting point rather than an automatically approved requirement.

#### Record 2: AI and LLM Service Foundation

Tool Name: ChatGPT (OpenAI), with AI coding-agent assistance where applicable  
Related discussion date: 29 October 2026 — AI service environment and configuration discussion. Exact AI access hour: not verified.  
Purpose: To plan and support the initial setup of the AI/LLM component and its communication with the Backend services.  
Prompts Provided: Requested help breaking down the AI service setup, environment configuration, service/API boundaries, development workflow, and integration tasks into implementable steps.  
AI Output Summary: Suggested an implementation sequence, configuration guidance, API integration considerations, and task-level instructions for the AI service foundation.  
Human Verification/Modifications: I adapted the suggestions to the existing AI repository and Backend contracts, reviewed configuration choices, and separated foundational setup from features that still required implementation and testing. Sprint reporting recorded AI/LLM setup and Backend API progress, not a completed end-to-end shopping assistant.

#### Record 3: AI Repository Tasks and Spec Kit Planning

Tool Name: ChatGPT (OpenAI)  
Related discussion date: 29 October 2026 — AI team Jira tasks and Spec Kit workflow. Exact AI access hour: not verified.  
Purpose: To clarify AI-team Jira work items and prepare manageable, reviewable tasks using the team's Git and Spec Kit conventions.  
Prompts Provided: Asked for help interpreting assigned Jira tasks, organizing branch-by-branch implementation prompts for an AI coding agent, and reviewing the roles of constitution.md, specifications, plans, tasks, and review steps in the Spec Kit workflow.  
AI Output Summary: Produced suggested task breakdowns, branch and Pull Request workflows, and review checkpoints for generated code and documentation; explained how specification artifacts should guide implementation.  
Human Verification/Modifications: I mapped the suggestions back to the team's Jira ownership and repository conventions, reviewed the scope before applying changes, and retained human review and testing as requirements before marking a task complete.

#### Record 4: AI Chatbox and Automatic Assistant UI Design Planning

Tool Name: ChatGPT (OpenAI)  
Related discussion date: 28 October 2026 — AI Chatbox and Automatic Assistant UI planning. Exact AI access hour: not verified.  
Purpose: To explore the user experience of the AI shopping assistant and prepare a UI design workflow consistent with the storefront and existing team designs.  
Prompts Provided: Described the proposed AI Chatbox and Automatic Assistant features, referenced existing login, home and cart designs, and asked for a workflow combining prompt development, UI generation, Figma refinement, and design consistency checks.  
AI Output Summary: Suggested interaction flows, chatbox states, confirmation steps for shopping actions, and a process for iterating UI concepts while maintaining consistency with the existing design system.  
Human Verification/Modifications: I selected the concepts relevant to our project, prioritized consistency with the shared components and existing screens, and kept the UI implementation and final design review as pending work at the Sprint 2 reporting checkpoint.

## 3\. AI Usage Notes – Access Metadata and Evidence Register (Pending Verification)

This section supplements the detailed records above. The “Prompts Provided” entries are summaries, not verified verbatim transcripts. For each record, the contributor must confirm the AI model/version and platform, actual access date and time, original prompt(s), and a chat-history link or genuine screenshot. Where code or outputs were produced, supporting commits, tests, or revised artifacts should be linked if available. Do not invent missing details or claim unperformed verification.  
Member 1 – Phan Thi Thanh Huyen: R1 User Flow Specification \[access time / platform / original prompt / evidence: pending\]; R2 User Flow Review \[model / access time / platform / original prompt / evidence: pending\]; R3 UI Wireframes \[model / access time / platform / original prompt / evidence: pending\]. R1 currently lists Gemini 3.8 Flash; contributor should confirm that this was the actual selected model.  
Member 2 – Trinh Van Thanh: The five records above cover only Backend-SWE Spec Kit command workflows in Codex for Visual Studio Code. They include recorded access times, model/platform, original prompt excerpts, AI outputs and contributor decisions. Codex Desktop and unrelated conversations are excluded. No separate screenshot or chat-history attachment is supplied; this scoped summary alone does not fulfill the guideline’s evidence requirement or the sprint-wide requirement to disclose all AI usage.  
Member 3 – Nguyen Cong Kien: R1 Frontend Routing \[Claude model / platform / time / original prompt / evidence: pending\]; R2 API Client and Authentication \[same: pending\].  
Member 4 – Nguyen Hoang Gia: R1 AI Constitution \[ChatGPT/Codex model(s) / platform(s) / time(s) / prompt / evidence: pending\]; R2 Product Dataset \[same: pending\]; R3 Catalog Import and Images \[same: pending\]; R4 Dataset Distribution \[same: pending\].  
Member 5 – Le Duc Thinh: R1 Vision Document \[ChatGPT model / platform / time / original prompt / evidence: pending\]; R2 AI/LLM Foundation \[tool/model actually used / platform / time / original prompt / evidence: pending\]; R3 AI Repository and Spec Kit \[same: pending\]; R4 Chatbox UI Planning \[same: pending\].  
Submission check: Each contributor should verify their Human Verification/Modifications statements against actual work, attach or link source evidence, and fill the pending fields before the report is treated as fully compliant. This supplementary register is not itself evidence of the underlying AI sessions.  

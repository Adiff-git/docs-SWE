# F - AI Usage Report and Weekly Report (5 points)

**Performed by:** All  
**Reviewer by:** Huyền  

---

## 1. AI Usage Declaration

### Member: Trinh Van Thanh
- **Did this member use AI tools during the PA3 work period?** Yes.
- **Scope:** Backend-SWE Spec Kit specification-to-implementation workflows and their direct implementation/validation follow-ups after the work already disclosed in PA2. Earlier PA2 records are not repeated. General knowledge questions, architecture/course discussions, standalone Git/CI/submission operations and other projects are excluded.

### Member: Phan Thi Thanh Huyen
- **Did this member use AI tools during the PA3 work period?** Yes.
- **Scope:** AI tools performed code generation, debugging and implementation tasks. My primary contributions involved defining requirements, directing workflows, reviewing proposed changes and evaluating the resulting functionality.

### Member: Lê Đức Thịnh
- **Did this member use AI tools during the PA3 work period?** Yes.
- **Scope:** ChatGPT supported Sprint 3 AI-task planning, PA3 use-case specification drafting, Vision revision and traceability, weekly-report preparation, and UI prototype consistency review. AI contributions were drafting and analysis assistance; unverified meetings, screenshots, implemented features, tests, or reviewer approvals are not claimed.

### Member: Nguyễn Hoàng Gia
- **Did this member use AI tools during the PA3 work period?** Yes.
- **Scope:** ChatGPT supported PA3 planning, Sprint 3 task allocation, technical decisions and prompt drafting. OpenAI Codex was used for Backend-SWE Search & Filter, User Behavior Tracking, and cross-repository AI Recommendation implementation, testing and Git workflows; ChatGPT also helped diagnose CI failures. I defined scope and acceptance criteria, reviewed AI reports and requested revisions. Codex-reported tests are not claimed as personally executed; frontend end-to-end and production deployment are not claimed.

### Member: Nguyễn Công Kiên
- **Did this member use AI tools during the PA3 work period?** Yes.
- **Scope:** Claude supported Sprint 3 use-case modelling: drafting Mermaid use-case diagrams (flowchart notation) for several functional groups, and suggesting where to use include, extend and generalization, abstract actors and use cases, and merged use cases. I supplied the requirement tables and the vision document, decided which suggestions to adopt, and requested revisions each time the tables changed. Claude's diagrams were not rendered or validated by Claude; Mermaid rendering, UC numbering and coverage of all functional requirements are checked by the team, and relationships are subject to instructor feedback.

*Did this member use AI tools during the PA3 work period? No.*  
*Scope: N/A.*

---

## 2. Detailed AI Usage Logs

### Member: Trinh Van Thanh
**Tool/model/platform:** OpenAI Codex desktop app; GPT-6.1 Sol (gpt-6.1-sol)

#### Record 1: Email Verification and Google OAuth2 — Specification and Security Review
- **Access log:** 4 November 2026, 23:01–23:49; 5 November 2026, 00:07–00:47 (UTC+7).
- **Purpose:** To define the email-verification, Google login/linking and first-password flows before implementing `specs/006-email-google-auth`.
- **Original prompt excerpts:**
  - “Review and clarify the combined Email Verification and Google OAuth2 Login feature against the current Backend-SWE repository.”
  - “Google’s verified email. Existing accounts would still require explicit Connect Google linking.”
  - “Resolve all findings I1, U1, I2, U2 and D1 directly in the existing specification artifacts.”
- **AI Output Summary:** Generated and revised the specification, plan, data model, HTTP contracts, checklists and task list. Analysis exposed conflicting registration rules, incomplete linking-proof tasks and browser cookie races; the revised design used pending registration, explicit account linking and response-order-safe browser correlation. The task list reached 71 tasks. This record concerns design work, not executed application tests.
- **Human Contribution/Review:** I supplied the feature requirements; chose email/password registration with an email-derived username, six-digit verification codes, one linked Google identity and revoke-all session behavior for first-password setup. I requested pending-only registration and direct corrections across artifacts rather than accepting inconsistent amendments.
- **Evidence:** Codex history: “Clarify email verification and OAuth2”, 4–5 November 2026; `specs/006-email-google-auth/{spec.md,plan.md,data-model.md,tasks.md,contracts/http.md}`.

#### Record 2: Email/Google Authentication — Implementation and Rate-Limit Policy Change
- **Access log:** 5 November 2026, 00:48–01:36 and 08:18–10:00; policy revision at 10:12, resumed 13:22–13:24 (UTC+7).
- **Purpose:** To implement the approved authentication flows, then revise the implementation after deciding not to apply rate limits.
- **Original prompt excerpts:**
  - “$speckit-implement”
  - “Approve mail dependency”
  - “continue the current job which was interrupted because of reaching usage limit”
- **AI Output Summary:** Implemented verification/challenge delivery, pending registration, Google login and explicit linking, password setup, persistence, cleanup and tests. Codex initially reported 283 unit/MVC and 311 integration tests passed, with 70/71 tasks complete; the human walkthrough/production acceptance task T070 remained open. After the policy change, Codex removed quotas, resend cooldowns, failed-attempt limits and 429/Retry-After behavior while retaining authentication, expiry and single-use checks. It reported a clean 579-test build and six additional regressions.
- **Human Contribution/Review:** I approved the mail dependency, requested continuation after usage-limit interruptions and explicitly changed the product policy to remove rate limits. These are documented human decisions; the code generation and automated test runs were performed by Codex. The test counts describe separate historical runs and are not combined into a new total.
- **Evidence:** Codex history: “Clarify email verification and OAuth2”, 5 November 2026; `specs/006-email-google-auth/tasks.md` and `quickstart.md`; authentication code and migration history.

#### Record 3: Shopping Cart — Specification, Planning and Analysis Remediation
- **Access log:** 11 November 2026, 16:41–18:47 (UTC+7); the storage implementation within this interval is disclosed separately in Record 5.
- **Purpose:** To adapt cart behavior to Backend-SWE and resolve scope, API, DTO and transaction-contract issues before implementation.
- **Original prompt excerpts:**
  - “Specify a shopping cart feature for the existing Backend-SWE project.”
  - “Q1: A, Q2: A: 1000 and explain more about Q3”
  - “Q3: approve D1–D8”
  - “I1: B, C1: prioritize `401/403` instead of `405/415`, give me detail information about U1,U2”
  - “Resolve C2 by moving CartReadSeed, PreparedCart, and AddCartResult to cart/dto/response as required by Constitution III.”
- **AI Output Summary:** Generated `specs/007-shopping-cart` artifacts and 46 dependency-ordered tasks. Revisions staged service/DTO introductions by story, documented security-first errors, resource-free image preparation and timeout-before-lock behavior, and placed the prepared/result DTOs under `cart/dto/response` as immutable Lombok classes. The final analysis reported no actionable design findings; task coverage at this stage was not implementation completion.
- **Human Contribution/Review:** I deferred inventory/stock validation, set the per-variant quantity maximum to 1,000, approved D1–D8 and selected the error-precedence and incremental-service options. I explicitly requested the DTO correction and prohibited cart implementation until the design work was resolved.
- **Evidence:** Codex history: “Specify shopping cart feature”, 11 November 2026; `specs/007-shopping-cart/{spec.md,plan.md,tasks.md,data-model.md,contracts/api.md,contracts/internal-services.md}`.

#### Record 4: Shopping Cart — Full Backend Implementation and Verification
- **Access log:** 11 November 2026, 23:23 to 12 November 2026, 00:13 (UTC+7).
- **Purpose:** To execute the approved 46-task cart plan after the analysis findings were resolved.
- **Original prompt excerpts:**
  - “$speckit-implement” (invoked after the final speckit-analyze result).
- **AI Output Summary:** Implemented the authenticated persistent cart, add/update/variant switch/merge/remove operations, item/bulk selection, exact VND totals, unavailable-item snapshots, permission grants, migration and tests. Codex reported 46/46 tasks complete and a full verify result of 342 unit/controller plus 337 integration tests, with no failures or skips. The recorded checks included real HTTP, database constraints, signing rollback, lock contention and complete 105-row reads. This was backend/database delivery; it did not establish completion of the team’s frontend, demo video or production deployment.
- **Human Contribution/Review:** I invoked implementation only after setting the business policies and requesting the earlier design corrections. The history supports my requirements/approval role; it does not establish that I manually authored the generated code or independently reran every test. The 679-test result is attributed to Codex’s session verification, not to a personal manual test claim.
- **Evidence:** Codex history: “Specify shopping cart feature”, 11–12 November 2026; `specs/007-shopping-cart/tasks.md` and `quickstart.md`; the session’s `demo/target/cart-verify-complete.log` and Surefire/Failsafe reports.

---

### Member: Phan Thi Thanh Huyen
**Tool/model/platform:** OpenAI Codex, ChatGPT and Google Gemini

#### Record 1: Authentication UI, Figma Adaptation and Session Foundation
- **Access log:** 3 November 2026, 18:48–19:30 (UTC+7).
- **Purpose:** To implement the authentication UI and establish frontend validation and session handling.
- **Original prompt excerpts:**
  - “Implement the login and signup pages from the Figma design.”
  - “Create reusable form components and support session persistence.”
- **AI Output Summary:** Added reusable authentication components, validation, login/signup integration, session persistence and tests.
- **Human Contribution/Review:** I supplied the design and requirements, reviewed the UI adaptation and confirmed the expected validation and session behavior.
- **Evidence:** Commits `29bfc92`–`4454571`; `src/features/customer/auth/`; `src/api/`; `tests/`.

#### Record 2: Email Authentication and Google OAuth2 — Frontend Implementation
- **Access log:** 4 November 2026, 19:51–20:15; 5 November 2026, 13:06–23:12 (UTC+7).
- **Purpose:** To implement email authentication, Google OAuth2 and customer account management.
- **Original prompt excerpts:**
  - “Update login and signup to use email and add Google login.”
  - “Implement Google OAuth with PKCE and connect the account screens to the backend contract.”
- **AI Output Summary:** Implemented email login/signup, Google OAuth PKCE, protected routes, session restoration, profile management, address CRUD and mock APIs.
- **Human Contribution/Review:** I defined the authentication and account scope and confirmed the required redirects, persistence and profile behavior.
- **Evidence:** Commits `6bdebd1`–`340ae18`, `82db894`, `216fd55`–`175dc4b`; `src/api/`; `src/features/customer/`.

#### Record 3: Real Backend Integration — Docker Environment and End-to-End Verification
- **Access log:** 9 November 2026, 19:31–23:58; 10 November 2026, 00:06–13:32 (UTC+7).
- **Purpose:** To verify the frontend against the real backend and its supporting services.
- **Original prompt excerpts:**
  - “Pull the latest backend and test the frontend against the complete Docker stack.”
  - “Verify OTP, sessions, profiles, avatars, addresses and Google OAuth, then conduct an independent review.”
- **AI Output Summary:** Started five backend services and verified 12 API groups and 14 browser scenarios. Fixed avatar and Google-error handling, documented a backend storage defect and passed lint, build and 36 tests.
- **Human Contribution/Review:** I approved the integration plan, backend pull and Docker installation, supplied OAuth configuration and deferred the backend storage issue.
- **Evidence:** `tasks/backend-integration/`; `tasks/progress.md`; commits `e2c21bf`, `175dc4b`, `555ed91`; backend revision `d4fec8f`.

#### Record 4: Signup Email Verification — OTP Screen and Race-Condition Hardening
- **Access log:** 13 November 2026, 20:04–20:26 (UTC+7).
- **Purpose:** To create a dedicated OTP screen and prevent stale requests from affecting replacement signup sessions.
- **Original prompt excerpts:**
  - “Move OTP confirmation to a dedicated verification page.”
  - “Test cancellation, resend and delayed responses so an old signup cannot authenticate or modify a new one.”
- **AI Output Summary:** Added the verification route, OTP state machine and session cleanup. Fixed token-commit and navigation races; 10 browser scenarios, 38 tests, lint and build passed.
- **Human Contribution/Review:** I specified the verification flow and edge cases and required independent review before completion.
- **Evidence:** `src/features/customer/auth/SignupVerifyScreen.jsx`; `useSignupVerify.js`; tests `signupVerify.test.js`.

---

### Member: Lê Đức Thịnh
**Tool/model/platform:** OpenAI ChatGPT (web); exact model/version not retained in the source conversations.

#### Record 1: Sprint 3 AI Workstream Planning and Task Decomposition
- **Access log:** 9–13 November 2026 (UTC+7; exact session times not retained).
- **Purpose:** To clarify the AI team's Sprint 3 responsibilities and translate the agreed Recommendation System (RS) and AI Shopping Agent work into trackable tasks.
- **Original prompt excerpts:**
  - “tuần này bên AI t làm task là hoàn thiện RS với tích hợp RS nha”
  - “Từ các task này bạn có thể chuyên thành các Jira ticket task ko”
- **AI Output Summary:** Helped organize RS completion/integration and Shopping Agent development into deliverables, dependencies and task descriptions. The team register and PA3 weekly-report draft separately list Agent tools, Chat API and scenario validation as Thịnh's planned responsibilities; they do not establish implementation completion.
- **Human Contribution/Review:** I supplied the teammate's RS direction, clarified that Gia and I formed the AI workstream, and determined which responsibilities belonged to each member. Jira assignments/statuses must be confirmed from the board before submission.
- **Evidence:** Sprint 3 team task register; PA3 > Weekly Report PA3 (`SWE-165`, `SWE-166`, `SWE-167` listed as assigned/to-do at the 13 November checkpoint); related 9 November ChatGPT conversation.

#### Record 2: PA3 Use-Case Specification Drafting and Coverage Review
- **Access log:** 13–14 November 2026 (UTC+7; exact session times not retained).
- **Purpose:** To organize and refine assigned use-case specifications for product management, order management, and the AI shopping assistant, using the team's existing requirements and peer specifications as reference.
- **Original prompt excerpt:**
  - “Sau đó dựa vào các UseCase Specification của Thành mà làm cho tôi các phần được giao à FG-06, FG-07, FG-10.”
- **AI Output Summary:** Assisted with structuring use-case coverage, actor identification, preconditions, basic and alternative flows, postconditions, and consistency checks. The working index covers FG-06 (`UC-030`–`UC-038`), FG-07 (`UC-039`–`UC-044`), and FG-10 (`UC-052`–`UC-059`). AI assistance does not by itself verify that every individual specification or prototype screenshot is complete.
- **Human Contribution/Review:** I selected the assigned functional groups, provided the team's reference material, and requested alignment with the actual frontend design. Final per-use-case coverage, prototype screenshots, and reviewer sign-off remained items to check.
- **Evidence:** PA3 > Use-Case Specification > Thịnh tab (FG-06, FG-07, FG-10 index); PA3 assignment and prototype requirements; related 13–14 November ChatGPT conversations.

#### Record 3: Detailed Vision Revision and Requirements Traceability
- **Access log:** 13 November 2026 (UTC+7; exact session times not retained).
- **Purpose:** To prepare the second-submission Vision revision while preserving the earlier PA2 document and identifying the changes required for PA3.
- **Original prompt excerpts:**
  - “Sau đó là làm phần Detailed Vision cần hoàn thiện”
  - “tập trung tab Vision. Dựa đúng trên các tính năng và vai trò thực tế trong Vision”
- **AI Output Summary:** Helped draft a Vision v1.4 change summary, clearer user environments and role boundaries, AI MVP scope and implementation boundaries, and a traceability check for FG-01–FG-10/`UC-001`–`UC-059`. Proposed workflow/diagram adjustments were checked conceptually against the requirements rather than presented as automatically approved.
- **Human Contribution/Review:** I directed the revision to retain the prior Vision, emphasized consistency with actual team features, and identified TA feedback, team approval and the shared `Changes.md` merge as pending verification.
- **Evidence:** PA3 > Vision (include `Changes.md`) tab, “PA3 VISION DELIVERABLE — VERSION 1.4 (13 NOV 2026)”; canonical Vision link and outstanding review checklist there.

#### Record 4: Weekly Report Drafting and Evidence-Risk Review
- **Access log:** 13–14 November 2026 (UTC+7; exact session times not retained).
- **Purpose:** To prepare the PA3 weekly report using the PA2 format and the latest team task/assignment information.
- **Original prompt excerpt:**
  - “Bạn hãy giúp tôi làm weekly report. Template lấy từ PA2 Weekly Report.”
- **AI Output Summary:** Assisted with organizing Sprint Planning, Scrum meeting and Sprint Review sections, owner/action summaries, Jira evidence requirements, risk items and submission checks. The report distinguishes draft/planned work from verified demonstrations and includes explicit placeholders for unconfirmed meeting records, screenshots, test evidence and reviewer decisions.
- **Human Contribution/Review:** I specified the PA2 template, assigned workstream and submission scope. Meeting attendance, decisions, Jira screenshots, demo links and reviewer approval require independent confirmation; AI-generated meeting minutes are not evidence that a meeting occurred.
- **Evidence:** PA3 > Weekly Report PA3 tab (evidence-status notes, planned owner matrix, Jira references and verification placeholders).

#### Record 5: UI Prototype and Frontend Design Consistency Consultation
- **Access log:** 14 November 2026 (UTC+7; exact session times not retained).
- **Purpose:** To clarify the PA3 UI prototype requirement and assess whether use-case screenshots should match the frontend team's Figma design.
- **Original prompt excerpts:**
  - “prototype có phải là UI đã được design lấy từ team frontend lúc design giao diện cho app ko”
  - “nếu tôi gửi bạn link figma frontend của nhóm tôi, bạn có thể sửa lại toàn bộ screenshot ở các file ko”
- **AI Output Summary:** Provided guidance on the difference between prototypes and implemented UI and the importance of keeping specification screenshots consistent with the team's design. This was consultation and planning; it did not establish that screenshots were already replaced.
- **Human Contribution/Review:** I identified a mismatch between current screenshots and the frontend design and shared the actual Figma reference. Screenshot updates and final visual verification remained pending.
- **Evidence:** 14 November ChatGPT conversation; frontend Figma reference supplied in that conversation.

---

### Member: Nguyễn Hoàng Gia
**Tool/model/platform:** OpenAI ChatGPT (web) and OpenAI Codex; exact model/version was not consistently retained.

#### Record 1: PA3 Project Planning, Sprint 3 Allocation and Documentation
- **Access log:** 3–14 November 2026 (UTC+7; exact session times not retained).
- **Purpose:** To revise the Chạm Tech PA3 Project Plan and organize Sprint 3 responsibilities using the PA2 structure and team task information.
- **Original prompt excerpts:**
  - “bạn hãy ghi lại trên docs”
  - “hãy sửa lại làm theo format của Project Plan ở PA2”
  - “bây giờ bạn hãy tổng hợp tất cả task thành một table task cho một sprint 3”
- **AI Output Summary:** ChatGPT assisted with Project Plan PA3 revisions, Sprint 3 task breakdown, responsibility tables and documentation formatting. The drafts were aligned with the earlier PA2 plan and evolving technical assignments; AI-generated plans are not evidence that every Jira ticket or planned task was completed.
- **Human Contribution/Review:** I provided the project name, assignments, Sprint 3 priorities, PA2 template references and the 7.5-hour-per-person weekly planning assumption. I requested corrections when the output used raw Markdown in Google Docs or differed from the team format.
- **Evidence:** PA3 > Project Plan PA3 and Task technical tabs; related ChatGPT planning conversations from November 2026.

#### Record 2: Product Search & Filter — Spec Kit, Scope Decisions and Local Acceptance
- **Access log:** November 2026 during PA3 (exact Codex session timestamps not retained).
- **Commands used:** Spec Kit specify/clarify/plan/tasks/analyze and subsequent Codex implementation, review, verification and Git-continuation prompts.
- **Purpose:** To deliver keyword and fuzzy search, relevance ranking, Category/Brand/Price/Specification filtering, sorting and pagination in Backend-SWE.
- **Original prompt excerpts:**
  - “bạn hãy gửi prompt để codex làm xong toàn bộ cho features này”
  - “Bạn có thể cắt giảm những cái gây cản trở ... mà không quá ảnh hướng đến tính năng”
  - “performance không cần quá khắt vì project của tôi chỉ tầm 1500 product thôi”
- **AI Output Summary:** Codex created and revised Search & Filter specification/evidence, then implemented US1–US4, Vietnamese normalization, safe identifier handling, variant-consistent filters and database migrations V16–V19. Its final local handoff reported 705 passing tests, valid OpenAPI, measured 1,500-product scenarios and 64 PASS / T059 DEFERRED / T063 BLOCKED. Codex also committed and merged the feature locally; this did not establish deployment readiness.
- **Human Contribution/Review:** I selected the MVP functionality, approved the bounded Vocabulary/Registry definitions, deferred unverified model ownership and unreliable specification facts, relaxed only the broad-keyword MVP latency budget after examining evidence, and directed safe commit/merge steps. Implementation and test execution were performed by Codex.
- **Evidence:** `Backend-SWE/specs/007-product-search-filter/evidence/{handoff.md,git-finalization-review.md}`; feature commit `067ba563`; local merge `c8b74357`; post-merge evidence `b0a22bc5`.

#### Record 3: User Behavior Tracking — Requirements and Backend Implementation
- **Access log:** November 2026 during PA3 (exact session times not retained).
- **Commands used:** Direct ChatGPT/Codex implementation prompts; Spec Kit was explicitly excluded.
- **Purpose:** To collect authenticated Customer behavioral signals for future Recommendation and basic administrator analytics.
- **Original prompt excerpts:**
  - “tiếp tục, bây giờ chúng ta sẽ làm features user behavior tracking”
  - “1. B 2. A 3. B mà không có Add to cart 4. A 5. B”
  - “Bạn hãy cho một prompt hoàn thành luôn, không cần dùng speckit”
- **AI Output Summary:** Codex reported implementing Product View, Search, Product Click and server-generated Wishlist Add/Remove events; JWT-derived ownership, idempotency, a 90-day retention policy, owner-scoped history and aggregated Admin analytics. It added Flyway V20 and reported 346 unit/MVC plus 384 integration tests passing, with local commit/merge. Browser event instrumentation and cross-user service authentication remained outside the verified scope.
- **Human Contribution/Review:** I restricted tracking to authenticated Customers, excluded Cart and Purchase, selected the 90-day retention period and authorized a secure AI-ready interface without direct AI database access. I reviewed the delivered results and accepted deferred frontend/service integration rather than asserting end-to-end completion.
- **Evidence:** `Backend-SWE/docs/{user-behavior-tracking.md,user-behavior-openapi.yaml,user-behavior-tracking-checkpoint.md}`; feature commit `2b089ce`; local merge `eafdc0b`.

#### Record 4: Hybrid AI Recommendation — Algorithm Selection and Two-Service Delivery
- **Access log:** 11–14 November 2026 (UTC+7; exact per-session times not retained).
- **Commands used:** Direct ChatGPT and Codex implementation/integration prompts, without Spec Kit.
- **Purpose:** To build personalized Customer recommendations, Guest general recommendations and Similar Products using Backend behavior data and a separate AI-SWE inference service.
- **Original prompt excerpts:**
  - “hãy qua bước AI Recommendation, chúng ta sẽ làm những gì tiếp theo, hãy thống nhất với nhau trước”
  - selected “1. B 2. B 3. B 4. A 5. B 6. A” for TF-IDF hybrid ranking, two writable repositories, Guest fallback, no reasons, Similar Products and frontend integration later.
- **AI Output Summary:** Codex reported implementing TF-IDF/cosine content similarity, behavior-weighted ranking, cold-start/popularity fallback and diversity in AI-SWE, with three secured Backend recommendation endpoints. Its local report recorded 255 AI tests and 752 Backend tests passing, plus real Spring Boot–FastAPI HTTP verification using 1,500 controlled products. Reported synthetic fixture consistency is not human-rated Recommendation accuracy; browser and production validation remained unverified.
- **Human Contribution/Review:** I chose the hybrid algorithm over LLM-only recommendations, established Backend ownership of authentication/publication and minimized AI payloads, requested a bounded MVP and reviewed the separate repositories' verification summaries. I did not claim that the model was trained on human-labeled relevance data.
- **Evidence:** `Backend-SWE/docs/{recommendation.md,recommendation-verification.md}`; `AI-SWE/docs/{recommendation.md,recommendation-verification.md}`; Backend feature `76aa0ef`, merge `713b76d`; AI feature `ac6a6ee`, merge `f57856d`.

#### Record 5: Recommendation GitHub Actions — Failure Diagnosis and CI Repair
- **Access log:** 11–14 November 2026 (UTC+7; exact session times not retained).
- **Purpose:** To investigate red GitHub checks and prepare a reviewable CI correction without changing Recommendation logic.
- **Original prompt excerpts:**
  - “hiện giwof dang fail à, bnaj hãy kiểm tra và fix lại”
  - “tôi muốn bạn soạn prompt để codex tạo nhánh rồi sửa”
  - “tôi muốn tạo pull request để teammate acp merge vào ấy”
- **AI Output Summary:** ChatGPT inspected actual GitHub Actions logs and found RecommendationHttpIT failed while starting uv because the workflow did not checkout AI-SWE or prepare Python/uv. Codex subsequently reported correcting `.github/workflows/test.yml` on a dedicated fix branch, validating YAML/actionlint and running 357 unit plus 395 integration tests locally with zero failures. At the reported checkpoint, no new GitHub Actions green run or teammate-approved merge had been verified.
- **Human Contribution/Review:** I requested a feature branch, preservation of the real two-service test and a Pull Request for teammate review rather than direct merge into `draft/version-1`. The local CI fix result is reported as Codex verification, not independent confirmation of GitHub CI success.
- **Evidence:** `Backend-SWE/.github/workflows/test.yml`; GitHub Actions failures on `76aa0ef` and `c25b577`; `fix/ci-ai-recommendation-integration-test` branch and Codex local verification report.

---

### Member: Nguyễn Công Kiên
**Tool/model/platform:** Anthropic Claude (Claude conversation)

#### Record 1: Use-Case Diagram Approach — Wishlist & Reviews, Abstract Actor
- **Access log:** 5 November 2026, 23:06–23:12 (UTC+7).
- **Purpose:** To agree a notation for Mermaid use-case diagrams (flowchart-based, since Mermaid has no native use-case type) and model the first functional group, Wishlist & Product Reviews, for the Sprint 3 use-case diagram deliverable.
- **Original prompt excerpts:**
  - "our lead allow us to group some feature into one use case, so like add/remove could be one?"
  - "about relationship, maybe an extension? rating extent review? what do you think?"
  - "as doing it like this can mean that use case require customer AND user, rahter than OR"
- **AI Output Summary:** Proposed sample Authentication and Profile Management diagrams to show the style, then drafted the Wishlist & Reviews diagram. Recommended keeping Add/Remove wishlist separate to match the UC table, making Write Review extend Rate Product, and removing the Administrator actor, which is not listed for this group. After the team raised the AND/OR ambiguity, redrew the diagram with an abstract User actor specialised by Guest and Customer. Mermaid code was not rendered or validated by Claude.
- **Human Contribution/Review:** I supplied the UC table, the lead's rule on merging use cases and the TA's advice on abstract classes. I questioned the extend direction and identified the AND/OR ambiguity with two actors on one use case, which led to the abstract actor. I asked for raw Mermaid code when the output did not display.
- **Evidence:** Claude conversation (Software Engineering Project), 5 November 2026, 23:06–23:12; Mermaid code blocks for Wishlist & Reviews.

#### Record 2: Use-Case Diagrams — AI Chatbot, Recommendations, AI Pet, Administration, Notifications (earlier numbering)
- **Access log:** 5 November 2026, 23:20–23:46 (UTC+7).
- **Purpose:** To model functional groups FG-08 to FG-12 of the first version of the requirements table.
- **Original prompt excerpts:**
  - "so maybe we could not included it? or what? if we keep then continued previous extend it i think?"
  - "maybe we could abstract uc-073/74?"
  - "i dont see anything worth mentioning? maybe uc085? it pretty much encapsulate all other action?"
  - "89-91, 92-96,104/105, 106/107, 97/98, 108/109 101 could also extend 100?"
  - "i feel like there othing much to do here?"
- **AI Output Summary:** Drafted five diagrams. Recommended keeping Start AI Conversation standalone with a precondition instead of include arrows, and Continue Previous Conversation extending it. For recommendations, used an abstract use case over the browsing-history and purchase-history variants. For AI Pet, made Give Natural Language Commands the parent of the search, filter, compare, cart and navigation use cases, and merged Confirm/Cancel. For Administration, agreed most of the team's merges, kept Promotions and Review Moderation separate, and flagged inconsistent handling of the list/detail pairs. For Notifications, used extend for Mark as Read and an abstract Receive Notifications. These diagrams were later superseded by renumbered tables (see Records 3 and 4).
- **Human Contribution/Review:** I supplied each UC table, proposed which use cases to merge (budget/usage recommendations, UC-073/074, Confirm/Cancel, the administration groupings), proposed the extension of UC-100 by UC-101, and judged that UC-085 or UC-077 should be the generalising use case for the AI Pet group. I decided which suggestions to adopt.
- **Evidence:** Claude conversation (Software Engineering Project), 5 November 2026, 23:20–23:46; table screenshots and Mermaid code blocks for each group.

#### Record 3: Use-Case Diagrams Revised After Requirements Condensed — AI Chatbot, Store Administration, Product and Order Management
- **Access log:** 13 November 2026, 08:37–08:47 (UTC+7).
- **Purpose:** To redraw the diagrams after the team condensed and renumbered the functional groups.
- **Original prompt excerpts:**
  - "so we condense a little bit now the ai and automation is just this can you adjust?"
  - "can 54 be seen as an extension of 52? or sometime we dont have to chat to get rec? or 58 with 52 as well"
  - "can 55/56 be seen as an extension of some generalize case? or is that too vague?"
  - "administration have also been condense significantly"
  - "yea, product and order management has its own section now"
- **AI Output Summary:** Redrew AI Chatbot & Shopping Automation, first with UC-059 extending UC-052, then at my request with UC-053 to UC-059 all extending UC-052. Advised against a shared parent for Compare Products and Manage Cart as too vague. Redrew Store Administration (five use cases, no relationships) and split Product Management and Order Management. In Order Management, Claude assumed Request Refund extends Cancel Order and Request Return and asked the team to check that against business rules. Claude also warned twice that UC numbers overlapped with earlier diagrams.
- **Human Contribution/Review:** I supplied the new UC tables. I proposed extending UC-052 from UC-054 and UC-058 and asked about generalising UC-055/056. I confirmed that Product and Order Management were now separate groups. I decided to apply to all of UC-053 to UC-059.
- **Evidence:** Claude conversation (Software Engineering Project), 13 November 2026, 08:37–08:47; Mermaid code blocks for AI Chatbot, Store Administration, Product Management and Order Management.

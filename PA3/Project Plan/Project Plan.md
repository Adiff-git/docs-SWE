# **Chạm Tech**

# **Software Development Plan (Small Project)**

# **Version 2.1**

# 

# **Revision History**

| Date | Version | Description | Author |
| ----- | ----- | ----- | ----- |
| 23 Oct 2026 | 1.0 | Initial draft | Nguyễn Công Kiên |
| 30 Oct 2026 | 1.5 | Refinement on Project Organization | Nguyễn Hoàng Gia |
| 31 Oct 2026 | 2.0 | Finalize details and correct typos | Nguyễn Công Kiên |
| 14 Nov 2026 | 2.1 | PA3 update: project name, PA dates, deliverables, ownership, Sprint 3 plan/tasks, effort units, release checkpoints, and risks; reconcile repository count. | Gia / Kiên — assigned PA3 owners; review pending |

# **Table of Contents**

[**1\.**	**Introduction 4**](#heading=h.nve10vhmdzid)

[*1.1*	*Purpose 4*](#heading=h.4avb79tllndm)

[*1.2*	*Scope 4*](#heading=h.dx9dnp8lufwh)

[*1.3*	*Overview 4*](#heading=h.7e2rnjbeezvi)

[**2\.**	**Project Overview 4**](#heading=h.tek0i8jifcjl)

[*2.1*	*Project Purpose, Scope, and Objectives 4*](#heading=h.mk3yd565s2s6)

[*2.2*	*Assumptions and Constraints 4*](#heading=h.mrhtiu72d8sn)

[*2.3*	*Project Deliverables 5*](#heading=h.wg3jxhw0hok)

[**3\.**	**Project Organization 5**](#heading=h.rjewiwxsm2p)

[*3.1*	*Organizational Structure 5*](#heading=h.r3ypg16f5t4c)

[*3.2*	*Roles and Responsibilities 5*](#heading=h.ij6jnay47wdz)

[**4\.**	**Management Process 5**](#heading=h.ap655meyxqje)

[*4.1*	*Project Estimates 5*](#heading=h.ryc79k7ecrs)

[*4.2*	*Project Plan 5*](#heading=h.x8ts2wxqmyyi)  
[4.2.1	Phase Plan 5](#heading=h.355ot2qs6pfr)  
[4.2.2	Iteration Objectives 6](#heading=h.8or7ztyiuawp)  
[4.2.3	Releases 6](#heading=h.b3kakhr42bzx)  
[4.2.4	Project Schedule 6](#heading=h.rbwq5fc0hnvx)  
[4.2.5	Project Resourcing 6](#heading=h.bwbl1kal56lc)

[*4.3*	*Project Monitoring and Control 6*](#heading=h.db9l4lqfk4io)  
[4.3.1	Requirements Management 6](#heading=h.nzr9y3p94ed9)  
[4.3.2	Reporting and Measurement 7](#heading=h.6msefeuua51u)  
[4.3.3	Risk Management 7](#heading=h.ikdvxh8hrjqc)  
[4.3.4	Configuration Management 7](#configuration-management)

# **Software Development Plan (Small Project)**

# 

1. # **Introduction**

*Performed by (assigned): Nguyễn Công Kiên \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*

1. ## **Purpose**

*Performed by (assigned): Nguyễn Công Kiên \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên (pending author sign-off)*  
The purpose of this Software Development Plan is to detail all the information needed to plan the development of the product effectively. This includes defining clear scope for the product, setting out reasonable objectives to achieve, and aligning multiple stakeholder visions of said product.

 This document benefits not only the project lead \- by providing a basis for planning and monitoring \- but also individual members, by providing more transparency about the process and mitigating risk of misalignment.

2. ## **Scope**

*Performed by (assigned): Nguyễn Công Kiên \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên* 

This Software Development Plan describes Chạm Tech’s development lifecycle, development priorities, key objectives, work allocation, quality controls, and related project-management processes.

3. ## **Overview**

*Performed by (assigned): Nguyễn Công Kiên \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*

   This Software Development Plan contains the following information:  
   Project Overview — detailing the goal of the project, what it set out to achieve, as well as the scope and limitation of said project. It will also clarify what will be the expected result of this development, and what assumptions will be made in said development.  
   Project Organization — describes the organizational structure of the project team, which include information such as the role of each member, the responsibility of each member and team and the expected workload during the development.  
   Project Plan — provides the comprehensive plan for the development process, details such as the estimated schedule, task assignments table and build plan will be provided in this section.

2. # **Project Overview**

   1. ## **Project Purpose, Scope, and Objectives**

*Performed by (assigned): Nguyễn Công Kiên / Nguyễn Hoàng Gia \| Reviewed by: Trịnh Văn Thành / Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*

   Chạm Tech is a single-vendor e-commerce web application for an electronics store, aimed mainly at customers who are not familiar with technical specifications or only have a basic level of tech literacy. We aim to develop a software solution for the task of online shopping, not only just to simplify the process, but also to be a helpful assistant during that process.  
   By the end of this project, we aim to deploy a fully functional web page, where customers can browse and search products, compare specifications, add items to a cart, check out, pay, and track their orders, and where store staff can manage products, stock, orders, promotions, and reviews. A key objective is our AI integration into the system, that recommends and compares products from everyday-language requests, helps with cart and checkout preparation, and answers order and stock questions, while the customer always confirms the order and payment.  
   The system is a desktop web application for modern browsers (Chrome and Firefox), requires an internet connection, and delegates card and e-wallet payments to an external payment gateway.

2. ## **Assumptions and Constraints**

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên* 

### **2.2.1 Assumptions**

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên (pending author sign-off)*  
The following assumptions are used to establish the initial project plan. These assumptions will be reviewed throughout the development process and updated if circumstances change.

| Assumption | Description |
| :---- | :---- |
| Team Member Availability | All five team members are assumed to be available to participate in development, testing, documentation, and Scrum activities according to the agreed project schedule. |
| Development Environment | Each team member is assumed to have access to a computer, an internet connection, and the necessary development tools to work on their assigned components. |
| Product Data Availability | Sufficient electronics product information, including product names, brands, prices, images, and technical specifications, is assumed to be available for building the product catalog, comparison features, and recommendation system. |
| API Integration | The Backend, Frontend, and AI components are assumed to be able to communicate through agreed API contracts. Required APIs are expected to become available according to the integration schedule. |
| AI Service Availability | The team assumes that suitable AI models or external LLM services will be accessible within the project's technical and financial limitations. |
| Testing Environment Availability | The team assumes that local development environments will support initial testing and that a remote testing environment can be made available before the planned integration and deployment tests. |

### **2.2.2 Constraints**

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên (pending author sign-off)*  
The project must operate within the following academic, resource, technical, and organizational constraints.

| Constraint | Description |
| :---- | :---- |
| Academic Schedule | The project must follow the university's assignment schedule. Development and documentation must be organized using Scrum, with the final Sprint supporting a demonstration of the completed application. |
| Team Size and Resources | The development team consists of five students who share responsibilities across Backend, Frontend, AI, testing, documentation, and project management. The project scope must remain achievable with the available workforce and time. |
| Technology Stack | The project uses React and Vite for the Frontend, Java Spring Boot and PostgreSQL for the Backend, and Python FastAPI for AI services. Significant technology changes require team agreement. |
| System Architecture | The project uses four GitHub repositories: Frontend-SWE, Backend-SWE, AI-SWE, and docs-SWE. The Backend is responsible for business logic, authentication, authorization, and business data management. The AI service communicates with the Backend through APIs rather than directly accessing the business database. |
| Platform Requirements | The application is developed as a web-based e-commerce platform targeting desktop users. It must support modern browsers, particularly Google Chrome and Mozilla Firefox, on the operating systems identified in the Project Proposal. |
| Security Requirements | The system must protect sensitive customer information and credentials. Authentication and authorization must be enforced for protected operations. AI-assisted shopping actions must respect user permissions, and final order submission must require explicit customer confirmation. |
| Development and Collaboration Standards | The team must follow the agreed Git workflow, including feature branches, Pull Requests, peer review, and testing before merging changes. Jira is used to manage tasks, assignments, and project progress. |
| Documentation and Submission Requirements | Project documentation must be written in English using Markdown. Required diagrams must use Mermaid, and submission documents must include their Markdown and PDF versions. Each document section must identify its performer, reviewer, and editor. |

### **2.2.3 Pending Decisions**

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên (pending author sign-off)*  
Some project conditions have not yet been finalized and may affect the assumptions and constraints above.

| ID | Pending Decision | Potential Impact |
| :---- | :---- | :---- |
| D1 | Deployment Platform and Budget | The team must confirm whether to use AWS or another hosting platform and determine the available infrastructure budget. |

These decisions will be incorporated into the project plan once they have been reviewed and approved by the team.

3. ## **Project Deliverables**

*Performed by (assigned): Nguyễn Hoàng Gia / Nguyễn Công Kiên \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên*  
The team delivers incremental software builds and assignment evidence over five PA-aligned iterations. The course dates below are taken from the shared schedule dated 14 November 2026\. Academic PA windows are distinguished from Jira Sprint dates, which are managed separately.

| Sprint / PA | Main deliverables | Academic milestone |
| :---- | :---- | :---- |
| Sprint 1 / PA1 | Project Proposal, Team Contract, Existing Apps Survey, tools/process setup, initial architecture. | PA1 released 03 Oct 2026; due 17 Oct 2026\. |
| Sprint 2 / PA2 | Initial Project Plan and Vision; Spec Kit training/artifacts; AI Usage and Weekly Reports; initial Backend, Frontend, and AI foundations. | PA2 released 17 Oct 2026; due 31 Oct 2026\. |
| Sprint 3 / PA3 | Revised Project Plan; revised Detailed Vision; one shared Changes.md; Mermaid Use-Case Model; complete Use-Case Specifications with UI prototype screenshots; one Spec Kit-driven functional group implemented end-to-end (Frontend \+ Backend \+ data persistence); narrated YouTube demo; source code and Spec Kit artifacts; AI Usage Report; Weekly Report and Jira screenshots; Git log; Markdown and PDF files. Technical targets include authentication, catalog/search/filter, cart, integration, and an AI recommendation/agent MVP where feasible. | PA3 released 31 Oct 2026; due 14 Nov 2026\. |
| Sprint 4 / PA4 | Architecture-focused assignment deliverables (requirements to be confirmed from the PA4 brief); continue checkout, payment, order management, administration, integration, and AI work as planned. | PA4 released 14 Nov 2026; due 28 Nov 2026\. |
| Sprint 5 / PA5 | Final assignment deliverables (requirements to be confirmed from the PA5 brief); full-system integration, regression evidence, deployment guidance, and final demonstration. | PA5 released 28 Nov 2026; submission deadline not stated in the supplied schedule. |

PA3 submission packaging: all report documents in English Markdown plus converted PDF, Mermaid diagrams, explicit performer/reviewer/editor attribution in each section, complete source code without generated dependencies, Spec Kit files, YouTube demo link, Jira progress screenshots, Git commit history, and a PA3-Group\[GroupId\].zip archive. The team must record actual changes to both the Project Plan and Vision in a single Changes.md, even if the TA provided no PA2 feedback.  
Four test builds are planned across Sprints 2–5. Their proposed scopes and checkpoints are detailed in Section 4.2.3; a target checkpoint does not establish that a release was delivered or tests passed.

3. # **Project Organization**

   1. ## **Organizational Structure**

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*

The team has five members. Gia is the Project Manager and coordinates the Sprint plan, assignments and integration work. Development is organized into Backend, Frontend and AI workstreams. Team members may contribute to more than one workstream.  
Backend — Lead: Trịnh Văn Thành; Member: Nguyễn Hoàng Gia.  
Frontend — Lead: Nguyễn Công Kiên; Members: Lê Đức Thịnh and Phan Thị Thanh Huyền.  
AI — Lead: Lê Đức Thịnh; Member: Nguyễn Hoàng Gia.  
Technical leads coordinate development and review changes in their areas. All members participate in Scrum meetings, documentation, self-testing and cross-testing.

2. ## **Roles and Responsibilities**

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên (pending author sign-off)*

| Person | Role | Main responsibilities |
| :---- | :---- | :---- |
| Nguyễn Hoàng Gia | Project Manager; Backend and AI member | Manage Sprint progress, assignments, and documents; build product catalog/data modules and recommendation baseline. |
| Trịnh Văn Thành | Backend Lead | Backend APIs, authentication/authorization, database, CI/CD and deployment. |
| Nguyễn Công Kiên | Frontend Lead | Frontend architecture, routing, customer interfaces, and Backend API integration. |
| Lê Đức Thịnh | AI Lead; Frontend member | AI Shopping Agent, LLM integration and AI–Backend contracts; support chatbox/UI work. |
| Phan Thị Thanh Huyền | Frontend member | Homepage and administrator interfaces; UI testing, documentation, and reporting. |

### **3.2.1 PA3 Documentation and Implementation Responsibility Matrix**

*Performed by (assigned): Nguyễn Hoàng Gia / Nguyễn Công Kiên \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên (pending author sign-off)*  
The following assignments reflect the group's PA3 tab; listed reviewers are assignments, not completed review approvals.

| PA3 deliverable | Primary performer(s) | Assigned reviewer(s) |
| :---- | :---- | :---- |
| A — Revised Project Plan | Gia, Kiên | Thành (Kiên also appears as a reviewer in the source table; independent review should be done by Thành). |
| B — Detailed Vision | Thịnh, Thành | Gia, Huyền |
| C — Use-Case Model (Mermaid) | Kiên, Huyền | Gia, Thịnh, Thành |
| D — Use-Case Specifications and UI Prototypes | Gia, Thịnh, Thành; Kiên owns FG-04 in the use-case allocation table | Kiên, Huyền (each author's work should be reviewed by someone other than themselves) |
| E — One functional group implemented with Spec Kit | Thành, Huyền | Kiên |
| F — AI Usage Report | All members provide logs; Huyền consolidates | Gia |
| F — Weekly Report, meetings and Jira evidence | Thịnh | Huyền |
| Shared Changes.md (A and B) | Gia, Thịnh | Kiên, Thành |

Use-case ownership (from the PA3 Use-Case Specification tab): Gia — FG-03, FG-08, FG-09; Thịnh — FG-06, FG-07, FG-10; Thành — FG-01, FG-02, FG-05; Kiên — FG-04. Every use case retained in the approved Mermaid diagrams requires its own specification and relevant prototype/screenshots. Changes to the use-case scope must be reconciled with Vision and the model before submission.  
Each Jira task should have one primary owner and a different teammate as reviewer. Members should report blockers early, maintain evidence, and cross-test integrated changes.

4. # **Management Process**

*Performed by (assigned): Nguyễn Hoàng Gia / Nguyễn Công Kiên \| Reviewed by: Trịnh Văn Thành / Nguyễn Công Kiên   \| Edited by (PA3 revision draft): Gia / Kiên* 

1. ## **Project Estimates**

*Performed by (assigned): Nguyễn Công Kiên / Nguyễn Hoàng Gia \| Reviewed by: Nguyễn Hoàng Gia / Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên (pending author sign-off)*  
Given the course timeline and available resources, the team retains the following estimates:  
\- Software size: The PA1 proposal identifies 10 functional groups and approximately 33 features. The current PA3 Use-Case Model lists 59 use cases; this count is subject to scope review and should not be interpreted as implemented features.  
\- Effort: The team consists of 5 members, each allocated approximately 7.5 hours per week for implementation, documentation, testing, and Scrum activities. This equals 37.5 team-hours per week and approximately 75 team-hours per two-week assignment window. Across the 11 scheduled course weeks (03 Oct–12 Dec 2026), the planning capacity is approximately 412.5 team-hours, assuming the same weekly allocation and full participation throughout. This is a planning estimate, not an actual time-tracking result.  
\- Time: The shared course schedule runs from 03 Oct to 12 Dec 2026 (11 listed weeks). PA3 is due on 14 Nov 2026; PA4 is due on 28 Nov 2026\. The supplied schedule does not specify the PA5 due date.  
\- Cost: Development costs are kept as low as possible.  
  \- Backend and API: Run locally during development at no hosting cost. Deployment platform (possibly AWS) and budget are still to be confirmed.  
  \- LLM API: Planned external LLM API budget is at most USD 1/month.  
  \- Email service: Use a free tier or console/log output during development for password-reset/restock messages.  
  \- Payment: Test payment scenarios in the payment gateway sandbox at no cost.  
Effort and budget estimates must be revisited if the scope, service charges, or available team time changes.

2. ## **Project Plan**

*Performed by (assigned): Nguyễn Hoàng Gia / Nguyễn Công Kiên \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên*

1. ### *Phase Plan*

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Nguyễn Công Kiên   \| Edited by (PA3 revision draft): Gia / Kiên*   
The current planning focus is Sprint 3 / PA3 (31 Oct–14 Nov 2026 academic window). The exact Jira Sprint 3 start/end timestamps must be verified in Jira; the academic dates should not be presented as verified Jira boundaries.  
Each Sprint has one Planning meeting, two Scrum meetings, and one Review. Each task has a primary owner and an independent reviewer; progress, risks, and carried-over work are reviewed at the end of the Sprint.  
Sprint 3 priorities:

- Revise PA2 Project Plan and Vision, record changes in one Changes.md, and obtain reviews  
- Align the Vision, Mermaid Use-Case Model, and all Use-Case Specifications; produce screenshots of UI prototypes, including screens used in alternative flows.  
- Implement and demonstrate one selected functional group end-to-end with Spec Kit (UI, API/business logic, database persistence). The selected group and proof of completion must be recorded; selection is currently to be confirmed in the available plan.  
- Continue Sprint 3 technical work on Backend, Frontend, and AI, prioritizing authenticated shopping/catalog functionality, integration, and a testable AI MVP where feasible.  
- Collect AI usage logs, meeting records, Jira screenshots, test evidence, Git logs, and demo artifacts for submission.

Five-Sprint roadmap:

| Sprint | Main objective | Milestone |
| :---- | :---- | :---- |
| 1 — PA1 | Initiation, proposal, and team setup | 03–17 Oct 2026 academic window |
| 2 — PA2 | Vision/Project Plan and implementation foundations | 17–31 Oct 2026 academic window |
| 3 — PA3 | Use cases, UI prototypes, and one full-stack Spec Kit implementation; continue core-shopping development | 31 Oct–14 Nov 2026 academic window |
| 4 — PA4 | Architecture assignment and extended commerce/AI integration | 14–28 Nov 2026 academic window |
| 5 — PA5 | Final integrated application, verification, and demonstration | From 28 Nov 2026; PA5 deadline not specified in supplied schedule |

2. ### *Iteration Objectives*

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Nguyễn Công Kiên   \| Edited by (PA3 revision draft): Gia / Kiên*  
Sprint 3 task assignments below are transcribed and consolidated from the team's PA3 and Task technical tabs. No Jira issue keys, completion states, or individual due dates are inferred when they were not provided. Detailed task status should remain authoritative in Jira.  
Table 2A — PA3 deliverable tasks:

| Work package | Owner(s) | Planned output / acceptance evidence |
| :---- | :---- | :---- |
| Revised Project Plan | Gia, Kiên | PA3 version, updated schedule, Sprint 3 tasks, and release/risk plan; Markdown \+ PDF; review evidence. |
| Revised Detailed Vision | Thịnh, Thành | Reviewed functional/non-functional requirements, competitors, user environment, traceability; Markdown \+ PDF. |
| Shared Changes.md | Gia, Thịnh | One file with separate Project Plan and Vision change sections, including no-TA-feedback status. |
| Use-Case Model | Kiên, Huyền | Mermaid diagrams aligned with the approved Vision. |
| Use-Case Specifications and prototypes | Gia (FG-03, FG-08, FG-09); Thịnh (FG-06, FG-07, FG-10); Thành (FG-01, FG-02, FG-05); Kiên (FG-04) | Detailed flows, alternative flows, postconditions and prototype screenshots for every retained use case. |
| Implement one functional group using Spec Kit | Thành, Huyền; reviewer Kiên | Approved feature scope, specs/plan/tasks, working FE \+ API/logic \+ DB persistence, source code and narrated YouTube demonstration. |
| AI Usage Report | All members; Huyền consolidates | Usage declarations and detailed log, reviewed by Gia. |
| Weekly Report / Jira progress | Thịnh; reviewer Huyền | Planning, Scrum, Review records and Jira assignment/progress screenshots. |
| Submission integration | Team; PM coordinates | Markdown \+ PDF files, Git log, source code and Spec Kit artifacts, YouTube link, and PA3-Group\[GroupId\].zip. |

Table 2B — Sprint 3 technical implementation tasks

| Workstream | Owner(s) | Sprint 3 planned tasks |
| :---- | :---- | :---- |
| Backend — API documentation and owned migrations/tests | Gia, Thành (each for owned modules) | Write OpenAPI documentation; add migrations; test modules. |
| Backend — customer/catalog/inventory/commerce | Gia | Implement User Behavior, Search & Filter, Inventory, Checkout, and Order modules. |
| Backend — media, review and cart | Thành | Implement Media, Review, and Cart modules; product image upload; import product data into database and object storage. |
| Backend — deployment and CI/CD | Thành (lead), Gia (support) | Deploy and configure CI/CD; preserve test and build evidence. |
| Frontend — shared customer UI, Week 1 | Kiên | Reusable components; customer header/footer; admin layout shell; product list, search and filter interfaces. |
| Frontend — auth/UI foundation, Week 1 | Huyền | Design tokens; login, sign-up, forgot/reset password; AuthContext and auth token handling. |
| Frontend — chat design/API, Week 1 | Thịnh | Finalize chatbox design and agree the chat API contract. |
| Frontend — pages/admin/cart, Week 2 | Kiên, Huyền (joint listing; confirm primary Jira owner per item) | Homepage; admin product list table and create/edit form. Kiên also plans cart and product-detail UI if time allows. |
| Frontend — chat prototype, Week 2 | Thịnh | Open/close chat widget; render chat message list and product cards using mock data. |
| AI — Recommendation baseline | Gia | Generate recommendations from real catalog metadata and available behavior; cold-start popularity/category fallback; Backend data/API integration and smoke/quality sanity checks. |
| AI — Shopping Agent MVP | Thịnh | Backend tools for search/product details/comparison; Agent Chat API with failure handling; validate at least three real-product consultation scenarios. |

Integration and acceptance: Verify Recommendation → Backend and Agent → Backend contracts, and Frontend connection where ready. Prioritize the actual PA3 full-stack group implementation over optional extensions. AI Sprint 3 MVP excludes advanced personalization and autonomous shopping automation. A task is marked Done only when its assigned reviewer accepts the implementation and supporting evidence. Incomplete tasks remain visible in Jira and are replanned for the following Sprint.

3. ### *Releases*

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên* 

The group plans four incremental testing builds. These are planned checkpoints, not claims of an already approved release. The shared academic calendar establishes PA3 on 14 Nov 2026 and PA4 on 28 Nov 2026; the final PA5 submission date is not specified. Thành leads CI/CD and deployment.  
Table 3 — Planned builds and release checkpoints

| Build | Target checkpoint | Planned scope | Proposed acceptance checkpoint |
| :---- | :---- | :---- | :---- |
| B1 — Foundation | Sprint 2 / 30 Oct 2026 Jira end (historical planning milestone) | Catalog/data, services startup, FE–BE foundations | Basic boot/API smoke and integration checks; acceptance not verified here. |
| B2 — PA3 / Core Shopping | 14 Nov 2026 (PA3 due) | Authentication, catalog/search/filter, cart, integration plus one full-stack Spec Kit functional group; supporting specs/prototypes/docs | Demonstrable selected feature with UI \+ API/logic \+ persistent data; relevant smoke/integration tests and source/spec artifacts; narrated video submitted. |
| B3 — PA4 / Architecture \+ Commerce Integration | 28 Nov 2026 (PA4 due) | PA4 architecture deliverables (subject to its brief); planned checkout/order/payment/admin/AI integration | Architecture documentation and recorded API/business-flow integration checks; review against PA4 brief before release. |
| B4 — PA5 / Final Demo | Sprint 5, following 28 Nov 2026; final academic due date not provided | Final integrated scope, deployment instructions, tests and presentation | E2E/regression/security evidence; retest critical bugs; narrated final demonstration. |

A build is accepted only after successful startup, the agreed tests, and documented results. Critical security, payment, stock, and order defects block release acceptance.  
Table 4 — Test levels and responsibility

| Testing activity | Primary responsibility |
| :---- | :---- |
| Unit/component | Each implementing developer |
| Backend API/contract | Gia, Thành, with FE/AI owners |
| Frontend/UI | Kiên, Huyền, Thịnh |
| AI recommendations/tools | Gia, Thịnh |
| Cross-service integration | Relevant Backend, Frontend and AI owners |
| E2E and regression | All five members |
| Preliminary performance/deployment | Gia, Thành; CI/CD lead Thành |

Development and basic tests run locally. A remote testing/deployment environment is used when available; do not claim it exists before it is confirmed. For each build, record tested versions, tests, defects, and retest results in Jira. Quality checks include Frontend npm run lint and npm run build, AI Ruff/pytest, and Backend Maven verification; actual passing status requires collected evidence.

4. ### *Project Schedule*

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Nguyễn Công Kiên   \| Edited by (PA3 revision draft): Gia / Kiên*   
The following dates come from the shared weekly course schedule. PA release/due dates are academic checkpoints and do not themselves verify Jira Sprint boundaries. The old PA2 Jira Sprint ran 22–30 Oct 2026\. Sprint 3 Jira start/end dates and individual task due dates should be confirmed in Jira.

| Academic week (Saturday) | PA release / due activity | Planning significance |
| :---- | :---- | :---- |
| 03 Oct 2026 (Week 1\) | PA1 released (Proposal) | Proposal kickoff |
| 17 Oct 2026 (Week 3\) | PA1 due; PA2 released (Vision) | PA1 submission / PA2 kickoff |
| 31 Oct 2026 (Week 5\) | PA2 due; PA3 released (Use case) | PA2 submission / PA3 kickoff |
| 14 Nov 2026 (Week 7\) | PA3 due; PA4 released (Architecture) | PA3 submission and PA4 kickoff |
| 28 Nov 2026 (Week 9\) | PA4 due; PA5 released (Final) | PA4 submission / PA5 kickoff |
| 12 Dec 2026 (Week 11\) | No due event stated on the supplied schedule | Week 11 listed; not a confirmed PA5 deadline |

Assignment-aligned roadmap

| Sprint / PA | Academic planning window | Deliverable milestone |
| :---- | :---- | :---- |
| Sprint 1 / PA1 | 03–17 Oct 2026 | Proposal and team setup |
| Sprint 2 / PA2 | 17–31 Oct 2026 | Project Plan, Vision, initial software foundation |
| Sprint 3 / PA3 | 31 Oct–14 Nov 2026 | Revised docs, complete use-case specs/prototypes, one Spec Kit full-stack functional group, demo and reports |
| Sprint 4 / PA4 | 14–28 Nov 2026 | Architecture assignment and continued integration |
| Sprint 5 / PA5 | Begins 28 Nov 2026; end date to confirm | Final integrated system and demonstration |

Gia coordinates Sprint 3 task owners and reviewers. All active issues should include a verified due date in Jira rather than a date inferred from the course calendar.

5. ### *Project Resourcing*

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*

 This is an undergrad course project, and therefore the number of staff/members is fixed (5), and it is expected to not be changed throughout the course.  
 The five members contribute across Backend, Frontend, and AI workstreams, with cross-team participation when needed. The planning allocation remains 7.5 hours per person per week (Section 4.1).

- Backend team \[2 members\]: both have prior experience with backend framework implementation and API gateway  
- Frontend team \[3 members\]: All three have some familiarity with HTML and CSS, and two have limited UI design skills. The project uses React; all three have limited experience with it.  
- AI team has \[2 members\]: both have worked together in developing an AI product in the past and integrated it into one of the prior course’s applications.

  3. ## **Project Monitoring and Control**

*Performed by (assigned): Nguyễn Hoàng Gia / Nguyễn Công Kiên \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*

1. ### *Requirements Management*

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*   
Requirements come from the Project Proposal and Vision Document. New requests are recorded in Jira, reviewed by the technical lead and approved by the team before work starts.  
Changes to shared APIs must be communicated to Backend, Frontend and AI owners. Approved changes are reflected in Jira and documentation.

2. ### *Reporting and Measurement*

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*   
Jira workflow: To Do → In Progress → Review → Done. Each issue should have an owner, reviewer, expected deliverable and due date. Members update their own issues.  
The team holds one Planning meeting, two Scrum meetings and one Review per Sprint. Gia monitors overall progress. Messenger is used for quick updates, Discord for meetings, and When2Meet for scheduling.  
Table 5\. Progress measures and reporting cadence

| Measure | Review frequency | Evidence |
| :---- | :---- | :---- |
| Task status / ownership / due dates | Ongoing; Scrum meetings | Jira board and issue history |
| Blockers and carryover | As discovered; Sprint Review | Jira blockers, Sprint Review notes |
| PR review and test checks | Every Pull Request | GitHub PR and CI logs |
| Integration and build readiness | At build checkpoints | Smoke/API/E2E evidence, build records |
| Documentation and training | Each PA submission | Markdown/PDF, reviewer metadata, screenshots/logs |

When a task is blocked, the owner informs the team. The lead helps resolve it; Gia reviews the schedule impact. Unfinished work moves to the next Sprint and Jira is updated.

3. ### *Risk Management* 

*Performed by (assigned): Nguyễn Công Kiên / Nguyễn Hoàng Gia \| Reviewed by: Nguyễn Hoàng Gia / Trịnh Văn Thành   \| Edited by (PA3 revision draft): Gia / Kiên*   
Risks are assessed at least once per iteration, ordered by their likely impact. The items below retain earlier project risks and add risks specific to PA3 submission and the shared course milestones.

| Priority | Risk and impact | Mitigation / contingency |
| :---- | :---- | :---- |
| High | Excessive use-case and UI prototype workload: 59 currently listed use cases could cause incomplete specifications, missing alternative flows, or absent screenshots, reducing PA3 evidence quality. | Freeze and validate the use-case scope against Vision; assign owners and reviewers per functional group; reuse shared prototype components; track specification and screenshot completion in Jira; avoid retaining unsupported optional use cases. |
| High | Misalignment among Vision, Mermaid Use-Case Model and specifications: renaming/removing use cases in one place creates inconsistent deliverables. | Maintain one approved use-case ID register and a Vision-to-use-case traceability matrix. Review changes across all three artifacts before export. |
| High | Full-stack Spec Kit group not demo-ready by PA3: Frontend, API, DB, and generated artifacts may not form a runnable feature. | Select a bounded functional group; verify an end-to-end acceptance scenario early; preserve source, Spec Kit files, test evidence, and narrated video before submission. |
| High | Missing Changes.md, performer/reviewer/editor attribution, PDF versions, Git log or demo link: required submission evidence may be omitted. | Use a PA3 packaging checklist; keep a single Changes.md with Plan/Vision sections; perform a cross-review of ZIP contents. |
| High | AI assistant scope exceeds schedule or available budget. | Prioritize browsing/checkout and a bounded real-catalog recommendation/agent MVP. Defer advanced personalization and autonomous shopping automation. |
| Medium | Schedule slippage due to late tasks or overloaded owners. | Check status during Scrum meetings; raise blockers early; balance tasks and carry unfinished work to the next Sprint transparently. |
| Medium | Frontend–Backend/AI integration breaks because API contracts change. | Agree on versioned contracts, announce changes, integrate incrementally, and use mocks only as temporary development support. |
| Medium | Third-party services (email, payment sandbox, infrastructure or LLM) fail or incur unexpected cost. | Use sandbox/free tiers, isolate providers behind modules, provide mock/log fallback, and cap AI API spending. |
| Low | Team member becomes unavailable or knowledge is concentrated. | Keep small tasks, documented implementation notes, peer review, and backup ownership. |
| Low | Defects discovered too late for demo. | Run checks on each build; reserve stabilization time; track fixes and retests in Jira. |

4. ### *Configuration Management* {#configuration-management}

*Performed by (assigned): Nguyễn Hoàng Gia \| Reviewed by: Phan Thị Thanh Huyền   \| Edited by (PA3 revision draft): Gia / Kiên*  
The team has four GitHub repositories: Frontend-SWE, Backend-SWE, docs-SWE and AI-SWE. Work is done on a separate branch and merged through a reviewed Pull Request. Do not push directly to main.  
Branch examples: feature/catalog-api, fix/login-validation, docs/project-plan. Commit example: feat: add catalog API. PRs should link to Jira and include test evidence.  
Documents use English Markdown, Mermaid diagrams where needed, and PDF for submission. Each section names its performer, reviewer and editor.  
Do not commit passwords, keys or .env files. Backend controls authentication and business data; AI accesses it through authorized APIs.  
If a build fails, the team checks logs, fixes or reverts the change, and tests again. Backup details are added when the server setup is finalized.  
Original PA2 document-section assignments (retained for traceability; PA3 assignments above take precedence):

| Section | Task / Content | Writer | Reviewer |
| :---- | :---- | :---- | :---- |
| 1\. Introduction | Purpose, Scope, Overview | Kiên | Huyền |
| 2\. Project Overview | Project Goals, Scope, Deliverables | Kiên | Huyền |
| 2\. Project Overview | Assumptions & Constraints | Gia | Thành |
| 3\. Project Organization | Team Structure & Roles | Gia | Huyền |
| 4.3.3 Risk Management | Project Risks & Mitigation Strategies | Kiên | Gia |
| 4.1 Project Estimates | Timeline & Resource Estimates | Kiên | Gia |
| 4\. Scrum Plan | Sprint Objectives, Tasks & Deliverables | Gia | Kiên |
| 4\. Project Schedule | Schedule, Milestones, Due Dates | Gia | Kiên |
| 4\. Build Plan | Testing Builds & Release Schedule | Gia | Thành |
| 4\. Monitoring & Control | Jira, Git Workflow, Progress Tracking | Gia | Huyền |


# **Weekly Scrum Meeting Minutes — Sprint 1**

**Performed by:** Phan Thi Thanh Huyen, Lê Đức Thịnh

**Reviewed by:** Nguyễn Hoàng Gia

---

## **Meeting 1: Sprint 1 Planning & Task Breakdown**

**Date & Time:** October 07, 2026 \| 08:30 PM – 10:30 PM  
**Location:** Online (Discord Server: [https\://discord.gg/ubBsx5Z5z](https://discord.gg/ubBsx5Z5z))

**Team members present:**

* Gia  
* Thành  
* Kiên  
* Huyền

**Team members absent:** Thịnh

### **1\. Agenda & Objective**

* Finalize sub-team divisions (Frontend, Backend, AI) and core responsibilities based on the Team Contract.  
* Brainstorm and establish the software project concept, target audience, and primary AI features.  
* Formulate the task breakdown for Project Assignment 1 (PA1) and assign initial Jira tickets with strict ownership.  
* Establish communication and repository workflows across teams.

### **2\. Discussion & Key Decisions**

#### **2.1 Sub-team Structuring & Technical Leadership**

Although all 5 members are required to contribute as full-stack engineers throughout the lifecycle, the team agreed on the primary focus areas and technical leads:

**Project Management & Tracking:**

Gia (PM): Monitors sprint progress, tracks blocked tasks, ensures synchronization between GitHub and Jira, and oversees project management documentation.

**Backend Sub-team:**

Thành (Lead) & Gia: Architecture design, RESTful APIs, database schema, server-side validation, and authentication/authorization.

**Frontend Sub-team:**

Kiên (Lead), Huyền, & Thịnh: UI/UX design, component library setup, client-side routing, state management, and API integration.

**AI Sub-team:**

Thịnh (Lead) & Gia: Research AI models/APIs, evaluate outputs, handle fallback cases, and lead technical documentation for AI components.

#### **2.2 App Idea Discussion & Scope Definition**

**Domain:** Consumer Electronics E-Commerce Web Application.

**Working Title:** To be finalized before PA2 submission (Working title candidate: TechZone E-Commerce / ElectroHub).

**Target Actors (2 Types):**

* **Customer / Buyer:** Search, compare specs, read reviews, checkout electronics, and interact with the AI assistant.  
* **Store Admin / Seller:** Manage product catalogs, inventory, orders, and review analytics.

**Proposed Functional Groups (Target: 8–10 distinct groups):**

1. Authentication & Authorization (Customer/Admin roles).  
2. Customer Profile & Address Book Management.  
3. Product Catalog & Advanced Technical Spec Filtering.  
4. Search & Multi-criteria Sorting.  
5. Shopping Cart & Checkout / Order Placement.  
6. Order Tracking & Order History.  
7. Ratings, Verified Customer Reviews & Q\&A.  
8. AI Product Consultant & Smart Specification Comparison.  
9. Inventory & Stock Management (Admin).  
10. Sales & Order Management Dashboard (Admin).

**Core AI Feature:**

**Initial Proposal:** An AI-powered Product Advisor & Comparison Assistant leveraging LLM and Vector Search to help users discover products, query natural language specs, and compare technical performance.

**Pivot Post-Feedback:** Following review and guidance from the instructor, the team decided to pivot the scope toward an **Automated Messaging & Task Automation Agent**

#### **2.3 Task Breakdown & Assignments for PA1**

All tasks were logged on Jira with explicit deadlines, creation dates, and assigned responsibilities:


###  

### 

| Jira ID | Task | Assignee |
| :---- | :---- | :---- |
| SWE-5 | Set up Jira and PA1 Sprint | Gia, Kiên |
| SWE-6 | Conduct and document sprint planning | Gia, Kiên |
| SWE-7 | Setup Github and document folders | Gia |
| SWE-9 | Set up the communication channel and meeting schedule | Gia |
| SWE-16 | Draft the team contract | Gia, Thịnh |
| SWE-14 | Survey CellphoneS features | Thành |
| SWE-26 | Write the summary for other apps' survey | Thành |
| SWE-10 | Define project scope and functional groups | Huyền |
| SWE-15 | Survey The Gioi Di Dong features | Kiên |
| SWE-11 | Write introduction and target user description | Thịnh |
| SWE-8 | Write git collaboration and review guidelines | Huyền |
| SWE-17 | Document Scrum meeting 1 | Huyền |
| SWE-22 | Verify development tools and AI coding account | Huyền |

### 

* Sub-teams and leads are officially operational under the agreed Team Contract rules.  
* The project scope for an Electronics E-Commerce Web Application with an AI Advisor was approved unanimously.  
* All PA1 deliverables were defined and distributed into Jira with clear ownership.  
* The team agreed to maintain continuous asynchronous updates on Discord and Messenger between scheduled meetings.

---

## **Meeting 2: PA1 Progress Review, Feedback Analysis & Scope Refinement**

**Date & Time:** October 10, 2026 \| 09:00 PM – 10:00 PM  
**Location:** Online (Discord Server: [https\://discord.gg/ubBsx5Z5z](https://discord.gg/ubBsx5Z5z))

**Team members present:**

* Gia  
* Thành  
* Kiên  
* Huyền  
* Thịnh

**Team members absent:** None

### **1\. Agenda & Objective**

* Review the completion status of tasks assigned during Meeting 1\.  
* Analyze instructor feedback and refine the project's concept and scope.  
* Clarify the objectives, capabilities, and limitations of the AI Shopping Assistant.  
* Assign new tasks and establish priorities for completing Project Assignment 1 (PA1).

### **2\. Discussion & Key Decisions**

#### **2.1 Progress Review — Meeting 1 Tasks**

All tasks assigned during Meeting 1 (SWE-01 to SWE-05) were still in progress.

The team reviewed the existing deliverables, including the Team Contract, GitHub repositories, existing application survey, project proposal, and development tool setup.

The team agreed to focus on reviewing, refining, and consolidating the PA1 documentation based on instructor feedback before final submission.

#### **2.2 Instructor Feedback & Project Scope Refinement**

The team collectively reviewed and analyzed the feedback received from the instructor regarding the proposed Consumer Electronics E-Commerce Web Application.

Key discussion points included:

* Refining the project concept to establish a clearer and more consistent application scope.  
* Reviewing the proposed functionalities to ensure alignment with the project's objectives and assignment requirements.  
* Clarifying the role and scope of the AI Shopping Assistant within the e-commerce platform.  
* Defining more clearly how the AI assistant will support customers during product discovery, recommendations, and comparisons through automatic agents.

**Decision:** The team agreed to refine the existing project proposal and present a more clearly defined and realistic scope for the AI Shopping Assistant.

#### **2.3 New Task Breakdown & Assignments**

The following responsibilities were assigned to team members for the next development phase:

| Jira ID | Task | Assignee |
| ----- | ----- | ----- |
| SWE-33 | Data Crawling | Gia |
| SWE-20 | Describe the project's key features | Huyền, Kiên, Thịnh |
| SWE-19 | Export, package and submit PA1 | Kiên |
| SWE-21 | Audit submission requirements and contribution evidence | Kiên |
| SWE-36 | Setup Frontend structure | Kiên |
| SWE-18 | Document Scrum meeting 2 | Thành |
| SWE-35 | Setup Backend structure | Thành |
| SWE-37 | Design Database ERD | Thành |
| SWE-12 | Define AI feature and their scope | Thịnh |
| SWE-34 | Setup AI structure | Thịnh |
| SWE-38 | Research AI feature | Thịnh |

**3\. Summary of Meeting 2**

* All tasks assigned during Meeting 1 were still in progress.  
* Instructor feedback was reviewed, and the team agreed to refine the project concept and clarify the scope of the AI Shopping Assistant.  
* New tasks were distributed among team members, covering project management, data collection, database design, documentation, and AI research.  
* **The team's immediate priority is to complete and finalize all PA1 deliverables before the submission deadline.**


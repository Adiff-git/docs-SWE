Spec Kit Training Evidence

**Jira Task:** SWE-100

**Performed by:** Lê Đức Thịnh

**Reviewed by:** Phan Thị Thanh Huyền

## 1. Training Overview

All five team members are required to complete Spec Kit
training as part of PA2 preparation.

This document consolidates individual training evidence
and records how each member practiced using Spec Kit.

## 2. Individual Training Evidence

**Member Name**: Phan Thi Thanh Huyen

**Summary of Spec Kit training**: By following the YouTube tutorials online, I gained an understanding of the basic principles of Specification-Driven Development (SDD) and learned how to systematically connect high-level vision requirements with specific tasks. I found out that the tool helps me set up projects’ structures and I learned how to create the baseline constitution.md file to establish the architectural rules for the entire project. Moreover, I acquired the knowledge of how to check and verify the generated Markdown specification documents for consistency, and how to use these specs for generating quality codes and tracking development progress effectively.

**Member Name:** Trinh Van Thanh

**Summary of Spec Kit training:** I learned Spec Kit through YouTube tutorials, ChatGPT explanations and feedback, and initialized it myself in the backend project source. I described the project's engineering principles to create constitution.md and learned the command sequence, including specify, clarify, plan, checklist, tasks, analyze and implement, along with the Markdown outputs to review after each step. I used the checklist command to generate review criteria, checked the artifacts against those criteria, and revised or supplemented incomplete requirements before rerunning the relevant commands. My main difficulty was understanding lengthy, technical command outputs, so I asked ChatGPT to explain unfamiliar terms and findings to help me review them more clearly. Applying this process to User Profiles and Addresses, Authentication, and Image Storage helped me understand how requirements, plans, tasks and implementation connect, and why generated artifacts need iterative review.

**Training log (reconstructed from Codex practice history)**

23–24 October 2026 — Constitution: Described backend engineering requirements and used speckit-constitution to establish and refine .specify/memory/constitution.md, including architecture, validation, security, testing and API contract rules.

26 October 2026 — User Profiles and Addresses: Practiced specify, clarify, plan, checklist, tasks, analyze and implement. Reviewed generated spec.md, plan.md, tasks.md, checklists and contracts; clarified privacy, field validation, ownership and locking decisions.

26 October 2026 — Authentication: Applied the specification-to-implementation workflow to JWT authentication and sessions. Supplied decisions about username rules, initial role and permissions, password policy and signing configuration, and reviewed the associated Markdown artifacts.

26–27 October 2026 — Iterative review: Requested checklist evaluation for profiles/addresses, authentication and storage; asked for explanations of unresolved items and supplied clarifications. Used the findings to refine requirements and task coverage rather than treating generated output as final.

27 October 2026 — Image Storage: Practiced specify, plan, tasks, checklist, analyze and implement for image uploads and avatar references. Clarified content identity, overwrite behavior and test scope, and distinguished implemented work from unresolved or deferred requirements.

**Member Name:** Gia

**Summary of Spec Kit training:**

I learned Spec Kit through YouTube tutorials, ChatGPT explanations, and hands-on practice with Codex. I initialized Spec Kit in the AI project repository and developed the project's constitution.md to define engineering principles, architecture boundaries, security requirements, and testing standards. I also learned the Spec Kit workflow, including specify, clarify, plan, tasks, analyze, and implement, and how to review generated artifacts.

Besides learning Spec Kit, I focused on preparing the Product Catalog dataset for the e-commerce system. I researched product datasets, processed approximately 10,000 products, and worked on data cleaning, category mapping, specification normalization, pricing policies, and image handling. I used Codex to develop and test data processing scripts, prepare import files, and check compatibility with the Backend database structure. I also worked on integrating product data and images into the Backend, validating import behavior, and preparing a reproducible setup for other team members.

My main difficulties were understanding the existing Backend data model, maintaining consistency between Product and Product Variant information, handling product images, and ensuring reliable data imports. I used ChatGPT and Codex to analyze these problems, review implementation decisions, and identify potential issues. Through this process, I improved my understanding of Spec Kit, AI-assisted development, data processing, database integration, and collaborative software development.

**Training log (reconstructed from Codex practice history)**

**28 October 2026 — Spec Kit Setup and Constitution:** Initialized Spec Kit in the AI repository and created .specify/memory/constitution.md. Defined engineering principles covering service boundaries, Backend integration, data ownership, security, testing, and AI agent behavior. Reviewed and refined the constitution using ChatGPT and Codex.

**29 October 2026 — Product Catalog and Database Preparation:** Studied the Backend Product Catalog structure, including Products, Variants, Brands, Categories, and Specifications. Worked on catalog metadata enrichment and database migration preparation. Reviewed data compatibility, backup procedures, and validation requirements before applying database changes.

**30 October 2026 — Dataset Processing and Import Preparation:** Prepared approximately 10,000 products for the e-commerce platform. Used Codex to process product data, review category mappings, define pricing policies, and generate import-ready datasets. Created validation reports to identify missing fields, inconsistent information, and compatibility issues with the Backend importer.

**30–31 October 2026 — Product Specification Normalization:** Improved product specification data through the V4.1 normalization process. Generated normalized product and specification files, reviewed before-and-after comparisons, and added regression tests. Focused on improving product information consistency without modifying the original dataset.

**31 October 2026 — Product Image Processing and Backend Integration:** Worked on importing real product images and connecting them to the Product Catalog. Developed and tested image import utilities, Backend media validation, and local preview functionality. Reviewed how product data and images could be distributed to teammates using GitHub repositories and Docker.

**31 October 2026 — Integration Testing and Deployment Preparation:** Added tests for catalog importing and image handling, validated the local development workflow, and committed the Backend catalog preparation changes. Investigated reducing the dataset to approximately 1,500 diverse products to minimize storage and download requirements. Planned a reproducible setup allowing teammates to clone the repositories, download product images, and import catalog data into their local environments.

**Member Name: Le Duc Thinh**  
Summary of Spec Kit training:  
During Sprint 2, I studied the fundamentals of Specification-Driven Development (SDD) and how GitHub Spec Kit turns an initial feature description into reviewable engineering artifacts. I learned the purpose of a project constitution, the relationship between requirements and implementation, and the roles of the specify, clarify, plan, tasks, analyze, and implement stages. I also learned that AI-generated specifications may contain assumptions or gaps, so the team needs to inspect and refine each artifact instead of treating it as a final decision.

As the AI team lead and a contributor to the Frontend workstream, I focused on understanding how Spec Kit should be used consistently across the AI, Frontend, and Backend repositories. I worked on the project constitution task (SWE-98) and a cross-repository status consolidation task (SWE-99), using the team conventions and existing artifacts as references. In this process, I practiced mapping a broad development objective into smaller tasks, identifying dependencies between services, and planning branch, Pull Request, and review steps. I used ChatGPT to clarify the workflow and prepare task-specific prompts for an AI coding agent, while keeping the team responsible for reviewing the resulting specifications and code.

The most useful lesson was the difference between generating documents and verifying that they accurately describe the intended system. I found cross-repository consistency and translating high-level AI features into testable requirements especially challenging. For the next iteration, I intend to apply the same workflow to the shopping assistant and AI integration tasks, with explicit acceptance criteria, API contracts, and test evidence. This training strengthened my understanding of how specifications, task tracking, code reviews, and human validation fit together.

Training log (reconstructed from project discussions and task work; exact timestamps should be checked before submission):  
Late October 2026 — SDD Concepts and Workflow: Reviewed the purpose of Spec Kit and its constitution, specification, planning, task breakdown, analysis, and implementation stages; used AI explanations to clarify how generated artifacts relate to actual development.  
28–29 October 2026 — Constitution and Repository Conventions: Worked on SWE-98 and reviewed the project's engineering principles, Git workflow, and documentation expectations. Compared the intended Spec Kit structure with the team's AI, Frontend, and Backend repositories.  
29–30 October 2026 — Cross-Repository Review: Worked on SWE-99 to consolidate the status of Spec Kit-related repositories and identify follow-up work or inconsistencies without assuming all generated artifacts were complete.  
30–31 October 2026 — Application to AI Tasks: Used the Spec Kit workflow as a guide to break AI foundation and shopping-agent work into reviewable tasks, prepare coding-agent prompts, and plan human verification and Pull Request steps.  
Evidence to attach (pending verification): A genuine screenshot of the SWE-98/SWE-99 Jira activity; the relevant constitution.md or .specify artifacts from the actual repository; and, if available, one screenshot of a real Spec Kit command output or training session. No screenshot or command execution is claimed here without an attached original record.  

# **Changes** 

**Performed by:** Nguyễn Công Kiên

**Reviewed by:**  Nguyễn Hoàng Gia

---

## **Project Plan**

**Performed by:** Nguyễn Hoàng Gia, Nguyễn Công Kiên

**Version:** 2.0 → 2.1 (PA3 revision)

### **Summary**

The Software Development Plan was updated for PA3. Main changes: the project name, real PA dates from the course schedule, PA3 deliverables and ownership, a detailed Sprint 3 task plan, updated effort estimates, release checkpoints, and risks. Section sign-off attribution was also added throughout.

### **Changes**

| No. | Section | Change |
| :---- | :---- | :---- |
| 1 | Title, 1.2, 2.1 | Project renamed from **Lẩu gà Lá É** to **Chạm Tech**. The `<project-name>` placeholders in Scope and Project Overview were replaced with the real name. |
| 2 | 1.1 Purpose, 1.2 Scope | Minor rewording only; no change in meaning. |
| 3 | 2.2.2 Constraints | System Architecture: **three** repositories → **four** (Frontend-SWE, Backend-SWE, AI-SWE, docs-SWE). This now matches Section 4.3.4. |
| 4 | 2.3 Deliverables | Rewritten around real PA1–PA5 release/due dates. Added the full PA3 deliverable list and PA3 submission packaging. Replaced the old "TBD" targets. |
| 5 | **3.2.1 (new)** | Added the PA3 responsibility matrix (performers and reviewers per deliverable) and use-case ownership by functional group. |
| 6 | 4.1 Estimates | Effort unit changed from per-sprint to **per-week** (7.5 h/person/week, ≈ 412.5 team-hours over 11 weeks, 03 Oct–12 Dec). Software size now notes the **59 use cases** in the current use-case model, next to the original \~33 features. |
| 7 | 4.2.1 Phase Plan | Focus moved from Sprint 2 to Sprint 3 / PA3, with five Sprint 3 priorities. The roadmap uses academic PA windows instead of Jira-only dates. |
| 8 | 4.2.2 Iteration Objectives | Replaced the Sprint 2 table with Sprint 3 plans: Table 2A (PA3 deliverables) and Table 2B (technical tasks per workstream). |
| 9 | 4.2.3 Releases | Build checkpoints re-aligned to PA dates: B2 \= PA3 (14 Nov), B3 \= PA4 (28 Nov), B4 \= PA5. Added a note that targets are planned checkpoints, not delivered releases. |
| 10 | 4.3.3 Risk Management | Added four **High** risks specific to PA3: use-case/prototype workload, Vision–use-case–spec misalignment, Spec Kit group not demo-ready, and missing submission evidence. The AI-scope risk was moved up to High. The remaining risks were condensed. |
| 11 | 4.3.4 Config Management | The old section-assignment table is kept as "PA2 assignments (for traceability)"; the PA3 matrix (3.2.1) takes precedence. |

### **Unchanged**

* 2.2.1 Assumptions, 2.2.3 Pending Decisions (D1)  
* Technology stack and team structure (3.1)  
* 4.3.1 Requirements Management, 4.3.2 Reporting and Measurement  
* Git workflow and CI/CD rules in 4.3.4

## **Vision**

**Performed by:** Lê Đức Thịnh \| **Reviewed by:** Nguyễn Hoàng Gia / Phan Thị Thanh Huyền \| **Edited by:** Lê Đức Thịnh  
**Version:** 1.3 → 1.4 (PA3 revision, 13–14 November 2026).

### **Summary**

Refined the PA2 Vision for PA3; standardized the project name, structure, product requirements, and traceability.

### **Changes**

| No. | Section | Change |
| :---- | :---- | :---- |
| **1** | **Title and revision history** | Renamed the product to Chạm Tech and added the PA3 revision entry and author/reviewer/editor metadata. |
| **2** | **Positioning and alternatives** | Clarified the problem statement, customer value proposition, and bounded comparison with electronics retailers. |
| **3** | **Users and environment** | Clarified Guest/Customer/Administrator boundaries, desktop-first browsers, internet access, error handling, and AI fallback. |
| **4** | **Product perspective** | Documented the Frontend–Backend–AI integration model, data ownership, provider assumptions, and pending API/security decisions. |
| **5** | **Feature scope** | Distinguished conventional shopping, Recommendation System, and AI Agent search/consultation/comparison from deferred automated cart and checkout actions. |
| **6** | **Requirements quality** | Defined measurable but unverified system/AI quality targets, including grounding, latency, authorization, fallback, integrity, and usability. |
| **7** | **Traceability** | Added FG-01–FG-10 / UC-001–UC-059 coverage and PA3 acceptance/review checkpoints. |
| **8** | **Formatting** | Standardized headings, restored version history, and improved the responsibilities table for readable PDF export. |

### **Unchanged**

* Original tables, AI NFRs, and other authors' sections were preserved.  
* Previous Vision non-functional requirements remain proposed acceptance targets; no unrun performance/quality test is presented as passed.


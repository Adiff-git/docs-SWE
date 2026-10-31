# A - Team Contract

## 1. Team Roles and Responsibilities

All members are expected to contribute as full-stack engineers throughout the project. The roles below indicate each member's primary responsibility and leadership area rather than restricting them to a specific technical domain.

### Project Manager

Gia

Primary responsibilities:
- Monitor project progress and internal deadlines.
- Coordinate project activities and meetings.
- Track the overall project status and identify blocked tasks.
- Coordinate work between Backend, Frontend, and AI areas.
- Take primary responsibility for project management documentation.
- Ensure that project documents, Jira tasks, and GitHub activities are kept up to date.

### Backend

Lead: Thành  
Members: Gia

Primary responsibilities:
- Design and implement backend services and APIs.
- Design and maintain database-related functionality.
- Implement business logic, authentication, authorization, and server-side validation.
- Integrate backend services with the frontend and AI components.
- Review backend-related technical decisions and implementation.

The Backend Lead is primarily responsible for coordinating backend-related work and reviewing important backend changes.

### Frontend

Lead: Kiên  
Members: Thịnh, Huyền

Primary responsibilities:
- Design and implement the application's user interface.
- Implement routing, state management, and frontend application logic.
- Integrate frontend components with backend APIs and AI services.
- Ensure that the interface is usable and responsive.
- Review frontend-related technical decisions and implementation.

The Frontend Lead is primarily responsible for coordinating frontend-related work and reviewing important frontend changes.

### AI

Lead: Thịnh  
Members: Gia

Primary responsibilities:
- Research and design the project's AI-powered features.
- Select appropriate AI models, APIs, libraries, or techniques.
- Develop and test AI-related functionality.
- Integrate AI components with the rest of the application.
- Evaluate AI outputs and handle possible failure cases.

The AI Lead is primarily responsible for coordinating AI-related work, reviewing AI implementation, and leading technical documentation related to the AI component.

### Testing

All members are responsible for testing.

Each member must:
- Self-test the features they implement.
- Participate in cross-testing features implemented by other members when applicable.
- Report discovered bugs or problems through the team's task management process.
- Re-test fixed issues before they are considered completed.

### Documentation

Documentation is a shared responsibility.
- The member responsible for a feature should provide the initial documentation for that feature when necessary.
- Gia is primarily responsible for project and management documentation.
- Technical leads are responsible for reviewing documentation related to their technical areas.
- Thịnh takes a leading role in technical documentation, especially for AI-related components.
- Documentation may be reviewed and edited by other members before submission.

## 2. Communication Plan

### Communication Channels

The team uses the following communication tools:
- Messenger: Used for quick messages, urgent notifications, reminders, and informal communication.
- Discord: Used for online meetings, technical discussions, development coordination, and GitHub activity monitoring.
- When2Meet: Used to collect each member's weekly availability.

WEEKLY availability must be updated at:  
<https://www.when2meet.com/?39008766-4A8Qp>

Discord server:  
<https://discord.gg/ubBsx5Z5z>

### GitHub Repositories

The team currently maintains the following repositories:
- Frontend: <https://github.com/Adiff-git/Frontend-SWE>
- Backend: <https://github.com/Adiff-git/Backend-SWE>
- AI: <https://github.com/Adiff-git/AI-SWE>

GitHub notifications may be integrated into Discord to help the team monitor commits, Pull Requests, and other development activities.

### Response Expectations

- Members should regularly check Messenger and Discord.
- Important project-related messages should be acknowledged within a reasonable period, normally within 24 hours.
- If a member expects to be unavailable for an extended period, they should inform the team in advance whenever possible.
- Members should notify the team as early as possible when a task is blocked or likely to miss its deadline.

### Meetings

Each Sprint follows the Scrum process required by the course:
- 1 Sprint Planning meeting.
- 2 Scrum meetings distributed throughout the Sprint.
- 1 Sprint Review meeting.

Meeting times are determined according to the team's weekly availability.

## 3. Work Schedule and Deadlines

Each Sprint lasts approximately 2–3 weeks.

At the beginning of each Sprint:
- The team identifies the Sprint goals.
- Tasks are created and assigned through Jira or another agreed task management tool.
- Each task must have exactly one primary owner.
- Tasks should have appropriate deadlines based on the Sprint schedule.

Members are expected to complete assigned work by the agreed deadline.

If a member expects to miss a deadline, they must inform the team as early as possible and provide:
- Current progress.
- Reason for the delay.
- Expected new completion time.
- Any support required from other members.

If necessary, the Project Manager and relevant technical lead may adjust task scope, reassign supporting work, or revise internal deadlines.

Unexpected delays should be discussed during team communication or Scrum meetings rather than being reported only after the deadline has passed.

## 4. Code and Documentation Standards

### Coding Standards

All members should follow consistent coding conventions agreed upon for the technologies used in the project.

General rules include:
- Follow consistent naming conventions.
- Follow the formatter and linter configuration selected for each project.
- Keep functions, classes, and modules reasonably focused and understandable.
- Do not hard-code API keys, passwords, access tokens, credentials, or other secrets.
- Use comments where they improve understanding of non-obvious logic.
- Avoid unnecessary comments that merely repeat what the code already expresses.

Technology-specific conventions may be added once the project's technology stack is finalized.

### Git Branching Convention

Branch names follow the format:
```text
type/<short-name>
```

Examples:
- `feature/login-api`
- `feature/user-profile`
- `fix/login-validation`
- `docs/team-contract`
- `test/authentication`

Recommended branch types include:
- `feature/`
- `fix/`
- `docs/`
- `test/`
- `refactor/`

Rules:
- Members must not push directly to `main`.
- Development should be performed on separate branches.
- Changes should normally be merged into `main` through a Pull Request.
- Branches that are no longer needed should be deleted after they are successfully merged.

### Commit Convention

Commit messages follow the format:
```text
type: short description
```

Examples:
- `feat: add login API`
- `fix: handle invalid login credentials`
- `docs: update team contract`
- `test: add authentication tests`
- `refactor: simplify user service`
- `chore: configure development tools`

Commit messages should briefly describe the actual change and should avoid unclear messages such as `update`, `done`, or `final`.

### Code Review and Testing Process

The normal development workflow is:

```text
Developer
    ↓
Self-test
    ↓
Pull Request
    ↓
Peer Review
    ↓
Cross-test
    ↓
Merge
```

Rules:
- The developer must self-test their implementation before requesting a merge.
- Important changes should be submitted through a Pull Request.
- At least one other team member should review the Pull Request when applicable.
- Technical leads should preferably review major changes in their responsibility area.
- Review comments should be resolved before merging.
- Another member should cross-test important features when practical.

### Documentation Standards

All official project documentation follows these standards:
- Documentation language: English
- Primary source format: Markdown (.md)
- Diagram format: Mermaid whenever possible
- Submission format: Markdown and PDF

Documentation should use a consistent heading structure and meaningful file names.

Examples:
- `team-contract.md`
- `project-proposal.md`
- `weekly-report-01.md`
- `sprint-review-01.md`

Files with unclear names such as `final2.md`, `new-report.md`, or `abc.md` should be avoided.

For each report or document section, the responsible members should be recorded when required, for example:
- `Performed by: <member>`
- `Reviewed by: <member>`
- `Edited by: <member>`

Project documentation should be version-controlled in Git together with the source code.

Sensitive information such as `.env` files, API keys, passwords, credentials, and access tokens must never be committed to the repository.

## 5. Accountability and Performance

### Contribution Evaluation

Member contribution is evaluated using multiple forms of project evidence rather than only the number of Git commits.

Relevant indicators include:
- Completion of assigned Jira tasks.
- Git commits and Pull Requests.
- Quality of completed work.
- Adherence to agreed deadlines.
- Participation in Sprint Planning, Scrum meetings, and Sprint Reviews.
- Participation in testing and code reviews.
- Communication with other team members.
- Documentation contribution.
- Willingness to support other members when necessary.

### Task Ownership

- Each task must have exactly one primary owner.
- The assigned member is responsible for ensuring that the task is completed according to the agreed requirements and deadline.
- A member may receive help from other members, but responsibility for the task remains with the assigned owner unless the task is formally reassigned.

### Definition of Done

A task must not be considered completed when the actual work is unfinished.

For a development task, the following conditions should normally be satisfied when applicable:
- The implementation is complete.
- The code runs correctly.
- The implementation satisfies the agreed requirements.
- The developer has performed self-testing.
- Relevant cross-testing or peer review has been completed.
- Important review comments have been resolved.
- Required documentation has been updated.
- The change has been merged into the appropriate branch when applicable.
- The corresponding Jira task accurately reflects its real completion status.

### Missed Deadlines

If a member expects to miss a deadline, they should notify the team before the deadline whenever possible.

They should explain:
- Current progress.
- Reason for the delay.
- Expected completion time.
- Whether assistance is required.

Repeated failure to meet deadlines without communication may be considered a performance issue.

### Underperformance

Minor or occasional performance issues are handled first through direct communication.

The process is:
1. The relevant Lead or Project Manager reminds the member and discusses the issue.
2. If the issue continues, the team discusses the reason and agrees on specific corrective actions or a revised deadline.
3. If repeated underperformance, lack of participation, or violation of the Team Contract continues after previous discussions, the issue may be escalated to the TA or instructor.

Performance concerns should be supported by objective project evidence such as Jira task history, GitHub activity, Pull Requests, meeting participation, and team communication.

## 6. Decision-Making Process

The team should attempt to reach decisions through discussion and consensus whenever possible.

For decisions that affect the whole project:
1. The issue is discussed by relevant team members.
2. Members attempt to reach consensus.
3. If consensus cannot be reached within a reasonable period, the decision is made by majority vote.

For technical decisions limited mainly to one responsibility area:
- The relevant technical Lead coordinates the discussion.
- Team members involved in the affected component should provide input.
- The Lead may make the final implementation decision when necessary, provided that the decision does not conflict with project-wide requirements.

For project management, scheduling, and coordination decisions:
- The Project Manager coordinates the decision.
- Major changes affecting the whole team should still be discussed with the team.

No member should make a major project-wide decision independently when that decision significantly affects other members' work.

## 7. Conflict Resolution

Team members should attempt to resolve disagreements professionally and focus on the project requirements rather than personal preferences.

The conflict resolution process is:
1. The members directly involved discuss the issue and attempt to understand each other's concerns.
2. Relevant requirements, technical evidence, project constraints, and alternatives are reviewed.
3. If the issue remains unresolved, the relevant technical Lead or Project Manager facilitates the discussion.
4. If necessary, the team applies the agreed Decision-Making Process.
5. If the conflict significantly affects teamwork or cannot be resolved internally, the issue may be escalated to the TA or instructor.

Personal attacks, disrespectful communication, or intentional obstruction of another member's work are not acceptable.

Technical disagreements should preferably be resolved using evidence such as prototypes, tests, documentation, or project requirements rather than personal preference.

## 8. Review and Update Process

This Team Contract should be reviewed at least once per Sprint, approximately every 2–3 weeks.

The contract may also be reviewed earlier when:
- The team changes its development workflow.
- Roles or responsibilities change.
- A recurring collaboration problem is identified.
- New tools or development processes are introduced.
- Existing rules are unclear or ineffective.

Changes to the Team Contract should be discussed with the team before being adopted.

Major changes should be agreed upon through the team's Decision-Making Process.

All approved changes should be reflected in the version-controlled Team Contract document stored in the project repository.

# SWE-99 — Reviewer Handoff

**Performed by:** Lê Đức Thịnh  
**Reviewed by:** Nguyễn Công Kiên (pending)  
**Edited by:** Pending feedback

## Collected scope

A reproducible 48-file manifest and SHA-verified collection script for the frontend, backend, and AI repositories. Each source's constitution and five Markdown templates are included, plus 10 per-repo Spec Kit commands or agent skills. The script will copy exact source files into `generated-files/<repo>/` while preserving their original paths.

## Known limitations / decisions for reviewer

- No feature-specific `spec.md`, `plan.md`, or `tasks.md` exists at the audited source commits. Templates alone are not equivalent.
- Current root-level `.specify/` structure does not literally match the team's requirement to verify generated artifacts under `/src`. Confirm with the per-repo owners and do not move working configuration without agreement.
- Backend constitution marks formal ratification as unverified; please do not imply it has been approved.
- This task does not include SWE-98's project-wide constitution nor SWE-100's five-member training evidence.
- In the generated-files inventory, 30 command/skill instruction files are included **for completeness**. Reviewer may decide they need only be linked rather than copied into the final submission.

## Approval checklist

- [ ] Execute the collection script and get 48/48 verified SHA check.
- [ ] Review source pinning and 3/3 repo coverage.
- [ ] Decide whether extra feature-level specs are necessary for PA2.
- [ ] Clarify `/src` placement requirement with module owners.
- [ ] Approve before moving SWE-99 to Done.

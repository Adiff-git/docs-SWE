# SWE-99 — Spec Kit Artifact Collection

**Owner:** Lê Đức Thịnh  
**Reviewer:** Kiên  
**Jira:** https://giagia8765.atlassian.net/browse/SWE-99

## How to use

1. From your **local** `docs-SWE` repository, create a branch from `main` if you have not already created one:

   ```bash
   git switch main
   git pull origin main
   git switch -c docs/pa2-speckit
   ```

   If `docs/pa2-speckit` already exists, switch to it instead. Do not recreate or overwrite it. Copy the entire `PA2/SpecKit/` folder into the **root** of your local `docs-SWE` working tree.
2. From the root of `docs-SWE`, run:

   ```bash
   python3 PA2/SpecKit/collect_speckit.py
   python3 PA2/SpecKit/collect_speckit.py --verify-only
   ```

3. Confirm the collector prints `PASS: All 48 real Markdown files collected` and `PASS: 48/48`.
4. Review `PA2/SpecKit/Generated_Markdown_Manifest.md`, which includes 48 pinned source permalinks and SHA checksums.
5. Commit all generated snapshot files with `git add PA2/SpecKit` and `git commit -m "docs: collect Spec Kit markdown artifacts (SWE-99)"`.
6. Ask Kiên to review this commit / the upcoming PR, and address any request for additional feature-level Spec Kit artifacts.

## Files in this starter package

- `Generated_Markdown_Manifest.md` — fully verified **source inventory**, status, caveats, and reviewer checklist.
- `Source_Files.tsv` — 48 machine-readable source paths, immutable source commit and Git blob SHA.
- `collect_speckit.py` — deterministic collector with SHA validation. **Needs internet access to fetch real Markdown files.**
- `SWE-99_Review_Notes.md` — concise reviewer handoff.

**Note:** The `generated-files/` directory is created by the collector. It is not populated in this starter package, because the ChatGPT runtime cannot download the source archives and the GitHub integration does not have permission to create a new branch in `docs-SWE`. The inventory is complete, but **SWE-99 should not be marked Done until the 48 real files have been collected and reviewed**.

### Scope boundaries

This task concerns collected Markdown artifacts only. The project-wide `constitution.md` is SWE-98 and individual training evidence is SWE-100. The source `.specify/` layout is preserved, and feature-level `spec.md`, `plan.md`, `tasks.md` files are not fabricated where absent.

# docs: collect PA2 Spec Kit generated Markdown artifacts (SWE-99)

## Task

- Jira: https://giagia8765.atlassian.net/browse/SWE-99
- Owner: Lê Đức Thịnh
- Reviewer: Kiên

## Summary

- Collect 48 Spec Kit-related Markdown files from three pinned source repositories: AI-SWE (16), Frontend-SWE (16) and Backend-SWE (16).
- Include 3 project-specific constitutions, 15 Spec Kit templates and 30 integration command/skill Markdown files.
- Preserve the original directory structure in `PA2/SpecKit/generated-files/{ai,frontend,backend}/`.
- Record source commit SHAs, blob SHAs and GitHub permalinks in `Generated_Markdown_Manifest.md`.
- Provide `collect_speckit.py` and `Source_Files.tsv` to reproduce and validate the collection.

## Validation

After materializing the files, run:

```bash
python3 PA2/SpecKit/collect_speckit.py --verify-only
```

Expected: `PASS: 48/48 Markdown snapshots are present and hash verified.`

## Reviewer notes

The feature-specific `spec.md`, `plan.md`, `tasks.md` are not present at the pinned source commits; template files are not substitutes. Source Spec Kit files are located in root-level `.specify/`, not directly in `/src`, pending clarification on the PA2 folder requirement.

Related tasks SWE-98 and SWE-100 should be reviewed independently; their deliverables can be added to the same branch/PR when ready.

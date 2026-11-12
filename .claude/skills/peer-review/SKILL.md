---
name: peer-review
description: Run a Staff-Engineer-grade code review of the latest changes (or named files) with a severity rubric, save the review, and optionally hand the findings to the backend / frontend developer to fix. Use when the user says "review my code", "is this good?", or before merging/releasing.
argument-hint: "[files or folder to review] [--fix]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Peer review

Target: **$ARGUMENTS** (empty = latest changes via `git diff`, or the whole app if git isn't set up).

1. Use the **code-reviewer** subagent. Pass it the target and point it at `checklist.md` in this folder.
2. Save its report to `docs/reviews/REVIEW-<YYYY-MM-DD>-<short-slug>.md`.
3. Show the user the verdict and the 🔴/🟠 findings.
4. If the arguments contain `--fix`, or the user agrees:
   - pass the 🔴/🟠 findings to the **backend-developer** and/or **frontend-developer** subagent (by file),
   - then the **tester** subagent runs the suite,
   - then the **code-reviewer** re-reviews only the fixed lines (max 2 rounds).
5. End with the final verdict and test result.

---
name: write-docs
description: Write or update documentation that matches the real code — README, student code walkthrough, user guide, CHANGELOG — in plain English. Use after features land, before a release, or when the user asks to "document this" or "explain the code for students".
argument-hint: "[readme | walkthrough | user-guide | changelog | all]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Documentation

What to write: **$ARGUMENTS** (empty = update `README.md` + `CHANGELOG.md` for recent changes).

1. Use the **tech-writer** subagent with the requested doc type(s):
   - `readme` → update `README.md`
   - `walkthrough` → `docs/WALKTHROUGH.md` (guided code tour following the RAG data flow)
   - `user-guide` → `docs/USER_GUIDE.md`
   - `changelog` → `CHANGELOG.md` `## [Unreleased]` section
2. If the writer reports code ↔ docs mismatches, show them to the user and ask which is right
   (per `CLAUDE.md`, `docs/SPEC.md` wins unless the user says otherwise).
3. List the files written.

---
name: ui-review
description: Review the Angular UI (Chat, Retrieval Lab, Vector Explorer) against docs/DESIGN_SYSTEM.md (tokens, components, states, dark mode, accessibility, microcopy) and get a "premium feel" score with exact fixes; optionally apply them. Use when the user says the UI looks off, before demos, or after UI changes.
argument-hint: "[component or area, e.g. 'sidebar'] [--fix]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# UI / UX review

Focus: **$ARGUMENTS** (empty = whole UI).

1. Use the **ux-designer** subagent in **Review mode**.
2. Show the score and the "Must fix" list.
3. If `--fix` is present or the user agrees: **frontend-developer** applies the fixes → **tester** runs the frontend suite
   (component specs must still pass, coverage must not drop).
4. Remind the user to look with their own eyes: `npx ng serve` (backend running), check light **and** dark mode
   (OS setting), and narrow the window to phone width.

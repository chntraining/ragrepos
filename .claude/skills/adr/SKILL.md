---
name: adr
description: Create an Architecture Decision Record — compare at least two design options, pick one, record the consequences and an implementation plan. Use when a feature involves a technical choice (new library, new module, storage or retrieval change) or when the user asks "how should we design X?".
argument-hint: "<decision to make, or path to a requirement doc>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Architecture Decision Record

Decision to make: **$ARGUMENTS**

1. Use the **architect** subagent. Pass it the topic (or requirement doc path) and tell it to use
   `template.md` in this folder and to number the ADR after the highest one in `docs/adr/`.
2. Show the user the options table and the recommended decision.
3. Ask: "Accept this ADR?" If yes, have the architect set `Status: Accepted` and apply any
   approved `docs/SPEC.md` contract changes.
4. Suggest next: `/feature` or `/sdlc` to implement it.

**Teaching tip:** `blueprint/STACK_DECISION.md` (copied into every project as `docs/adr/0001-stack-decision.md`) is a worked example — show it first.

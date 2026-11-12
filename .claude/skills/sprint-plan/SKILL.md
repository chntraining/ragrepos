---
name: sprint-plan
description: Turn a backlog of ideas or requirement docs into an ordered sprint plan — small tasks with estimates, dependencies, owners (which agent) and a definition of done. Use when the user has several features and asks what to build first or how to plan the work.
argument-hint: "[list of ideas | 'from docs/requirements' | sprint goal]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Sprint planning

Input: **$ARGUMENTS** (if empty, use every requirement doc in `docs/requirements/` with Status ≠ Released,
plus the ideas in `prompts/03_NEXT_FEATURES.md`).

1. Use the **product-manager** subagent to rank the backlog by **value ÷ effort** (and dependencies first).
2. Break the top items into tasks of **≤ ½ day** each. For every task give:
   - ID (`T1`, `T2`…), title, owner agent (`architect` / `backend-developer` / `frontend-developer` / `tester` / `ux-designer` / …)
   - estimate in story points (1, 2, 3, 5, 8 — Fibonacci)
   - depends on (task IDs)
   - done when (one testable sentence)
3. Fit a **sprint goal** (one sentence) and a capacity of ~20 points.
4. Write the plan to `docs/sprints/SPRINT-<n>.md` (n = next number) with:
   - Sprint goal
   - Task table
   - A Mermaid Gantt or simple ordered list showing the critical path
   - Risks
   - Definition of Done (tests green · coverage met · reviewed · security clean · docs updated)
5. Tell the user which command starts task T1 (usually `/sdlc <first feature>` or `/feature ...`).

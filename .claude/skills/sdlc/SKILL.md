---
name: sdlc
description: Run the complete Software Development Life Cycle for an idea — requirements → design → UX → build → test → review → security → eval → docs → release — using the full agent team with quality gates between phases. Use when the user wants to take a feature from idea to release, or to demonstrate the whole SDLC.
argument-hint: "<feature idea in plain English>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Full SDLC run

Idea from the user: **$ARGUMENTS**

You are the **engineering lead** orchestrating a team of specialist subagents. Run the phases
below **in order**. After each phase, print a one-line status like
`✅ Phase 2 — Design: ADR 0003 accepted` so the audience can follow along.

If `$ARGUMENTS` is empty, ask the user for the idea (suggest three from `prompts/03_NEXT_FEATURES.md`).
If the app isn't built yet (`backend/app/main.py` missing), tell the user to run `/build` first and stop.

---

## Phase 1 — Requirements  (agent: `product-manager`)
Pass the idea. Get back a requirement doc in `docs/requirements/` with stories + Given/When/Then.
**Gate 1:** show the stories and open questions to the user. If there are open questions, ask them and wait.
Otherwise continue (the user can say "skip gates" to run unattended).

## Phase 2 — Design  (agent: `architect`)
Pass the requirement doc path. Get back an ADR in `docs/adr/` with an implementation plan.
Skip this phase only if the change is trivial (one file, no new contracts) — say so explicitly.
**Gate 2:** the ADR must list files to touch and any new contracts.

## Phase 3 — UX spec  (agent: `ux-designer`, Mode A)
Only if the feature changes the UI. Adds a "UX spec" section to the requirement doc.

## Phase 4 — Build  (agents: `backend-developer`, `frontend-developer`)
Pass the requirement doc + ADR paths. They can work in parallel once the API contract is fixed in `docs/SPEC.md`.

## Phase 5 — Test  (agent: `tester`)
Add test cases to `docs/TEST_PLAN.md` for each acceptance criterion, write the tests, run both suites with coverage.
**Fix loop:** failures → `backend-developer` / `frontend-developer` (or `debugger` if the cause is unclear) → `tester`, max 3 rounds.
**Gate 5:** both suites green and coverage ≥ 85 % backend / 80 % frontend.

## Phase 6 — Review  (agents in parallel: `code-reviewer`, `security-auditor`, and `ux-designer` Mode B if UI changed)
Launch them in the same turn — they are read-only and independent.
Save the code review to `docs/reviews/REVIEW-<YYYY-MM-DD>-<slug>.md` and the security report to
`docs/security/SECURITY-<YYYY-MM-DD>.md` (you write the files from their reports).
**Fix loop:** any 🔴/🟠 → the right developer → `tester` → re-review, max 2 rounds.
**Gate 6:** review verdict APPROVE and security not FAIL.

## Phase 6b — Performance  (agent: `performance-engineer`) — when hot paths changed
Retrieval, ingestion, agent graph, DB queries or streaming changed → load test against the SPEC budgets (fake provider, offline).

## Phase 7 — Evaluate  (agent: `ai-evaluator`) — optional
Only if the change affects chunking, retrieval techniques, prompts, agent tools or models **and** the user has an API key set up.
Ask before running (it uses real free-tier quota).

## Phase 8 — Document  (agent: `tech-writer`)
Update `README.md` if user-facing behaviour changed, and add the feature under `## [Unreleased]` in `CHANGELOG.md`.

## Phase 9 — Release readiness  (agent: `release-manager`)
Run the go/no-go checklist and propose the version. Do **not** tag or push.

---

## Final summary for the user
Print a table:

| Phase | Agent | Output | Status |
|---|---|---|---|

Then: how to try the feature in the UI (start backend + `npx ng serve` → what to click), tests + coverage, and the release decision.

See `phases.md` in this folder for the one-page SDLC cheat-sheet you can show students.

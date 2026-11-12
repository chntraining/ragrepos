---
description: Build the complete Bodhi Agentic RAG app (Angular + FastAPI + SQLAlchemy/SQLite + ChromaDB + LangChain providers + LangGraph) from the specs, test it with coverage, fix until green, then review it
argument-hint: "[optional extra instructions]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

Build the **Bodhi** app end-to-end. Extra instructions from the user: $ARGUMENTS

Print a one-line status after each step (e.g. `✅ Step 2 — Backend built (coverage 88 %)`).

## Step 0 — Find the project and its specs
Project name = first word of the arguments if it looks like a name (lower-case, `a-z0-9-`), otherwise the
**Active project** from `CLAUDE.md`. Work only inside `projects/<name>/`.
- The project must already have `docs/SPEC.md`, `docs/DESIGN_SYSTEM.md`, `docs/TEST_PLAN.md` and `docs/adr/`.
  If it doesn't (new project), run `/client-intake <name> <requirement>` first — ask the user for the requirement in
  one sentence if none was given. (`/create-app` does both steps in one go.)
- Read `CLAUDE.md` and those project docs. If any ADR is still **Proposed**, ask the user to accept it before building
  (unless this is a `/create-app` autonomous run).

## Step 1 — Plan
Make a todo list from the SPEC layout, split into **backend** and **frontend**.

## Step 2 — Backend (backend-developer)
Build `backend/` in the agent's build order (config → db + migration → security → providers incl. `fake` → stores →
ingestion → retrieval → normal RAG → LangGraph agent → services → API). Install requirements, run `alembic upgrade head`.

## Step 3 — Frontend (frontend-developer)
Build `frontend/` (Login, Chat with all controls, Compare, Retrieval Lab, Vector Explorer, Documents, Admin) in the
Dinesh AI Academy brand, then `npm ci` / `npm install` and `npx ng build`.
Steps 2 and 3 may run in parallel once the API contract in the SPEC is final.

## Step 4 — Test (tester)
Write every test in `docs/TEST_PLAN.md` (unit, integration, contract, security, frontend, E2E), run all suites with coverage.

## Step 5 — Fix loop (max 3 rounds)
Failures or coverage below target (backend 85 %, frontend 80 %) → **backend-developer** / **frontend-developer**
(or **debugger** when the cause is unclear) → **tester** re-runs. Stop when green or after 3 rounds and explain what is left.

## Step 6 — Quality review (parallel, read-only)
Launch **code-reviewer**, **security-auditor**, **ux-designer** (Mode B) and **performance-engineer** in the same turn.
Save reports to `docs/reviews/REVIEW-<date>-initial-build.md`, `docs/security/SECURITY-<date>.md`, and let the
performance engineer save `docs/perf/PERF-<date>.md`.
🔴 findings → the right developer fixes → tester re-runs (1 round). 🟠 and below are listed for the user.

## Step 7 — Summary
- ✅ what was built (short tree)
- 🧪 tests + coverage table, E2E result
- 🔍 review / security / UX / performance verdicts (links)
- ▶️ run (from `projects/<name>/`): `cd backend && alembic upgrade head && uvicorn app.main:app --reload --port 8000`
  + `cd frontend && npx ng serve` — or `docker compose -f deploy/docker-compose.yml up --build`
- 🎬 next: `/demo-prep` for a client demo
- 🔑 in `projects/<name>/`, copy `.env.example` → `.env`, set `GOOGLE_API_KEY`, `JWT_SECRET`, admin password

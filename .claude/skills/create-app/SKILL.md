---
name: create-app
description: One command from a plain-English requirement to a running, tested, reviewed Agentic RAG application in projects/<name>/. The agent team asks a few well-chosen questions, then autonomously writes requirements, SPEC, ADRs, UX spec, test plan and eval set, builds backend + frontend, tests with coverage, debugs, reviews (code, security, UX, performance), documents and gives a release decision. Use when the user says "create / build an app for <requirement>" and wants the agents to do everything.
argument-hint: "<project-name> <your requirement in plain English, or a path to a filled requirements form>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Create an application — requirement in, running app out

Input: **$ARGUMENTS**
- First word = **project name** (lower-case `a-z0-9-`). If missing or invalid, suggest one from the requirement and use it.
- The rest = the **requirement** (free text, or a path to a filled `blueprint/CLIENT_REQUIREMENTS.md`-style form).
- If the requirement is empty, ask the user for it in one sentence — nothing else.

You are the **engineering lead**. The user gave the requirement and delegated everything else to the team.
Work autonomously; stop only at the gates marked 🛑. Print one status line per phase, e.g.
`✅ Phase 3/10 — Design: SPEC + 2 ADRs written (projects/acme/docs/)`.

## Phase 1 — Discovery and design  → run `/client-intake <name> <requirement>`
It creates the project, asks the **right questions once** (🛑 the only interactive stop), and produces:
`docs/REQUIREMENT_INPUT.md`, `docs/CLIENT_REQUIREMENTS.md`, `docs/requirements/REQ-001-*.md`, `docs/SPEC.md`,
`docs/adr/`, `docs/DESIGN_SYSTEM.md`, `docs/TEST_PLAN.md`, `evals/golden_set.jsonl` — and a consistency check between them.

**Autonomous decisions.** ADRs written in this run are recorded as `Accepted (autonomous run <date>, delegated by the user)`
and listed in the final report for review. Anything that needs money, credentials, or a legal / compliance claim is
**never** decided autonomously — it becomes an open item in the report.

## Phase 2 — Build, test, fix, review  → run `/build <name>`
Backend + frontend, every test suite with coverage, fix loops (developers / debugger ↔ tester), then code review,
security audit, UX review and performance test in parallel, with one fix round for 🔴 findings.

## Phase 3 — Evaluate answer quality  (ai-evaluator)
- Always (offline, free): check the eval set is valid and every question maps to a document in `evals/fixtures/` or the user's uploads.
- 🛑 Real-API evaluation only if the project's `.env` has a provider key **and** the user agrees (it uses quota).
  If skipped, say so in the report and give the command to run later (`/eval-rag --mode both`).

## Phase 4 — Documentation  (tech-writer)
`README.md` (inside the project), `docs/USER_GUIDE.md`, `docs/WALKTHROUGH.md`, `docs/DEMO_SCRIPT.md`, `docs/EXTENDING.md`,
and the project's `CHANGELOG.md`.

## Phase 5 — Release readiness  (release-manager)
Go / no-go against the checklist; version `0.1.0` for a first build. Never tag or push.

## Phase 6 — Final report → `docs/PROJECT_REPORT.md` (and a short summary in chat)
| Section | Content |
|---|---|
| What was asked | the requirement, verbatim |
| What was decided | answers to the questions + every autonomous ADR (one line each) |
| What was built | screens, endpoints, retrieval techniques, modes, models — short tree |
| Proof | test counts per suite, coverage table, E2E result, review / security / UX / performance verdicts with links |
| Answer quality | eval scores or "not run — command to run it" |
| Open items | anything not done, every ⚠️ / 🟠 finding, every decision needing a human |
| Run it | exact commands from `projects/<name>/`, which `.env` values to fill |
| Next | `/demo-prep <name>`, `/feature …`, `/add-llm-provider …` |

## Rules
- Everything goes inside `projects/<name>/`. Never write app files, data or reports anywhere else.
- Never invent facts about the user's business, model ids, prices or compliance — ask in Phase 1 or list as open items.
- If a phase fails after its fix-loop limit, **continue with the remaining phases that don't depend on it** and report
  the failure honestly — never claim done when it isn't.
- Reuse the agents and skills named here; do not do their jobs yourself.

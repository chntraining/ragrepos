---
description: Add a new feature end-to-end (requirements -> design -> code -> tests -> review)
argument-hint: "<feature description>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

New feature request: **$ARGUMENTS**

A lighter version of `/sdlc` — use `/sdlc` when you want every phase (UX, evals, docs, release).

1. **Requirements** — **product-manager** subagent writes `docs/requirements/REQ-<NNN>-<slug>.md`
   and adds the story to `docs/SPEC.md`. If it lists open questions, ask the user before continuing.
2. **Design** — if the feature adds an endpoint, a table, a Chroma change, a retrieval technique, an agent tool
   or a dependency, the **architect** subagent writes an ADR in `docs/adr/`. Otherwise say "no ADR needed" and why.
3. **Test plan** — add the feature's test cases to `docs/TEST_PLAN.md`.
4. **Build** — **backend-developer** and/or **frontend-developer** implement it (they can run in parallel
   once the API contract is fixed). UI must match `docs/DESIGN_SYSTEM.md`.
5. **Test** — **tester** writes the tests and runs both suites with coverage.
   Fix loop (developers / debugger ↔ tester) up to 3 rounds.
6. **Review** — **code-reviewer** reviews the change. Any 🔴/🟠 → the right developer fixes → tester re-runs (max 2 rounds).
7. **Changelog** — add one line under `## [Unreleased]` → `### Added` in `CHANGELOG.md`.
8. Summarise: what changed (files), how to try it in the UI, tests + coverage, review verdict.

---
description: Run the backend and frontend test suites with coverage and report results
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

Use the **tester** subagent to:
1. Check every case in `docs/TEST_PLAN.md` has a test (add missing ones).
2. Run, from `backend/`: `python -m pytest --cov=app --cov-report=term-missing`
3. Run, from `frontend/`: `npx ng test --no-watch` with the coverage flag for its runner (`--coverage` Vitest, `--code-coverage` Karma).
4. Return the TEST REPORT with the coverage table (targets: backend 85 %, frontend 80 %).

If anything fails or coverage is below target, show the report and ask the user whether to run `/fix` on it.

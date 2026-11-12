---
name: cicd
description: Set up continuous integration (GitHub Actions running the offline backend + frontend tests with coverage), backend + frontend Dockerfiles and docker-compose, and deployment + runbook docs. Use when the user wants automated testing on every push, wants to containerise, or asks how to deploy Bodhi.
argument-hint: "[ci | docker | deploy | runbook | all]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# CI / CD

What to set up: **$ARGUMENTS** (empty = `all`).

1. Use the **devops-engineer** subagent and tell it which parts to build:
   - `ci` → `.github/workflows/ci.yml`
   - `docker` → `backend/Dockerfile`, `frontend/Dockerfile`, `docker-compose.yml`, `.dockerignore` files
   - `deploy` → `docs/DEPLOYMENT.md`
   - `runbook` → `docs/RUNBOOK.md`
2. Then use the **security-auditor** subagent to check the new files for leaked secrets or
   insecure defaults (non-root user, no `.env` copied into the image).
3. Run the same commands CI will run (backend pytest with coverage, `npx ng test --no-watch`, `npx ng build`) to prove they are green.
4. Tell the user, in plain steps, how to see it work:
   - CI: create a GitHub repo, push, open the **Actions** tab.
   - Docker: `docker compose up --build`, then open the frontend URL from the compose file.

---
name: demo-prep
description: Get Bodhi ready for a client demo or class — health checks, sample workspace with documents, enabled models, the demo script with the exact questions that show Normal vs Agentic RAG, technique differences and model switching, plus a fallback plan if the internet or provider quota fails. Use before a client meeting, webinar or class.
argument-hint: "[project-name] [audience, e.g. 'pharma client' | 'students' | 'executives'] [minutes]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Demo preparation

Arguments: **$ARGUMENTS**. If the first word is a folder in `projects/`, that is the project; otherwise use the
Active project from `CLAUDE.md`. The rest is the audience and length (default: business client, 10 minutes).

1. **Health** — run `/test` (all green) and check the readiness endpoint. Stop and report if anything is red.
2. **Workspace** — confirm the sample documents for this audience are loaded (ask the user for domain documents;
   never use confidential client data without permission). Check the Vector Explorer consistency card is green.
3. **Models** — list enabled providers/models from `GET /api/models`; confirm the default model works with one live question
   (ask before using real quota).
4. **Script** — use the **tech-writer** subagent to write or tailor `docs/DEMO_SCRIPT.md` for this audience:
   - opening problem statement in business language,
   - 1 question where **Quick answer** is enough, 1 multi-part question where **Deep research** clearly wins (show the steps),
   - 1 exact-term question where **keyword/hybrid** beats **dense** (show in Retrieval Lab),
   - switch model live and compare speed/quality,
   - 1 question the documents can't answer → honest "couldn't find" (trust),
   - security & scale talking points (login, data isolation, limits, Postgres / multi-instance path) — only claims the code supports.
5. **Fallback** — note how to run with the `fake` provider (offline mode) if the network or quota fails, and say clearly
   in the demo that it is a simulated model when it is.
6. Give the user a one-screen checklist to follow on the day.

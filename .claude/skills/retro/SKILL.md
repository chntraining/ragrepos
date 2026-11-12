---
name: retro
description: Run a blameless sprint/session retrospective — what went well, what didn't, what we learned, and concrete action items (including improvements to the agents, skills or CLAUDE.md themselves). Use at the end of a sprint, session or class.
argument-hint: "[topic or time period]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Retrospective

Scope: **$ARGUMENTS** (empty = the work done in this session).

Do this yourself. Gather evidence first: this conversation, `docs/requirements/`, `docs/reviews/`,
`docs/security/`, `docs/evals/`, `CHANGELOG.md`, and `git log --oneline -20` if git exists.

Write `docs/retros/RETRO-<YYYY-MM-DD>.md` with:

1. **What we shipped** — features, fixes, test count.
2. **😀 Went well** — keep doing.
3. **😕 Didn't go well** — e.g. fix loops that took 3 rounds, review findings that kept repeating.
4. **💡 Learned** — about RAG, the code, or working with agents.
5. **🔧 Improve the system** — the most valuable part. Propose concrete edits to
   `CLAUDE.md`, an agent in `.claude/agents/`, a skill, a checklist or a hook so the same problem
   can't happen again (e.g. "review keeps flagging unescaped HTML → add it to frontend-developer.md rules").
   Show each as a short diff, and **apply only the ones the user approves**.
6. **Action items** — owner (agent or human) + due.

Blameless: describe what happened and why the system allowed it, never "who messed up".

---
name: add-retrieval-technique
description: Add a new retrieval technique to Bodhi (e.g. HyDE, parent-document, query decomposition) as one new file behind the Retriever interface — registered, selectable in the UI, visible in the Retrieval Lab, tested and evaluated. Use when the user or a student wants to try or teach a new way of finding chunks.
argument-hint: "<technique name and idea>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Add a retrieval technique

Technique: **$ARGUMENTS**

1. **Design check (architect, short)** — use the **architect** subagent only if the technique needs new stored data
   (e.g. parent chunks) or a new dependency; it writes a small ADR. Otherwise skip and say why.
2. **Build (backend-developer)** — one new file `backend/app/retrieval/<name>.py`:
   - implements the `Retriever` interface and returns `RetrievedChunk`s tagged with its name,
   - starts with the **What it does · When to use it · Trade-off** docstring in plain English,
   - respects `top_k`, document filter and owner scoping; has a fallback if an LLM call fails,
   - registered in `registry.py` with a one-line hint for the UI.
3. **UI** — nothing to build if the frontend reads techniques from `GET /api/retrieval/techniques`. If it doesn't,
   ask the **frontend-developer** to make it data-driven once (then every future technique is free).
4. **Test (tester)** — a small hand-made dataset where this technique clearly wins, plus fallback and scoping tests.
5. **Measure (ai-evaluator)** — with the user's permission, `/eval-rag --level retrieval --techniques hybrid,<name>`.
   Report hit@k and MRR before claiming it helps.
6. **Teach** — add a short section to `docs/WALKTHROUGH.md` (tech-writer) and a Retrieval Lab question that shows the difference.

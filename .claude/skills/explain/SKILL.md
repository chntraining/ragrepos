---
name: explain
description: Teach a file, function, concept or error in plain English for students — analogy first, then the real code, then a tiny exercise. Use when the user asks "what does this do?", "explain X", or wants a code walkthrough for a class.
argument-hint: "<file, function, concept or error to explain>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Explain it like a great teacher

Topic: **$ARGUMENTS** (empty = explain the whole RAG flow of this project).

Do this yourself (no subagent needed). Read the relevant files first — never explain code you haven't read.
If the app hasn't been built yet, explain from `docs/SPEC.md` and say so.

Structure your answer exactly like this:

1. **In one sentence** — what it is / does.
2. **Analogy** — a real-world comparison (e.g. embeddings = GPS coordinates for meaning;
   vector DB = a library sorted by topic instead of title; chunking = cutting a book into index cards).
3. **Where it lives** — clickable `file:line` links and how it connects to the step before and after
   in the flow `upload → load → chunk → embed → store (SQLite + ChromaDB) → retrieve (technique) → prompt → generate → show sources`.
   Where it helps, point the student at the **Retrieval Lab** or **Vector Explorer** to *see* it.
4. **The real code** — the 5–15 most important lines, with a short note on each important line.
5. **What would break if…** — one "what if we removed this?" to build intuition.
6. **Try it (2 minutes)** — one tiny exercise the student can do now (change a number, run a test, ask a question in the app).
7. **Key terms** — 3–5 words with one-line definitions.

Keep it friendly, concrete and short. No jargon without a definition.

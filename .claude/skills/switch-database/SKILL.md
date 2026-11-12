---
name: switch-database
description: Move Bodhi from SQLite to Postgres (or another SQLAlchemy-supported database), and/or from embedded ChromaDB to Chroma server mode or another vector store — with migrations, the keyword-index adapter, data migration steps, tests on the new backend and a runbook. Use when the user asks to scale up, go multi-instance, or "use Postgres / pgvector / Chroma server".
argument-hint: "<target, e.g. 'postgres' | 'chroma-server' | 'pgvector'>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Switch database / vector store

Target: **$ARGUMENTS**

Follow the **scale-up path** in `docs/SPEC.md` — only move what the load actually requires.

1. **Plan (architect)** — confirm why (load numbers from `docs/perf/` if available), what changes, and the data migration.
   A new vector-store adapter or keyword-index adapter needs an ADR.
2. **Build (backend-developer)**:
   - Postgres: new `DATABASE_URL`, driver in requirements, `alembic upgrade head`; Postgres full-text adapter for `KeywordIndex`
     (SQLite FTS5 stays for local).
   - Chroma server: switch the vector-store settings from embedded path to host/port (same adapter).
   - pgvector / other: a new adapter in `stores/` implementing `VectorStore` — business code untouched.
   - A one-off migration script (copy documents/chunks; re-embed or copy vectors) with a dry-run flag.
3. **Test (tester)** — the full suite against the new backend (CI `backend-postgres` job), plus a migration test on sample data.
4. **Operate (devops-engineer)** — compose `scale` profile, backups for the new stores, runbook update.
5. **Verify (performance-engineer)** — re-run the load test; show before → after.

If no measured need exists yet, say so and recommend staying on the simpler setup.

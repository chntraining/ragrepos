# 0001. Stack decision: pluggable database, vector store and LLM providers; LangGraph for agentic RAG

> **Kit standard — Dinesh AI Academy · Agentic Engineering Kit.** Every new project receives this file as
> `docs/adr/0001-stack-decision.md`. A project may supersede it only with its own ADR and a clear reason.

| | |
|---|---|
| **Status** | Accepted (kit standard) |
| **Date** | 2026-10-30 |
| **Deciders** | Dinesh AI Academy (course author), architect |
| **Replaces** | the earlier kit rule "plain SDKs only, no frameworks" |
| **Related** | `CLAUDE.md`, the project's `docs/SPEC.md` |

## Context
Bodhi is now a client-demo and production-grade product, not only a classroom app. New requirements:
1. Switch the **LLM provider and model** from the UI (Gemini by default, others by configuration).
2. Move from **SQLite to another database** (e.g. Postgres) without rewriting business code.
3. A real **agentic RAG** mode with visible steps, hard limits and streaming.
4. Stay **easy to read** for students and avoid over-engineering.

The earlier kit rule banned frameworks so every RAG step stayed visible. That still matters for retrieval — but
hand-writing an adapter for every LLM vendor, a SQL dialect layer and an agent state machine is exactly the
work mature libraries already do well.

## Options considered
| Option | Pros | Cons |
|---|---|---|
| A. Stay plain SDK everywhere | Maximum visibility | One adapter per provider; own SQL portability; own agent loop with limits/streaming/persistence — lots of code to maintain and secure |
| B. Full framework (LangChain chains + retrievers + agents, or LlamaIndex) | Fastest to start | Hides retrieval — the core teaching content; heavy abstractions; harder to debug |
| C. **Frameworks at the edges, our code in the middle** | Providers, DB and agent orchestration handled by proven libraries; retrieval and prompts stay hand-written | Two styles in one codebase — needs clear boundaries |

## Decision
**Option C.**
- **LangChain model integrations only** (`init_chat_model`, `Embeddings` classes, provider packages installed per enabled provider) in `providers/`.
- **LangGraph** `StateGraph` for the agentic RAG graph in `rag/agent/`.
- **SQLAlchemy 2.0 + Alembic** in `db/` — SQLite by default, Postgres via `DATABASE_URL`.
- **ChromaDB** behind our own `VectorStore` interface in `stores/`; keyword search behind `KeywordIndex`.
- **Retrieval techniques, prompts, normal RAG and the explorer stay our own code.**
- Business code never imports a vendor SDK, `chromadb` or a DB driver directly — only the adapter folders do.

## Consequences
- ✅ New provider/model = one entry in `model_catalog.yaml` (+ its LangChain package). New DB = new URL + migration run.
- ✅ Agent steps are explicit graph nodes — easy to draw, stream, test and limit.
- ✅ Tests use fake chat models / fake embeddings through the same interfaces.
- ⚠️ Library APIs change: pin versions, and check the installed version's docs before using an API.
- ⚠️ Embeddings are tied to their model: changing the embedding model needs a **re-index** (the vector collection name includes the embedding model id, so vectors never mix).
- ⚠️ SQLite and embedded Chroma are single-instance. Horizontal scale needs Postgres + Chroma server mode (or pgvector) — see SPEC "Scale-up path".

## Implementation plan
See `docs/SPEC.md` (layout, API contract, data model, agent graph) and `docs/TEST_PLAN.md`.

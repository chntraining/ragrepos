# Prompt 1 — Create an app from a requirement

> Dinesh AI Academy · Agentic Engineering Kit

You give one thing: **a requirement in plain English**. The agents ask a few questions once, then produce everything
inside `projects/<name>/` and finish with `docs/PROJECT_REPORT.md`. You choose `<name>` (lower-case letters, digits and `-`).

## In Claude Code (recommended)

```
/create-app <project-name> <your requirement>
```
Example:
```
/create-app acme-sop "A chat assistant for our QA team to search SOPs and get answers with citations"
```
Related commands: `/client-intake` runs phase 1 only (questions, requirements, SPEC, ADRs, test plan, eval set).
`/build <name>` runs phase 2 only (build, test, fix, review) on a project that has finished intake.
The full guide is [`guides/REQUIREMENT_TO_APP.md`](../guides/REQUIREMENT_TO_APP.md).

### Fill-in requirement template
Copy, fill in what you know, and delete the rest. Unknowns are fine: the team asks about them once.
Never put keys or passwords here.

```
/create-app <project-name>
Problem:       <one sentence: who struggles with what today>
Users:         <roles, how many now and in a year, how many at the same time>
Documents:     <types (PDF, DOCX, TXT, MD...), roughly how many, languages, confidential or personal data?>
Questions:     <3 to 5 real questions users will ask, with the correct answer and the source document>
AI rules:      <which providers are allowed? can documents go to a cloud AI?>
Success:       <1 or 2 numbers, e.g. "time to find an answer drops from 20 min to 2 min">
Hosting:       <laptop demo / Docker / cloud / unknown>
Brand:         <Dinesh AI Academy "Bodhi" default, or your own name and colours>
```
For a larger client project, fill in `blueprint/CLIENT_REQUIREMENTS.md` instead and pass its path:
```
/create-app <project-name> C:\work\my-requirements.md
```

### What you will be asked, and when
- **Once, in phase 1:** at most 8 questions that change the design. Say "use defaults" to accept every recommendation.
- **Before real API use:** the team asks before any evaluation that spends provider quota.

Then run the app from `projects/<name>/` (the report lists the exact commands; the standard ones are in the root `README.md`, "Quick start").

---

## Or paste this prompt into any coding agent
(Cursor, Copilot Chat, and so on. These agents will not have the kit's slash commands, so this prompt asks them to
do the work by hand.)

You are a senior full-stack and Generative-AI engineer. Build a "chat with your documents" web app inside the
folder `projects/<project-name>/`. The default product brand is **Bodhi — Agentic RAG Studio by Dinesh AI Academy**
unless the requirement says otherwise.

**Requirement:** `<paste your requirement here>`

**Read first:** `CLAUDE.md` (rules and layout). Then create these in `projects/<project-name>/docs/` before writing code:
- `docs/DESIGN_SYSTEM.md`: start from a copy of `blueprint/BRAND_DESIGN_SYSTEM.md`
- `docs/adr/0001-stack-decision.md`: a copy of `blueprint/STACK_DECISION.md`
- `docs/requirements/REQ-001-<slug>.md`: stories with Given/When/Then, non-goals, success metric
- `docs/SPEC.md`: features, API contract, data model, agent graph, limits, assumptions
- `docs/TEST_PLAN.md`: every test with a stable ID
Ask me at most 8 questions first if something would change the design. Otherwise state your assumptions in the SPEC.

**Stack**
- Frontend: Angular (standalone components, signals, SCSS)
- API: FastAPI + Pydantic v2, streaming answers over SSE
- App database: SQLAlchemy 2.0 + Alembic. SQLite by default, Postgres by changing `DATABASE_URL`
- Vector store: ChromaDB behind a `VectorStore` interface. Keyword search behind a `KeywordIndex` interface (SQLite FTS5)
- LLMs and embeddings: LangChain model integrations, with models allow-listed in `backend/model_catalog.yaml`
- Agentic RAG: a LangGraph `StateGraph` (understand, retrieve, grade, rewrite if needed, generate, verify) with hard limits
- Retrieval techniques: our own small modules, one file each: `dense`, `keyword`, `hybrid`, `mmr`, `multi_query`, `rerank`

**The user can choose, from the composer:** Normal RAG or Agentic RAG, a retrieval technique, an LLM provider and
model, and advanced settings (top-k, temperature, relevance threshold, which documents to search).
Also build the Compare, Retrieval Lab and Vector Explorer screens.

**Rules**
- Secure by design: login and roles, every query scoped to its owner, secrets only on the server, document text is data and never instructions.
- Tests never call a real LLM. Use the `fake` provider and fake embeddings.
- Follow the brand in `docs/DESIGN_SYSTEM.md`. Design every state (empty, loading, error).

**Work as a team** (the roles in `.claude/agents/`): `backend-developer` builds `backend/`, `frontend-developer` builds
`frontend/`, `tester` writes and runs the tests, `debugger` fixes hard failures. Loop developer, then tester,
until green (max 3 rounds). Targets: backend coverage 85 %, frontend 80 %.

**Finish with:** a file tree, test results with coverage, the run commands, and a list of open items.

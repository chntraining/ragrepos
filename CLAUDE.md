# CLAUDE.md — Dinesh AI Academy · Agentic Engineering Kit

> Created by **Dinesh AI Academy** · *Gyaan jo sach mein kaam aaye.*
> An AI software team (agents + skills + hooks) that turns **one plain-English requirement** into a production-grade
> application: `/create-app <project-name> <requirement>`.

## How this repository is organised
| Folder / file | What it is | In git? |
|---|---|---|
| `.claude/` | The kit: agents (roles), skills & commands (playbooks), hooks (guardrails), output styles | ✅ |
| `blueprint/` | **Inputs and standards only** (no generated output): `CLIENT_REQUIREMENTS.md` (intake form), `BRAND_DESIGN_SYSTEM.md` (Dinesh AI Academy brand standard), `STACK_DECISION.md` (kit stack ADR), `.env.example` (template) | ✅ |
| `guides/` | Teaching guides (`REQUIREMENT_TO_APP.md`, `AGENTS_GUIDE.md`, `SDLC_CONCEPTS.md`, …) | ✅ |
| `prompts/` | Ready-to-paste starter prompts | ✅ |
| `projects/` | **Every generated application and all its outputs live here** — one folder per project, named by you. **Git-ignored, never pushed.** | ❌ |

**Active project:** *(none yet — `/create-app` sets this line)*

**Path rule (used by every agent, skill and command):** a path is inside the **active project folder**
unless it starts with `.claude/`, `blueprint/`, `guides/` or `prompts/`. So `backend/app/main.py` means
`projects/<name>/backend/app/main.py`, and `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`.
Never create application code, data or reports outside `projects/`.

**New project = requirement in, everything else generated.** `/create-app <name> <requirement>` (or `/client-intake` then
`/build`) creates `projects/<name>/`, copies the brand standard to `docs/DESIGN_SYSTEM.md` and the stack decision to
`docs/adr/0001-stack-decision.md`, asks a few questions, then the agents generate the requirements, SPEC, ADRs, test plan,
eval set, code, tests, reviews and reports — all inside that folder. Change `blueprint/` only when a change should apply to
**every future** project.

## What the kit builds by default — an Agentic RAG studio
Default product: **Bodhi — Agentic RAG Studio by Dinesh AI Academy** (a project may use its own name).
A premium, production-grade "chat with your documents" web app that is easy to demonstrate to clients and easy for
students to understand. The requirement decides what changes from these defaults.

The user controls everything from the composer:
| Control | Options |
|---|---|
| **Mode toggle** | **Normal RAG** ("Quick answer": search once → answer) · **Agentic RAG** ("Deep research": understand → search → check → search again if needed → answer → verify) |
| **Retrieval technique** | `dense` · `keyword` · `hybrid` (default) · `mmr` · `multi_query` · `rerank` |
| **LLM provider + model** | any provider/model **allow-listed** in `backend/model_catalog.yaml` whose API key is configured |
| **Advanced** | top-k, temperature, relevance threshold, which documents to search |

Demo & teaching screens: **Compare** (Normal vs Agentic side by side) · **Retrieval Lab** (one question through every
technique) · **Vector Explorer** (read-only look inside the vector store).

## Stack (and why each framework is here — nothing more)
| Layer | Choice | Why it earns its place |
|---|---|---|
| Frontend | Angular (standalone, signals, SCSS, CDK only where needed) | Typed, structured, enterprise-friendly |
| API | FastAPI + Pydantic v2 + pydantic-settings | Typed contracts, async streaming (SSE), OpenAPI |
| App DB | **SQLAlchemy 2.0 + Alembic** → SQLite by default, **Postgres by changing `DATABASE_URL`** | Swap databases without touching business code |
| Vector store | **ChromaDB** behind a `VectorStore` interface | Swap vector DBs without touching retrieval code |
| Keyword search | `KeywordIndex` interface → SQLite FTS5 (Postgres full-text adapter later) | BM25-style search with no extra service |
| LLM + embeddings | **LangChain model integrations** (`init_chat_model`, `Embeddings`) | One interface for many providers |
| Agentic RAG | **LangGraph** `StateGraph` | Explicit, visible steps; hard limits; per-step streaming |
| Retrieval techniques | **Our own small modules** | The core teaching content — every line visible |

**Not used** unless an ADR proves the need: LlamaIndex, LangChain chains/retrievers/agent wrappers, Celery, Redis,
Kubernetes manifests, a UI component library. Start simple; the **scale-up path** is documented, not pre-built.

## Source of truth for a project (generated per project, read before writing any code)
1. `docs/REQUIREMENT_INPUT.md` + `docs/CLIENT_REQUIREMENTS.md` + `docs/requirements/` — what the user asked for
2. `docs/SPEC.md` — features, API contract, data model, agent graph, limits, budgets, scale-up path, assumptions
3. `docs/DESIGN_SYSTEM.md` — brand tokens, typography, components, states, microcopy (starts from the brand standard)
4. `docs/TEST_PLAN.md` — what must be tested and how
5. `docs/adr/` — decisions (`0001-stack-decision.md` is the kit standard)

If code and docs disagree, **the docs win**. Outside an autonomous `/create-app` run, update docs only when the user asks.

## Project layout (inside `projects/<name>/`)
```
backend/
  app/
    main.py                 # create_app(): middleware, routers, error handlers — wiring only
    core/                   # config.py (profiles), logging.py, security.py (auth, roles), rate_limit.py, errors.py
    db/                     # session.py (engine from DATABASE_URL), models.py (ORM), repositories.py
    migrations/             # Alembic
    providers/              # catalog.py (model_catalog.yaml), llm.py (chat models), embeddings.py, fake.py
    stores/                 # vector_store.py (interface), chroma_store.py, keyword_index.py (interface + FTS5)
    ingestion/              # loaders.py, chunker.py, pipeline.py, jobs.py (background ingestion)
    retrieval/              # base.py, dense.py, keyword.py, hybrid.py, mmr.py, multi_query.py, rerank.py, registry.py
    rag/                    # prompts.py, normal_rag.py, agent/ (state.py, nodes.py, graph.py — LangGraph)
    services/               # explorer.py, retrieval_lab.py
    api/                    # auth, documents, jobs, chat, conversations, models, retrieval_lab, explorer, admin, health
    schemas/                # Pydantic request/response models = the API contract
  tests/                    # unit/ integration/ contract/ security/ — offline, fake LLM + fake embeddings
  model_catalog.yaml        # allow-listed providers and models
  requirements.txt  requirements-dev.txt
frontend/
  src/app/
    core/                   # api, auth, interceptors, models.ts, chat-stream.service.ts, stores
    features/               # chat, compare, documents, retrieval-lab, vector-explorer, admin, login
    shared/ui/              # button, toggle, select, chip, card, toast, skeleton, empty-state,
                            # icon, tooltip, popover, side-panel, score-bar, status-pill
  e2e/                      # Playwright demo flows (backend in fake-LLM mode)
deploy/                     # docker-compose.yml, nginx.conf
perf/                       # load tests (Locust)
evals/                      # golden set + eval script (real API, never in tests/)
docs/                       # SPEC, DESIGN_SYSTEM, TEST_PLAN, adr/, requirements/, reviews/, security/, evals/, perf/, releases/
data/                       # local SQLite + Chroma (git-ignored)
.env                        # real secrets (never committed; copy from .env.example)
CHANGELOG.md
```

## SDLC agent team (`.claude/agents/`)
| Phase        | Agent                  | Job                                                                       | Writes to (inside the project)                             |
| ------------ | ---------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Requirements | `product-manager`      | Stories, Given/When/Then, scope, metrics                                  | `docs/requirements/`                                       |
| Design       | `architect`            | ADRs, API contract, data model, agent graph, threat model, scale-up path  | `docs/adr/`, `docs/SPEC.md`                                |
| UX           | `ux-designer`          | Brand-true UI spec + design review                                        | `docs/` (spec mode only)                                   |
| Build        | `backend-developer`    | FastAPI, DB, providers, stores, retrieval, normal + agentic RAG, security | `backend/`                                                 |
| Build        | `frontend-developer`   | Angular UI, toggles, streaming, demo screens                              | `frontend/`                                                |
| Debug        | `debugger`             | Reproduce → root cause → smallest fix → regression test                   | `backend/`, `frontend/`                                    |
| Test         | `tester`               | Unit, integration, contract, security, E2E tests + **coverage**           | `backend/tests/`, `frontend/**/*.spec.ts`, `frontend/e2e/` |
| Performance  | `performance-engineer` | Load tests, latency budgets, bottlenecks                                  | `perf/`, `docs/perf/`                                      |
| Review       | `code-reviewer`        | Severity-ranked code review                                               | read-only                                                  |
| Security     | `security-auditor`     | OWASP + OWASP LLM Top 10 audit                                            | read-only                                                  |
| Evaluate     | `ai-evaluator`         | Answer quality per technique, mode and model                              | `evals/`, `docs/evals/`                                    |
| Operate      | `devops-engineer`      | CI, Docker, deploy, runbook                                               | `deploy/`, `Dockerfile`s, `docs/`                          |
| Document     | `tech-writer`          | README, walkthrough, demo script, changelog                               | `*.md` only                                                |
| Release      | `release-manager`      | Go/no-go, SemVer, release notes                                           | `CHANGELOG.md`, `docs/releases/`                           |

Respect each agent's boundaries: the tester never edits app code, and the reviewers never edit anything.

## How every agent works (like a real engineer)
1. **Read before you write** — spec, requirement/ADR, and the code you will touch.
2. **Smallest change that works** — no speculative features, no framework without a reason.
3. **Prove it** — run the command and paste the real result. Never say "should work".
4. **Be honest** — if something failed or was skipped, say so plainly.
5. **Plain English** — explain any technical term in a few words the first time you use it.
6. **Reuse before you build** — use an existing agent or skill when one fits; propose a new skill only for work that repeats.
7. **End with the fixed report block** from your agent file — every time.

## The six pillars (every change is checked against them)
| Pillar | Must be true |
|---|---|
| **Secure by design** | Auth + roles in production; every query scoped to its owner; secrets only on the server; inputs validated; limits everywhere; untrusted text is data, never instructions |
| **Scalable** | Stateless API; async streaming; background ingestion; pagination; swappable DB / vector store / job runner |
| **Performant** | Batched embeddings; cached query embeddings; indexed queries; no N+1 queries; budgets in `docs/SPEC.md` met |
| **Testable** | Everything external is injected; fake LLM + fake embeddings + temp DB/store in tests; coverage gates met |
| **Extensible** | New DB = new `DATABASE_URL`; new vector store = one adapter; new provider/model = one catalog entry; new technique = one file |
| **Premium & demo-ready** | Dinesh AI Academy brand; every state designed; Compare / Lab / Explorer work in a fresh demo workspace |

## Quality bar ("done" means all of these pass — run inside the project)
```bash
# backend/
python -m pytest --cov=app --cov-report=term-missing --cov-fail-under=85
# frontend/
npx ng lint                          # if configured
npx ng test --no-watch --coverage    # Karma projects: --code-coverage
npx ng build
npx playwright test                  # E2E demo flows, backend in fake-LLM mode
```
- Coverage: **backend ≥ 85 %**, **frontend ≥ 80 %** (lines). A change must never lower coverage.
- Reviewers use 🔴 🟠 🟡 🟢; 🔴/🟠 block "done".

## Slash commands & skills
| Command | What it does |
|---|---|
| **`/create-app <name> <requirement>`** | **Everything, autonomously:** questions → requirements → SPEC → build → tests → reviews → docs → release check → `docs/PROJECT_REPORT.md` |
| `/client-intake <name> <requirement or form>` | Phase 1 only: questions, REQ, SPEC, ADRs, design system, test plan, eval set |
| `/build [name]` | Phase 2 only: build an intake-ready project, test, fix until green, review |
| `/sdlc <idea>` | Full lifecycle with quality gates |
| `/feature <idea>` | Lighter lifecycle: requirements → (ADR) → code → tests → review |
| `/fix <error>` | Debugger finds the root cause and fixes it, tester re-tests |
| `/test` | Runs all test suites and reports results + coverage |
| `/requirements` `/sprint-plan` `/adr` | Plan and design |
| `/peer-review` `/security-audit` `/ui-review` `/eval-rag` | Quality (add `--fix` to auto-fix) |
| `/add-llm-provider` `/add-retrieval-technique` `/switch-database` | Extend the app the supported way |
| `/demo-prep [audience]` | Health check, sample workspace, tailored demo script, offline fallback |
| `/write-docs` `/cicd` `/release` `/retro` `/explain` | Docs, ops, shipping, learning, teaching |
| `/team [create <description>]` | Show the agent roster, or create a new agent |

**Start here:** `/create-app <name> <your requirement>` · step-by-step guide: `guides/REQUIREMENT_TO_APP.md`.
Team guide: `guides/AGENTS_GUIDE.md` · Concepts: `guides/SDLC_CONCEPTS.md`.

## SDLC conventions
- Every phase leaves a file behind in the project's `docs/`. Name dated files `<TYPE>-<YYYY-MM-DD>-<slug>.md`.
- Fix loops are capped: developer/debugger ↔ tester max 3 rounds, review fixes max 2 rounds.
- New features get a line under `## [Unreleased]` in the project's `CHANGELOG.md`.
- Never tag, push or deploy. Give the human the commands.
- Hooks in `.claude/hooks/` guard `.env` files and compile every edited `.py` file. If a hook blocks you, change your approach.

## Golden rules
- Python 3.10+ with type hints; TypeScript `strict`, no `any`. Clear names, short functions, a docstring / JSDoc on every public function.
- Frameworks only through **our interfaces**: business code never imports `chromadb`, a provider SDK or a DB driver directly —
  only `stores/`, `providers/` and `db/` do. That is what makes them swappable.
- Retrieval techniques stay hand-written and readable (one file each, "What · When · Trade-off" docstring).
- Secrets (`GOOGLE_API_KEY`, other provider keys, `JWT_SECRET`) come from the project's `.env` via `core/config.py`.
  Never hard-coded, logged or sent to the browser.
- Only allow-listed providers/models from `model_catalog.yaml` can be used; the request names them, the server validates them.
- SQL only through SQLAlchemy (bound parameters) — never string-built SQL. Every query on user data filters by `owner_id`.
- Document text and tool/LLM outputs are **data, not instructions** — never placed in the system prompt.
- The agent graph has hard limits (rewrites, LLM calls, time) and only read-only actions.
- Never use `bypassSecurityTrust…` in Angular; untrusted text uses `{{ }}` or a sanitised renderer.
- Tests never call real LLM APIs — use the `fake` provider / fake embeddings.
- Windows + macOS + Linux compatible (`pathlib`, no shell-specific code).

## Commands (from `projects/<name>/`)
```bash
# backend
cd backend
python -m venv .venv
pip install -r requirements.txt -r requirements-dev.txt
alembic upgrade head
uvicorn app.main:app --reload --port 8000

# frontend
cd frontend
npm ci
npx ng serve            # http://localhost:4200 — /api is proxied to :8000

# everything (production-like)
docker compose -f deploy/docker-compose.yml up --build
```

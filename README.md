# Dinesh AI Academy · Agentic Engineering Kit

> **Bodhi — Agentic RAG Studio by Dinesh AI Academy**
> *Gyaan jo sach mein kaam aaye.*

An AI software team for [Claude Code](https://claude.com/claude-code): 14 specialist agents, a set of skills, and safety hooks.
Give it **one requirement in plain English** and it asks a few questions, then builds, tests, reviews and documents a
production-style "chat with your documents" application. The default product brand is **Bodhi**.

> **Status:** this repository holds the kit only: agents, skills, hooks, standards and guides. **No application code
> and no generated specs exist here.** Running `/create-app <name> <requirement>` makes the kit write everything into
> `projects/<name>/`, so every run starts fresh.

---

## What the kit builds

**Bodhi** is a web app where a user uploads documents, then asks questions and gets answers with numbered citations.
The user chooses how the answer is made:

| Control | Options |
|---|---|
| **Mode** | **Normal RAG** ("Quick answer": search once, then answer) or **Agentic RAG** ("Deep research": understand, search, check, search again if needed, answer, verify) |
| **Retrieval technique** | `dense`, `keyword`, `hybrid` (default), `mmr`, `multi_query`, `rerank` |
| **LLM provider and model** | Any provider/model in the allow-list `backend/model_catalog.yaml` whose API key is set |
| **Advanced** | top-k, temperature, relevance threshold, which documents to search |

Three screens help you demo and teach: **Compare** (Normal vs Agentic side by side), **Retrieval Lab**
(one question through every technique) and **Vector Explorer** (a read-only look inside the vector store).

**Stack:** Angular, FastAPI, SQLAlchemy (SQLite by default, Postgres by changing `DATABASE_URL`), ChromaDB,
LangChain model integrations and LangGraph for the agentic mode. The reasons for these choices are in
[`blueprint/STACK_DECISION.md`](blueprint/STACK_DECISION.md) and [`CLAUDE.md`](CLAUDE.md). Each project gets its own
`docs/SPEC.md`.

*RAG = Retrieval-Augmented Generation: look up the most relevant pieces of your documents, then let the AI answer from them.*

---

## Who it is for

| You are | Use the kit to |
|---|---|
| **A student** | Watch a real software team (as agents) work, and read the guides in [`guides/`](guides/) |
| **An engineering team** | Start a new RAG app from a spec with tests, reviews and security checks built into the workflow |
| **Presenting to a client** | Create an app from the client's requirement, then run `/demo-prep <name>` to get a sample workspace and a demo script |

---

## Start here

Type one command in Claude Code, in this folder:

```
/create-app <project-name> <your requirement in plain English>
```
For example:
```
/create-app acme-sop "A chat assistant for our QA team to search SOPs and get answers with citations"
```
You can also pass the path to a filled copy of the intake form
[`blueprint/CLIENT_REQUIREMENTS.md`](blueprint/CLIENT_REQUIREMENTS.md) instead of text.

The team asks a few questions once (and asks permission before spending real API quota). Then it works on its own:
requirements, SPEC, decisions, design, test plan, backend, frontend, tests, reviews, docs and a release check, all inside
`projects/<project-name>/`. It ends with `docs/PROJECT_REPORT.md`: what was built, the proof, and the open items.

Prefer to go step by step? `/client-intake` runs phase 1 only (questions, requirements, SPEC, ADRs, test plan, eval set).
`/build` runs phase 2 only (build, test, fix, review) on a project that has finished intake.
Full guide: [`guides/REQUIREMENT_TO_APP.md`](guides/REQUIREMENT_TO_APP.md).

---

## Quick start

**You need:** [Claude Code](https://claude.com/claude-code), Python 3.10+, Node.js with npm, and an API key for at least one
LLM provider. The default is Google Gemini; get a key at https://aistudio.google.com/apikey.

**1. Open Claude Code in this folder and create the app.**
```
/create-app my-first-app "Chat with my course notes and get answers with citations"
```
Answer the few questions (or say "use defaults"). The kit creates `projects/my-first-app/`, builds the backend and
frontend, runs the tests, fixes failures (up to 3 rounds), reviews the result and writes `docs/PROJECT_REPORT.md`.
Replace `my-first-app` with your own project name. There is no default project.

**2. Add your keys.** From `projects/<name>/`, copy `.env.example` to `.env` and fill in `GOOGLE_API_KEY`,
`JWT_SECRET` and the admin password.

- Windows: `copy .env.example .env`
- macOS / Linux: `cp .env.example .env`

**3. Run the backend** (from `projects/<name>/`).
```bash
cd backend
python -m venv .venv
```
Activate the environment: Windows `.venv\Scripts\activate`, macOS / Linux `source .venv/bin/activate`. Then:
```bash
pip install -r requirements.txt -r requirements-dev.txt
alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

**4. Run the frontend** (a second terminal, from `projects/<name>/`).
```bash
cd frontend
npm ci
npx ng serve
```
Open http://localhost:4200. The `/api` path is proxied to port 8000.

**Or run everything with Docker** (from `projects/<name>/`):
```bash
docker compose -f deploy/docker-compose.yml up --build
```

**5. Test it** (from `projects/<name>/`).
```bash
cd backend
python -m pytest --cov=app --cov-fail-under=85
```
The tests use a fake LLM and fake embeddings, so they never call a real provider. Frontend and end-to-end
commands are listed in [`CLAUDE.md`](CLAUDE.md#quality-bar-done-means-all-of-these-pass--run-inside-the-project).

---

## What is in this repository

| Folder / file | What it is | In git? |
|---|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Project memory: rules every agent follows | Yes |
| `.claude/` | The kit: agents, skills, commands, hooks, output styles | Yes |
| [`blueprint/`](blueprint/) | **Inputs and standards only**, no generated output: `CLIENT_REQUIREMENTS.md` (intake form), `BRAND_DESIGN_SYSTEM.md` (Dinesh AI Academy brand standard), `STACK_DECISION.md` (the kit's stack decision), `.env.example` | Yes |
| [`guides/`](guides/) | Teaching guides | Yes |
| [`prompts/`](prompts/) | Ready-to-paste prompts for any coding agent | Yes |
| [`projects/`](projects/README.md) | Every generated app and all its outputs, one folder per project, named by you. **Git-ignored, never pushed** | No |
| [`CHANGELOG.md`](CHANGELOG.md) | History of the kit | Yes |

**What a new project gets.** `/create-app` (or `/client-intake`) creates `projects/<name>/`, copies
`blueprint/BRAND_DESIGN_SYSTEM.md` to `docs/DESIGN_SYSTEM.md` and `blueprint/STACK_DECISION.md` to
`docs/adr/0001-stack-decision.md`, and the agents generate the rest there: requirements, SPEC, more ADRs, test plan, eval
set, code, tests, reviews and reports. Change `blueprint/` only when a change should apply to **every future** project.

**Path rule:** a path in an agent or skill refers to the active project (`projects/<name>/`) unless it starts with
`.claude/`, `blueprint/`, `guides/` or `prompts/`.

---

## The team (14 agents)

| Phase | Agent | Job |
|---|---|---|
| Requirements | `product-manager` | Stories, Given/When/Then, scope, metrics |
| Design | `architect` | ADRs, API contract, data model, agent graph, scale-up path |
| UX | `ux-designer` | Brand-true UI spec and design review |
| Build | `backend-developer` | FastAPI, database, providers, stores, retrieval, Normal and Agentic RAG |
| Build | `frontend-developer` | Angular UI, mode and model pickers, streaming, Compare, Retrieval Lab, Vector Explorer |
| Debug | `debugger` | Reproduce, find the root cause, smallest fix, regression test |
| Test | `tester` | Unit, integration, contract, security and E2E tests, with coverage |
| Performance | `performance-engineer` | Load tests, latency budgets, bottlenecks (reports only) |
| Review | `code-reviewer` | Severity-ranked code review (read-only) |
| Security | `security-auditor` | OWASP and OWASP LLM Top 10 audit (read-only) |
| Evaluate | `ai-evaluator` | Answer quality per technique, mode and model |
| Operate | `devops-engineer` | CI, Docker, deployment, runbook |
| Document | `tech-writer` | README, walkthrough, user guide, demo script, changelog |
| Release | `release-manager` | Go/no-go, version number, release notes |

Each agent has one job and limited file access. For example, the tester never edits app code and the reviewers edit nothing.

---

## Commands

Type these in Claude Code. `/team` shows the live roster.

| Command | What it does |
|---|---|
| **`/create-app <name> <requirement>`** | **The main entry point.** Questions once, then requirements, SPEC, build, tests, reviews, docs, release check and `docs/PROJECT_REPORT.md`, all in `projects/<name>/` |
| `/client-intake <name> <requirement or form>` | Phase 1 only: questions, requirements, SPEC, ADRs, design system, test plan, eval set |
| `/build [name]` | Phase 2 only: build an intake-ready project, test, fix until green, review |
| `/sdlc <idea>` | Full lifecycle with quality gates, from idea to release check |
| `/feature <idea>` | Lighter lifecycle: requirements, design if needed, code, tests, review |
| `/fix <error>` | Debugger finds the root cause and fixes it; tester re-tests |
| `/test` | Run all test suites and report results and coverage |
| `/requirements` `/sprint-plan` `/adr` | Plan and design |
| `/peer-review` `/security-audit` `/ui-review` `/eval-rag` | Quality checks (add `--fix` to apply fixes) |
| `/add-llm-provider` `/add-retrieval-technique` `/switch-database` | Extend the app the supported way |
| `/demo-prep [audience]` | Health check, sample workspace, demo script, offline fallback |
| `/write-docs` `/cicd` `/release` `/retro` `/explain` | Docs, ops, shipping, learning, teaching |
| `/team [create <description>]` | Show the roster, or create a new agent |

New here? Read [`guides/AGENTS_GUIDE.md`](guides/AGENTS_GUIDE.md), then [`guides/SDLC_CONCEPTS.md`](guides/SDLC_CONCEPTS.md).
Not using Claude Code? Copy a prompt from [`prompts/`](prompts/) into any coding agent.

---

## The six pillars

Every change is checked against these.

| Pillar | Must be true |
|---|---|
| **Secure by design** | Login and roles; every query scoped to its owner; secrets stay on the server; inputs validated; document text is data, never instructions |
| **Scalable** | Stateless API; streaming; background ingestion; swappable database, vector store and job runner |
| **Performant** | Batched embeddings; cached query embeddings; indexed queries; latency budgets in the SPEC |
| **Testable** | Fake LLM and fake embeddings in tests; coverage gates (backend 85 %, frontend 80 %) |
| **Extensible** | New database = a new `DATABASE_URL`; new model = one catalog entry; new technique = one file |
| **Premium and demo-ready** | Dinesh AI Academy brand; every UI state designed; Compare, Lab and Explorer work in a demo workspace |

## Guardrails

Hooks in `.claude/hooks/` block access to `.env` files, compile every edited Python file and catch pasted API keys.
The **Mentor** output style (`/config`, then Output style) makes Claude explain each step for students.
Agents never push, tag or deploy; they give you the commands.

---

## Guides

| Guide | Read it to learn |
|---|---|
| [`guides/REQUIREMENT_TO_APP.md`](guides/REQUIREMENT_TO_APP.md) | **Start here:** requirement to a running app, with `/create-app` or step by step |
| [`guides/AGENTS_GUIDE.md`](guides/AGENTS_GUIDE.md) | How to use the team, plus a class demo script |
| [`guides/SDLC_CONCEPTS.md`](guides/SDLC_CONCEPTS.md) | The SDLC, agents, skills, hooks |
| [`guides/AGENTS_VS_SKILLS.md`](guides/AGENTS_VS_SKILLS.md) | The difference between an agent and a skill |
| [`guides/AGENT_PROMPTS.md`](guides/AGENT_PROMPTS.md) | What to type for each agent |
| [`guides/SDLC_STEP_BY_STEP.md`](guides/SDLC_STEP_BY_STEP.md) | One feature through every agent, with checks |
| [`guides/SDLC_WORKED_EXAMPLE.md`](guides/SDLC_WORKED_EXAMPLE.md) | A narrated example with sample output |
| [`.claude/skills/README_When_to_Use_Skills.md`](.claude/skills/README_When_to_Use_Skills.md) | When to make a skill, and when not to |

---

*Created by **Dinesh AI Academy**, an applied AI education, engineering and consulting academy founded by Dinesh Kushwaha.
More at https://dineshaiacademy.com.*
*Gyaan jo sach mein kaam aaye.*

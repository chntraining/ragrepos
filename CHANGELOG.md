# Changelog

All notable changes to the **Dinesh AI Academy · Agentic Engineering Kit** are recorded here.
(Each generated project, such as `projects/acme-sop/`, keeps its own `CHANGELOG.md`.)
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · Versioning: [SemVer](https://semver.org/).

## [Unreleased]

### Added
- **`/create-app <project-name> <requirement>`**: the new main entry point. The only input is the requirement, in plain
  English or as a path to a filled intake form. The agents ask a few questions once (the only interactive stop, plus
  permission before spending real API quota), then work autonomously and write everything inside
  `projects/<project-name>/`: requirements, SPEC, ADRs, design system, test plan, eval set, code, tests, reviews,
  documentation, a release check and a final `docs/PROJECT_REPORT.md`.
- **Bodhi spec, now generated per project:** **Bodhi — Agentic RAG Studio by Dinesh AI Academy** remains the default
  product brand. It describes Normal and Agentic RAG, six retrieval techniques, a switchable provider and model, and the
  Compare, Retrieval Lab and Vector Explorer screens. The SPEC is written for each project by the architect.
- **`blueprint/BRAND_DESIGN_SYSTEM.md` and `blueprint/STACK_DECISION.md`:** the Dinesh AI Academy brand standard and the
  kit's stack decision, kept as standards. Each new project gets copies as `docs/DESIGN_SYSTEM.md` and
  `docs/adr/0001-stack-decision.md`.
- **New stack in the spec:** Angular, FastAPI, SQLAlchemy (SQLite, Postgres by changing `DATABASE_URL`), ChromaDB,
  LangChain model integrations and LangGraph for agentic RAG.
- **3 new agents:** `backend-developer`, `frontend-developer` and `debugger`.
- **5 new skills:** `/add-llm-provider`, `/add-retrieval-technique`, `/switch-database`, `/demo-prep` and `/client-intake`.
- **Client intake:** the form `blueprint/CLIENT_REQUIREMENTS.md` and the guide `guides/REQUIREMENT_TO_APP.md`
  (now rewritten around `/create-app`, with the step-by-step route as Option B).
- **Projects folder:** every generated app lives in `projects/<name>/`, named by the user. The folder is git-ignored
  and never pushed. There is no default project any more.
- Rewritten root `README.md`, starter prompts in `prompts/` and teaching guides in `guides/` for Bodhi.
- Full SDLC agent team, SDLC skills, safety hooks and the Mentor output style.
- RAG evaluation harness. The golden set of questions is now written per project, in `evals/golden_set.jsonl`.

### Changed
- **`/client-intake` reworked:** it is now phase 1 of `/create-app`. It creates `projects/<name>/`, copies in the standards,
  asks at most 8 questions once, then writes the requirements, SPEC, ADRs, design system, test plan and eval set
  from scratch, and runs one consistency check across them.
- **`/build` reworked:** it is now phase 2 only. It needs an intake-ready project (`docs/SPEC.md`, `docs/DESIGN_SYSTEM.md`,
  `docs/TEST_PLAN.md`, `docs/adr/`) and runs `/client-intake` first if they are missing. It no longer assumes a project
  called `bodhi`.
- **`blueprint/` now holds inputs and standards only:** `CLIENT_REQUIREMENTS.md`, `BRAND_DESIGN_SYSTEM.md`,
  `STACK_DECISION.md` and `.env.example`. Generated documents are never kept there.
- **Docs updated for the one-command flow:** `README.md`, `prompts/01_BUILD_APP.md` (now the `/create-app` prompt with a
  requirement template), `guides/REQUIREMENT_TO_APP.md` and the other guides. Hard-coded `projects/bodhi/` and
  `/build bodhi` were replaced with `projects/<name>/` and named examples.
- **Restructure:** specs first moved to `blueprint/` (later reduced to inputs and standards, see above), teaching guides to `guides/`, and generated apps to `projects/`.
  Paths in agents, skills and commands now refer to the active project unless they start with `.claude/`,
  `blueprint/`, `guides/` or `prompts/`.
- **Team of 14:** `performance-engineer` joins the team, and the single `developer` agent is replaced by
  `backend-developer`, `frontend-developer` and `debugger`.
- `/fix` now starts with the `debugger`; `/build` builds backend and frontend and runs a performance review.
- **Branding:** the kit is now the Dinesh AI Academy · Agentic Engineering Kit, and the app is named Bodhi
  (it was Lumen in the first version).
- Quality bar: backend coverage at least 85 %, frontend coverage at least 80 %.

### Removed
- **Clean-up of generated outputs, so every run starts fresh.** These were deleted at the user's request:
  the generated `blueprint/SPEC.md`, `blueprint/TEST_PLAN.md`, `blueprint/golden_set.jsonl`, the sample requirements
  (`blueprint/requirements/`, REQ-001 and REQ-002), the sample ADRs (`blueprint/adr/`, ADRs 0001, 0002 and 0004) and the old
  v1 (Streamlit) history in `guides/archive/`. Reason: so every run starts fresh.
  Each project now generates its own, and nothing in the kit links to the deleted files.
- The first (Streamlit) version of the app description. Its old docs were removed with `guides/archive/`.

## [0.1.0] - 2026-10-15

### Added
- Project template: specs (`SPEC.md`, `DESIGN_SYSTEM.md`, `TEST_PLAN.md`), developer and tester agents, and the
  `/build`, `/fix`, `/test` and `/feature` commands. (In this first version the app was a Streamlit app called Lumen.)

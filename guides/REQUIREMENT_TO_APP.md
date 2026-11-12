# From Requirement to a Running Agentic RAG App

> Dinesh AI Academy · Agentic Engineering Kit · *Gyaan jo sach mein kaam aaye.*
>
> For: anyone running the kit — trainers, students, engineers, consultants. No prior Claude Code experience needed.
> Default product brand: **Bodhi — Agentic RAG Studio by Dinesh AI Academy**.

You give the kit **one thing: a requirement in plain English**. The agents ask a few questions, then build,
test, review and document the app inside `projects/<name>/`. You choose the project name.

There are two ways to run it:

| | Command | Use it when |
|---|---|---|
| **Option A (recommended)** | `/create-app <name> <requirement>` | You want the whole journey in one go |
| **Option B** | `/client-intake`, then `/build`, then the later steps by hand | You want to check each hand-off, or you are teaching |

---

## Before you start (one time)
1. Install Python 3.10+, Node.js LTS and Claude Code (VS Code extension or terminal). Git is optional.
2. Open this repository folder in Claude Code.
3. Type `/team`. You should see 14 agents.
4. Have an API key ready for at least one LLM provider (the default is Google Gemini). You add it to the project's
   `.env` file later. **Never paste keys or passwords into the requirement.**

---

## Option A (recommended): `/create-app <name> <requirement>`

```
/create-app acme-sop "A chat assistant for our QA team to search SOPs and get answers with citations"
```

- `<name>`: lower-case letters, digits and `-` (for example `acme-sop`). If you leave it out or it is invalid, the kit
  suggests one.
- `<requirement>`: plain English, or the path to a filled copy of `blueprint/CLIENT_REQUIREMENTS.md`.
- If you give no requirement, the kit asks for one in a single sentence.

### What happens, phase by phase
The lead prints one status line per phase, for example `✅ Phase 3/10 — Design: SPEC + 2 ADRs written`.

| Phase | Who does it | What you get |
|---|---|---|
| **1. Discovery and design** (runs `/client-intake`) | product-manager, architect, ux-designer, tester, ai-evaluator | Project folder, questions to you, requirements, SPEC, ADRs, design system, test plan, eval set, and a consistency check between them |
| **2. Build, test, fix, review** (runs `/build`) | backend-developer, frontend-developer, tester, debugger, then code-reviewer, security-auditor, ux-designer, performance-engineer | Backend and frontend code, all test suites with coverage, fixes (max 3 rounds), review reports |
| **3. Evaluate answer quality** | ai-evaluator | Offline check of the eval set. Real-API scoring only if you agree |
| **4. Documentation** | tech-writer | `README.md`, user guide, walkthrough, demo script, extending guide, `CHANGELOG.md` (all inside the project) |
| **5. Release readiness** | release-manager | Go / no-go and version `0.1.0` for a first build. It never tags or pushes |
| **6. Final report** | engineering lead | `docs/PROJECT_REPORT.md` and a short summary in chat |

### What questions to expect
There is **one interactive stop**, in Phase 1, plus one permission request later.

1. **Discovery questions (once).** The product-manager fills the intake form from your requirement and the kit defaults,
   then asks **at most 8 questions** that would change the design (for example: how many users, which documents,
   can documents go to a cloud AI, which providers). You see up to 4 questions per batch, at most 2 batches, with a
   recommended answer first. Say **"use defaults"** to accept all recommendations.
2. **Permission before spending quota.** In Phase 3, real-API evaluation runs only if the project's `.env` has a
   provider key **and** you agree. If you skip it, the report gives the command to run later.

After that the team works on its own. Decisions it makes alone are recorded as ADRs marked
`Accepted (autonomous run <date>, delegated by the user)` and listed in the report for you to review. Anything that
needs money, credentials, or a legal or compliance claim is **not** decided for you: it becomes an open item.

### Where each output lands
All paths are inside `projects/<name>/`. The folder is git-ignored and never pushed.

| Output | Path |
|---|---|
| Your requirement, verbatim | `docs/REQUIREMENT_INPUT.md` |
| Filled intake form (with your answers) | `docs/CLIENT_REQUIREMENTS.md` |
| Requirements and acceptance criteria | `docs/requirements/REQ-001-<slug>.md` |
| Specification (features, API, data model, agent graph, limits) | `docs/SPEC.md` |
| Decisions | `docs/adr/` (`0001-stack-decision.md` is the kit standard; more are added per project) |
| Design system (brand standard plus this project's screens) | `docs/DESIGN_SYSTEM.md` |
| Test plan | `docs/TEST_PLAN.md` |
| Evaluation questions and sample documents | `evals/golden_set.jsonl`, `evals/fixtures/` |
| Application code | `backend/`, `frontend/`, `deploy/`, `perf/` |
| Tests | `backend/tests/`, `frontend/**/*.spec.ts`, `frontend/e2e/` |
| Reviews, security, performance | `docs/reviews/`, `docs/security/`, `docs/perf/` |
| User docs and demo script | `README.md`, `docs/USER_GUIDE.md`, `docs/WALKTHROUGH.md`, `docs/DEMO_SCRIPT.md`, `docs/EXTENDING.md` |
| Release notes | `CHANGELOG.md`, `docs/releases/` |
| **The final report** | **`docs/PROJECT_REPORT.md`** |
| Settings template | `.env.example` (copy to `.env`) |

### Review `docs/PROJECT_REPORT.md` first
Open it before you run anything. It has these sections:

| Section | What to check |
|---|---|
| What was asked | Is your requirement quoted correctly? |
| What was decided | Your answers, plus one line for every autonomous ADR. Disagree with one? Tell the team. |
| What was built | Screens, endpoints, techniques, modes, models |
| Proof | Test counts per suite, coverage (target: backend 85 %, frontend 80 %), E2E result, review and security verdicts |
| Answer quality | Eval scores, or "not run" with the command to run it |
| Open items | Anything not done, every warning, every decision that needs a human. **Read this section carefully** |
| Run it | The exact commands and which `.env` values to fill |
| Next | Suggested next commands, such as `/demo-prep <name>` |

If a phase failed after its fix-loop limit, the team continues with the phases that do not depend on it and says so
in the report. It does not claim "done" when something is red.

### Run the app afterwards
From `projects/<name>/`:

1. Copy `.env.example` to `.env`. Windows: `copy .env.example .env`. macOS / Linux: `cp .env.example .env`.
   Fill in `GOOGLE_API_KEY` (or your provider's key), `JWT_SECRET` (long random text) and `ADMIN_PASSWORD`.
2. Backend:
   ```bash
   cd backend
   python -m venv .venv
   ```
   Activate it (Windows `.venv\Scripts\activate`, macOS / Linux `source .venv/bin/activate`), then:
   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
   alembic upgrade head
   uvicorn app.main:app --reload --port 8000
   ```
3. Frontend, in a second terminal:
   ```bash
   cd frontend
   npm ci
   npx ng serve
   ```
   Open http://localhost:4200.
4. Log in with the admin account, upload a document, ask a question in **Quick answer**, then in **Deep research**.

Or run everything with Docker: `docker compose -f deploy/docker-compose.yml up --build`.
The commands above come from `CLAUDE.md`. If `PROJECT_REPORT.md` lists different commands for your project, follow the report.

### Example requirements (three sizes)

**1. One-liner.** The kit fills the gaps with its defaults and asks only what matters.
```
/create-app course-notes "Let students upload lecture notes and ask questions with citations"
```

**2. A paragraph.** Better: it states users, documents and a success measure.
```
/create-app acme-sop "Our QA team of about 30 people spends hours searching SOPs (PDF and DOCX, around 400
documents, English). Build a chat app where they ask a question and get an answer with citations to the exact
SOP. Documents must not leave our network, so no cloud AI. Success: time to find an answer drops from 20 minutes
to 2 minutes."
```
Because the paragraph says "no cloud AI", expect a question or ADR about local models (for example Ollama).

**3. A filled form.** Best for a real client. Copy `blueprint/CLIENT_REQUIREMENTS.md` outside the repository
if it holds client details, fill it in **with the client**, then:
```
/create-app acme-sop C:\work\acme-requirements.md
```
Sections that matter most: 1 (problem and success number), 3 (are documents confidential?), **4 (10 to 20 real
questions with correct answers, which become the eval set)** and 6 (which AI providers are allowed). Leave `?` where nobody
knows yet; each `?` becomes a question. Never put real keys or passwords in the file.

---

## Option B: step by step

Use this to learn, or when you want to approve each hand-off. Replace `acme-sop` with your project name.

```
 Requirement
     │
 1 INTAKE ──────── /client-intake ──► projects/<name>/ with requirements, SPEC, ADRs, design system, test plan, eval set
 2 ANSWER ──────── you ─────────────► the agents' questions (asked once)
 3 BUILD ───────── /build <name> ───► backend/ + frontend/, tests green, reviews
 4 EVAL ────────── /eval-rag ───────► docs/evals/EVAL-<date>.md
 5 DEMO ────────── /demo-prep ──────► docs/DEMO_SCRIPT.md + checklist
 6 RELEASE ─────── /release ────────► go / no-go + release notes
```

### Step 1 — Intake
```
/client-intake acme-sop "A chat assistant for our QA team to search SOPs"
```
(or pass the path to a filled form instead of text)

**What happens.** The kit creates `projects/acme-sop/`, copies in the standards
(`blueprint/BRAND_DESIGN_SYSTEM.md` becomes `docs/DESIGN_SYSTEM.md`, `blueprint/STACK_DECISION.md` becomes
`docs/adr/0001-stack-decision.md`, plus the intake form and `.env.example`), and saves your requirement in
`docs/REQUIREMENT_INPUT.md`. Then, in order:

| Step | Agent | Output |
|---|---|---|
| Discovery | product-manager | Filled form, at most 8 questions |
| Questions | you | Answers written into `docs/CLIENT_REQUIREMENTS.md` |
| Requirements | product-manager | `docs/requirements/REQ-001-<slug>.md` (stories with Given/When/Then, non-goals) |
| Design | architect | `docs/SPEC.md` and an ADR for every decision that differs from the stack decision |
| UX | ux-designer | `docs/DESIGN_SYSTEM.md` extended for this project's screens |
| Test plan and eval set | tester, ai-evaluator (in parallel) | `docs/TEST_PLAN.md`, `evals/golden_set.jsonl` (no API calls) |
| Consistency check | tester, then architect and ux-designer fix | One round; leftovers become explicit assumptions in the SPEC |

**Check:** the summary lists what you decided versus what is a default, the assumptions and the open risks.
If the project already exists, the kit reuses it and does not overwrite its docs.

### Step 2 — Answer the questions
Answer the batch of questions in Claude Code, or say **"use defaults"**. For a real client, send the questions to the
client first. **Check:** no open question blocks the build.

### Step 3 — Build
```
/build acme-sop
```
The **backend-developer** and **frontend-developer** build, the **tester** writes and runs every test in the test plan,
the **debugger** fixes what fails (max 3 rounds), then the reviewers check the result in parallel and one fix round
handles 🔴 findings. `/build` needs the intake docs (SPEC, design system, test plan, ADRs); if they are missing, it runs `/client-intake` first and asks you for the requirement.
Run the app as described under Option A.

**Check:** the summary shows tests green and coverage of at least 85 % backend and 80 % frontend.
Run the quality gates again after changes:

| Command | Agent | Must be |
|---|---|---|
| `/peer-review` | code-reviewer | APPROVE (no 🔴 or 🟠) |
| `/security-audit` | security-auditor | not FAIL; every query scoped to its owner |
| `/ui-review` | ux-designer | score 8 or more, no "Must fix" |
| "Use the performance-engineer agent" | performance-engineer | budgets in the SPEC met |

Something broken? `/fix <paste the error>`. The **debugger** reproduces it, fixes the root cause and adds a test.

### Step 4 — Prove it on real questions
```
/eval-rag --level retrieval      (cheap: no answers generated)
/eval-rag --mode both            (full answers; uses real API quota, it asks first)
```
**Check:** the report meets the success metric from your requirement. If not, follow its single recommendation and
re-run, one change at a time.

### Step 5 — Prepare the demo
```
/demo-prep acme-sop pharma 10
```
You get `docs/DEMO_SCRIPT.md` with the questions that show Quick answer versus Deep research, keyword versus meaning
search, model switching, an honest "couldn't find", and an offline fallback plan.

### Step 6 — Release
```
/release
```
The **release-manager** checks every gate and gives a GO or NO-GO with reasons. It prints the git commands but never
pushes. `projects/` is git-ignored, so give a client project its **own private repository**.

---

## Cheat sheet — what to give each agent
| Agent | Give it | You get back |
|---|---|---|
| product-manager | the requirement (or a filled form) | REQ doc and open questions |
| architect | the REQ doc | SPEC and ADRs |
| ux-designer | REQ doc and "Specify" or "Review" | UX spec or UX report with a score |
| backend-developer / frontend-developer | REQ and ADR paths | code and verification output |
| debugger | the error text or "expected X, got Y" | root cause, fix and regression test |
| tester | "test REQ-…" or nothing (full suite) | TEST REPORT with a coverage table |
| performance-engineer | "load-test chat and retrieval" | PERFORMANCE REPORT against budgets |
| code-reviewer / security-auditor | nothing (reviews the latest changes) or file paths | severity-ranked findings |
| ai-evaluator | "retrieval level", "both modes" or a model to compare | EVAL REPORT |
| devops-engineer | "ci", "docker", "deploy" or "runbook" | files and exact commands |
| tech-writer | "readme", "walkthrough" or "demo script" | docs that match the code |
| release-manager | "minor", "patch" or nothing | GO / NO-GO and release notes |

**Golden rule:** every agent ends with a fixed report. If a report says ❌ or lists open questions, fix that before the next step.

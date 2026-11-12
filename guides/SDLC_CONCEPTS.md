# Dinesh AI Academy · 🧠 SDLC + AI Agents — The Concepts

> Part of the **Dinesh AI Academy · Agentic Engineering Kit**. *Gyaan jo sach mein kaam aaye.*

A one-stop explainer for students: what the Software Development Life Cycle is, and every
Claude Code building block this kit uses to automate it. The example app is
**Bodhi — Agentic RAG Studio by Dinesh AI Academy**. File paths such as `docs/…` or `backend/…` below are
inside the active project (`projects/<name>/`, named by you).

---

## Part 1 — The Software Development Life Cycle (SDLC)

The **SDLC** is the series of steps every professional team follows to turn an idea into working,
safe, maintained software. Skip a step and you pay for it later: building the wrong thing,
shipping bugs, getting hacked.

| # | Phase | Question it answers | Real-world role | Our agent | Artifact it leaves behind |
|---|---|---|---|---|---|
| 1 | **Requirements** | Are we building the right thing? | Product Manager | `product-manager` | `docs/requirements/REQ-*.md` |
| 2 | **Planning** | In what order? How big? | Scrum Master / PM | `product-manager` via `/sprint-plan` | `docs/sprints/SPRINT-*.md` |
| 3 | **Design** | What's the simplest design that works? | Architect | `architect` | `docs/adr/NNNN-*.md` |
| 4 | **UX design** | Is it easy and pleasant to use? | Product Designer | `ux-designer` | "UX spec" section |
| 5 | **Build** | Does the code do what the spec says? | Backend + frontend developers | `backend-developer`, `frontend-developer` | `backend/`, `frontend/` |
| 5b | **Debug** | What is the real cause of this failure? | Developer on support | `debugger` | A fix plus a regression test |
| 6 | **Test** | Can we prove it works? | QA Engineer | `tester` | `backend/tests/`, `frontend/**/*.spec.ts`, `frontend/e2e/` |
| 6b | **Performance** | Is it fast enough, and will it scale? | Performance Engineer | `performance-engineer` | `perf/`, `docs/perf/` |
| 7 | **Review** | Is it correct and maintainable? | Staff Engineer | `code-reviewer` | `docs/reviews/` |
| 8 | **Security** | Can it be abused? | AppSec Engineer | `security-auditor` | `docs/security/` |
| 9 | **Evaluate** | Are the AI's answers actually good? | AI Eval Engineer | `ai-evaluator` | `docs/evals/` |
| 10 | **Document** | Can others understand and use it? | Tech Writer | `tech-writer` | `README.md`, `CHANGELOG.md` |
| 11 | **Release** | Is it ready to ship? | Release Manager | `release-manager` | `docs/releases/` |
| 12 | **Operate** | Will it keep working? | DevOps / SRE | `devops-engineer` | CI, Dockerfiles, `deploy/`, runbook |
| 13 | **Learn** | How do we get better? | Whole team | `/retro` | `docs/retros/` |

### Key ideas
- **Quality gates** — you can't enter the next phase until the current one passes (e.g. no review until tests are green).
- **Fix loops** — when a gate fails, the work goes back to the developer (or the `debugger`), then gets re-checked. We cap the loops (max 3) so nothing runs forever.
- **Shift left** — catch problems as early as possible. A missing requirement costs 1 minute to fix in phase 1 and 1 day in phase 11.
- **Artifacts are memory** — every phase writes a file. Agents (and humans) forget conversations; files remain.
- **Evidence over opinion** — "it works" means tests pass; "it's good" means the evals say so.

### Waterfall vs Agile — where does this fit?
Running `/sdlc` once is a **mini-waterfall for a single feature**. Running it again and again for
small features, with `/sprint-plan` and `/retro` around it, is **Agile**: short cycles, constant feedback.

---

## Part 2 — The Claude Code building blocks

```
.
├── CLAUDE.md                  ① Project memory — rules every agent reads
├── .claude/
│   ├── agents/                ② Subagents — specialist team members (14)
│   ├── skills/                ③ Skills — reusable workflows + their templates
│   ├── commands/              ④ Slash commands — simple one-file workflows
│   ├── hooks/                 ⑤ Hooks — automatic guardrails (scripts)
│   ├── output-styles/         ⑥ Output styles — how Claude talks (Mentor mode)
│   └── settings.json          ⑦ Permissions + hook wiring
├── blueprint/                 ⑧ Inputs and standards only: intake form, brand design system, stack decision, .env.example
├── guides/                    Teaching guides (you are here)
├── prompts/                   Ready-to-paste prompts
└── projects/                  Generated apps — git-ignored, never pushed
    └── <name>/                One folder per project, named by you
        ├── docs/              ⑧ The project's own requirements, SPEC, ADRs, design system, test plan and every SDLC artifact
        └── evals/             ⑨ Golden dataset for AI quality
```

### ① `CLAUDE.md` — project memory
Loaded automatically at the start of every session. Holds what never changes: the stack, the repository layout,
the golden rules ("never hard-code keys", "tests never call a real LLM", "frameworks only through our interfaces").
Think of it as the team handbook taped to every desk.

### ② Subagents — `.claude/agents/*.md`
A subagent is a **specialist with its own instructions, its own tools and a fresh context window**.
The main Claude acts as the team lead and *delegates* to them.

```markdown
---
name: code-reviewer                     # how you call it
description: Staff Engineer ... Use PROACTIVELY after ...   # tells Claude WHEN to use it
tools: Read, Glob, Grep, Bash           # what it is ALLOWED to do (no Write = read-only)
model: opus                             # which brain: opus (deep), sonnet (fast), inherit
color: orange                           # its colour in the UI
---
You are a Staff Engineer ...            # the persona and the playbook
```

Why use subagents instead of one big chat?
- **Focus:** each one has a short, sharp job description, so it's better at that job.
- **Clean context:** the reviewer doesn't carry 2 hours of build chatter, so it sees the code with fresh eyes.
- **Safety:** tool limits enforce separation of duties (the tester *can't* "fix" a test by changing the app).
- **Parallelism:** independent agents (reviewer + security auditor) can run at the same time.
- **Right model for the job:** deep reasoning (architect, security) vs. fast writing (tech writer).

### ③ Skills — `.claude/skills/<name>/SKILL.md`
A skill is a **packaged workflow**: instructions plus supporting files (templates, checklists,
scripts) in one folder. You can run it with `/name`, and Claude can also pick it **automatically**
when your plain-English request matches its `description`.

Useful frontmatter fields:
- `description` — when to use it (Claude reads this to decide)
- `argument-hint` — what to type after the command
- `disable-model-invocation: true` — only a human can trigger it (we use this for `/release`)

Supporting files keep the skill short: `requirements/template.md`, `peer-review/checklist.md`,
`release/notes-template.md`…

This kit also has skills that teach the app how to grow: `/add-llm-provider`, `/add-retrieval-technique`,
`/switch-database` and `/demo-prep`.

### ④ Slash commands — `.claude/commands/*.md`
The older, simpler form of a skill: one Markdown file, with `$ARGUMENTS` replaced by whatever you
type after the command. `/build`, `/fix`, `/test` and `/feature` live here. (`/create-app` and `/client-intake` are skills.) Use a command for
"one file of instructions"; use a skill when you need templates or want automatic invocation.

### ⑤ Hooks — `.claude/hooks/` wired in `settings.json`
Hooks are **scripts the harness runs automatically** at specific moments. They don't depend on
Claude remembering a rule, so they're **guaranteed**.

| Hook event | Our script | What it guarantees |
|---|---|---|
| `SessionStart` | `session_start.py` | Claude always knows the project status |
| `PreToolUse` | `protect_secrets.py` | `.env` can never be read, edited or printed |
| `PostToolUse` | `check_python.py` | Syntax errors and leaked keys are caught seconds after writing |

How they talk back: exit code `0` = OK, exit code `2` = block / complain (the message goes to Claude).

> **Rule of thumb:** put *advice* in `CLAUDE.md` and agents; put *must-never-happen* rules in hooks and permissions.

### ⑥ Output styles — `.claude/output-styles/mentor.md`
Changes *how* Claude communicates, not *what* it can do. **Mentor** labels SDLC phases, explains
why, defines jargon and ends with a key takeaway. Switch it on with `/config` → Output style.

### ⑦ Permissions — `settings.json`
- `allow` — runs without asking (running tests, `git diff`)
- `ask` — asks you first (`git push`, `git tag`, real-API evals)
- `deny` — never allowed (reading `.env`)

### ⑧ Spec-driven development — `blueprint/` and the project's `docs/`
`SPEC.md`, `DESIGN_SYSTEM.md` and `TEST_PLAN.md` are the **source of truth**. They are **generated for each project**, so every run starts fresh.
`blueprint/` holds only the inputs and standards: the intake form, the brand design system (copied to the project as
`docs/DESIGN_SYSTEM.md`) and the stack decision (copied as `docs/adr/0001-stack-decision.md`). `/client-intake` writes the
requirements, `docs/SPEC.md` and `docs/TEST_PLAN.md` into `projects/<name>/docs/`. Agents build *from*
them, and tests check *against* them. If code and docs disagree, the docs win. This is how you get
consistent results from AI: precise specs in, precise software out.

### ⑨ Evals — `evals/`
Unit tests check the *code*; evals check the *AI's answers*. A golden set of questions with known
answers (`evals/golden_set.jsonl`, written for each project from the user's example questions) gives you a score you can track over time,
so you can tell whether a change to a prompt, a retrieval technique or a model actually helped.

---

## Part 3 — How a request flows through the team

```
 You: "/sdlc Add a Copy button"
        │
        ▼
 ┌──────────────── Main Claude = Engineering Lead ─────────────────┐
 │  reads CLAUDE.md · follows .claude/skills/sdlc/SKILL.md          │
 │                                                                  │
 │  product-manager ─► architect ─► ux-designer                     │
 │        ─► backend-developer + frontend-developer (↔ debugger)    │
 │                                                    │   ▲         │
 │                                                    ▼   │ fix     │
 │                                                  tester┘ loop    │
 │                                                    │             │
 │              ┌───────────────┬───────────────┬─────┴─────────┐   │
 │              ▼               ▼               ▼               ▼   │
 │        code-reviewer  security-auditor  ux-designer  performance-engineer
 │              └───────┬───────┘   (all read-only, run in parallel)│
 │                      ▼                                           │
 │           ai-evaluator ─► tech-writer ─► release-manager         │
 └──────────────────────────────────────────────────────────────────┘
        │   hooks guard every file read/write the whole time
        ▼
 You: a GO/NO-GO decision, tested code, and a trail of docs explaining every decision
```

---

## Glossary
| Term | Plain English |
|---|---|
| **Agent / subagent** | An AI team member with one job, its own instructions and limited tools |
| **Skill** | A saved, reusable workflow you trigger with `/name` |
| **Hook** | A script that runs automatically before/after Claude acts — a guardrail |
| **ADR** | Architecture Decision Record: a short note on *why* we designed something this way |
| **Acceptance criteria** | The test a feature must pass to count as "done" (Given / When / Then) |
| **Regression test** | A test that makes sure a fixed bug never comes back |
| **Quality gate** | A checkpoint that must pass before moving to the next phase |
| **SemVer** | Version numbers MAJOR.MINOR.PATCH (breaking . feature . fix) |
| **CI/CD** | Robots that test (CI) and ship (CD) your code on every change |
| **RAG** | Retrieval-Augmented Generation: look up relevant text, then let the AI answer from it |
| **Normal RAG / Agentic RAG** | Normal: search once, then answer. Agentic: a small loop (understand, search, check, search again if needed, answer, verify) with hard limits |
| **Retrieval technique** | One way of finding chunks: `dense`, `keyword`, `hybrid`, `mmr`, `multi_query` or `rerank` |
| **Blueprint** | The inputs and standards in `blueprint/` (intake form, brand design system, stack decision, `.env.example`). It holds no generated output |
| **Eval / golden set** | Questions with known answers used to score the AI |
| **Prompt injection** | Hidden instructions in a document that try to hijack the AI |
| **OWASP** | A non-profit that publishes the standard lists of top security risks |

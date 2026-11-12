# Dinesh AI Academy · 🧰 When to Use Skills — and When Not To

> Part of the **Dinesh AI Academy · Agentic Engineering Kit**. *Gyaan jo sach mein kaam aaye.*
> This folder holds the kit's **skills**: saved, reusable workflows you run with `/name`.
> This guide explains, with real examples from this kit, when a skill is the right tool and when something else fits better.
> (Paths like `backend/app/rag/` are inside the active project, `projects/<name>/`.)

---

## 1. What is a skill? (30 seconds)

A skill is a **recipe written in plain English** that Claude follows step by step.

```
.claude/skills/
└── peer-review/            ← folder name = command name  →  /peer-review
    ├── SKILL.md            ← the recipe (required)
    └── checklist.md        ← supporting file the recipe uses (optional)
```

There are two ways to run one:
- **You type it:** `/peer-review backend/app/rag/`
- **Claude picks it:** you say *"review my code"*, and Claude matches that to the skill's `description`.

---

## 2. ✅ Use a skill when…

| # | Situation | Why a skill fits | Example from this project |
|---|---|---|---|
| 1 | **You'll do the same task again and again** | Write the steps once, reuse them forever | `/peer-review` after every feature |
| 2 | **The task has several steps in a fixed order** | The recipe makes sure no step is forgotten | `/sdlc` runs every phase with gates |
| 3 | **Several agents must work in sequence** | The skill is the "manager" that passes work along | `/feature`: product-manager → backend/frontend-developer → tester → code-reviewer |
| 4 | **The output must follow a standard format** | A template in the skill folder keeps every result consistent | `/requirements` uses `requirements/template.md` |
| 5 | **A checklist must be applied the same way every time** | Nothing depends on memory | `/security-audit` uses `security-audit/checklist.md` |
| 6 | **The whole class / team should work the same way** | Everyone types the same command and gets the same quality | `/explain` gives every student the same 7-part lesson |
| 7 | **The task has real-world side effects** | You can make it manual-only (`disable-model-invocation: true`) | `/release` never starts by itself |
| 8 | **Extending the app should always follow the same steps** | The recipe covers every file that must change | `/add-llm-provider`, `/add-retrieval-technique`, `/switch-database` |

**Rule of thumb:** if you've typed the same long instructions **3 times**, turn them into a skill.

---

## 3. ❌ Don't use a skill when…

| # | Situation | Use this instead | Example |
|---|---|---|---|
| 1 | **It's a one-off question** | Just ask in the chat | *"What does `top_k` mean?"* — no skill needed |
| 2 | **It's a tiny edit** | Just ask in the chat | *"Rename `src` to `sources` in chroma_store.py"* |
| 3 | **You're exploring or brainstorming** | Just talk to Claude | *"What features could make Bodhi better?"* |
| 4 | **You need one expert with limited permissions** | An **agent** (`.claude/agents/`) | *"Use the security-auditor agent to check uploads"* — the agent is read-only, which a skill can't enforce |
| 5 | **A rule must apply to every task, always** | **`CLAUDE.md`** | "Business code never imports `chromadb` or a provider SDK directly" lives in `CLAUDE.md`, not in a skill |
| 6 | **Something must *never* happen, guaranteed** | A **hook** or a **permission** | Blocking `.env` is done by `hooks/protect_secrets.py` — a skill is only advice, a hook is enforced |
| 7 | **The steps change every time** | Just describe the task | A recipe that changes every time isn't a recipe |
| 8 | **It needs data a skill can't know** | Ask a question or pass arguments | Don't hard-code a file name into a skill; use `$ARGUMENTS` |

---

## 4. 🧭 Decision guide: which tool should I use?

```
 Is it a rule that should ALWAYS apply to every task?
   └─ YES → put it in CLAUDE.md                     (e.g. "use pathlib for paths")
   └─ NO ↓
 Must it be GUARANTEED / impossible to skip?
   └─ YES → hook or permission in settings.json     (e.g. block .env)
   └─ NO ↓
 Do you need ONE specialist with its own limited tools?
   └─ YES → agent in .claude/agents/                (e.g. code-reviewer, read-only)
   └─ NO ↓
 Will you repeat it, and does it have fixed steps / a template / several agents?
   └─ YES → skill in .claude/skills/                (e.g. /peer-review)
   └─ NO  → just ask in the chat                    (e.g. "explain this error")
```

### The four building blocks side by side

| | `CLAUDE.md` | **Skill** | Agent | Hook |
|---|---|---|---|---|
| **What it is** | Team handbook | Recipe | Team member | Automatic guard |
| **When it runs** | Always loaded | When you type `/name` or Claude matches it | When delegated to | Automatically, on events |
| **Can it be skipped?** | Claude may forget | Claude follows it when run | Works only within its tools | ❌ never, it's code |
| **Best for** | Always-on rules | Repeatable workflows | Focused expertise + limited permissions | Must-never-happen rules |
| **Example here** | "Tests never call a real LLM" | `/sdlc`, `/requirements` | `tester`, `security-auditor` | `protect_secrets.py` |

> 💡 **They work together:** the `/peer-review` **skill** calls the `code-reviewer` **agent**, which follows the rules in **`CLAUDE.md`**, while the **hooks** protect `.env` the whole time.

---

## 5. 🎯 Good vs bad requests — worked examples

### Example A — Reviewing code
- ❌ Without a skill: *"Please review my code. Check correctness, contracts, error handling, readability, architecture, tests, security and performance, use 🔴🟠🟡🟢, save it to docs/reviews with today's date…"* (and you have to remember all of that every time)
- ✅ With a skill: `/peer-review`. The same complete checklist, every time.

### Example B — A quick question
- ❌ Overkill: `/explain what is top_k` gives a 7-part lesson with an exercise when you wanted one line
- ✅ Better: *"What is top_k, in one sentence?"*
- ✅ Use `/explain` when you **want** the full lesson, for example for a class.

### Example C — Protecting secrets
- ❌ Wrong tool: a `/no-secrets` skill that says "please don't read .env". It only works when someone runs it.
- ✅ Right tool: the `protect_secrets.py` **hook**. It runs on *every* file access, automatically.

### Example D — A new feature
- ❌ Without a skill: *"Write requirements… now design it… now code it… now test it… now review it…"* (5 messages, easy to skip a step)
- ✅ With a skill: `/feature Show answer latency` or `/sdlc Show answer latency`. All steps, in order, with gates.

### Example E — A tiny fix
- ❌ Overkill: `/sdlc Fix a typo in the welcome message` runs 9 phases for one word
- ✅ Better: *"Fix the typo 'Helo' in the chat empty-state text"*, or `/fix` if you want a regression test too.

---

## 6. 📚 The skills in this folder

| Skill | Use it when… | Don't use it when… |
|---|---|---|
| `/create-app <name> <requirement>` | you want a whole new app from a plain-English requirement, with the team doing everything after a few questions | the app already exists (use `/feature` or `/sdlc`) |
| `/client-intake <name> <requirement>` | you want only the planning phase (requirements, SPEC, ADRs, test plan, eval set) so you can review it before building | you want the full journey (use `/create-app`) |
| `/sdlc <idea>` | a feature should go through **every** phase (great for demos) | it's a one-line change |
| `/requirements <idea>` | an idea is still vague | you already know exactly what to build |
| `/sprint-plan` | you have several features and need an order | you have just one task |
| `/adr <decision>` | there's a real choice between 2+ designs | there's only one sensible way |
| `/peer-review` | a change is "done" and needs a second pair of eyes | nothing has changed since the last review |
| `/security-audit` | before a release, or after touching uploads, HTML, prompts or auth | for a docs-only change |
| `/ui-review` | before a demo, or after UI changes | for back-end-only changes |
| `/eval-rag` | you changed chunking, top-k, the prompt, a retrieval technique or the model | in CI or offline (it uses the real API) |
| `/add-llm-provider <provider>` | you want another provider or model in the model picker | the model is already in `model_catalog.yaml` |
| `/add-retrieval-technique <name>` | you or a student want to try a new way of finding chunks | you only want to change a technique's settings |
| `/switch-database <target>` | you want Postgres or another vector store | SQLite and embedded Chroma are enough |
| `/demo-prep [audience]` | before a client meeting, webinar or class | the app is not built yet |
| `/cicd` | you want automatic tests on every push, or Docker | it's already set up |
| `/write-docs` | features landed and the docs are out of date | the code is still changing |
| `/release` | everything is reviewed and you want to ship | anything is still red |
| `/explain <topic>` | you want a full lesson: analogy, code, exercise | you want a one-line answer |
| `/retro` | at the end of a sprint, session or class | in the middle of work |
| `/team` | to see the roster or create a new agent | — |

Commands in `.claude/commands/` (`/build`, `/fix`, `/test`, `/feature`) work the same way. They're the simpler one-file form of a skill.
`/build <name>` is phase 2 only (it needs a project that has finished `/client-intake`); `/create-app` runs both phases and more.

---

## 7. ✍️ Create your own skill — full example

**Goal:** a `/standup` skill that writes a daily stand-up update from the project's files.

**Step 1 — create the folder and file**
```
.claude/skills/standup/SKILL.md
```

**Step 2 — write the recipe**
```markdown
---
name: standup
description: Write a daily stand-up update (Yesterday / Today / Blockers) from recent project changes. Use when the user asks for a standup or a daily update.
argument-hint: "[date, default today]"
---

# Daily stand-up

Date: **$ARGUMENTS** (empty = today)

1. Read the project's `CHANGELOG.md` → `## [Unreleased]`, the newest files in `docs/reviews/`,
   `docs/security/` and `docs/requirements/`, and `git log --oneline -10` if git exists.
2. Write three short sections:
   - **Yesterday** — what was finished (link files)
   - **Today** — the next task from the newest `docs/sprints/SPRINT-*.md`, or the next open requirement
   - **Blockers** — any 🔴/🟠 findings still open, failing tests, open questions
3. Keep it under 10 lines. Plain English.
```

**Step 3 — use it**
Start a new Claude Code session, then type:
```
/standup
```
or just say *"give me today's standup"*.

### Writing a great skill: checklist
- [ ] **`name`** matches the folder name (lowercase-with-dashes)
- [ ] **`description`** says *what* it does **and** *when to use it*, because Claude reads this to decide
- [ ] **`argument-hint`** shows what to type after the command
- [ ] Uses **`$ARGUMENTS`** instead of hard-coded values
- [ ] **Numbered steps**, each one clear and checkable
- [ ] Says **which agent** does each step, if it uses agents
- [ ] Says **where the output is saved** (so the next step or agent can read it)
- [ ] Long templates/checklists go in **separate files** in the same folder
- [ ] Add `disable-model-invocation: true` if it pushes, deploys, deletes or spends money

### Common mistakes
| Mistake | Fix |
|---|---|
| Vague description: *"Helps with code"* | *"Review changed code for bugs and readability. Use before merging."* |
| One giant skill that does everything | Several small skills (`/requirements`, `/adr`, …), with one orchestrator (`/sdlc`) to chain them |
| Putting always-on rules in a skill | Move them to `CLAUDE.md` |
| Relying on a skill for safety | Use a hook or a permission |
| Skill doesn't appear | Start a new session; check the folder name and that the `name:` line match |

---

> **💡 Key takeaway:** a skill is the right tool when a task is **repeated, multi-step and needs the same quality every time**. For one-off questions just ask, for always-on rules use `CLAUDE.md`, and for guarantees use hooks.

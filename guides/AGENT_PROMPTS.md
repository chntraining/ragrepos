# Dinesh AI Academy · 📝 Agent Prompts: What to Type

> Part of the **Dinesh AI Academy · Agentic Engineering Kit**. *Gyaan jo sach mein kaam aaye.*

Copy a prompt, paste it into Claude Code, then check the output.
Go in order, from 1 to 11. Each agent's **output** is the next agent's **input**.
Extra specialists you can call at any time: **debugger** (when something is broken) and **performance-engineer**
(before a demo or release).

> The examples use the feature **"Chat with selected documents only"**:
> a requirement file `REQ-NNN-chat-with-selected-documents.md` and an ADR `docs/adr/NNNN-filter-retrieval-by-selected-sources.md`.
> Your project's numbers and file names will differ: the agents create these files, so look in `docs/requirements/` and
> `docs/adr/` for the real names and use them in the prompts below (the examples show `REQ-001` and `ADR 0002`).
> For your own feature, change the idea and the file names.
> **Paths:** `docs/…`, `backend/…` and `frontend/…` are inside the active project, `projects/<name>/`.

**Before Step 4:** create the app once, then add your keys.
```
/create-app acme-sop "A chat assistant for our SOP documents"
```
Then, in `projects/acme-sop/`, copy `.env.example` to `.env` (Windows: `copy`, macOS/Linux: `cp`) and add your `GOOGLE_API_KEY`.
The full run commands are in the root `README.md`.

---

## 1. 📋 Product Manager: *what* to build

**Prompt (pick one):**
```
Use the product-manager agent to write requirements for: "Chat with selected documents only — I uploaded three files but want answers from just one."
```
```
/requirements Chat with selected documents only — I uploaded three files but want answers from just one.
```
The second one also asks you the open questions.

**Input:** your idea
**Output:** `docs/requirements/REQ-001-….md` (user stories, Given/When/Then, open questions)

**Then:** answer its questions, and say:
```
Mark REQ-001 as Approved and append its stories to docs/SPEC.md §2
```

---

## 2. 📐 Architect: *how* to build it

**Prompt (pick one):**
```
Use the architect agent to design docs/requirements/REQ-001-chat-with-selected-documents.md
```
```
/adr docs/requirements/REQ-001-chat-with-selected-documents.md
```
The second one also asks "Accept this ADR?"

**Input:** the REQ file
**Output:** `docs/adr/0002-….md` (options, decision, file plan, new function signatures)

**Then:**
```
Accept ADR 0002 and update docs/SPEC.md §6 with the new contracts
```

---

## 3. 🎨 UX Designer: how it *looks*

**Prompt (pick one):**
```
Use the ux-designer agent in Specify mode for docs/requirements/REQ-001-chat-with-selected-documents.md and docs/adr/0002-filter-retrieval-by-selected-sources.md
```
```
/ui-review
```
The second one is **only after the app is built**. It scores the real screen.

**Input:** REQ + ADR + `docs/DESIGN_SYSTEM.md`
**Output:** a **UX spec** (§7) in the REQ file: layout, states, exact words, colours

---

## 4. 🛠️ Backend / Frontend Developer: writes the code

**Prompt (pick one):**
```
Use the backend-developer agent to implement the backend part of docs/requirements/REQ-001-chat-with-selected-documents.md following docs/adr/0002-filter-retrieval-by-selected-sources.md
```
```
Use the frontend-developer agent to implement the UI part of docs/requirements/REQ-001-chat-with-selected-documents.md, following its UX spec (§7)
```
```
/fix <paste the error message here>
```
The first two build a feature. `/fix` is for fixing a bug: it uses the **debugger** agent.

**Input:** REQ + ADR + UX spec
**Output:** code changes in `backend/` (backend-developer) and `frontend/` (frontend-developer)

---

## 5. 🧪 Tester: proves it works

**Prompt (pick one):**
```
Use the tester agent: add TEST_PLAN cases for every acceptance criterion in REQ-001, write the tests, run the full suite
```
```
/test
```
The second one just runs all the tests and reports.

**Input:** REQ (Given/When/Then) + the new code
**Output:** tests in `backend/tests/`, `frontend/**/*.spec.ts` and `frontend/e2e/`, cases in `docs/TEST_PLAN.md`, a **TEST REPORT** (pass/fail, with coverage)

**If tests fail:**
```
Use the debugger agent to fix: <paste the TEST REPORT>
```
(or the backend-developer / frontend-developer agent, when the cause is already clear)

---

## 6. 🔍 Code Reviewer: checks code quality

**Prompt (pick one):**
```
Use the code-reviewer agent to review the REQ-001 changes (git diff HEAD~2)
```
```
/peer-review
```
```
/peer-review --fix
```
(`projects/` is git-ignored in this kit. If your project has its own git repository, `git diff` works inside it; otherwise give the reviewer a list of files.)
The `--fix` version also fixes the problems it finds.

**Input:** the changed code + REQ + ADR
**Output:** `docs/reviews/REVIEW-<date>-….md`, verdict **APPROVE** or **REQUEST CHANGES**

---

## 7. 🔒 Security Auditor: checks safety

**Prompt (pick one):**
```
Use the security-auditor agent to audit the REQ-001 changes
```
```
/security-audit
```
```
/security-audit --fix
```
The `--fix` version also fixes the problems it finds.

**Input:** the code
**Output:** `docs/security/SECURITY-<date>.md`, verdict **PASS**, **PASS WITH RISKS** or **FAIL**

💡 Tip: run 6 and 7 together:
```
Run the code-reviewer and security-auditor agents in parallel on the REQ-001 changes and save their reports
```

---

## 8. 📊 AI Evaluator: are the answers good?

⚠️ Uses your real API key and provider quota.

**Prompt (pick one):**
```
/eval-rag
```
```
/eval-rag --top-k 6
```
```
/eval-rag --compare "chunk_size 500"
```
The second one changes one setting; the third compares before and after. You can also ask it to compare retrieval techniques
(`dense`, `keyword`, `hybrid`, `mmr`, `multi_query`, `rerank`), Normal vs Agentic mode, or models.

**Input:** `evals/golden_set.jsonl` (questions with known answers; the ai-evaluator writes it for your project during `/client-intake`, from your example questions)
**Output:** `docs/evals/EVAL-<date>.md` (scores and one recommendation)

**Plain-English version (when you need to add something):**
```
Use the ai-evaluator agent to check answer quality when only one document is selected.
Compare it with all documents selected (REQ-001 success metric).
```
> 💡 Keep it short. The agent file already knows *how* (golden set, hit@k, correctness, citations, refusals, latency).
> Only add what it can't know, such as **which feature** to measure (*"REQ-001"*), **what to compare** (*"one document vs all"*, *"top-k 4 vs 6"*) or a **limit** (*"only 10 questions, save quota"*).
> **Tests vs eval:** the **tester** checks the *code works* (offline, fake LLM). The **ai-evaluator** checks the *answers are good* (real LLM).

---

## 9. ✍️ Tech Writer: writes the docs

**Prompt (pick one):**
```
/write-docs
```
```
/write-docs readme
```
```
/write-docs changelog
```
```
/write-docs user-guide
```
```
/write-docs walkthrough
```
These write: README + CHANGELOG · README only · CHANGELOG only · a guide for users · a code tour for students.

**Input:** the final code + REQ
**Output:** `.md` files only

**Plain-English version (when you need to add something):**
```
Use the tech-writer agent to write docs/USER_GUIDE.md for end users.
Include the REQ-001 document selection feature. Only edit that one file.
```
> 💡 Keep it short. The agent file already knows *how* (read the real code first, plain English, no jargon, every claim true to the code).
> Only add what it can't know, such as the **audience** (*"for students"* / *"for end users"*), **which feature** to cover (*"REQ-001"*), **which file** to touch, or the current situation (*"the frontend has uncommitted changes, document what's there now"*).
> If it reports a **code ↔ docs mismatch**, you decide which is right. By default `docs/SPEC.md` wins.

---

## 10. 🚀 Release Manager: ready to ship?

**Prompt (pick one):**
```
/release
```
```
/release minor
```
```
/release patch
```
The first one picks the version for you.

**Input:** test result + review + security + eval + CHANGELOG
**Output:** **GO / NO-GO**, `docs/releases/v0.2.0.md`, and git commands **you** run

**Plain-English version (when you need to add something):**
```
Use the release-manager agent to check if REQ-001 is ready to ship.
Confirm docs/USER_GUIDE.md covers the new feature and link it in the release notes.
```
> 💡 The Release Manager does **not write** `docs/USER_GUIDE.md`. It can only write `CHANGELOG.md` and `docs/releases/`.
> It **checks** that the guide is up to date as part of "docs updated". If the guide is out of date, the answer is **NO-GO**. Then run
> `/write-docs user-guide` (the **Tech Writer** writes it) and run `/release` again.

---

## 11. ⚙️ DevOps Engineer: automatic tests and deploy

**Prompt (pick one):**
```
/cicd
```
```
/cicd ci
```
```
/cicd docker
```
```
/cicd deploy
```
```
/cicd runbook
```
These create: everything · GitHub tests only · Dockerfiles and compose · deploy guide · ops guide.

**Input:** `backend/requirements.txt`, `frontend/package.json` + the tests
**Output:** CI workflow files (`.github/`), Dockerfiles, `deploy/docker-compose.yml`, deploy and runbook docs in `docs/`
(exact file names are chosen by the agent and listed in its DEVOPS REPORT)

**Plain-English version (when you need to add something):**
```
Use the devops-engineer agent to set up CI, Docker, deploy guide and runbook.
The tester is still running, so don't run the tests.
```
> 💡 Keep it short. The agent file already knows *how* (Dockerfile rules, no secrets, never deploys).
> Only add what it can't know, such as a different deploy target (*"deploy to Cloud Run"*), your own rule (*"CI only on PRs to main"*) or the current situation (*"tester still running"*).

---

## 12. 🐞 Debugger and ⏱️ Performance Engineer: on demand

**Prompt (pick one):**
```
/fix <paste the error or describe the bug>
```
```
Use the performance-engineer agent to load-test Normal and Agentic chat in the fake-LLM profile and compare with the budgets in docs/SPEC.md
```
The first finds the root cause and fixes it. The second only measures and reports (`docs/perf/`).

---

## 🔁 Bonus: Retro (look back and improve)

```
/retro
```
**Output:** `docs/retros/RETRO-<date>.md` (what went well, what to fix, improvements to the agents)

---

## ⚡ Shortcuts: many agents at once

| Prompt | What it does |
|---|---|
| `/sdlc <idea>` | Runs the whole team, in order, pausing at each gate |
| `/feature <idea>` | Lighter: requirements → design → code → tests → review |
| `/create-app <name> <requirement>` | Everything in one go: questions, requirements, design, build, tests, reviews, docs, release check, `docs/PROJECT_REPORT.md` |
| `/client-intake <name> <requirement>` | Phase 1 only: creates `projects/<name>/` and its requirements, SPEC, ADRs, test plan and eval set |
| `/build [name]` | Phase 2 only: builds an intake-ready project, tests it, fixes until green, reviews it |
| `/demo-prep` | Gets the built app ready for a client demo or class |
| `/team` | Lists all agents |
| `/explain <topic>` | Explains any file or idea in simple words |

---

## ✅ After every step

1. Open the file the agent created.
2. Read it. If something is wrong, tell the agent in plain English.
3. Save your work (inside your project folder, if it has its own git repository):
   ```
   git add -A
   git commit -m "step N done"
   ```
4. Go to the next step.

📘 Full details: [SDLC_STEP_BY_STEP.md](SDLC_STEP_BY_STEP.md)

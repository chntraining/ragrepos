# Dinesh AI Academy · 🧭 SDLC Worked Example — From One Idea to a Release, Agent by Agent

> Part of the **Dinesh AI Academy · Agentic Engineering Kit**. *Gyaan jo sach mein kaam aaye.*

> **Note on the code snippets.** This example was written for the first version of the app (a Streamlit app called
> Lumen), so the file names and code in the excerpts (`core/`, `ui/`, `app.py`, `pytest -q`) show **that v1 app**.
> The **flow is the same** with the current team and the new app, **Bodhi**. There, the developer step is done by
> the **backend-developer** (in `backend/`) and the **frontend-developer** (in `frontend/`), the **debugger** handles hard
> failures, and the **performance-engineer** joins the review step. Paths such as `docs/…` are inside
> `projects/<name>/`. Today's real file layout is in `CLAUDE.md`. The requirement and ADR numbers (`REQ-001`,
> `ADR 0002`) are examples: in your project, the agents pick the next free number.

This walkthrough follows **one real feature** through the whole AI team. At every step you'll see:

- 🗣️ **what you type** in Claude Code
- 🤖 **which agent** does the work
- 📥 **which earlier file it reads** (the hand-off it receives)
- 📤 **which new file it creates** (the hand-off it passes on)

> **The big idea:** agents don't remember each other's conversations — they hand over **files**.
> Each artifact is the *input contract* for the next team member, exactly like a real company
> where the designer works from the PM's spec and QA tests against the acceptance criteria.

> 📝 The reports and excerpts below are **illustrative examples** of what each agent produces. Your real run
> will differ in details (line numbers, test counts, findings), but the shape and the hand-offs are the same.

**Before you start:** the app must exist — run `/create-app <name> <requirement>` once (see `REQUIREMENT_TO_APP.md`). Turn on Mentor mode (`/config` → Output style → Mentor)
and ask Claude to *"announce the agent before every hand-off"* so the class can follow along.

---

## 🎯 The idea

> *"I uploaded three files but I only want answers from one of them."*

Feature: **Chat with selected documents only** — tick which documents the AI may use.

---

## 🔗 The artifact chain at a glance

```
 💡 Idea
  │
  ▼ 1. product-manager ──► docs/requirements/REQ-001-chat-with-selected-documents.md
  │                                   │  (stories + acceptance criteria)
  ▼ 2. architect ─────── reads REQ ──► docs/adr/0002-filter-retrieval-by-source.md
  │                                   │  (decision + new function signatures)
  ▼ 3. ux-designer ───── reads REQ+ADR ► REQ-001 §7 "UX spec"
  │                                   │  (states, microcopy, tokens)
  ▼ 4. developer(s) ──── reads all 3 ──► v1: core/vector_store.py, core/rag_pipeline.py, ui/components.py, app.py
  │       (now: backend-developer → backend/, frontend-developer → frontend/)
  │                                   │
  ▼ 5. tester ────────── reads REQ criteria ► docs/TEST_PLAN.md + tests/test_source_filter.py
  │        ▲ fix loop ▼               │
  ▼ 6. code-reviewer ─── reads code+REQ+ADR ► docs/reviews/REVIEW-2026-10-15-source-filter.md
  ▼ 7. security-auditor  reads code ──► docs/security/SECURITY-2026-10-15.md
  │        ▲ fix loop ▼               │
  ▼ 8. ai-evaluator ──── reads REQ metric ► evals/golden_set.jsonl + docs/evals/EVAL-2026-10-15.md
  ▼ 9. tech-writer ───── reads REQ+code ► README.md + CHANGELOG.md
  ▼10. release-manager ─ reads EVERYTHING ► docs/releases/v0.2.0.md  (GO / NO-GO)
  ▼11. devops-engineer ─ reads release ─► .github/workflows/ci.yml  (tests on every push)
  ▼
 🚀 Shipped
```

---

## The hand-off table

| # | Agent | 📥 Reads (input) | 📤 Writes (output) | How the **next** agent uses it |
|---|---|---|---|---|
| 1 | 📋 product-manager | your idea, `docs/SPEC.md` | `REQ-001-…md` | Architect designs to satisfy its stories |
| 2 | 📐 architect | `REQ-001` | `ADR 0002` | Developer follows its implementation plan & signatures |
| 3 | 🎨 ux-designer | `REQ-001`, `ADR 0002`, `DESIGN_SYSTEM.md` | `REQ-001 §7 UX spec` | Developer builds the exact states & words |
| 4 | 🛠️ developer (now backend-developer + frontend-developer) | `REQ-001`, `ADR 0002`, UX spec | code changes | Tester tests the new code |
| 5 | 🧪 tester | `REQ-001` acceptance criteria | `TEST_PLAN.md`, `tests/…` | Reviewers know it's proven to work |
| 6 | 🔍 code-reviewer | code diff, `REQ-001`, `ADR 0002` | `REVIEW-…md` | Developer fixes 🔴/🟠; release manager checks verdict |
| 7 | 🔒 security-auditor | code, checklist | `SECURITY-…md` | Release manager checks verdict |
| 8 | 📊 ai-evaluator | `REQ-001` §5 success metric | `EVAL-…md` | Release manager checks quality bar |
| 9 | ✍️ tech-writer | `REQ-001`, code | `README.md`, `CHANGELOG.md` | Release manager reads "Unreleased" |
| 10 | 🚀 release-manager | all of the above | `docs/releases/v0.2.0.md` | Human runs the git tag commands |
| 11 | ⚙️ devops-engineer | `requirements.txt`, tests | `ci.yml` | Every future change is auto-tested |

---

## Step 1 — 📋 Product Manager: *what* and *why*

🗣️ **You type**
```
Use the product-manager agent to write requirements for: "Chat with selected documents only —
I uploaded three files but want answers from just one."
```
(or the shortcut: `/requirements Chat with selected documents only`)

📥 **Reads:** your idea, `docs/SPEC.md` §1–§2 (to continue at story U10)
📤 **Creates:** `docs/requirements/REQ-001-chat-with-selected-documents.md`

**Excerpt of what it produces:**
````markdown
# REQ-001 — Chat with selected documents only
| Status | Draft | Priority | Should |

## 1. Problem
Users with several documents get answers mixed from all of them, even when the
question is about one file. Citations then point to irrelevant sources.

## 3. User stories
### U10 — Choose which documents the AI may use
As a user with several documents, I want to tick which ones are searched,
so that answers come only from the files I care about.

```gherkin
Scenario: Only selected documents are searched
  Given "handbook.pdf" and "notes.md" are indexed
  And   only "notes.md" is ticked
  When  I ask "What is due on Friday?"
  Then  every source chip shows "notes.md"

Scenario: Nothing selected
  Given documents are indexed but none are ticked
  When  I ask a question
  Then  I see "Select at least one document, or tick all to search everything"
  And   no search is run

Scenario: New uploads are selected by default
  When  I upload "report.docx"
  Then  "report.docx" appears ticked
```

## 4. Non-goals
- Saving the selection between browser sessions
- Selecting individual pages

## 5. Success metric
- 100 % of answers cite only selected documents (measured by the eval set)

## 6. Open questions
| 1 | Should the header pill show "2 of 3 documents"? | PM | Yes |
````

🔎 **Gate:** no unanswered open questions → hand to the architect.

---

## Step 2 — 📐 Architect: *how*, written down

🗣️ **You type**
```
Use the architect agent to design docs/requirements/REQ-001-chat-with-selected-documents.md
```
(or `/adr docs/requirements/REQ-001-chat-with-selected-documents.md`)

📥 **Reads:** `REQ-001` (the stories it must satisfy), `docs/SPEC.md` §6, ADR 0001
📤 **Creates:** `docs/adr/0002-filter-retrieval-by-source.md`

**Excerpt:**
````markdown
# 0002. Filter retrieval by source using Chroma's `where` clause
| Status | Accepted | Related | REQ-001, ADR 0001 |

## Options considered
| Option | Pros | Cons |
|---|---|---|
| A. Chroma `where={"source": {"$in": [...]}}` | DB does the filtering; top-K stays correct | Must handle empty list ourselves |
| B. Search everything, filter in Python | No Chroma knowledge needed | May return fewer than K results |

## Decision
Option A — filtering inside the DB guarantees K relevant results from the chosen files.

## Implementation plan
| Step | File | Change | Proven by |
|---|---|---|---|
| 1 | core/vector_store.py | `search(query_embedding, top_k, sources: list[str] \| None = None)` | test_search_filters_by_source |
| 2 | core/rag_pipeline.py | `retrieve(..., sources=None)` and `answer(..., sources=None)` pass it through | test_answer_uses_only_selected |
| 3 | ui/components.py | checkbox per document row → `st.session_state.selected_sources` | test_app_smoke |
| 4 | app.py | pass `selected_sources` into `answer()`; block when empty list | test_empty_selection_message |

Rule: `None` = search all, `[]` = search nothing (show message).
````

🔎 **Gate:** files to touch + new contracts are listed → hand on. The architect also updates `docs/SPEC.md` §6 with the new signatures.

---

## Step 3 — 🎨 UX Designer: the exact look and words

🗣️ **You type**
```
Use the ux-designer agent in Specify mode to add a UX spec to REQ-001, following ADR 0002
```

📥 **Reads:** `REQ-001`, `ADR 0002` (what data the UI gets), `docs/DESIGN_SYSTEM.md`
📤 **Updates:** `REQ-001` §7 "UX spec"

**Excerpt:**
```markdown
## 7. UX spec
- Each document row: [checkbox] 📄 name · muted "N chunks" · ✕ on hover
- Checkbox uses --accent-1 when ticked; row keeps radius-sm and hover --bg-subtle
- Header pill: "● Grounded in 2 of 3 documents" (green) — "○ General chat" when 0 indexed
- Empty selection: soft card, left border --accent-1, text
  "Select at least one document, or tick all to search everything"
- Keyboard: Space toggles the focused checkbox; visible focus ring
- File names inserted into HTML are passed through html.escape
```

---

## Step 4 — 🛠️ Developer: build exactly what was specified

🗣️ **You type** (v1 had one `developer` agent; today use the two below, one for each side of the app)
```
Use the backend-developer agent to implement the backend part of REQ-001 following ADR 0002
Use the frontend-developer agent to implement the UI part of REQ-001 following the UX spec in REQ-001 §7
```

📥 **Reads:** all three artifacts above + existing code
📤 **Changes:** `core/vector_store.py`, `core/rag_pipeline.py`, `ui/components.py`, `app.py`

**What it hands back:**
```
DEVELOPER REPORT
Files changed : core/vector_store.py, core/rag_pipeline.py, ui/components.py, app.py
What I did    : • search() accepts sources and adds where={"source": {"$in": sources}}
                • retrieve()/answer() pass sources through (None = all)
                • sidebar checkboxes, default ticked; pill shows "2 of 3"
Verification  : python -m pytest -q -> 31 passed
Open issues   : none
```

> 🛡️ While it works, the **check_python.py hook** compiles every file it saves — a typo is bounced back in seconds.

---

## Step 5 — 🧪 Tester: prove it against the acceptance criteria

🗣️ **You type**
```
Use the tester agent to add tests for every acceptance criterion in REQ-001 and run the full suite
```

📥 **Reads:** `REQ-001` §3 Gherkin scenarios (each becomes a test), `docs/TEST_PLAN.md`
📤 **Creates/updates:** `docs/TEST_PLAN.md` (new section), `tests/test_source_filter.py`

**Scenario → test mapping:**
| Acceptance scenario | Test |
|---|---|
| Only selected documents are searched | `test_search_filters_by_source` |
| Nothing selected | `test_empty_selection_runs_no_search` |
| New uploads selected by default | `test_new_upload_is_selected` |

```
TEST REPORT
Result   : ❌ FAIL (1 of 34 failed)
Failures :
  1. tests/test_source_filter.py::test_empty_selection_runs_no_search
     Root cause    : core/rag_pipeline.py:58 — `if not sources:` treats [] like None, so it searches ALL docs
     Suggested fix : use `if sources is not None and len(sources) == 0: return []`
```

🔁 **Fix loop:** the report goes back to the developer (or the `debugger`) → fixed → tester re-runs → `✅ PASS (34 tests)`.

> 💡 This is why the tester can't edit app code: it **found** the bug instead of quietly "fixing" the test.

---

## Step 6 — 🔍 Code Reviewer *and* Step 7 — 🔒 Security Auditor (in parallel)

🗣️ **You type**
```
Use the code-reviewer and security-auditor agents in parallel to review the REQ-001 changes
```
(or `/peer-review` then `/security-audit`)

📥 **Both read:** the changed code; the reviewer also reads `REQ-001` + `ADR 0002` to check the code matches the decision
📤 **Create:** `docs/reviews/REVIEW-2026-10-15-source-filter.md` and `docs/security/SECURITY-2026-10-15.md`

```
CODE REVIEW
Verdict  : 🔁 REQUEST CHANGES
  🟠 ui/components.py:74 — selection lost when a document is removed; stale name stays in
       selected_sources — Fix: intersect with list_sources() on every rerun
  🟡 core/vector_store.py:61 — name `src` → `sources` for readability
  🟢 Clean None-vs-[] contract, documented in the docstring — nice.
```
```
SECURITY REPORT
Verdict   : ✅ PASS
  🔵 [LLM05] checkbox labels use st.checkbox (auto-escaped) — chips already html.escape'd
  🔵 [LLM08] $in values come from list_sources(), never from free user text
```

🔁 **Fix loop:** 🟠 → developer → tester → reviewer re-checks → `✅ APPROVE`.

---

## Step 8 — 📊 AI Evaluator: are the answers actually right?

🗣️ **You type**
```
Use the ai-evaluator agent to check REQ-001's success metric
```

📥 **Reads:** `REQ-001` §5 ("100 % of answers cite only selected documents")
📤 **Adds** cases to `evals/golden_set.jsonl` and writes `docs/evals/EVAL-2026-10-15.md`

```
EVAL REPORT
Hit@4      : 6/6 (100 %)     Correct : 5/6     Refusals : 1/1
Selected-only citations : 4/4 ✅  (meets REQ-001 §5)
Recommend  : none for this feature
```
⚠️ This is the only step that calls a real LLM API — Claude asks before running it.

---

## Step 9 — ✍️ Tech Writer: tell the world

🗣️ **You type**
```
Use the tech-writer agent to document REQ-001 in the README and CHANGELOG
```

📥 **Reads:** `REQ-001` (user-facing wording), the real code (to stay accurate)
📤 **Updates:** `README.md`, `CHANGELOG.md`

```markdown
## [Unreleased]
### Added
- Chat with selected documents only — tick documents in the sidebar to limit which files answers come from (REQ-001).
```

---

## Step 10 — 🚀 Release Manager: GO or NO-GO on evidence

🗣️ **You type**
```
/release
```

📥 **Reads:** test run, newest `docs/reviews/`, `docs/security/`, `docs/evals/`, `CHANGELOG.md` Unreleased
📤 **Creates:** `docs/releases/v0.2.0.md`, moves Unreleased → `## [0.2.0] - 2026-10-15`

```
RELEASE REPORT
Decision  : 🟢 GO
Version   : v0.2.0 (MINOR — new feature, nothing broken)
Checklist : tests ✅ | review ✅ | security ✅ | evals ✅ | docs ✅
Run these : git add -A
            git commit -m "feat: chat with selected documents only (REQ-001)"
            git tag -a v0.2.0 -m "Bodhi v0.2.0"
            git push && git push --tags
```
👤 **You** run the commands — the agent never pushes.

---

## Step 11 — ⚙️ DevOps Engineer: keep it working forever

🗣️ **You type**
```
/cicd ci
```
📥 **Reads:** `requirements.txt`, the test command · 📤 **Creates:** `.github/workflows/ci.yml`
(today also Dockerfiles and `deploy/docker-compose.yml`)
From now on, GitHub re-runs all 34 tests on Windows, macOS and Linux for every push —
**automatic regression testing**.

---

## ⚡ The one-command version

Everything above, with the same agents, the same artifacts and quality gates between them:
```
/sdlc Chat with selected documents only
```
Run the step-by-step version first in class so students *see* each hand-off — then show that `/sdlc`
does the same thing in one go.

---

## ✅ What students should notice

1. **Files are the hand-off.** Every agent starts by reading the previous agent's artifact — nobody relies on memory.
2. **Traceability.** `REQ-001` → `ADR 0002` → code → `test_empty_selection_runs_no_search` → review → release notes. You can trace any line of code back to the user need that caused it.
3. **Separation of duties caught real bugs.** The tester found the `[]` vs `None` bug; the reviewer found the stale-selection bug. One agent doing everything would likely have missed both.
4. **Gates stop bad work early.** Nothing reached release until tests, review and security were green.
5. **Humans keep the final say.** Open questions go to you; the release button is yours.

> **💡 Key takeaway:** a great team — human or AI — is a chain of clear hand-offs, where each person's output is the next person's input.

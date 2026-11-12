# Dinesh AI Academy · 🤖 Agents vs 🧰 Skills — What's the Difference?

> Part of the **Dinesh AI Academy · Agentic Engineering Kit**. *Gyaan jo sach mein kaam aaye.* Examples use the
> **Bodhi** app; paths such as `docs/…` are inside the active project (`projects/<name>/`).

> **One-line answer:** an **agent** is a *team member* (who does the work).
> A **skill** is a *playbook* (what happens, in what order, every time).
> You need both, just as a company needs employees **and** standard procedures.

---

## 0. 🧠 In plain words (the 1-minute version)

### Think of your phone 📱
- **Agents are your contacts.** You have a plumber, an electrician and a painter saved.
- **A skill is a saved shortcut.** One button, *"Fix my bathroom"*, calls the plumber first, then the electrician, then the painter, in the right order, every time.

Without the shortcut, **you** must remember who to call, in what order, and what to tell each one. Every single time.

### In one sentence
> **An agent knows how to do a job. A skill remembers the steps, so you don't have to.**

### The simplest example
**Without a skill**, you type 6 messages and must remember each one:
```
Ask the PM to write requirements
Ask the backend-developer to build the API part
Ask the frontend-developer to build the screen
Ask the tester to test it
Ask the debugger to fix what broke
Ask the tester to test again
Ask the reviewer to check it
```
**With a skill**, you type one line:
```
/feature Copy button
```
Same people, same work. You just didn't have to remember the steps.

### Easy to remember
> 🤖 **Agent = WHO** does the work
> 🧰 **Skill = HOW** the work flows
>
> **"Agents are the team. Skills are the plan."**

### When to make a skill: the 3-times rule
> If you've typed the same instructions **3 times**, make it a skill.

Done once? Just ask. Done every day? Make it a skill.

---

## 1. 🍽️ The restaurant analogy

Imagine a restaurant kitchen.

| In the kitchen | In Claude Code | In this project |
|---|---|---|
| 👨‍🍳 **The chefs**: the pastry chef, the grill chef, the head chef | **Agents** | `backend-developer`, `frontend-developer`, `tester`, `code-reviewer`, `security-auditor`… |
| 📖 **The recipe card**: "Step 1: grill chef sears. Step 2: pastry chef plates dessert. Step 3: head chef checks the dish." | **Skills** | `/feature`, `/sdlc`, `/peer-review`… |
| 🧾 **The order**: "One burger, please" | **What you type** | `/feature Show answer latency` |

- A great chef with **no recipe** cooks something different every time.
- A great recipe with **no chef** cooks nothing.
- **Chef + recipe** gives you the same great dish every time.

---

## 2. 🔍 Side by side

| | 🤖 **Agent** | 🧰 **Skill** |
|---|---|---|
| **What it is** | A specialist team member | A step-by-step workflow |
| **Answers the question** | *Who* does the work? | *What* happens, in *what order*? |
| **Lives in** | `.claude/agents/<name>.md` | `.claude/skills/<name>/SKILL.md` |
| **How you use it** | *"Use the **tester** agent to…"* | `/test` |
| **Has its own tools / permissions** | ✅ Yes (e.g. the reviewer is read-only) | ❌ No, it uses the agents' |
| **Has its own fresh memory** | ✅ Yes, starts clean for every job | ❌ No, runs in your chat |
| **Can include templates & checklists** | ❌ Not really | ✅ Yes (`template.md`, `checklist.md`) |
| **Can call several agents in order** | ❌ No | ✅ Yes |
| **Can be "manual only"** | ❌ No | ✅ Yes (`/release`) |
| **Best for** | Expertise, focus, safety limits | Consistency, repeatability, multi-step work |

---

## 3. 👀 See it with one example

**Goal:** add a feature that shows how long each answer took.

### ❌ Option A — Agents only (you are the manager)

You have to type **every hand-off yourself** and remember the order:

```
1. Use the product-manager agent to write requirements for "show answer latency"
2. Use the backend-developer and frontend-developer agents to build what's in docs/requirements/REQ-003...
3. Use the tester agent to write tests and run them
4. (tests failed) Use the debugger agent to fix the failure the tester reported
5. Use the tester agent to run the tests again
6. Use the code-reviewer agent to review the change
7. Save the review to docs/reviews/ with today's date
8. Add a line to CHANGELOG.md
```
😓 8 messages. Forget step 6 and nobody reviews the code. Forget step 7 and the next agent can't find the review.

### ✅ Option B — A skill (the skill is the manager)

```
/feature Show answer latency
```
😀 **One message.** The skill calls the **same agents**, in the **right order**, sends failures back automatically, and saves every result where the next agent expects it.

```
 You: /feature Show answer latency
        │
        ▼
 🧰 feature skill (the playbook)
        │
        ├─► 🤖 product-manager ──► REQ-003.md
        ├─► 🤖 backend / frontend developer ──► code
        ├─► 🤖 tester ───────────► tests  ── ❌ fail? ──► back to the developer / debugger
        ├─► 🤖 code-reviewer ────► REVIEW.md
        └─► 📝 CHANGELOG.md updated
```

> **Same agents. Same quality. Zero steps forgotten.**

---

## 4. 🧪 Five quick examples: agent or skill?

| # | You want to… | Use | Type this | Why |
|---|---|---|---|---|
| 1 | Get **one expert opinion** on security | 🤖 Agent | *"Use the security-auditor agent to check the upload code"* | One expert, one job |
| 2 | Run the **full security process**: audit, save the report, fix, re-check | 🧰 Skill | `/security-audit --fix` | Several steps, same every time |
| 3 | Ask the tester a **quick question** | 🤖 Agent | *"Use the tester agent to tell me which tests cover chunking"* | One-off |
| 4 | Take an idea **all the way to release** | 🧰 Skill | `/sdlc Add a Copy button` | Many phases, up to 14 agents, gates in between |
| 5 | Make sure the reviewer **can't edit code** | 🤖 Agent | (set `tools: Read, Glob, Grep, Bash` in `code-reviewer.md`) | Only agents have tool limits |

---

## 5. 🧩 How they work together in this project

Most skills **call** agents. That's the whole idea:

| Skill (playbook) | Agents it calls (team members) | Artifact it saves |
|---|---|---|
| `/requirements` | 📋 product-manager | `docs/requirements/REQ-*.md` |
| `/adr` | 📐 architect | `docs/adr/NNNN-*.md` |
| `/feature` | 📋 product-manager → 🛠️ backend / 🖥️ frontend developer → 🧪 tester → 🔍 code-reviewer | code, tests, review |
| `/fix` | 🐞 debugger → 🧪 tester | a fix and a regression test |
| `/peer-review` | 🔍 code-reviewer (→ 🛠️ developers if `--fix`) | `docs/reviews/` |
| `/security-audit` | 🔒 security-auditor (→ 🛠️ developers if `--fix`) | `docs/security/` |
| `/eval-rag` | 📊 ai-evaluator | `docs/evals/` |
| `/release` | 🚀 release-manager (+ 🔍 + 🔒 if reports are missing) | `docs/releases/` |
| `/sdlc` | **the whole team** (up to 14 agents) | everything above |
| `/explain`, `/retro` | *none*: Claude does it directly | a lesson, `docs/retros/` |

> 💡 A skill doesn't *have* to use an agent (`/explain` doesn't). But an agent never runs a workflow on its own. It does its one job and reports back.

---

## 5b. 🔁 Can one skill use many agents, in order?

**Yes.** A skill can use **one** agent, or **many agents in order**. It can even run some **at the same time**, or **repeat** them until the work passes. All four patterns are already in this project.

### 1️⃣ One agent
```
/peer-review   →   🔍 code-reviewer
```
The skill adds the steps *around* that agent: which checklist to use, where to save the report, and what to do next.

### 2️⃣ Several agents, one after another
```
/feature   →   📋 product-manager → 🛠️ backend / 🖥️ frontend developer → 🧪 tester → 🔍 code-reviewer
```
Each agent finishes, saves a file, and the next agent reads that file.

### 3️⃣ Several agents at the same time
```
/build (review phase)  →   🔍 code-reviewer
                           🔒 security-auditor     ← all four work at once
                           🎨 ux-designer
                           ⏱️ performance-engineer
```
This is faster, because none of them needs the others' results.

### 4️⃣ A loop: repeat until it passes
```
/build   →   🛠️ developers → 🧪 tester → ❌ failed? → 🛠️ developer / 🐞 debugger → 🧪 tester → ✅
             (maximum 3 rounds)
```

### How you write the order
Just write the steps in plain English inside `SKILL.md`. The numbers set the order:
```markdown
1. Use the product-manager agent to write the requirements.
2. Use the backend-developer and frontend-developer agents to build it.
3. Use the tester agent to run the tests.
   If any test fails, send the report to the debugger and repeat step 3 (max 3 times).
4. Use the code-reviewer and security-auditor agents at the same time.
```

### One rule to remember
> **The skill is the boss. Agents don't call each other.**

The tester can't call the debugger directly. The skill (through the main Claude) takes the tester's report and hands it to the debugger. That's why the skill is needed: it's the one holding the plan.

> 🎵 **Easy to remember:** a **skill is a playlist**, and **agents are the songs**.
> A playlist can have one song or many, play them in order, or play one on repeat.

---

## 6. 🧭 How to choose (3 questions)

```
 1. Is it one job for one expert?
      └─ YES → 🤖 Agent          "Use the architect agent to…"

 2. Is it several steps, repeated often, or does it need a template/checklist?
      └─ YES → 🧰 Skill          /feature, /peer-review, /sdlc

 3. Is it a quick question or a tiny edit?
      └─ YES → 💬 Just ask       "What does top_k mean?"
```

---

## 7. 📁 What they look like inside

### 🤖 An agent: `.claude/agents/tester.md`
```markdown
---
name: tester
description: QA engineer. Use after any code change to write and run tests.
tools: Read, Write, Edit, Glob, Grep, Bash     ← what it's ALLOWED to do
model: inherit                                 ← which AI brain
---
You are a meticulous QA engineer...            ← WHO it is and HOW it works
You may edit files only in the test folders.
```

### 🧰 A skill: `.claude/skills/peer-review/SKILL.md`
```markdown
---
name: peer-review
description: Run a code review, save it, optionally fix findings.
argument-hint: "[files] [--fix]"               ← what you type after /peer-review
---
1. Use the code-reviewer agent with checklist.md     ← WHICH agent
2. Save the report to docs/reviews/REVIEW-<date>.md  ← WHERE the output goes
3. If --fix: developers fix → tester re-runs         ← WHAT happens next
```

**Notice:** the agent file describes a **person**, and the skill file describes a **process**.

---

## 8. ❓ FAQ

**Q: If I have agents, why do I need skills at all?**
Agents give you *expertise*; skills give you *consistency*. Without skills, **you** are the manager who must remember every step, every time.

**Q: If I have skills, why do I need agents?**
Skills can't limit permissions or give a fresh, focused mind. Only an agent can be **read-only** (the reviewer) or **forbidden from touching app code** (the tester). That separation is what catches bugs.

**Q: Can I use an agent without a skill?**
Yes: *"Use the code-reviewer agent to review backend/app/ingestion/chunker.py."* Great for one-off jobs.

**Q: Can I use a skill without an agent?**
Yes. `/explain` and `/retro` are done by Claude directly.

**Q: Which one does Claude pick when I just ask in plain English?**
Claude reads the `description` of every agent and skill and picks the best match. Say *"Tell me which agent or skill you'll use before starting"* to see its choice first.

**Q: How do I see all of them?**
Type `/` to list skills. Type `/team` to see the agents.

---

## 9. 🏋️ Try it yourself (5 minutes)

1. **Agent:** type
   `Use the product-manager agent to write requirements for a dark-mode toggle`
   and notice that it does **one job** and stops.
2. **Skill:** type
   `/requirements A dark-mode toggle`
   and notice that it uses the **same agent**, but also asks you the open questions and suggests the next command.
3. **Compare:** what did the skill add on top of the agent? *(Answer: the steps around it: questions, approval, adding to SPEC.md, next step.)*

---

> **💡 Key takeaway:** 🤖 **Agents = who** (experts with limits). 🧰 **Skills = how** (the same steps, every time).
> The best results come from using them **together**: skills that call the right agents in the right order.

📚 More: [AGENTS_GUIDE.md](AGENTS_GUIDE.md) · [../.claude/skills/README_When_to_Use_Skills.md](../.claude/skills/README_When_to_Use_Skills.md) · [SDLC_CONCEPTS.md](SDLC_CONCEPTS.md)

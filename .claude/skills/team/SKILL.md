---
name: team
description: Show the SDLC agent team — every agent in .claude/agents/ with its role, tools, model and the command that uses it — or create a new agent from a plain-English description. Use when the user asks "who is on the team?", "list the agents", or "create a new agent".
argument-hint: "[create <plain-English description of a new agent>]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# The team

Request: **$ARGUMENTS**

## If empty — show the roster
Read every file in `.claude/agents/` (frontmatter + first lines). Print one table, in SDLC order
(product-manager, architect, ux-designer, backend-developer, frontend-developer, debugger, tester,
performance-engineer, code-reviewer, security-auditor, ai-evaluator, tech-writer, release-manager, devops-engineer, then any others):

| # | Agent | Role (one line) | Can edit? | Model | Try it |
|---|---|---|---|---|---|

- **Can edit?** = "read-only" if `tools` has no `Write`/`Edit`, otherwise where it is allowed to write.
- **Try it** = the slash command that uses it (e.g. `/peer-review`), from `guides/AGENTS_GUIDE.md`.

End with: "Call any agent in plain English, e.g. *Use the architect agent to design chat history*."

## If it starts with `create` — make a new agent
1. Ask at most 2 clarifying questions if the role is unclear.
2. Write `.claude/agents/<kebab-name>.md` in the same style as the existing agents:
   frontmatter (`name`, `description` saying **when** to use it, the minimal `tools`, `model: inherit`, `color`),
   then: persona → mission → process → boundaries → a fixed-format report block.
3. Give it the fewest tools that do the job (reviewers get no `Write`/`Edit`).
4. Add it to the team table in `CLAUDE.md` and to "Meet the team" in `guides/AGENTS_GUIDE.md`.
5. Tell the user to start a new session so Claude Code loads it.

---
name: requirements
description: Turn a rough idea into a requirement document with user stories, Given/When/Then acceptance criteria, non-goals, MoSCoW priority and a success metric. Use when the user describes something they want but it isn't yet specified.
argument-hint: "<idea in plain English>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Requirements

Idea: **$ARGUMENTS**

1. Use the **product-manager** subagent. Pass it the idea and tell it to use `template.md` in this folder.
2. Show the user the stories and any **open questions**. Ask the open questions now.
3. When the user is happy, ask the product-manager to append the stories to `docs/SPEC.md` §2.
4. Finish with: the doc path, and the suggested next command:
   - design choices involved → `/adr docs/requirements/REQ-...md`
   - straightforward → `/feature <idea>` or `/sdlc <idea>`

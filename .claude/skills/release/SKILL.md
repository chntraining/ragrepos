---
name: release
description: Prepare a release — go/no-go checklist, semantic version, CHANGELOG entry, release notes and the exact git tag commands. Only run when the user explicitly asks to release.
argument-hint: "[major | minor | patch]  (optional — otherwise inferred)"
disable-model-invocation: true
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Release

Requested bump: **$ARGUMENTS** (empty = let the release-manager infer it from the changes).

1. Use the **release-manager** subagent with `checklist.md` and `notes-template.md` from this folder.
2. If the review or security report is missing or older than the latest code change, first run
   the **code-reviewer** and **security-auditor** subagents (in parallel) and save their reports
   (see `/peer-review` and `/security-audit`).
3. Show the GO / NO-GO decision.
   - **NO-GO** → list blockers and the command that fixes each one. Stop.
   - **GO** → show the version, the CHANGELOG diff, the release-notes path and the git commands.
4. **Never** run `git tag`, `git push` or any deploy command yourself — the human ships.

> `disable-model-invocation: true` in this skill's header means Claude will never start a release on
> its own — only when you type `/release`. Use this for any skill with real-world side effects.

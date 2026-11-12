---
name: client-intake
description: Turn a requirement (plain English or a filled blueprint/CLIENT_REQUIREMENTS.md form) into a ready-to-build project in projects/<name>/ — asks the right clarifying questions once, then writes requirements with acceptance criteria, the SPEC, ADRs, the project design system, the test plan and the evaluation set, and checks they agree. Use for a new client or use case before /build (it is Phase 1 of /create-app).
argument-hint: "<project-name> <requirement text or path to a filled requirements form>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Client intake — requirement → ready-to-build project

Arguments: **$ARGUMENTS**. Print one status line per step.

1. **Create the project** — `projects/<name>/` with `docs/`, `docs/adr/`, `docs/requirements/`, `evals/`. Copy:
   `blueprint/BRAND_DESIGN_SYSTEM.md` → `docs/DESIGN_SYSTEM.md` · `blueprint/STACK_DECISION.md` → `docs/adr/0001-stack-decision.md`
   · `blueprint/CLIENT_REQUIREMENTS.md` → `docs/CLIENT_REQUIREMENTS.md` (unless the user gave a filled form — copy that instead)
   · `blueprint/.env.example` → `.env.example` · start `CHANGELOG.md`. Save the requirement verbatim in `docs/REQUIREMENT_INPUT.md`.
   If the project already exists, reuse it and never overwrite its docs. Set **Active project** in `CLAUDE.md` to it.
2. **Discovery (product-manager)** — input: `docs/REQUIREMENT_INPUT.md`, `docs/CLIENT_REQUIREMENTS.md`, `CLAUDE.md`.
   It fills the form with what the requirement says plus kit defaults (marked "default"), and returns **at most 8 questions**
   that would change the design — each with options and a recommended default. Skip anything the defaults already answer well.
3. 🛑 **Ask the user once** — use the AskUserQuestion tool (≤ 4 questions per batch, ≤ 2 batches, recommended option first).
   If the user says "use defaults" or doesn't care, take the recommended options. Write the answers into `docs/CLIENT_REQUIREMENTS.md`.
4. **Requirements (product-manager)** — `docs/requirements/REQ-001-<slug>.md`: goal, success metric, user stories with
   Given/When/Then, non-goals, MoSCoW. No open questions may remain that block the build.
5. **Design (architect)** — writes `docs/SPEC.md` from scratch for this project (all sections in its agent file, including the
   completeness checklist) and an ADR for each decision that differs from `docs/adr/0001-stack-decision.md` or the kit defaults.
6. **UX (ux-designer, Mode A)** — extends `docs/DESIGN_SYSTEM.md` for this project's screens and states (keeps the brand),
   with a `data-testid` for every control the SPEC names.
7. **Test plan + eval set (in parallel)** — **tester** writes `docs/TEST_PLAN.md` with stable IDs and traceability;
   **ai-evaluator** writes `evals/golden_set.jsonl` from the user's example questions (or proposes a small sample set with
   sample documents in `evals/fixtures/` if none were given). No API calls.
8. **Consistency check (tester)** — list every place where SPEC, DESIGN_SYSTEM and TEST_PLAN disagree or leave a behaviour
   undefined (error codes, limits reject vs clamp, wording, missing test ids). The architect and ux-designer fix them —
   **one round**; anything left is written into the SPEC as an explicit assumption.
9. **Summary** — decided vs default table, assumptions, open risks, next command: `/build <name>` (or continue `/create-app`).

Never invent client facts, model ids, prices or compliance claims — unknowns become questions (step 3) or open items.

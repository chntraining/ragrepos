# SDLC cheat-sheet — who does what

```
 IDEA
  │
  ▼
 1. REQUIREMENTS ── product-manager ──► docs/requirements/REQ-*.md      (WHAT & WHY)
  │   gate: no open questions
  ▼
 2. DESIGN ──────── architect ────────► docs/adr/NNNN-*.md              (HOW)
  │   gate: files + contracts listed
  ▼
 3. UX SPEC ─────── ux-designer ──────► "UX spec" section               (LOOK & FEEL)
  ▼
 4. BUILD ───────── backend-developer ─► backend/app/                    (CODE)
             └───── frontend-developer ► frontend/src/                   (CODE)
  ▼
 5. TEST ────────── tester ───────────► backend/tests/, *.spec.ts      (PROOF + COVERAGE)
  │   gate: green + coverage  ◄── fix loop with developers / debugger
  ▼
 6. REVIEW ──────── code-reviewer ────► docs/reviews/                   (QUALITY)
             ├───── security-auditor ─► docs/security/                  (SAFETY)
             └───── ux-designer ──────► UX report                       (POLISH)
  │   gate: approve + no critical   ◄── fix loop with developers
  ▼
 6b. PERFORMANCE ── performance-engineer ► docs/perf/                  (SPEED & SCALE)
  ▼
 7. EVALUATE ────── ai-evaluator ─────► docs/evals/                     (ANSWER QUALITY)
  ▼
 8. DOCUMENT ────── tech-writer ──────► README.md, CHANGELOG.md         (KNOWLEDGE)
  ▼
 9. RELEASE ─────── release-manager ──► docs/releases/vX.Y.Z.md         (GO / NO-GO)
  ▼
10. OPERATE ─────── devops-engineer ──► .github/workflows/, Dockerfile  (SHIP & RUN)
  ▼
11. LEARN ───────── /retro ───────────► docs/retros/                    (IMPROVE)
```

| Phase | Skill to run alone | Key question |
|---|---|---|
| Requirements | `/requirements` | Are we building the right thing? |
| Planning | `/sprint-plan` | In what order, in what size? |
| Design | `/adr` | What's the simplest design that works? |
| Build + Test | `/feature`, `/build`, `/fix`, `/test` | Does it work? |
| Review | `/peer-review`, `/security-audit`, `/ui-review` | Is it good, safe and beautiful? |
| Evaluate | `/eval-rag` | Are the AI answers actually correct? |
| Document | `/write-docs` | Can someone else understand it? |
| Release | `/release` | Is it ready to ship? |
| Operate | `/cicd` | Will it keep working? |
| Learn | `/retro` | What do we do better next time? |

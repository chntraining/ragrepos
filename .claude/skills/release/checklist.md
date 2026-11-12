# Release go / no-go checklist

| # | Gate | Evidence | Pass when |
|---|---|---|---|
| 1 | Backend tests | `python -m pytest --cov=app` (from `backend/`) | 0 failures |
| 2 | Backend coverage | same run | ≥ 85 % lines |
| 3 | Frontend tests | `npx ng test --no-watch` + coverage flag (from `frontend/`) | 0 failures, ≥ 80 % lines |
| 4 | Frontend build | `npx ng build` | no errors |
| 5 | Code review | newest `docs/reviews/*.md` | APPROVE or no open 🔴/🟠 |
| 6 | Security | newest `docs/security/*.md` | not FAIL; no open 🔴/🟠 |
| 7 | Evals (optional) | newest `docs/evals/*.md` | default technique hit@k ≥ 80 %, refusals correct; required if retrieval or agent changed |
| 8 | Docs | `README.md`, `CHANGELOG.md` | new features described; Unreleased not empty |
| 9 | Secrets | `.gitignore` has `.env` and `data/`; no `AIza…` keys in repo | clean |
| 10 | Specs | `docs/SPEC.md` matches what shipped | API contract, schema and Chroma design updated |

Missing evidence = **UNKNOWN** = blocker, unless the user explicitly waives it (record the waiver in the release notes).

## SemVer rules
- **MAJOR** (x.0.0) — something that used to work now works differently (breaking API change, DB/Chroma rebuild needed).
- **MINOR** (0.x.0) — new feature, nothing broken.
- **PATCH** (0.0.x) — bug fixes only.

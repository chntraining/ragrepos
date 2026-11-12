# Bodhi v<x.y.z> — <one-line theme>

_Released YYYY-MM-DD_

## ✨ Highlights
- **<Feature>** — <what users can now do, in one sentence>

## 🐛 Fixes
- <bug> — <what was wrong, now fixed>

## 🔒 Security
- <hardening item>

## ⬆️ Upgrade steps
```bash
git pull
cd backend && pip install -r requirements.txt && uvicorn app.main:app --port 8000
cd frontend && npm ci && npx ng serve
```

## ⚠️ Known issues
- <issue + workaround>

## ✅ Quality evidence
| Gate | Result |
|---|---|
| Tests | N passed |
| Review | APPROVE (docs/reviews/...) |
| Security | PASS (docs/security/...) |
| Evals | hit@k xx % (docs/evals/...) |

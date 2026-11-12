# Security checklist — Bodhi (OWASP Top 10 for LLM Apps 2025 + OWASP Top 10)

## OWASP Top 10 for LLM Applications (2025)
| ID | Risk | What to check in Bodhi |
|---|---|---|
| **LLM01** | Prompt injection | Document text and tool results only inside CONTEXT / tool-result areas; system prompt fixed in `rag/prompts.py`; model told context is data, not instructions |
| **LLM02** | Sensitive information disclosure | No tracebacks or keys in API responses or the UI; logs never include the key; free-tier data-use notice in README |
| **LLM03** | Supply chain | `backend/requirements.txt` and `frontend/package-lock.json` current; no unused deps; `pip-audit` / `npm audit --omit=dev` if available |
| **LLM05** | Improper output handling (XSS) | No `bypassSecurityTrust…` in Angular; any `[innerHTML]` sanitised; file names, excerpts and answers render as text |
| **LLM06** | Excessive agency | Agent tools read-only and allow-listed; arguments validated (`top_k` 1–10, known technique names); step limit enforced |
| **LLM07** | System prompt leakage | Nothing secret in the system prompt (assume users can extract it) |
| **LLM08** | Vector & embedding weaknesses | Chroma + SQLite paths from config; no Chroma port exposed; delete removes vectors too; Explorer GET-only and capped |
| **LLM09** | Misinformation | Answers cite sources; "I couldn't find that in your documents." when context is missing; UI disclaimer |
| **LLM10** | Unbounded consumption | Retries bounded (max 4); embedding batch ≤ 100; upload ≤ 25 MB; question length capped; agent steps capped; Retrieval Lab / rerank / multi-query bounded |

## Classic OWASP Top 10
| ID | Risk | What to check |
|---|---|---|
| **A01** | Broken access control | No login: documented as local / single-user; never exposed publicly without auth |
| **A02** | Secrets | `.env` git-ignored; `.env.example` placeholders only; no `AIza…` keys anywhere; key never in the frontend |
| **A03** | Injection | SQL with `?` placeholders only; FTS5 input escaped; no `eval`/`exec`/`subprocess` on user data; file names never used to build paths |
| **A04** | Insecure design | Upload allow-list and size limit enforced **on the server**; parsers wrapped with friendly errors |
| **A05** | Security misconfiguration | CORS allow-list (no `*`); no `--reload` / debug in production; `.claude/settings.json` denies reading `.env` |
| **A09** | Logging & monitoring | Request id on every log line; errors logged with context, without secrets or full document text |

## Quick read-only commands
```bash
grep -rnE "AIza[0-9A-Za-z_-]{35}" --include=*.py --include=*.ts --include=*.md --include=*.json .
grep -rn "bypassSecurityTrust\|innerHTML" frontend/src
grep -rnE "execute\(f\"|execute\(.*\+|execute\(.*%" backend/app
grep -rn "allow_origins" backend/app
```

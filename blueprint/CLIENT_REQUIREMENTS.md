# Client Requirements — Bodhi (Agentic RAG Studio)

> Dinesh AI Academy · Agentic Engineering Kit · *Gyaan jo sach mein kaam aaye.*
>
> **How to use this file:** fill it in **with the client** (call, workshop or email). Plain answers are fine.
> Leave a line as `?` if nobody knows yet — the product-manager agent turns every `?` into an open question.
> The values already filled in are **Bodhi's defaults**; change only what this client needs.
> Then follow `guides/REQUIREMENT_TO_APP.md` (or run `/client-intake <project> <this file>`).

---

## 1. The client and the problem
| Question | Answer |
|---|---|
| Client / team name | ? |
| Industry | ? (e.g. pharma, healthcare, manufacturing, finance, telecom, e-commerce) |
| What problem should this solve? (one sentence) | ? (e.g. "Our QA team spends hours searching SOPs for the right procedure.") |
| What happens today without it? | ? |
| How will we know it worked? (1–2 numbers) | ? (e.g. "time to find an answer drops from 20 min to 2 min", "80 % of answers rated correct") |
| Demo / go-live date | ? |
| Decision maker and contact for questions | ? |

## 2. Users
| Question | Answer |
|---|---|
| Who will use it? (roles) | ? (e.g. QA analysts, support agents, managers) |
| How many users? (now / in 1 year) | ? / ? |
| How many at the same time (peak)? | ? |
| Do users need separate private document spaces? | **Yes** (default — each user sees only their own documents) |
| Who are the admins? | ? |
| Login method | **Email + password** (default) · company SSO later? ? |
| Languages of users | English (default) · others? ? |

## 3. Documents (the knowledge)
| Question | Answer |
|---|---|
| File types | **PDF, DOCX, TXT, MD** (default) · others? ? |
| How many documents, roughly? Typical size? | ? documents · ? pages each |
| Largest single file | ≤ **25 MB** (default) |
| Languages of the documents | ? |
| Are there scanned PDFs (images, no text)? | ? (needs OCR — not in the default build) |
| Do documents contain personal or confidential data? | ? (PII, patient data, financial data, trade secrets) |
| How often do documents change? | ? (once / weekly / daily) |
| Where do documents come from? | **Manual upload** (default) · SharePoint / Drive / S3 later? ? |

## 4. Questions users will ask (the most important section)
Write **10–20 real questions** with the **correct answer** and **which document** it comes from.
These become the evaluation set that proves the app works for this client.

| # | Question | Correct answer (short) | Source document | Type |
|---|---|---|---|---|
| 1 | ? | ? | ? | exact-term / paraphrase / multi-step / not-in-docs |
| 2 | ? | ? | ? | |
| 3 | ? | ? | ? | |

Include at least: 3 exact-term questions (codes, names, numbers) · 3 "same meaning, different words" questions ·
3 multi-step questions (need 2+ facts) · 2 questions the documents **cannot** answer (the app must say so).

## 5. Answer behaviour
| Question | Answer |
|---|---|
| Answer modes | **Quick answer (Normal RAG)** and **Deep research (Agentic RAG)** with a toggle (default) |
| Retrieval techniques offered | **dense, keyword, hybrid (default), mmr, multi_query, rerank** · hide any? ? |
| Must every answer show its sources? | **Yes** (default) |
| If the documents don't contain the answer | **Say "I couldn't find that in your documents."** (default) · allow general knowledge? ? |
| Tone / length of answers | ? (e.g. short and formal) |
| Anything the app must never do or say? | ? |

## 6. AI models and data rules
| Question | Answer |
|---|---|
| Allowed AI providers | **Google Gemini** (default) · OpenAI? Anthropic? Azure? local (Ollama)? ? |
| Models users may pick | `gemini-3.5-flash-lite` (default — verify id before go-live) · others? ? |
| Can documents be sent to a cloud AI provider? | ? (if **No** → local models only) |
| Data must stay in which country / region? | ? |
| Paid tier with "no training on our data" required? | ? (free tiers may use data — tell the client) |
| Monthly AI budget limit | ? |

## 7. Security and compliance
| Question | Answer |
|---|---|
| Login required | **Yes** (default in production) |
| Roles | **admin, user** (default) · more? ? |
| Compliance needs | ? (e.g. GDPR, HIPAA, GxP, SOC 2, internal policy) — the kit never claims compliance without evidence |
| Audit log needed? | **Yes** (default — login, upload, delete, settings) |
| How long to keep chats and traces? | **30 days** (default) · ? |
| Penetration test / security review before go-live? | ? |

## 8. Scale, speed and hosting
| Question | Answer |
|---|---|
| Expected documents / chunks in year 1 | ? |
| Acceptable wait for a Quick answer to start | **≈ 2–3 s** (default target) · ? |
| Hosting | **Docker on one server / VM** (default) · cloud (AWS / Azure / GCP)? on-premise? ? |
| Database | **SQLite** (default, single server) · **Postgres** (multi-server or > ~50 users) ? |
| Vector store | **ChromaDB** (default) · pgvector / other? ? |
| Uptime expectation | ? (e.g. business hours only / 24×7) |
| Backups | **Daily** (default) · ? |

## 9. Look and feel
| Question | Answer |
|---|---|
| Branding | **Dinesh AI Academy** (default: navy + amber, Poppins / Inter) · client white-label? ? |
| Client logo / colours (if white-label) | ? |
| Must-have screens | **Chat, Compare, Retrieval Lab, Vector Explorer, Documents, Admin** (default) · hide any for this client? ? |
| Accessibility level | **WCAG 2.1 AA** contrast and keyboard use (default) |

## 10. Scope
| Question | Answer |
|---|---|
| Must have for the first version | ? |
| Nice to have later | ? |
| Explicitly **not** in scope | ? |
| Integrations (Slack, Teams, email, API for other apps) | ? (not in the default build) |

## 11. Sign-off
| | Name | Date |
|---|---|---|
| Client approver | ? | ? |
| Dinesh AI Academy lead | ? | ? |

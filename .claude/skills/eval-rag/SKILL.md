---
name: eval-rag
description: Measure RAG quality per retrieval technique (dense, keyword, hybrid, mmr, multi_query, rerank) and per mode (normal vs agentic) — hit@k, MRR, correctness, citations, refusals, latency, cost — against the golden set in evals/ using the real Gemini API, and recommend measured improvements. Use after changing chunking, retrieval, prompts or models, or when the user asks "how good are the answers?".
argument-hint: "[--level retrieval|answers|both] [--techniques a,b] [--mode normal|agentic|both] [--compare 'what to try']"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# RAG evaluation

Options: **$ARGUMENTS**

> ⚠️ Evals call the **real** Gemini API (free-tier quota) and need `GOOGLE_API_KEY` in `.env`.
> Unit tests (`/test`) are offline; evals are not. Ask the user to confirm before running.

1. Use the **ai-evaluator** subagent.
2. It runs `python evals/run_eval.py` (start with `--level retrieval` — cheapest) and writes `docs/evals/EVAL-<date>.md`.
3. If `--compare` was given (e.g. `--compare "chunk_size 500"`), the evaluator runs a baseline and
   the variant, changing **one** thing at a time, and shows a before/after table.
4. Show the user the score table and the single most valuable recommendation.

## How the golden set works
`evals/golden_set.jsonl` — one JSON object per line:
```json
{"id": "deadline", "type": "exact-term", "question": "When is the final report due?", "expected_keywords": ["15 March"], "should_refuse": false}
```
Add your own cases for your own documents — that's how real AI teams catch regressions.

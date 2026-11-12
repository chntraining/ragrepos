# Code review checklist — Bodhi (Angular + FastAPI + SQLite + ChromaDB)

## 1. Correctness
- [ ] Does exactly what the spec / acceptance criteria say
- [ ] Edge cases: empty, one item, huge input, unicode, duplicate file names, no documents uploaded
- [ ] Page numbers 1-based; re-uploading a file replaces its chunks in SQLite **and** Chroma

## 2. Contract (docs/SPEC.md)
- [ ] File layout matches the SPEC
- [ ] Endpoints, Pydantic schemas, stream events and `frontend/src/app/core/models.ts` all agree
- [ ] System prompt is verbatim from the SPEC and lives in `rag/prompts.py`

## 3. Backend
- [ ] Routers thin; logic in `rag/`; settings / DB / Chroma / Gemini injected with `Depends`
- [ ] SQL uses `?` placeholders; connections closed; `foreign_keys = ON`
- [ ] Gemini calls retried on 429/503 (max 4) with timeouts; friendly errors with the right status code
- [ ] No traceback ever reaches the client; request id in logs

## 4. ChromaDB & retrieval
- [ ] Our Gemini embeddings passed to Chroma — never Chroma's default embedding model
- [ ] Distance → similarity converted in one place, with a comment
- [ ] A document is in both stores or neither (rollback on failure); delete removes both
- [ ] Every technique implements `Retriever`, returns `RetrievedChunk` with its name, respects `top_k` + document filter
- [ ] Each technique file has a "What · When · Trade-off" docstring
- [ ] RRF uses **ranks**, not raw scores; FTS5 input escaped; LLM JSON (rewrites, rerank scores) validated, with fallback
- [ ] Explorer endpoints are GET-only, paged, `limit` capped

## 5. Agentic RAG
- [ ] Step limit enforced; tools read-only and allow-listed; arguments validated; unknown tool handled
- [ ] Steps recorded and streamed; tool output treated as data

## 6. Frontend
- [ ] Standalone + OnPush; state in signals inside services; no `any`
- [ ] Streams / subscriptions cleaned up; Stop aborts the request
- [ ] Every UI state present; design tokens only; `data-testid` on key elements
- [ ] No `bypassSecurityTrust…`; untrusted text shown with `{{ }}` or a sanitised renderer

## 7. Readability
- [ ] Clear names, short functions, type hints / strict TypeScript
- [ ] Docstring / JSDoc on every public function; comments explain *why*
- [ ] No dead code, commented-out code, `print` or `console.log`

## 8. Tests & coverage
- [ ] New behaviour and its failure paths tested; bug fixes have regression tests
- [ ] Offline (fake Gemini), temp SQLite + temp Chroma in `tmp_path`
- [ ] Coverage did not drop (backend ≥ 85 %, frontend ≥ 80 %)

## 9. Performance & cost
- [ ] Embedding requests batched (≤ 100)
- [ ] No embedding call when the store is empty
- [ ] Rerank / multi-query make one batched LLM call, not one per chunk

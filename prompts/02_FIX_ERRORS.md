# Prompt 2 — Fix Any Error

> Dinesh AI Academy · Agentic Engineering Kit

**In Claude Code, type `/fix` followed by the error:**
```
/fix ModuleNotFoundError: No module named 'langgraph'
```
```
/fix POST /api/chat/stream returns 422 when I pick the "rerank" technique
```
```
/fix Deep research stops after "Searching" and the answer never appears
```
```
/fix The model picker is empty in the Angular app
```

**Or paste this prompt** (replace the block with your error):

---

The app (in `projects/<name>/`) is showing this error / behaving like this:

```
<paste the full traceback, the browser console error, or describe what you see>
```

Act as the **debugger** agent:
1. Reproduce the problem (run the relevant test, a small script or the failing request).
2. Find the root cause. Give me the exact `file:line` and explain it in one sentence.
3. Apply the smallest correct fix. Keep it consistent with `docs/SPEC.md`.

Then act as the **tester** agent:
4. Add a regression test if it can be tested offline (fake LLM, fake embeddings).
5. Run the backend and frontend tests and show the result.

Reply with: **What was wrong → What I changed → Proof (tests)**.

For "wrong answer" problems, look at the retrieval trace, the Retrieval Lab and the Vector Explorer first.

---

## Common errors and what they mean

| Error | Meaning | Usual fix |
|---|---|---|
| Model picker is empty | No provider key is set, so no model is enabled | Add a key (for example `GOOGLE_API_KEY`) to `projects/<name>/.env` and restart the backend |
| `401` / `403` from `/api/...` | Not signed in, or the role is not allowed | Sign in again; check the user's role |
| `422 Unprocessable Entity` | The request body does not match the Pydantic schema (for example an unknown technique name) | Compare the request with the schema in `docs/SPEC.md` |
| `429 Too Many Requests` | A rate limit was hit (app limit or provider quota) | Wait a minute; check the limits in the settings |
| CORS error in the browser console | The frontend origin is not in `CORS_ORIGINS` | Add `http://localhost:4200` to `CORS_ORIGINS` in `.env` (never use `*`) |
| `Collection expecting embedding with dimension X` (Chroma) | The embedding model or dimension changed after indexing | Re-index the documents (the admin re-index action), or delete the `data/chroma` folder in dev |
| `sqlite3` version error from Chroma on Linux | Old system SQLite | Use a newer Python build or the Docker image |
| `alembic` says the database is not up to date | A migration has not been applied | Run `alembic upgrade head` in `backend/` |
| Agent timeline stops early | A hard limit (LLM calls, rewrites, time) was reached, or a node raised an error | Read the last `step` event and the backend log with its request id |
| Upload stays `queued` or ends `failed` | The ingestion job failed (bad file, empty file, embedding error) | Check the job's `error_code` in the Documents screen |
| `ng serve` shows `/api` 404 or connection refused | The backend is not running on port 8000 | Start `uvicorn app.main:app --reload --port 8000` in `backend/` |

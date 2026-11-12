# Prompt 3 — Extend your app (ready-made feature prompts)

> Dinesh AI Academy · Agentic Engineering Kit

Use `/feature <description>` in Claude Code for a small change, or `/sdlc <description>` for the full lifecycle.
Copy any line below. These run **after** `/create-app <name> <requirement>` has built your project
(the commands work on the active project, `projects/<name>/`).

## Level 1 — Quick wins
```
/feature Add a "Copy" button under every assistant answer
```
```
/feature Show a latency and token caption under each answer (for example "1.8s · 412 tokens")
```
```
/feature Let the user export a conversation as a Markdown file, including its citations
```

## Level 2 — Better RAG
```
/add-retrieval-technique HyDE: ask the LLM to write a hypothetical answer, embed it, and search with that
```
```
/add-retrieval-technique Parent-document retrieval: search small chunks, return the larger section around them
```
```
/feature Rewrite follow-up questions into standalone questions using chat history before retrieval
```
```
/feature Show a "Why this answer?" panel that lists each agent step, the chunks it used and their scores
```

## Level 3 — Agentic RAG
```
/feature Add a query-decomposition step to the Deep research graph: split a multi-part question into sub-questions
```
```
/feature Let the Deep research verify step flag any sentence in the answer that no cited chunk supports
```
```
/feature Add a per-conversation budget (maximum LLM calls) that the user can see before running Deep research
```

## Level 4 — Pro
```
/add-llm-provider OpenAI
```
```
/add-llm-provider Ollama, for local models with no API key
```
```
/switch-database Move from SQLite to Postgres, and keep local development on SQLite
```
```
/feature Add web page ingestion: paste a URL and index its main text (with limits against abuse)
```
```
/eval-rag Compare all six techniques in Normal mode on the golden set
```

Before a client meeting, run `/demo-prep` to get a sample workspace and a demo script.

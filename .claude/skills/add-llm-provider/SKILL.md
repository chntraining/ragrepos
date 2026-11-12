---
name: add-llm-provider
description: Add a new LLM provider or model (e.g. OpenAI, Anthropic, Ollama, Azure, another Gemini model) to Bodhi's model picker — catalog entry, LangChain package, env var, capability flags, tests and docs. Use when the user says "add <provider>", "let users pick <model>", or "support local models".
argument-hint: "<provider> [model ids…]"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

# Add an LLM provider / model

Request: **$ARGUMENTS**

New providers are **configuration, not code** — that is the point of the catalog (see `docs/adr/0001-stack-decision.md`).

1. **Check facts first.** Confirm the provider's LangChain integration package name and the exact model ids from the
   provider's official docs (don't guess ids or pricing). Note whether each model supports streaming and tool calling.
2. Use the **backend-developer** subagent to:
   - add the models to `backend/model_catalog.yaml` (provider, model id, display name, capabilities, `enabled_by_env`),
   - add the LangChain package to `backend/requirements.txt` (pinned),
   - add the key variable name (placeholder only) to `.env.example`,
   - only if the provider needs special setup (e.g. a base URL for Ollama / Azure), extend `providers/llm.py` — still validated against the catalog.
3. Use the **tester** subagent to add tests: catalog loads; provider hidden when its key is missing; disallowed model rejected (400);
   a model without tool calling is not offered for Deep research.
4. If the user has a key and agrees, run `/eval-rag --mode both` with the new model to compare quality, speed and cost.
5. Tell the user: the env var to set, how to restart, and where the model appears in the picker.

Never put a real key in any file. Never let the client send a key or base URL.

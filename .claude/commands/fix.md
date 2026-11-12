---
description: Diagnose and fix an error (paste the traceback or describe the bug), then re-test with coverage
argument-hint: "<error message, traceback or description>"
---

> **Dinesh AI Academy · Agentic Engineering Kit** — created by Dinesh AI Academy · *Gyaan jo sach mein kaam aaye.*
> Paths are inside the active project (`projects/<name>/`) unless they start with `.claude/`, `blueprint/`, `guides/` or `prompts/` — e.g. `docs/SPEC.md` means `projects/<name>/docs/SPEC.md`, created when the project is created (it does not exist at the repo root).

The user reports this problem:

```
$ARGUMENTS
```

1. Use the **debugger** subagent: reproduce the bug, find the root cause (`file:line`), apply the smallest
   correct fix and add a regression test. For "wrong answer" bugs it should check the retrieval trace,
   the Retrieval Lab and the Vector Explorer first.
2. Use the **tester** subagent to run both suites with coverage and confirm nothing else broke.
3. If tests still fail, loop debugger → tester up to 3 times.
4. If the debugger says the fix needs a design or API change, stop and suggest `/adr`.
5. Reply to the user in plain language:
   - **What was wrong** (one sentence)
   - **Why it happened** (root cause)
   - **What I changed** (files)
   - **Proof** (test result + coverage)

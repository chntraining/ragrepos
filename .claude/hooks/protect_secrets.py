"""PreToolUse hook: stop Claude from reading, editing or printing the real .env file.

Claude Code sends the pending tool call as JSON on stdin. Exiting with code 2 blocks
the call and shows our stderr message to Claude, so it can choose a safer action.
`.env.example` is allowed — it only contains placeholders.
"""

import json
import re
import sys

# Matches ".env" as a whole file name — but not ".env.example", ".envrc" or ".venv".
ENV_FILE = re.compile(r"(^|[\s/\\'\"=<>|;&(])\.env(?![\w.\-])")


def is_blocked(tool_name: str, tool_input: dict) -> bool:
    """Return True when the tool call would touch the real .env file."""
    if tool_name == "Bash":
        return bool(ENV_FILE.search(tool_input.get("command", "")))
    path = str(tool_input.get("file_path", "")).replace("\\", "/")
    return path == ".env" or path.endswith("/.env")


def main() -> int:
    """Read the hook payload and block secret access."""
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never break the session because of a malformed payload
    if is_blocked(payload.get("tool_name", ""), payload.get("tool_input", {}) or {}):
        print(
            "Blocked by .claude/hooks/protect_secrets.py: the .env file holds the real API key "
            "and must never be read, edited or printed. Use .env.example for the variable names.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

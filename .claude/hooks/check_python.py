"""PostToolUse hook: instant quality gate after Claude writes or edits a file.

1. Python files must compile (catches syntax errors seconds after they are written).
2. No file may contain something that looks like a real Google API key.

Exit code 2 sends our stderr message back to Claude so it fixes the problem right away.
"""

import json
import py_compile
import re
import sys
from pathlib import Path

GOOGLE_KEY = re.compile(r"AIza[0-9A-Za-z_\-]{35}")


def check_file(path: Path) -> list[str]:
    """Return a list of human-readable problems found in the file."""
    problems = []
    if path.suffix == ".py":
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as err:
            problems.append(f"Syntax error in {path.name}: {err.msg}")
    try:
        if GOOGLE_KEY.search(path.read_text(encoding="utf-8", errors="ignore")):
            problems.append(
                f"{path.name} contains what looks like a real Google API key. "
                "Remove it and read GOOGLE_API_KEY via core/config.py instead."
            )
    except OSError:
        pass
    return problems


def main() -> int:
    """Read the hook payload and report problems in the edited file."""
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    file_path = (payload.get("tool_input") or {}).get("file_path")
    if not file_path or not Path(file_path).is_file():
        return 0
    problems = check_file(Path(file_path))
    if problems:
        print("Quality gate (.claude/hooks/check_python.py):\n- " + "\n- ".join(problems), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

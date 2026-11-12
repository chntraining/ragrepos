"""SessionStart hook: give Claude a quick status of the kit and of every project at session start.

Dinesh AI Academy · Agentic Engineering Kit.
Whatever this script prints on stdout is added to Claude's context, so Claude knows immediately which
projects exist under projects/, whether each one is built, and how many SDLC documents it has.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECTS = ROOT / "projects"


def count(base: Path, pattern: str) -> int:
    """Count files under base matching a glob pattern."""
    return sum(1 for _ in base.glob(pattern))


def project_status(project: Path) -> str:
    """Return a one-line status for one project folder."""
    backend = "yes" if (project / "backend/app/main.py").exists() else "no"
    frontend = "yes" if (project / "frontend/angular.json").exists() else "no"
    env = "present" if (project / ".env").exists() else "missing (copy .env.example)"
    tests = f"{count(project, 'backend/tests/**/test_*.py')} py / {count(project, 'frontend/src/**/*.spec.ts')} spec"
    docs = project / "docs"
    sdlc = (f"REQ {count(docs, 'requirements/REQ-*.md')} | ADR {count(docs, 'adr/[0-9]*.md')}"
            f" | reviews {count(docs, 'reviews/*.md')} | security {count(docs, 'security/*.md')}"
            f" | evals {count(docs, 'evals/*.md')} | perf {count(docs, 'perf/*.md')}")
    return (f"- projects/{project.name}: backend {backend} | frontend {frontend} | tests {tests}"
            f" | .env {env} | {sdlc}")


def main() -> int:
    """Print a short status block."""
    projects = sorted(p for p in PROJECTS.iterdir() if p.is_dir()) if PROJECTS.exists() else []
    lines = [
        "DINESH AI ACADEMY KIT STATUS (from .claude/hooks/session_start.py)",
        f"- Agents: {count(ROOT, '.claude/agents/*.md')} | Skills: {count(ROOT, '.claude/skills/*/SKILL.md')}"
        f" | Commands: {count(ROOT, '.claude/commands/*.md')}",
        "- Blueprint standards: " + ", ".join(
            name for name in ("CLIENT_REQUIREMENTS.md", "BRAND_DESIGN_SYSTEM.md", "STACK_DECISION.md")
            if (ROOT / "blueprint" / name).exists()),
    ]
    if projects:
        lines += [project_status(p) for p in projects]
    else:
        lines.append("- No projects yet - run /create-app <project-name> <your requirement>")
    lines.append("- Path rule + active project: see CLAUDE.md | Team guide: guides/AGENTS_GUIDE.md")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # a status banner must never break a session
        sys.exit(0)

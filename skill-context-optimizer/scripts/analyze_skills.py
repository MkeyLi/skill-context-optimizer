#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)

ISSUE_RULES = [
    {
        "id": "onboarding-hot-path",
        "label": "Onboarding in hot path",
        "severity": "high",
        "change_type": "safe-structural",
        "patterns": [r"first run", r"onboarding", r"quick start", r"welcome"],
        "recommendation": "Move onboarding copy to references/start.md and keep only detection plus routing in SKILL.md.",
    },
    {
        "id": "variant-sprawl",
        "label": "Platform or delivery branch sprawl",
        "severity": "high",
        "change_type": "safe-structural",
        "patterns": [
            r"\btelegram\b",
            r"\bemail\b",
            r"\bcron\b",
            r"\bweekly\b",
            r"\bdaily\b",
            r"\bopenclaw\b",
            r"\bclaude code\b",
            r"\bvercel\b",
            r"\bexport to pdf\b",
        ],
        "recommendation": "Convert branch-heavy prose into a compact routing table plus variant references.",
    },
    {
        "id": "philosophy-load",
        "label": "Long philosophy or manifesto in hot path",
        "severity": "medium",
        "change_type": "safe-structural",
        "patterns": [
            r"why this approach works",
            r"content philosophy",
            r"design identity",
            r"who this is for",
            r"make it memorable",
            r"core principles",
        ],
        "recommendation": "Keep actionable invariants in SKILL.md and move broad rationale or teaching philosophy into references.",
    },
    {
        "id": "hardcoded-copy",
        "label": "Hardcoded user-facing copy",
        "severity": "medium",
        "change_type": "content-sensitive",
        "patterns": [r"tell the user", r"ask:", r"i'm ", r"let me ", r"just point me at"],
        "recommendation": "Replace long speeches with intent-level constraints unless exact wording is essential.",
    },
    {
        "id": "example-load",
        "label": "Large example or command load",
        "severity": "medium",
        "change_type": "safe-structural",
        "patterns": [r"\bexample\b", r"\bexamples:\b", r"```bash", r"```python"],
        "recommendation": "Keep one canonical template in SKILL.md and move long examples into references or scripts.",
    },
    {
        "id": "eager-reads",
        "label": "Unconditional file-loading instructions",
        "severity": "medium",
        "change_type": "safe-structural",
        "patterns": [
            r"before generating",
            r"before coding",
            r"read these supporting files",
            r"always read",
            r"include the full contents",
        ],
        "recommendation": "Gate supporting-file reads by phase or branch so cold-path files stay cold.",
    },
    {
        "id": "high-cost-defaults",
        "label": "High-cost actions on the default path",
        "severity": "medium",
        "change_type": "safe-structural",
        "patterns": [r"show the full list", r"full source list", r"open each preview", r"run it once immediately"],
        "recommendation": "Keep expensive actions behind explicit conditions instead of default onboarding or delivery flow.",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze skill folders for context bloat.")
    parser.add_argument("paths", nargs="*", help="Explicit skill directories to analyze")
    parser.add_argument(
        "--installed",
        action="store_true",
        help="Analyze installed Claude Code and OpenClaw skills from standard personal and workspace directories",
    )
    parser.add_argument(
        "--root",
        action="append",
        default=[],
        help="Additional roots to scan for skill directories",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="Output format",
    )
    return parser.parse_args()


def default_skill_roots() -> list[Path]:
    home = Path.home()
    cwd = Path.cwd()
    return [
        home / ".claude" / "skills",
        cwd / ".claude" / "skills",
        home / ".openclaw" / "skills",
        home / ".agents" / "skills",
        cwd / ".agents" / "skills",
        cwd / "skills",
    ]


def discover_skills(roots: list[Path]) -> list[Path]:
    found: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for child in sorted(root.iterdir()):
            if child.name in {".system", "builtin", "builtins"}:
                continue
            if (child / "SKILL.md").is_file():
                found.append(child)
    return found


def resolve_targets(args: argparse.Namespace) -> list[Path]:
    targets = [Path(path).expanduser().resolve() for path in args.paths]
    roots = [Path(root).expanduser().resolve() for root in args.root]
    if args.installed:
        roots.extend(root.resolve() for root in default_skill_roots())
    if roots:
        targets.extend(discover_skills(roots))
    unique: list[Path] = []
    seen: set[Path] = set()
    for target in targets:
        if any(part in {".system", "builtin", "builtins"} for part in target.parts):
            continue
        if target not in seen:
            seen.add(target)
            unique.append(target)
    return unique


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def count_matches(text: str, patterns: list[str]) -> int:
    total = 0
    lower = text.lower()
    for pattern in patterns:
        total += len(re.findall(pattern, lower))
    return total


def analyze_skill(path: Path) -> dict[str, object]:
    skill_file = path / "SKILL.md"
    if not skill_file.is_file():
        return {
            "path": str(path),
            "error": "Missing SKILL.md",
        }

    text = skill_file.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    lines = text.splitlines()
    headings = len(HEADING_RE.findall(text))
    code_fences = text.count("```") // 2
    table_lines = sum(1 for line in lines if "|" in line)
    quote_lines = sum(1 for line in lines if line.lstrip().startswith(">"))
    link_count = text.count("](")
    issues = []

    for rule in ISSUE_RULES:
        hits = count_matches(text, rule["patterns"])
        if hits == 0:
            continue
        threshold = 1 if rule["id"] != "variant-sprawl" else 3
        if hits < threshold:
            continue
        if rule["id"] == "onboarding-hot-path" and len(lines) < 80 and quote_lines < 4:
            continue
        if rule["id"] == "variant-sprawl" and len(lines) < 100:
            continue
        if rule["id"] == "philosophy-load" and len(lines) < 80:
            continue
        if rule["id"] == "hardcoded-copy" and hits < 3 and quote_lines < 2:
            continue
        if rule["id"] == "example-load" and code_fences < 2 and hits < 2:
            continue
        if rule["id"] == "eager-reads" and len(lines) < 80 and hits < 2:
            continue
        issues.append(
            {
                "id": rule["id"],
                "label": rule["label"],
                "severity": rule["severity"],
                "change_type": rule["change_type"],
                "hits": hits,
                "recommendation": rule["recommendation"],
            }
        )

    if len(lines) > 220:
        issues.append(
            {
                "id": "oversized-skill-md",
                "label": "Oversized SKILL.md",
                "severity": "medium",
                "change_type": "safe-structural",
                "hits": len(lines),
                "recommendation": "Shrink the hot path and route detail into references before the file grows further.",
            }
        )

    description = frontmatter.get("description", "")
    if "use when" not in description.lower():
        issues.append(
            {
                "id": "trigger-metadata",
                "label": "Trigger metadata needs work",
                "severity": "medium",
                "change_type": "safe-structural",
                "hits": 1,
                "recommendation": "Make the frontmatter description say both what the skill does and when to use it.",
            }
        )
    elif len(description) > 450:
        issues.append(
            {
                "id": "frontmatter-too-long",
                "label": "Frontmatter description is too long",
                "severity": "low",
                "change_type": "safe-structural",
                "hits": len(description),
                "recommendation": "Shorten the description so triggers stay precise without carrying body-level detail.",
            }
        )

    return {
        "name": frontmatter.get("name", path.name),
        "path": str(path),
        "skill_md": str(skill_file),
        "metrics": {
            "lines": len(lines),
            "words": len(text.split()),
            "description_chars": len(description),
            "headings": headings,
            "code_fences": code_fences,
            "table_lines": table_lines,
            "blockquote_lines": quote_lines,
            "links": link_count,
        },
        "issues": issues,
        "summary": build_summary(len(lines), issues),
    }


def build_summary(line_count: int, issues: list[dict[str, object]]) -> str:
    if not issues:
        return f"SKILL.md is {line_count} lines and shows no heuristic bloat issues."
    labels = ", ".join(issue["label"] for issue in issues[:3])
    return f"SKILL.md is {line_count} lines with likely hot-path waste in: {labels}."


def render_markdown(results: list[dict[str, object]]) -> str:
    sections: list[str] = []
    for result in results:
        if "error" in result:
            sections.append(f"## {result['path']}\n- Error: {result['error']}")
            continue
        metrics = result["metrics"]
        sections.append(
            "\n".join(
                [
                    f"## {result['name']}",
                    f"- Path: `{result['path']}`",
                    f"- Lines: {metrics['lines']}",
                    f"- Words: {metrics['words']}",
                    f"- Description chars: {metrics['description_chars']}",
                    f"- Summary: {result['summary']}",
                ]
            )
        )
        issues = result["issues"]
        if not issues:
            sections.append("- Issues: none detected")
            continue
        sections.append("- Issues:")
        for issue in issues:
            sections.append(
                f"  - [{issue['severity']}] {issue['label']} ({issue['change_type']}): {issue['recommendation']}"
            )
    return "\n".join(sections)


def main() -> int:
    args = parse_args()
    targets = resolve_targets(args)
    if not targets:
        print("[]", end="" if args.format == "json" else "\n")
        return 0

    results = [analyze_skill(target) for target in targets]
    if args.format == "markdown":
        print(render_markdown(results))
    else:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

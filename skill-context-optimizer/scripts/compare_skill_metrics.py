#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def skill_metrics(skill_dir: Path) -> dict[str, int]:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    refs = skill_dir / "references"
    scripts = skill_dir / "scripts"
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "reference_files": len(list(refs.glob("**/*"))) if refs.exists() else 0,
        "script_files": len(list(scripts.glob("**/*"))) if scripts.exists() else 0,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare before and after skill metrics.")
    parser.add_argument("before", help="Original skill directory")
    parser.add_argument("after", help="Compressed skill directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    before = skill_metrics(Path(args.before).expanduser().resolve())
    after = skill_metrics(Path(args.after).expanduser().resolve())
    delta = {key: after[key] - before[key] for key in before}
    print(
        json.dumps(
            {
                "before": before,
                "after": after,
                "delta": delta,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

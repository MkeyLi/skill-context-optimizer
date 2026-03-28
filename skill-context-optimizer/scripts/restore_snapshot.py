#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Restore skill directories from a snapshot manifest.")
    parser.add_argument("manifest", help="Path to a manifest.json created by snapshot_skills.py")
    parser.add_argument(
        "names",
        nargs="*",
        help="Optional subset of skill names to restore",
    )
    return parser.parse_args()


def restore_entry(entry: dict[str, str]) -> dict[str, str]:
    source = Path(entry["backup"]).resolve()
    target = Path(entry["source"]).resolve()
    if not source.is_dir():
        raise SystemExit(f"Missing backup directory: {source}")

    moved_existing = ""
    if target.exists():
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        moved_target = target.parent / f"{target.name}.pre-restore-{timestamp}"
        shutil.move(str(target), str(moved_target))
        moved_existing = str(moved_target)

    shutil.copytree(source, target)
    return {
        "name": entry["name"],
        "restored_to": str(target),
        "previous_version_moved_to": moved_existing,
    }


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest).expanduser().resolve()
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    selected = set(args.names)

    results = []
    for entry in data["entries"]:
        if selected and entry["name"] not in selected:
            continue
        results.append(restore_entry(entry))

    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

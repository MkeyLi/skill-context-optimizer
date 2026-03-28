#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create reversible snapshots of skill directories.")
    parser.add_argument("paths", nargs="+", help="Skill directories to snapshot")
    parser.add_argument(
        "--backup-root",
        default=".skill-context-optimizer-backups",
        help="Directory where snapshots will be stored",
    )
    return parser.parse_args()


def copy_skill(source: Path, destination: Path) -> None:
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"),
    )


def main() -> int:
    args = parse_args()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = Path(args.backup_root).expanduser().resolve() / timestamp
    backup_root.mkdir(parents=True, exist_ok=True)

    entries = []
    for raw_path in args.paths:
        source = Path(raw_path).expanduser().resolve()
        if not source.is_dir():
            raise SystemExit(f"Not a directory: {source}")
        destination = backup_root / source.name
        copy_skill(source, destination)
        entries.append(
            {
                "name": source.name,
                "source": str(source),
                "backup": str(destination),
            }
        )

    manifest = {
        "created_at": datetime.now().isoformat(),
        "backup_root": str(backup_root),
        "entries": entries,
    }
    manifest_path = backup_root / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

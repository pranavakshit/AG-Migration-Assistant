from __future__ import annotations

import argparse
import shutil
from pathlib import Path


DEFAULT_SOURCE = Path.home() / ".gemini" / "antigravity"
DEFAULT_TARGET = Path.home() / ".gemini" / "antigravity-ide"


def _copy_tree(source: Path, target: Path, dry_run: bool) -> list[str]:
    actions: list[str] = []

    if not source.exists():
        actions.append(f"SKIP missing source: {source}")
        return actions

    for subdir_name in ("conversations", "brain"):
        src = source / subdir_name
        dst = target / subdir_name

        if not src.exists():
            actions.append(f"SKIP missing folder: {src}")
            continue

        for path in src.rglob("*"):
            relative = path.relative_to(src)
            destination = dst / relative

            if path.is_dir():
                if destination.exists():
                    continue
                actions.append(f"CREATE DIR {destination}")
                if not dry_run:
                    destination.mkdir(parents=True, exist_ok=True)
                continue

            if destination.exists():
                actions.append(f"SKIP existing file: {destination}")
                continue

            actions.append(f"COPY {path} -> {destination}")
            if not dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, destination)

    return actions


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="antigravity-migrator",
        description="Copy legacy Antigravity chats and brain data into Antigravity IDE.",
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Legacy Antigravity data directory.")
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET, help="Antigravity IDE data directory.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be copied without changing files.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    actions = _copy_tree(args.source.expanduser(), args.target.expanduser(), args.dry_run)
    for action in actions:
        print(action)

    if not actions:
        print("Nothing to do.")

    return 0


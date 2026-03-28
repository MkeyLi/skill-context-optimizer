# Verification And Rollback

Use this reference after the plan is ready.

## Approval Gate

Before editing, show:

1. the target skills
2. the main hot-path problems per skill
3. the planned safe structural edits
4. the planned content-sensitive edits

Wait for the user's approval before executing any content-sensitive compression.

## Snapshot

Create a snapshot before modifying files:

```bash
python scripts/snapshot_skills.py <skill-path>...
```

The command prints a manifest path. Keep it in the final report.

## Validation Checklist

After compression:

1. `SKILL.md` still has valid frontmatter.
2. All links from `SKILL.md` point to real files.
3. Variant-specific details remain reachable from `SKILL.md`.
4. Trigger coverage in the frontmatter is still specific.
5. The edited skill passes:

```bash
python /Users/pipi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>
```

6. Before and after metrics show a useful reduction or cleaner issue profile.

## Rollback

Restore from a manifest with:

```bash
python scripts/restore_snapshot.py <manifest.json>
```

The restore script moves the current target to a timestamped `pre-restore` folder before copying the backup back into place. This keeps the rollback itself reversible.

## Final Report

Always include:

- edited skills
- before and after `SKILL.md` line counts
- major structural moves
- any content-sensitive decisions that were preserved or deferred
- validator results
- the exact rollback command

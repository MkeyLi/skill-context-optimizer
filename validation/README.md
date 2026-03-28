# Validation

This folder records how `skill-context-optimizer` compressed four public skills from `zarazhangrui` without breaking their skill structure.

## Backup

The validation workdirs were snapshotted before edits with this manifest:

`/Users/pipi/Documents/Comp_Skill/validation/backups/20260328-124341/manifest.json`

Restore command:

```bash
python /Users/pipi/Documents/Comp_Skill/skill-context-optimizer/scripts/restore_snapshot.py /Users/pipi/Documents/Comp_Skill/validation/backups/20260328-124341/manifest.json
```

## Summary

| Skill | Lines | Words | Heuristic issues |
| --- | --- | --- | --- |
| `follow-builders` | 466 -> 44 | 2851 -> 294 | 6 -> 0 |
| `frontend-slides` | 322 -> 46 | 2868 -> 343 | 8 -> 0 |
| `youtube-to-ebook` | 171 -> 43 | 555 -> 309 | 3 -> 0 |
| `codebase-to-course` | 273 -> 45 | 3933 -> 401 | 5 -> 0 |

All four compressed skills still pass `quick_validate.py`.

See `reports/` for per-skill details.

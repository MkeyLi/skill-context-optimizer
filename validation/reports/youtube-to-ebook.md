# youtube-to-ebook

## Problems found before compression

- `SKILL.md` mixed setup, commands, known quirks, automation, customization, and pipeline overview.
- The frontmatter described what the skill does but not clearly when to use it.
- Long code examples and implementation details were still on the hot path.

## Compression plan

Safe structural moves:

- keep a small workflow router and invariants in `SKILL.md`
- move setup and file orientation into `references/setup.md`
- move recurring local automation into `references/automation.md`
- move API and transcript edge cases into `references/known-quirks.md`
- tighten the frontmatter so it includes both task scope and trigger conditions

Content-sensitive changes accepted for this validation:

- rewrite quick-start prose into shorter route-oriented instructions

## Result

- `SKILL.md`: 171 lines -> 43 lines
- words: 555 -> 309
- heuristic issues: 3 -> 0
- validator: pass

## Files added

- `references/setup.md`
- `references/automation.md`
- `references/known-quirks.md`

## Notes

This repo needed the lightest compression. The final structure keeps command discovery and operational quirks visible without letting setup or automation crowd the hot path.

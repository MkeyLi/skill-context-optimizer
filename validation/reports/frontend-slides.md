# frontend-slides

## Problems found before compression

- `SKILL.md` carried intake, style discovery, enhancement rules, PPT conversion, deployment, PDF export, and gotchas all at once.
- The design manifesto was too large for hot-path use.
- Share and export guidance was cold-path material but always loaded.
- Generation resources were mentioned too eagerly.

## Compression plan

Safe structural moves:

- keep only core invariants, mode routing, and density limits in `SKILL.md`
- move visual-direction guidance into `references/design-principles.md`
- move new-deck intake and style discovery into `references/intake-and-style-discovery.md`
- move enhancement and PPT conversion rules into `references/modes.md`
- move deployment and PDF export into `references/sharing-and-export.md`

Content-sensitive changes accepted for this validation:

- shorten the long anti-generic-design manifesto into a smaller design-quality contract
- replace some long user-facing wording with routing-level instructions

## Result

- `SKILL.md`: 322 lines -> 46 lines
- words: 2868 -> 343
- heuristic issues: 8 -> 0
- validator: pass

## Files added

- `references/design-principles.md`
- `references/intake-and-style-discovery.md`
- `references/modes.md`
- `references/sharing-and-export.md`

## Notes

The compressed version still preserves the three top-level modes, viewport constraints, and generation requirements, but deploy or export guidance now stays off the hot path until the user actually needs it.

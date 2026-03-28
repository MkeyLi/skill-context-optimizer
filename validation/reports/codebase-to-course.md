# codebase-to-course

## Problems found before compression

- `SKILL.md` held a first-run welcome, audience model, pedagogy, content philosophy, design identity, and implementation gotchas.
- The frontmatter was carrying body-level detail and was too long.
- Important workflow steps existed, but they were surrounded by large amounts of philosophy that only matters during authoring.

## Compression plan

Safe structural moves:

- keep only workflow routing and non-negotiable output constraints in `SKILL.md`
- move the learner persona and goals into `references/learner-model.md`
- move curriculum and quiz design into `references/course-design.md`
- move build-order and implementation rules into `references/implementation-rules.md`
- shorten the frontmatter while keeping trigger coverage

Content-sensitive changes accepted for this validation:

- replace the long first-run welcome with route-level guidance
- compress the "vibe coder" framing into a smaller audience definition

## Result

- `SKILL.md`: 273 lines -> 45 lines
- words: 3933 -> 401
- heuristic issues: 5 -> 0
- validator: pass

## Files added

- `references/learner-model.md`
- `references/course-design.md`
- `references/implementation-rules.md`

## Notes

The compressed version still preserves the core promise: analyze a codebase, design a practical course for non-technical builders, generate a single HTML artifact, and review it with the user. The large pedagogy blocks are still available, just no longer resident in the hot path.

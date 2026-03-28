# follow-builders

## Problems found before compression

- `SKILL.md` mixed first-run onboarding, runtime digest execution, and config mutation.
- Platform, delivery, cron, and language branches all lived on the hot path.
- OpenClaw channel targeting, Telegram or email setup, and welcome-digest behavior loaded on every trigger.
- Runtime invariants were buried inside long prose.

## Compression plan

Safe structural moves:

- keep only platform detection, state detection, runtime invariants, and workflow routing in `SKILL.md`
- move setup into `references/start.md`
- move delivery and cron details into `references/delivery-setup.md`
- move digest execution into `references/digest-run.md`
- move settings and prompt changes into `references/config-ops.md`

Content-sensitive changes accepted for this validation:

- rewrite long onboarding speeches into shorter intent-level instructions
- stop dumping the full source list by default; show it when the user asks

## Result

- `SKILL.md`: 466 lines -> 44 lines
- words: 2851 -> 294
- heuristic issues: 6 -> 0
- validator: pass

## Files added

- `references/start.md`
- `references/delivery-setup.md`
- `references/digest-run.md`
- `references/config-ops.md`

## Notes

The hot path now contains only the information needed to detect environment, detect onboarding state, and route into the correct runtime branch. All cold-path setup detail remains one hop away from `SKILL.md`.

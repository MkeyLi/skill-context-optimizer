# Compression Playbook

Use this reference when deciding what belongs on the hot path.

## Goal

Reduce the cost of loading a skill without reducing its effectiveness.

Treat context as three tiers:

| Tier | Belongs here | Never put here by default |
| --- | --- | --- |
| Hot path: `SKILL.md` | trigger-critical routing, invariants, workflow skeleton, file map | onboarding scripts, long examples, full prompt copy, platform-specific branches |
| Warm path: `references/` | chosen variants, start flows, troubleshooting, examples, schemas | unrelated branches, dead examples, duplicated philosophy |
| Cold path: `scripts/` or assets | deterministic transforms, generators, snapshots, templates | prose that only documents what a script already guarantees |

## Core Rule

Preserve behavior first. Compress structure aggressively. Compress meaning only with user approval.

## Risk Classes

| Class | Typical change | Approval needed |
| --- | --- | --- |
| Safe structural | move onboarding to `references/start.md`, split variants into tables, dedupe repeated facts, route examples to references | no, but still report the plan first |
| Cautious structural | replace long shell recipes with script wrappers, convert prose branches to pseudo-schema, shorten long checklists | usually no if semantics are unchanged |
| Content-sensitive | rewrite user-facing copy into constraints, collapse nuanced requirements, remove examples that carry unique intent | yes |

## Decision Rules

1. Keep only the smallest text needed for correct triggering and task routing in `SKILL.md`.
2. Keep every reference one hop away from `SKILL.md`.
3. Prefer tables, matrices, and schemas over branch-heavy prose.
4. Prefer scripts over repeated operational command blocks.
5. Prefer constraints over hardcoded speeches, unless exact wording is part of the behavior.
6. Prefer one canonical example or template rule over many expanded examples.
7. Gate expensive actions behind conditions. Never keep them as default onboarding steps.
8. Preserve trigger coverage. Frontmatter should stay specific even if the body gets shorter.

## Extra Optimization Targets

- Unconditional "read these three files first" instructions.
- Philosophy repeated in several sections.
- Multiple `CRITICAL` or `NON-NEGOTIABLE` paragraphs saying the same thing.
- Full source lists, exhaustive inventories, or entire catalog dumps shown on first run.
- Variants mixed by platform, delivery, cron, language, hosting provider, or file type.
- Troubleshooting blocks that only matter after a failure.
- Output-format speeches that are better represented as a concise schema.
- Human README content copied into `SKILL.md`.

## What Not to Do

- Do not turn precise operational knowledge into vague advice.
- Do not hide mandatory invariants in deep references.
- Do not create a maze of nested references.
- Do not silently delete unique edge-case handling.
- Do not change frontmatter triggers unless the new version is at least as precise.

---
name: skill-context-optimizer
description: Audit and compress installed or explicitly provided Codex/OpenClaw skills to reduce hot-path context cost without harming behavior. Use when a user asks to compress, trim, optimize, refactor, or de-bloat a skill, or right after another skill reveals context waste such as onboarding in SKILL.md, platform-branch sprawl, repeated copy, long examples, or unconditional high-cost reads. This skill analyzes targets first, proposes a plan, waits for approval before meaning-changing edits, creates rollback snapshots, and then refactors one or many skills with progressive disclosure.
---

# Skill Context Optimizer

Use this skill to shrink skill context safely. Preserve capability, routing accuracy, and trigger quality; compress wording and structure, not behavior.

## Workflow

1. Discover targets.
   - Default to installed user skills under `${CODEX_HOME:-$HOME/.codex}/skills`.
   - Exclude `.system` unless the user explicitly asks to touch it.
   - Accept explicit skill paths when the user points at repos or local folders.
   - Run `python scripts/analyze_skills.py --installed` or pass the target paths directly.

2. Analyze before editing.
   - Summarize each target's hot-path waste, trigger risks, and cold-path material.
   - Separate the plan into:
     - `Safe structural edits`: moving onboarding, branching details, examples, prompt copy, or troubleshooting into `references/`, tables, schemas, or scripts.
     - `Content-sensitive edits`: shortening or abstracting requirements in ways that could change meaning.
   - Do not compress yet. Present the plan and wait for user approval before any content-sensitive change.

3. Create a rollback point.
   - Run `python scripts/snapshot_skills.py <skill-path>...`.
   - Keep the printed manifest path. Report it back to the user.
   - If the user later wants to undo, run `python scripts/restore_snapshot.py <manifest.json>`.

4. Refactor after approval.
   - If more than one skill is being compressed and subagents are available, spawn one subagent per skill after the snapshot is taken.
   - Give each subagent ownership of one skill folder. They are not alone in the codebase and must not revert other edits.
   - Prefer progressive disclosure:
     - keep only trigger-critical routing and invariants in `SKILL.md`
     - move onboarding, variants, examples, and full prompt copy into `references/`
     - convert branch-heavy prose into compact decision tables or pseudo-schemas
     - move deterministic operations into scripts
   - Keep reference depth shallow. Every reference file should be linked directly from `SKILL.md`.
   - Do not silently drop requirements. If compression would remove nuance, keep the detail but move it off the hot path.

5. Validate the result.
   - Run `python /Users/pipi/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>` on every edited skill.
   - Re-run `python scripts/analyze_skills.py <skill-dir>` to compare size and issue profile.
   - Check that every referenced file exists and every moved branch is still reachable from `SKILL.md`.
   - Report before/after metrics, residual risks, and the rollback command.

## Read Next

- Read `references/compression-playbook.md` for compression goals, risk classes, and decision rules.
- Read `references/rewrite-patterns.md` for common transformations and destination patterns.
- Read `references/verification-and-rollback.md` for approval gates, validation, and undo procedure.

## Output Contract

Always return:
- the target skill list
- the issue summary per skill
- the proposed compression plan before edits
- the snapshot manifest path
- the validation result and rollback command after edits

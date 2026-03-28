# Skill Context Optimizer

`skill-context-optimizer` is a skill for Claude Code and OpenClaw that compresses other skills without weakening their behavior. It focuses on context engineering: keep trigger-critical routing in `SKILL.md`, move cold-path detail into `references/`, move deterministic operations into `scripts/`, and preserve rollback at every step.

## Repository layout

- `skill-context-optimizer/`: the installable skill
- `validation/`: verification artifacts for four public skills from `zarazhangrui`

## What the skill does

1. Scans installed skills or explicit skill folders.
2. Analyzes hot-path waste such as onboarding in `SKILL.md`, variant sprawl, repeated copy, long examples, and eager file reads.
3. Produces a plan before editing.
4. Creates reversible snapshots.
5. Refactors one or many skills with progressive disclosure.
6. Validates the result and returns a rollback command.

## Install

Paste one of the prompts below directly into Claude Code or OpenClaw. The agent should fetch the GitHub repo, copy only the `skill-context-optimizer/` folder, and place it in the correct skills directory.

### Claude Code

```text
Install https://github.com/MkeyLi/skill-context-optimizer as a Claude Code skill.

Requirements:
- Default target: ~/.claude/skills/skill-context-optimizer
- If I ask for project-only install, use .claude/skills/skill-context-optimizer instead
- Only copy the repository's skill-context-optimizer/ folder
- Do not copy validation/ or other repo-level files
- If the target already exists, explain what will change before overwriting it
- Confirm that SKILL.md exists after installation
- Do not modify any other skills
- Remind me to start a new Claude Code session after installation
```

### OpenClaw

```text
Install https://github.com/MkeyLi/skill-context-optimizer as an OpenClaw skill.

Requirements:
- Default target: ~/.openclaw/skills/skill-context-optimizer
- If I ask for workspace-only install, use skills/skill-context-optimizer instead
- If I ask for agent-skill install, use ~/.agents/skills/skill-context-optimizer or .agents/skills/skill-context-optimizer as appropriate
- Only copy the repository's skill-context-optimizer/ folder
- Do not copy validation/ or other repo-level files
- If the target already exists, explain what will change before overwriting it
- Confirm that SKILL.md exists after installation
- Do not modify any other skills
- Remind me to start a new OpenClaw session after installation
```

### References

- Claude Code skills docs: [Extend Claude with skills](https://code.claude.com/docs/en/skills)
- Claude Code installation: [Set up Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- OpenClaw skills docs: [Skills](https://docs.openclaw.ai/skills)

## Validation target set

The validation artifacts cover these public skills:

- `follow-builders`
- `frontend-slides`
- `youtube-to-ebook`
- `codebase-to-course`

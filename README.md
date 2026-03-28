# Skill Context Optimizer

`skill-context-optimizer` is a Codex/OpenClaw skill for compressing other skills without weakening their behavior. It focuses on context engineering: keep trigger-critical routing in `SKILL.md`, move cold-path detail into `references/`, move deterministic operations into `scripts/`, and preserve rollback at every step.

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

### Claude Code

Claude Code skills live in either your personal skills directory or a project-local `.claude/skills/` directory.

1. Install Claude Code if needed:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
2. Install this skill as a personal skill:
   ```bash
   mkdir -p ~/.claude/skills
   cp -R skill-context-optimizer ~/.claude/skills/skill-context-optimizer
   ```
3. Or install it only for the current repository:
   ```bash
   mkdir -p .claude/skills
   cp -R skill-context-optimizer .claude/skills/skill-context-optimizer
   ```
4. Start a new Claude Code session and invoke it directly with `/skill-context-optimizer`, or let Claude load it when relevant.

### OpenClaw

OpenClaw loads skills from a shared local directory and from workspace-local `skills/` folders.

1. Install OpenClaw if needed.
2. Install this skill for all OpenClaw workspaces on the machine:
   ```bash
   mkdir -p ~/.openclaw/skills
   cp -R skill-context-optimizer ~/.openclaw/skills/skill-context-optimizer
   ```
3. Or install it only in the current OpenClaw workspace:
   ```bash
   mkdir -p ./skills
   cp -R skill-context-optimizer ./skills/skill-context-optimizer
   ```
4. Start a new OpenClaw session so the skill is reloaded.

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

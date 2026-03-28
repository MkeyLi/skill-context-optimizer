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

Before copying the skill into Claude Code or OpenClaw, you need a local copy of this repository. The `cp -R skill-context-optimizer ...` command only works after you have cloned or downloaded the repo.

If you want the agent to do the installation for you, the easiest approach is to paste one of the prompts below directly into Claude Code or OpenClaw. These are agent instructions, not built-in product commands.

### Paste into Claude Code

Install as a personal skill:

```text
Install the skill from https://github.com/MkeyLi/skill-context-optimizer into my personal Claude Code skills directory at ~/.claude/skills/skill-context-optimizer.

Requirements:
- Only copy the repository's skill-context-optimizer/ folder.
- Do not copy validation/ or other repo-level files.
- If the target already exists, show me the diff or explain what would change before overwriting it.
- Confirm that SKILL.md exists after installation.
- Tell me that I need to restart Claude Code for the new skill to load.
```

Install only for the current project:

```text
Install the skill from https://github.com/MkeyLi/skill-context-optimizer into this project's .claude/skills/skill-context-optimizer directory.

Requirements:
- Only copy the repository's skill-context-optimizer/ folder.
- Do not copy validation/ or other repo-level files.
- If the target already exists, show me the diff or explain what would change before overwriting it.
- Confirm that .claude/skills/skill-context-optimizer/SKILL.md exists after installation.
- Do not modify any other skills.
```

### Paste into OpenClaw

Install as a shared machine-wide skill:

```text
Install the skill from https://github.com/MkeyLi/skill-context-optimizer into ~/.openclaw/skills/skill-context-optimizer for OpenClaw.

Requirements:
- Only copy the repository's skill-context-optimizer/ folder.
- Do not copy validation/ or other repo-level files.
- If the target already exists, show me the diff or explain what would change before overwriting it.
- Confirm that SKILL.md exists after installation.
- Tell me that I need to start a new OpenClaw session for the skill to load.
```

Install only for the current workspace:

```text
Install the skill from https://github.com/MkeyLi/skill-context-optimizer into this workspace's skills/skill-context-optimizer directory for OpenClaw.

Requirements:
- Only copy the repository's skill-context-optimizer/ folder.
- Do not copy validation/ or other repo-level files.
- If the target already exists, show me the diff or explain what would change before overwriting it.
- Confirm that skills/skill-context-optimizer/SKILL.md exists after installation.
- Do not modify any other skills.
```

### Get the files

Option 1: clone the repository

```bash
git clone https://github.com/MkeyLi/skill-context-optimizer.git
cd skill-context-optimizer
```

Option 2: download the ZIP from GitHub, extract it locally, and enter the extracted folder. In both cases, you should end up with a local `skill-context-optimizer/` directory that contains `SKILL.md`.

### Claude Code

Claude Code skills live in either your personal skills directory or a project-local `.claude/skills/` directory.

1. Install Claude Code if needed:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
2. After cloning or extracting this repository, install this skill as a personal skill:
   ```bash
   mkdir -p ~/.claude/skills
   cp -R ./skill-context-optimizer ~/.claude/skills/skill-context-optimizer
   ```
3. Or install it only for the current repository:
   ```bash
   mkdir -p .claude/skills
   cp -R ./skill-context-optimizer .claude/skills/skill-context-optimizer
   ```
4. Start a new Claude Code session and invoke it directly with `/skill-context-optimizer`, or let Claude load it when relevant.

### OpenClaw

OpenClaw can load skills from `~/.openclaw/skills`, `~/.agents/skills`, `<workspace>/.agents/skills`, and `<workspace>/skills`.

1. Install OpenClaw if needed.
2. After cloning or extracting this repository, install this skill as a shared skill for all workspaces on the machine:
   ```bash
   mkdir -p ~/.openclaw/skills
   cp -R ./skill-context-optimizer ~/.openclaw/skills/skill-context-optimizer
   ```
3. Or install it as a personal agent skill:
   ```bash
   mkdir -p ~/.agents/skills
   cp -R ./skill-context-optimizer ~/.agents/skills/skill-context-optimizer
   ```
4. Or install it only for the current workspace:
   ```bash
   mkdir -p ./skills
   cp -R ./skill-context-optimizer ./skills/skill-context-optimizer
   ```
5. Or install it as a project agent skill:
   ```bash
   mkdir -p ./.agents/skills
   cp -R ./skill-context-optimizer ./.agents/skills/skill-context-optimizer
   ```
6. Start a new OpenClaw session so the skill is reloaded.

Note: if this skill is ever published to ClawHub, OpenClaw can install it with `openclaw skills install <skill-slug>`. This repository is currently distributed through GitHub, so users should clone or download it first.

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

# Skill Context Optimizer

`skill-context-optimizer` 是一个用于压缩其他 Codex/OpenClaw skills 的技能，目标是在不削弱原有效果的前提下，降低热路径上下文成本。它的核心方法是：`SKILL.md` 只保留触发与路由关键内容，把冷路径细节移到 `references/`，把确定性操作移到 `scripts/`，并且全程保留可回退能力。

## 仓库结构

- `skill-context-optimizer/`：可安装的技能本体
- `validation/`：针对 `zarazhangrui` 4 个公开 skills 的验证产物

## 这个 skill 会做什么

1. 扫描已安装 skills 或显式传入的 skill 目录。
2. 分析热路径浪费来源，例如 onboarding 在 `SKILL.md`、平台/交付分支膨胀、重复话术、长示例、无条件全量读取等。
3. 在修改前先给出压缩计划。
4. 创建可恢复快照。
5. 以渐进式披露方式重构一个或多个 skills。
6. 校验结果并返回回退命令。

## 安装方式

### Claude Code

Claude Code 的 skills 可以放在个人目录，也可以放在当前项目的 `.claude/skills/` 目录。

1. 如未安装 Claude Code，先安装：
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
2. 安装为个人 skill：
   ```bash
   mkdir -p ~/.claude/skills
   cp -R skill-context-optimizer ~/.claude/skills/skill-context-optimizer
   ```
3. 或者只在当前仓库内安装：
   ```bash
   mkdir -p .claude/skills
   cp -R skill-context-optimizer .claude/skills/skill-context-optimizer
   ```
4. 重新开启一个 Claude Code 会话，然后直接用 `/skill-context-optimizer` 调用，或者让 Claude 在匹配场景下自动加载。

### OpenClaw

OpenClaw 会从共享本地目录和工作区本地 `skills/` 目录加载 skills。

1. 如未安装 OpenClaw，先完成 OpenClaw 安装。
2. 安装为当前机器上的共享 skill：
   ```bash
   mkdir -p ~/.openclaw/skills
   cp -R skill-context-optimizer ~/.openclaw/skills/skill-context-optimizer
   ```
3. 或者只安装到当前 OpenClaw 工作区：
   ```bash
   mkdir -p ./skills
   cp -R skill-context-optimizer ./skills/skill-context-optimizer
   ```
4. 重新开启一个 OpenClaw 会话，使 skill 被重新加载。

### 参考文档

- Claude Code skills 文档：[Extend Claude with skills](https://code.claude.com/docs/en/skills)
- Claude Code 安装文档：[Set up Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- OpenClaw skills 文档：[Skills](https://docs.openclaw.ai/skills)

## 验证对象

当前验证产物覆盖以下 4 个公开 skill：

- `follow-builders`
- `frontend-slides`
- `youtube-to-ebook`
- `codebase-to-course`

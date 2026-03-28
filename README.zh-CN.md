# Skill Context Optimizer

`skill-context-optimizer` 是一个面向 Claude Code 和 OpenClaw 的 skill，用来在不削弱原有效果的前提下压缩其他 skills，降低主上下文负担。它的核心方法是：`SKILL.md` 只保留触发与路由关键内容，把按需才需要的信息移到 `references/`，把确定性操作移到 `scripts/`，并且全程保留可回退能力。

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

把下面任意一段直接发给 Claude Code 或 OpenClaw，agent 就会自行拉取 GitHub 仓库，并把 `skill-context-optimizer/` 放到正确的技能目录里。

### 直接贴给 Claude Code

```text
请把 https://github.com/MkeyLi/skill-context-optimizer 安装成 Claude Code skill。

要求：
- 默认安装到 ~/.claude/skills/skill-context-optimizer
- 只复制仓库里的 skill-context-optimizer/ 目录
- 不要复制 validation/ 或其他仓库级文件
- 安装完成后确认 SKILL.md 存在
- 不要修改其他 skills
```

### 直接贴给 OpenClaw

```text
请把 https://github.com/MkeyLi/skill-context-optimizer 安装成 OpenClaw skill。

要求：
- 默认安装到 ~/.openclaw/skills/skill-context-optimizer
- 只复制仓库里的 skill-context-optimizer/ 目录
- 不要复制 validation/ 或其他仓库级文件
- 安装完成后确认 SKILL.md 存在
- 不要修改其他 skills
```

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

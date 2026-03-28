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

在把这个 skill 放进 Claude Code 或 OpenClaw 之前，用户需要先把本仓库下载到本地。`cp -R skill-context-optimizer ...` 这一步只有在你已经克隆仓库或下载 ZIP 后才成立。

### 先获取仓库文件

方式一：直接克隆仓库

```bash
git clone https://github.com/MkeyLi/skill-context-optimizer.git
cd skill-context-optimizer
```

方式二：在 GitHub 页面下载 ZIP，解压后进入目录。无论使用哪种方式，本地都应该先有一个包含 `SKILL.md` 的 `skill-context-optimizer/` 目录。

### Claude Code

Claude Code 的 skills 可以放在个人目录，也可以放在当前项目的 `.claude/skills/` 目录。

1. 如未安装 Claude Code，先安装：
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
2. 克隆或解压本仓库后，安装为个人 skill：
   ```bash
   mkdir -p ~/.claude/skills
   cp -R ./skill-context-optimizer ~/.claude/skills/skill-context-optimizer
   ```
3. 或者只在当前仓库内安装：
   ```bash
   mkdir -p .claude/skills
   cp -R ./skill-context-optimizer .claude/skills/skill-context-optimizer
   ```
4. 重新开启一个 Claude Code 会话，然后直接用 `/skill-context-optimizer` 调用，或者让 Claude 在匹配场景下自动加载。

### OpenClaw

OpenClaw 支持从 `~/.openclaw/skills`、`~/.agents/skills`、`<workspace>/.agents/skills` 和 `<workspace>/skills` 加载 skills。

1. 如未安装 OpenClaw，先完成 OpenClaw 安装。
2. 克隆或解压本仓库后，安装为当前机器上所有工作区共用的 skill：
   ```bash
   mkdir -p ~/.openclaw/skills
   cp -R ./skill-context-optimizer ~/.openclaw/skills/skill-context-optimizer
   ```
3. 或者安装为当前用户的 agent skill：
   ```bash
   mkdir -p ~/.agents/skills
   cp -R ./skill-context-optimizer ~/.agents/skills/skill-context-optimizer
   ```
4. 或者只安装到当前 OpenClaw 工作区：
   ```bash
   mkdir -p ./skills
   cp -R ./skill-context-optimizer ./skills/skill-context-optimizer
   ```
5. 或者安装为当前项目的 agent skill：
   ```bash
   mkdir -p ./.agents/skills
   cp -R ./skill-context-optimizer ./.agents/skills/skill-context-optimizer
   ```
6. 重新开启一个 OpenClaw 会话，使 skill 被重新加载。

补充说明：如果这个 skill 以后发布到 ClawHub，也可以通过 `openclaw skills install <skill-slug>` 安装；但当前这个仓库是通过 GitHub 分发的，所以应先克隆仓库或下载 ZIP，再复制 skill 目录。

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

---
name: skill-context-optimizer
description: 给 Claude Code 和 OpenClaw 的 skills 做瘦身和整理，在不影响原有效果的前提下减少无关上下文占用。用户提到压缩、精简、优化、整理、重写 skill，或者刚用完某个 skill 后发现它把新手引导、平台分支、重复说明、长示例、完整话术等内容都堆在 SKILL.md 里时使用。此 skill 会先找出问题，再给出整理方案；凡是可能改动原意的内容，都会先征求用户确认；正式修改前会先做备份，最后再按渐进式披露的方式完成重构。
---

# Skill Context Optimizer

用更节省上下文的方式重写其他 skills。优先保留原有能力、触发准确性和使用效果；重点整理主提示词里的常驻内容，不随意改动真正影响结果的要求。

## 工作流

1. 找出目标 skill。
   - 默认检查这些位置里用户自己安装的 skills：
     - Claude Code：`~/.claude/skills`、当前项目的 `.claude/skills`
     - OpenClaw：`~/.openclaw/skills`、`~/.agents/skills`、当前工作区的 `.agents/skills`、当前工作区的 `skills`
   - 严禁改动 Claude Code 或 OpenClaw 自带的系统 skills；这个限制不因用户要求而放宽。
   - 如果用户给了仓库路径或本地目录，也接受显式路径。
   - 运行 `python scripts/analyze_skills.py --installed`，或直接传入目标路径。

2. 先分析，再动手。
   - 汇总每个目标 skill 在主提示词里塞了哪些不该常驻的内容、哪些地方可能影响触发、哪些细节更适合按需读取。
   - 把计划拆成两类：
     - `Safe structural edits`：把 onboarding、分支细节、示例、完整 prompt 文案、troubleshooting 等移到 `references/`、表格、schema 或脚本里。
     - `Content-sensitive edits`：会压缩或抽象原要求、可能改变语义的内容调整。
   - 这一阶段先不要实际压缩。先把计划告诉用户；凡是涉及 `Content-sensitive edits`，都必须先等用户确认。

3. 先做回退备份。
   - 运行 `python scripts/snapshot_skills.py <skill-path>...`。
   - 记住输出的 manifest 路径，并反馈给用户。
   - 如果用户之后要撤销，运行 `python scripts/restore_snapshot.py <manifest.json>`。

4. 用户确认后再整理。
   - 如果有多个 skills 需要压缩，且可以使用 sub-agent，就在快照完成后为每个 skill 启一个 sub-agent。
   - 每个 sub-agent 只负责一个 skill 目录。它们不是独占代码库，不得回滚其他并行改动。
   - 再次确认目标里没有系统自带 skills；一旦发现，直接跳过并告知用户原因。
   - 优先使用渐进式披露：
     - `SKILL.md` 只保留触发关键的路由和不变量
     - 把 onboarding、variants、examples、完整 prompt 文案移到 `references/`
     - 把分支很重的自然语言改成决策表或 pseudo-schema
     - 把确定性操作移到脚本
   - 引用层级保持浅。所有 reference 文件都应当直接从 `SKILL.md` 链接到。
   - 不要静默删除要求。如果压缩会损失细节，就保留内容，但把它移出热路径。

5. 最后验证结果。
   - 如果你的环境里有 skill 结构校验工具，就对每个改过的 skill 跑一次校验。
   - 再运行一次 `python scripts/analyze_skills.py <skill-dir>`，比较压缩前后体积和问题画像。
   - 检查所有被引用的文件都存在，并且所有被迁移出去的分支都仍然能从 `SKILL.md` 到达。
   - 最终反馈前后指标、残余风险和回退命令。

## 按需读取

- 读取 `references/compression-playbook.md`：了解压缩目标、风险分类和决策规则。
- 读取 `references/rewrite-patterns.md`：了解常见重写模式和迁移目的地。
- 读取 `references/verification-and-rollback.md`：了解确认门槛、验证步骤和撤销流程。

## 输出约定

- 目标 skill 列表
- 每个 skill 的问题摘要
- 修改前的压缩计划
- 快照 manifest 路径
- 修改后的验证结果与回退命令

# 常见改写方式

把一个很臃肿的 skill 改写成“按需展开”的结构时，可以优先参考下面这些模式。

## 问题与改法对照表

| `SKILL.md` 里的常见问题 | 推荐改法 | 适合移到哪里 |
| --- | --- | --- |
| 首次欢迎语、配置引导、很长的 onboarding 文案 | 主文件里只保留“何时需要 onboarding”和入口 | `references/start.md` |
| OpenClaw / Claude Code 之类的平台分支 | 把长篇说明改成紧凑的决策表 | `references/platform-variants.md` |
| 交付方式、cron、语言、托管、导出这些分支 | 改成 pseudo-schema 或决策矩阵 | `references/variants.md` |
| 完整 prompt 文案或整段用户话术模板 | 主文件里只保留意图约束和占位符，长样例移出去 | `references/prompt-templates.md` |
| 重复出现的命令块或 shell 流程 | 如果操作够确定，就改成脚本 | `scripts/` |
| 很长的排错说明 | 主文件里只保留一句“遇到这类问题去哪里看”，详细修复移出去 | `references/troubleshooting.md` |
| 一长串示例 | 只留一个模板或参数生成规则 | `references/examples.md` |
| 强制要求把很多文件一次性全读完 | 改成按阶段、按分支加载 | `SKILL.md` 加引用文档 |

## 优先采用的整理方式

### 把 onboarding 改成“只负责分流”

改之前：
- 几大段开场介绍
- 在 `SKILL.md` 里直接写完整提问流程

改之后：
- 主文件里只写“什么情况下需要 onboarding”
- 加一个指向 `references/start.md` 的入口
- 在 `SKILL.md` 里只保留状态判断规则

### 把很多分支的自然语言改成表格

改之前：
- Telegram、email、stdout、OpenClaw、cron、weekly、daily 各写一大段

改之后：
- 一张分流表
- 一个列出各分支所需字段的 schema
- 分支细节移到引用文档

### 把硬编码话术改成意图约束

改之前：
- 大段“告诉用户：……”的原话

改之后：
- 只保留类似“简单说明交付方式差异，并收集频道、频率、时区”的约束
- 只有当原话本身会影响行为时，才保留原文

### 把一堆示例改成模板

改之前：
- 大量展开的自然语言示例

改之后：
- 一个命令模板
- 一条参数生成规则
- 真有独特价值的长示例，移到引用文档

### 把重复事实收敛成不变量清单

改之前：
- 同一条提醒在好几个章节里重复

改之后：
- 在前面集中列一份不变量清单
- 后面章节只引用这条规则，不再重复展开

## 压缩后的常见目录结构

```text
skill-name/
├── SKILL.md
├── references/
│   ├── start.md
│   ├── variants.md
│   ├── prompt-templates.md
│   └── troubleshooting.md
└── scripts/
    └── optional deterministic helpers
```

不要机械地把这些文件全建出来。只创建当前 skill 真正需要的那几个目标文件。

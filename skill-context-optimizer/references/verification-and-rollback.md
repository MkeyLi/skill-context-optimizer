# 验证与回退

当压缩方案已经定下来之后，按这份文档做确认、验证和回退准备。

## 用户确认前必须展示的内容

正式修改前，至少要告诉用户这些内容：

1. 这次要处理哪些 skills
2. 每个 skill 目前最主要的问题
3. 准备做哪些“纯结构整理”
4. 哪些改动可能会碰到原意
5. 明确说明：目标里不包含 Claude Code 或 OpenClaw 自带的内置 skills

凡是可能改动原意的压缩，都必须先等用户确认。

## 备份快照

修改前先做快照备份：

```bash
python scripts/snapshot_skills.py <skill-path>...
```

这个命令会输出一个 manifest 路径。最后汇报结果时要把它一并告诉用户。

## 修改后的检查清单

压缩完成后，至少检查下面这些事：

1. `SKILL.md` 的 frontmatter 仍然合法。
2. `SKILL.md` 里所有链接都能指向真实文件。
3. 被移出去的分支细节，仍然能从 `SKILL.md` 找到入口。
4. frontmatter 里的触发描述仍然足够具体。
5. 如果你的环境里有 skill 结构校验工具，就跑一次：

```bash
python quick_validate.py <skill-dir>
```

6. 前后指标确实有改善，或者至少问题画像更干净了。

## 回退

如果用户要恢复原状，用 manifest 执行回退：

```bash
python scripts/restore_snapshot.py <manifest.json>
```

回退脚本会先把当前版本挪到一个带时间戳的 `pre-restore` 目录里，再把备份拷回来。这样即使执行了回退，这次回退动作本身也还是可逆的。

## 最终汇报至少包含

- 改了哪些 skills
- 每个 `SKILL.md` 压缩前后的行数
- 这次最关键的结构调整是什么
- 哪些涉及原意的改动被保留、延后或放弃了
- 校验结果
- 具体的回退命令

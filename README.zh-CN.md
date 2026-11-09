# 即梦短剧创作插件（Dreamina Novel Plugin）

本插件将 `dreamina-skills` 中的 8 个短剧技能打包给 Codex、ZCode 与 Kimi，通过本机 `jimeng-novel` CLI 执行，不携带账户凭据。当前为不可变预发布候选版；付费生成与真实宿主验收完成前不晋升正式版。

## 能力

- 从创意、小说、剧本或现有分镜进入对应阶段，保留用户原文和本地素材。
- 覆盖剧本、角色与场景、分镜、样片、批量生成、局部返修和本地合成。
- 生成前报价并等用户同意；运行中与结果不明时只查询原任务。

## 本地使用

先运行 `jimeng-novel --help`、`jimeng-novel version`、`jimeng-novel status`。未安装时按 `dreamina-novel-cli-setup` 使用官方安装入口。插件根目录的 `skills/` 可供宿主按本地插件路径加载；市场安装需在本仓发布后另行完成。

## 验证

```bash
python3 -m unittest discover -s tests -q
python3 scripts/verify_vendored_skills.py
```

技能锁定到 `dreamina-skills` 的提交 `87c7f92d38fab1e937ae1c1231a229f7237b1ec0`。CLI 命令以已安装版本的 `--help` 和 `schema get` 为准；本地测试不等于付费生成、真实宿主或成片质量验收。

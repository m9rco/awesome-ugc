# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 的结构，版本号语义化。

## [Unreleased]

### Changed

- **final pass 复核处置**：Roblox 开发者论坛条目换为规范 URL `https://devforum.roblox.com/`（直连 404 / 代理 200 的边缘节点差异）；剔除 2 条全路不可复核的 CN 新闻页（GameLook、半月谈），URL 与原因留档。
- 对复跑时出现 401/403 的条目补 `verify_note`（站点风控抖动，收录时实测 200），并已进入每周体检。
- 目录条目数由 147 调整为 **145**。

### Added

- `docs/RESEARCH.md` §7「剔除留档」：补录六条调研轨自述的 **65 条被拒候选**（URL + 状态码 + 剔除理由），补齐"为什么没收录"这半条证据链（标注为自述、未经逐条复测）。
- `scripts/check_links.py`：代理回退条件扩展——直连返回 4xx（非反爬白名单）时也回退代理复测，使本机结果与 CI 更一致。

## [0.1.0] - 2026-10-28

### Added

- 初始版本：`data/catalog.json`（schema v1）作为唯一数据源，收录平台、编辑器、美术/建模/贴图、AI 提效、素材、教程、创作者计划、社区、数据、政策十类资源。
- `README.md`（简体中文）+ `README.en.md`（English），表格与统计区由脚本生成。
- `scripts/build_readme.py`：由数据生成 README 表格，`--check` 供 CI 校验同步。
- `scripts/check_links.py`：并发链接体检，支持 `--strict` 与 JSON 报告。
- `docs/ART-PIPELINE.md`：各平台头部作者的出图工艺拆解。
- `docs/AI-WORKFLOW.md`：按工序落位的 AI 提效工作流与提示词骨架。
- `docs/RESEARCH.md`：调研方法与核验证据记录。
- `docs/PLATFORMS/`：各平台深度笔记。
- `tests/test_catalog.py`：结构、词表、唯一性、README 同步校验。
- CI：`ci.yml`（lint + test + 链接体检）、`links-weekly.yml`（每周体检，腐烂自动开 issue）。
- Issue 模板与 PR 模板，强制附带实测证据。

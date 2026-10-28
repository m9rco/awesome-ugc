# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 的结构，版本号语义化。

## [Unreleased]

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

# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 的结构，版本号语义化。

## [Unreleased]

### Changed

- 2026-11-23：`create-roblox-com-store` 链接复核 create.roblox.com → create.roblox.com（URL 未变），周体检 DEAD 实为 `SSL UNEXPECTED_EOF_WHILE_READING` TLS 握手瞬时异常、非站点下线；curl 代理实测 200（301 至 /store/models）、直连重试亦曾 200，联网搜索确认仍为官方创作者商店入口，保留官方 URL 并补 `verify_note`。
- 2026-11-23：`docs-neoforged-net-docs-resources` 链接复核 docs.neoforged.net → docs.neoforged.net（URL 未变），同上 TLS 误报；curl 代理实测 200、`<title>`「Resources | NeoForged docs」与库内记录一致，保留官方 URL 并补 `verify_note`。
- 2026-11-16：`huggingface-co-briaai-rmbg-1-4` 链接复核 huggingface.co → huggingface.co（URL 未变），周体检 DEAD 实为 `SSL UNEXPECTED_EOF_WHILE_READING` TLS 握手瞬时异常、非站点下线；curl 代理实测 200、`<title>`「briaai/RMBG-1.4 · Hugging Face」与库内记录一致，保留官方 URL 并补 `verify_note`。
- 2026-11-16：`huggingface-co-microsoft-florence-2-large` 链接复核 huggingface.co → huggingface.co（URL 未变），同上 TLS 误报；curl 直连/代理均 200、`<title>`「microsoft/Florence-2-large · Hugging Face」与库内记录一致，保留官方 URL 并补 `verify_note`。
- **final pass 复核处置**：Roblox 开发者论坛条目换为规范 URL `https://devforum.roblox.com/`（直连 404 / 代理 200 的边缘节点差异）；剔除 2 条全路不可复核的 CN 新闻页（GameLook、半月谈），URL 与原因留档。
- 对复跑时出现 401/403 的条目补 `verify_note`（站点风控抖动，收录时实测 200），并已进入每周体检。
- 目录条目数由 147 调整为 **145**。

### Added

- **2026-11-23 周维护新增 5 条**（全部本机 curl 直连实测 200，`<title>` 取页面原文，访问日期 2026-11-23；覆盖 mini_world / aola_star / channels 三个薄弱平台）：
  - `wiki-miniworldgame-com` — Mini World: CREATA 官方 Wiki（国际版）首页，`https://wiki.miniworldgame.com/`。
  - `wiki-miniworldgame-com-map-developer-guide` — 官方地图开发者指南（尺寸/UI/字体/排行榜规范），`https://wiki.miniworldgame.com/developer_center:developer_editor:map_developer_guide`。
  - `www-100bt-com-alx-320287` — 奥拉星手游六周年「伊乐头像创作征集」规则（含 AI 生成内容限制与版权归属），`https://www.100bt.com/alx/320287/`。
  - `channels-weixin-qq-com` — 视频号助手（微信官方创作者后台），`https://channels.weixin.qq.com/`。
  - `findeross-weixin-qq-com-helper-center-guide` — 微信视频号·视频号助手使用指南，`https://findeross.weixin.qq.com/cgi-bin/mmfindernodelivecrmwebbroker-bin/helper-center/pages/CFop5MyQaj10zRco`。
- **2026-11-23 链接体检**：154 条全量复测，143 ok / 9 反爬拦截（401/403）/ 2 条误报 DEAD（TLS 握手异常，curl 复核均 200）；无真实死链、无链接更新、无移除。剔除不合格候选：dev-wiki 规范/违规案例页（HTTP 200 但无 `<title>`、正文 JS 加载）、`support.weixin.qq.com` 权益指南（无 `<title>`）、`member.bilibili.com/platform/home`（标题与正文均空）、`qmcz.mini1.cn/rules` 与 bilibili 创作功能图鉴（正文仅 JS 壳，无可验证内容）、`blender.org` 与 `docs.blender.org`（403 Cloudflare 反爬盾，无法按命令行复核）、`aola.100bt.com/dayi/93649.html`（与既有投稿说明重复）。
- **2026-11-16 周维护新增 4 条**（补齐 mini_world / aola_star / channels 薄弱平台，全部本机 curl 实测 200，标题取页面 `<title>` 原文，访问日期 2026-11-16）：
  - `www-mini1-cn-article-20190527-839-html` — 《迷你世界》游戏许可及服务协议释义，`https://www.mini1.cn/article/20190527/839.html`。
  - `aola-100bt-com-zixun-167753-html` — 奥拉星官网投稿说明，`https://aola.100bt.com/zixun/167753.html`。
  - `creator-douyin-com` — 抖音创作者中心，`https://creator.douyin.com/`。
  - `creator-xiaohongshu-com` — 小红书创作服务平台，`https://creator.xiaohongshu.com/`。
- **2026-11-16 链接体检**：150 条全量复测，138 ok / 10 反爬拦截（401/403）/ 2 条误报 DEAD（TLS 握手异常，curl 复核均 200）；无真实死链、无链接更新、无移除。剔除 2 条不合格候选：mini1 创作者学院规范页（无 `<title>`、正文 JS 加载）与 samr 国标立项公示页（非已发布标准文本）。
- **2026-11-09 周维护新增 5 条**（补齐 mini_world / aola_star / channels 三个薄弱平台，全部本机 curl 实测 200，标题取页面 `<title>` 原文）：
  - `www-mini1-cn-picture-list` — 迷你世界 图音专区（同人绘 / 壁纸），`https://www.mini1.cn/picture_list`。
  - `www-mini1-cn-news-list-activity-html` — 迷你世界 官方活动（高校游戏创作挑战赛、绘画创作赛等），`https://www.mini1.cn/news_list/activity.html`。
  - `aola-100bt-com-tougaocenter-html` — 奥拉星 投稿专区（亚比手绘 / 鼠绘 / 四格漫画投稿），`https://aola.100bt.com/tougaocenter.html`。
  - `www-kuaishou-com-norm` — 快手社区规范，`https://www.kuaishou.com/norm`。
  - `weixin-qq-com-cgi-bin-readtemplate-t-weixin-agreement-s-video` — 微信视频号运营规范，`https://weixin.qq.com/cgi-bin/readtemplate?t=weixin_agreement&s=video`。
- **2026-11-09 链接体检**：145 条全量复测，136 ok / 0 DEAD / 9 反爬拦截（401/403，非下线），本轮无死链、无链接更新、无移除。

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

# Awesome UGC

**UGC 创作生态资源清单：平台、编辑器、出图工艺，以及能真正省掉工时的那部分 AI。**

[![CI](https://github.com/m9rco/awesome-ugc/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/m9rco/awesome-ugc/actions/workflows/ci.yml)
[![Weekly link check](https://github.com/m9rco/awesome-ugc/actions/workflows/links-weekly.yml/badge.svg?branch=main)](https://github.com/m9rco/awesome-ugc/actions/workflows/links-weekly.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Entries](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fm9rco%2Fawesome-ugc%2Fmain%2Fdata%2Fcatalog.json&query=%24.entries.length&label=entries&color=6f42c1)](data/catalog.json)

简体中文 · [English](README.en.md)

**[资源目录](#资源目录) · [作者怎么做图](#作者怎么做图) · [用-ai-提效](#用-ai-提效) · [贡献](#贡献)**

这不是一份"链接堆"。它回答三个问题：

1. **有哪些地方可以发布 UGC** —— Roblox / 罗布乐思、蛋仔派对、元梦之星、奥拉星、迷你世界、我的世界，各自的分发入口、编辑器与创作者计划在哪。
2. **做得好的人是怎么做图的** —— 从概念、三视图、建模、贴图到上线图和视频，头部作者的流水线长什么样，卡点在哪。
3. **哪些工序可以换成 AI，省掉多少工时** —— 按工序（出图 / 3D / 贴图 / 放大 / 抠图 / 视频 / 配音 / 批量排版 / 发布）钉死工具，而不是罗列一堆"AI 神器"。

每一条链接都经过实测：`HTTP 200` + 页面标题核对，并在 `data/catalog.json` 里留下了状态与核验时间。链接会烂，所以有每周自动体检与自动开 issue。

## 目录

- [为什么做这个仓库](#为什么做这个仓库)
- [资源目录](#资源目录)
- [作者怎么做图](#作者怎么做图)
- [用 AI 提效](#用-ai-提效)
- [数据与统计](#数据与统计)
- [收录标准](#收录标准)
- [仓库结构](#仓库结构)
- [贡献](#贡献)
- [许可](#许可)

## 为什么做这个仓库

UGC 创作者的痛点不是"缺工具"，而是三件事：

- **信息是碎的**：官方文档、编辑器教程、皮肤规格、模型面数限制、审核红线散在官网、贴吧、B 站、Discord 和一堆过期博客里；
- **工艺是隐性的**：头部作者的出图流程几乎不公开，新人只能靠猜分辨率、猜流程、猜配色；
- **AI 工具泛滥且不可靠**：真正稳定能进流水线的工具，和"演示很惊艳、批量就崩"的工具混在一起。

这个仓库把这三件事拆成可核验的条目：**官方优先、注明工序、标注授权、保留核验证据**。

## 资源目录

> 表格由 `data/catalog.json` 生成（`python scripts/build_readme.py`）。**不要手改这一节**，改数据文件。

<!-- CATALOG:BEGIN -->
### Roblox / 罗布乐思

全球最大的 UGC 游戏平台，Roblox Studio + Blender 是服饰/道具创作主流程。

> 深度笔记：[docs/PLATFORMS/roblox.md](docs/PLATFORMS/roblox.md)

_待收录。_

### 蛋仔派对

网易派对游戏，蛋仔工坊承载地图与皮肤创作，乐园是分发入口。

> 深度笔记：[docs/PLATFORMS/eggy-party.md](docs/PLATFORMS/eggy-party.md)

_待收录。_

### 元梦之星 / 圆梦之星

腾讯天美派对游戏，UGC 编辑器与创作者激励并行。

> 深度笔记：[docs/PLATFORMS/dreamstar.md](docs/PLATFORMS/dreamstar.md)

_待收录。_

### 奥拉星

国产精灵养成 / 角色 IP 生态，含玩家自制角色与同人出图社群。

> 深度笔记：[docs/PLATFORMS/aola-star.md](docs/PLATFORMS/aola-star.md)

_待收录。_

### 迷你世界

国产沙盒，皮肤与地图创作门槛低，128×128 皮肤是典型交付物。

> 深度笔记：[docs/PLATFORMS/mini-world.md](docs/PLATFORMS/mini-world.md)

_待收录。_

### 我的世界 / Minecraft

像素皮肤、材质包、模组与数据包，社区工具链最成熟。

> 深度笔记：[docs/PLATFORMS/minecraft.md](docs/PLATFORMS/minecraft.md)

_待收录。_

### 跨平台 · AI 提效 · 生态

不绑定单一平台：AI 出图/建模/贴图工具链、素材授权、数据选品、政策合规。

> 深度笔记：[docs/PLATFORMS/agnostic.md](docs/PLATFORMS/agnostic.md)

_待收录。_
<!-- CATALOG:END -->

## 作者怎么做图

拆解各平台头部作者的出图工艺：交付物规格、软件栈、卡点与可复用技巧。详见 [`docs/ART-PIPELINE.md`](docs/ART-PIPELINE.md)。

- **规格先行**：每个平台的交付物都有硬约束（皮肤尺寸、贴图通道、面数上限、审核禁区）。先看规格再动手，能省掉一半返工。
- **三视图是枢纽**：概念 → 三视图 → 建模/绘制 → 贴图 → 上线图。三视图做扎实，后面每一步都能并行或外包。
- **上线图与实物是两套活**：标题、封面、九宫格排版的点击率，跟作品本身的质量不是一回事，值得单独当一条产线。

## 用 AI 提效

按工序钉工具，而不是按热度。完整工作流、提示词骨架与踩坑见 [`docs/AI-WORKFLOW.md`](docs/AI-WORKFLOW.md)。

| 工序 | 换成什么 | 判断标准 |
| --- | --- | --- |
| 概念与灵感 | 参考图检索 + 文生图批量探索 | 能否 10 分钟出 20 个方向的缩略图 |
| 出图 / 立绘 | 文生图 + 图生图 + 局部重绘 | 风格一致性是否可复现（同 seed / 同一 LoRA） |
| 3D 与模型 | 图生 3D、体素/低模生成 | 导出格式能否进目标编辑器 |
| 贴图与材质 | 文生贴图、材质 PBR 化 | 是否无缝平铺、能否批量 |
| 放大与修复 | 超分 / 去噪 / 脸部修复 | 批量稳定性 > 单张惊艳 |
| 抠图与去背 | 自动分割 | 边缘发丝与半透明处理 |
| 视频与动效 | 图生视频、动捕重定向 | 时长/时长成本比 |
| 配音与音频 | TTS、音效生成 | 商用授权是否明确 |
| 批量排版与产能 | 模板 + 脚本出图 | 一天出多少套，而不是"能不能出" |
| 发布与自动化 | 端自动化 / 开放接口 | 有无账号风险 |

**一条硬规矩**：任何 AI 产物进流水线前，先问三件事——授权能不能商用、结果能不能复现、失败时能不能批量回滚。三条有一条不成立，就不要接进主线。

## 数据与统计

<!-- STATS:BEGIN -->
- 条目总数：**0**（收录时实测 HTTP 200：0）
- 按平台：—
- 按类别：—
- 数据文件：`data/catalog.json`（schema v1，更新于 2026-10-28）
- 报告生成时间：2026-10-28
<!-- STATS:END -->

## 收录标准

**收**：官方站点与官方文档；在维护的开源项目；真实存在且可访问的教程与社区；明确授权的素材库（CC0 / CC-BY / 商用买断）。

**不收**：盗版、破解、外挂、私服、账号与虚拟物品交易；纯推广页；无法访问或需要登录才能判断内容的链接；与现有条目重复的资源；把"AI 神器"当标题的软文。

每条条目必须带：**实测 HTTP 状态** + **页面标题** + **一句话用途** + **授权情况**。

## 仓库结构

```text
awesome-ugc/
├── README.md               # 简体中文（主）
├── README.en.md            # English
├── CONTRIBUTING.md         # 收录门槛与提交流程
├── CHANGELOG.md
├── data/catalog.json       # 唯一数据源（schema v1）
├── docs/
│   ├── ART-PIPELINE.md     # 作者怎么做图
│   ├── AI-WORKFLOW.md      # 用 AI 提效
│   ├── RESEARCH.md         # 调研方法与核验证据
│   ├── ROADMAP.md
│   └── PLATFORMS/          # 各平台深度笔记
├── scripts/
│   ├── build_readme.py     # 由数据生成 README 表格（--check 供 CI）
│   └── check_links.py      # 链接体检（并发，可 --strict）
└── tests/test_catalog.py   # 结构校验 + README 同步校验
```

## 贡献

见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。最短路径：改 `data/catalog.json` → 跑 `python scripts/build_readme.py` → 跑 `python -m pytest` → 提 PR，附上你的实测命令与输出。

## 许可

代码与文档：[MIT](LICENSE)。收录的第三方资源版权归各自作者；条目只提供指路，不镜像、不搬运任何素材。素材授权以各站条款页为准。

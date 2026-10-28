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

全球 UGC 平台标杆：Studio 编辑器 + 创作者商店（Creator Store）+ 开发者兑换（DevEx）。

> 深度笔记：[docs/PLATFORMS/roblox.md](docs/PLATFORMS/roblox.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [Roblox Creator Hub（创作者中心）](https://create.roblox.com) | 平台与官方文档 | — | 创作者一站式入口：文档、商店、人才库、分析与发布后台。 |
| [Roblox 官方创作者文档](https://create.roblox.com/docs) | 平台与官方文档 | — | 官方权威文档总览，覆盖资产、脚本、上架与变现全流程。 |
| [Roblox Studio 文档](https://create.roblox.com/docs/studio) | 编辑器与开发工具 | — | 官方编辑器 Studio 的安装、界面与建模/脚本工作流说明。 |
| [3D 资产通用规格](https://create.roblox.com/docs/art/modeling/specifications) | 美术与建模 | — | 官方建模规格：面数、尺寸、贴图与文件格式的硬性要求。 |
| [Roblox 3D 艺术文档](https://create.roblox.com/docs/art) | 美术与建模 | — | 官方 3D 美术总入口：建模、材质、光照与角色资产做法。 |
| [自定义 3D 资产（建模）](https://create.roblox.com/docs/art/modeling) | 美术与建模 | — | 讲清外部建模工具导入 Roblox 的流程与网格资产规范。 |
| [AI on Roblox（AI 加速工作流）](https://create.roblox.com/docs/ai/accelerated-workflows) | AI 提效工具 | — | 官方 AI 文档：文生 3D、自动绑定、材质与贴图生成等提效功能。 |
| [Roblox Cube（3D 生成基础模型）](https://github.com/Roblox/cube) | AI 提效工具 | — | 官方开源的 3D 生成模型，可自建管线批量产出三维资产。 |
| [Creator Store 官方文档](https://create.roblox.com/docs/production/creator-store) | 素材与资源库 | — | 说明商店资产类型、搜索方法与创作者售卖变现规则。 |
| [Creator Store（创作者商店 / 模型市集）](https://create.roblox.com/store) | 素材与资源库 | — | 官方资产市集，可下载模型、插件、材质与音效直接复用。 |
| [发布到 Marketplace（UGC 上架）](https://create.roblox.com/docs/marketplace/publish-to-marketplace) | 素材与资源库 | — | UGC 饰品与服装上传上架的官方步骤与账号资质要求。 |
| [Roblox Education（教育计划）](https://education.roblox.com) | 教程与学习路径 | — | 官方教学与课程资源，适合系统学习创作与教学者使用。 |
| [Roblox 官方教程](https://create.roblox.com/docs/tutorials) | 教程与学习路径 | — | 官方分步教程，从零完成首个体验与美术/脚本基础。 |
| [DevEx 开发者兑换计划](https://create.roblox.com/docs/production/monetization/developer-exchange) | 创作者计划与变现 | — | 官方文档：创作者把 Robux 收益兑换成现金的门槛与流程。 |
| [Talent Hub（人才协作平台）](https://create.roblox.com/talent) | 创作者计划与变现 | — | 官方创作者招聘/接单平台，供美术与程序分工组队合作。 |
| [Roblox 开发者论坛](https://devforum.roblox.com/) | 社区与交流 | — | 官方开发者社区，美术、脚本与上架问题的第一手答疑地。 |
| [罗布乐思开发者网站（中国版）](https://dev.roblox.cn) | 社区与交流 | — | 罗布乐思中国版开发者站，含中文文档与国内创作者支持入口。 |
| [Roblox 分析文档](https://create.roblox.com/docs/production/analytics) | 数据与选品 | — | 官方数据分析文档，用留存、付费与性能指标指导创作迭代。 |
| [Marketplace 市场政策](https://create.roblox.com/docs/marketplace/marketplace-policy) | 政策与合规 | — | UGC 上架合规红线与分类/内容规范，避免资产被驳回下架。 |
| [Rojo（专业工程化工作流）](https://github.com/rojo-rbx/rojo) | 开源项目 | — | 开源工具，把文件系统同步进 Studio，接入 Git 等工程化协作。 |

### 蛋仔派对

网易派对游戏，内置蛋仔工坊 / 乐园模式，主打低门槛地图与皮肤创作。

> 深度笔记：[docs/PLATFORMS/eggy-party.md](docs/PLATFORMS/eggy-party.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [《蛋仔派对》官方网站](https://party.163.com) | 平台与官方文档 | — | 网易《蛋仔派对》国服官网，游戏本体、派对季与官方资讯总入口。 |
| [《蛋仔派對》港澳台官网](https://www.eggyparty.com/hmt) | 平台与官方文档 | — | 蛋仔派对港澳台/海外版官方网站，含当地活动与创作者激励公告。 |
| [工坊乐园（UGC 地图大厅）](https://party.163.com/m/workplace_ugc?tab=0) | 平台与官方文档 | — | 官网 UGC 板块，乐园地图创作与游玩聚合页，含“跟蛋仔学编程”编辑器平台介绍。 |
| [工坊手册（PC 端编辑器文档）](https://u5-creator.s3.game.163.com/manual/pc) | 编辑器与开发工具 | — | 官方 PC 端蛋仔编辑器（Eggitor）使用手册，编辑器功能与工作流说明。 |
| [工坊手册（移动端编辑器文档）](https://u5-creator.s3.game.163.com/manual/mobile) | 编辑器与开发工具 | — | 官方移动端地图编辑器手册，含游戏示例、Lua 玩法、协作与性能优化说明。 |
| [蛋仔 PC 编辑器安装指引](https://u5-creator.s3.game.163.com/manual/pc_md/installation.html) | 编辑器与开发工具 | — | PC 端编辑器下载安装与配置指引，从 0 搭建创作环境的第一步。 |
| [ZBrush 教程：Q版蛋仔派对全流程雕刻](https://www.youtube.com/watch?v=B7G5uppQNeo) | 美术与建模 | — | ZBrush 零基础雕刻 Q 版蛋仔造型全过程，可参考官方 Q 萌 3D 角色的建模工艺。 |
| [中国日报：蛋仔派对升级自研编辑器（AI 创作）](https://tech.chinadaily.com.cn/a/202607/14/WS6a55ea5fa310d709c2fbd71d.html) | AI 提效工具 | — | 报道编辑器接入 DeepSeek/GLM/Kimi 等大模型，落地 AI 辅助建模、问答与 Lua 编程。 |
| [B站教程：工坊教程1-新建一幅地图](https://www.bilibili.com/video/BV16M411872t) | 教程与学习路径 | — | UP主“啡色小熊”出品的蛋仔工坊入门教程第 1 集，讲解新建地图流程。 |
| [B站教程：零基础超详细制作地图教程](https://www.bilibili.com/video/BV1rd4y1L7uH) | 教程与学习路径 | — | UP主“椰姊”的零基础地图制作系统教程，覆盖视角/复制/绑定/组合/锁定等操作。 |
| [YouTube 官方教程：Creator Workshop Tutorial 01](https://www.youtube.com/watch?v=XKTyWjw6Whk) | 教程与学习路径 | — | 蛋仔派对官方英文频道 Workshop 教程第 1 集，基础操作演示（海外版）。 |
| [蛋仔大学·开发者学院（教程中心）](https://ugc.163.com/study) | 教程与学习路径 | — | 官方开发者学院教程中心，海量视频教程与个性化学习路径推荐。 |
| [《蛋仔派对》创作者中心](https://party.163.com/2023/czzzx) | 创作者计划与变现 | — | 官方创作者中心入口页，创作者登录与管理平台的门户。 |
| [共创蛋时代（5 亿奖励创作者计划）](https://party.163.com/2023/czz) | 创作者计划与变现 | — | 官方创作者招募与激励活动页，宣传与创作者共创瓜分 5 亿奖励。 |
| [地图激励的获取方式（工坊手册）](https://u5-creator.s3.game.163.com/manual/mobile/ugcgoods/ugcearnings.html) | 创作者计划与变现 | — | 官方文档说明地图现金激励申请条件与获取方式（工匠点门槛等）。 |
| [B站官方号：网易蛋仔派对](https://space.bilibili.com/1306451842) | 社区与交流 | — | 网易蛋仔派对 B 站官方空间，官方教程、活动与社区内容主阵地。 |
| [B站官方号：蛋仔派对主官方](https://space.bilibili.com/3493108171934127) | 社区与交流 | — | 蛋仔派对主官方 B 站空间，发布版本预告、联动与创作相关内容。 |
| [全民乐园狂欢（乐园榜单/活动）](https://eggy.163.com/202401/lys) | 社区与交流 | — | 官方乐园创作者狂欢活动页，含社媒平台创作者排名与乐园展示。 |
| [蛋仔派对地图工具（第三方乐园图库）](https://www.onebiji.com/hykb_tools/dzpd/dtdq/index.php) | 数据与选品 | — | 第三方收集的乐园地图工具页，可浏览热门地图合集供选题参考。 |
| [蛋仔派对创作者维权中心](https://eggy.163.com/m/202401/dtwq) | 政策与合规 | — | 官方版权维权通道，公示乐园地图知识产权保护与创作者投诉处理规则。 |

### 元梦之星

腾讯天美派对游戏（UE4），内置「造梦空间」地图编辑器与「星世界」UGC 平台。

> 深度笔记：[docs/PLATFORMS/dreamstar.md](docs/PLATFORMS/dreamstar.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [《元梦之星》官方网站](https://ymzx.qq.com) | 平台与官方文档 | — | 腾讯天美官方站，聚合造梦空间编辑器、星世界地图、造梦课、创作赛与版权保护计划。 |
| [元梦之星 - TapTap](https://www.taptap.cn/app/383413) | 平台与官方文档 | — | TapTap 游戏主页，含下载、评分、玩家论坛与地图制作攻略聚合。 |
| [元梦之星 - 维基百科](https://zh.wikipedia.org/zh-hans/%E5%85%83%E6%A2%A6%E4%B9%8B%E6%98%9F) | 平台与官方文档 | — | 百科条目，记录开发商天美、UE4引擎、2023-12-15上线及内置地图编辑器与UGC玩法。 |
| [元梦之星 App - App Store](https://apps.apple.com/cn/app/id1632344522) | 平台与官方文档 | — | 苹果商店官方页，更新说明记录星世界造梦空间AI辅助工具、生成器元件等UGC能力。 |
| [元梦之星地图编辑器新功能介绍（bilibili）](https://www.bilibili.com/video/BV1mw411j7nU) | 编辑器与开发工具 | — | 视频演示造梦空间编辑器新增功能，直观展示建模、特效与玩法编辑操作。 |
| [开星造梦！《元梦之星》地图编辑器介绍（TapTap）](https://www.taptap.cn/moment/456219695461171265) | 编辑器与开发工具 | — | 官方「造梦空间」地图编辑器功能总览介绍贴，讲解可视化搭建与玩法编辑入口。 |
| [腾讯扣叮携手《元梦之星》推出可视化编程游戏创作功能（中国日报网）](https://cn.chinadaily.com.cn/a/202403/18/WS65f80148a3109f7860dd5ec6.html) | 编辑器与开发工具 | — | 报道「元梦扣叮」积木式可视化编程上线，零基础玩家可拼装事件/角色/动作设计玩法。 |
| [腾讯扣叮携手《元梦之星》推出可视化编程游戏创作功能（腾讯云开发者）](https://cloud.tencent.com/developer/news/1330522) | 编辑器与开发工具 | — | 腾讯云开发者社区同题报道，说明元梦扣叮降低创作门槛并提供200万创作赛奖金。 |
| [腾讯自研游戏AI引擎GiiNEX，UGC工具已上线《元梦之星》 - 量子位](https://www.qbitai.com/2024/03/129590.html) | AI 提效工具 | — | 介绍GiiNEX生成式AI在元梦之星落地：文生灵感图、一键建模、NPC动作迁移等提效工具。 |
| [《元梦之星》新手玩家技巧介绍 - 游民星空](https://www.gamersky.com/handbook/202312/1684765.shtml) | 教程与学习路径 | — | 新手入门与上手教学攻略，讲解核心闯关技巧与游戏基础机制。 |
| [【元梦之星】全网最全元梦地图制作教程（bilibili）](https://www.bilibili.com/video/BV1Je411v7Ev) | 教程与学习路径 | — | 长视频地图制作系统教程，覆盖从元件到玩法逻辑的完整造图链路。 |
| [元梦之星地图制作指南 - TapTap](https://www.taptap.cn/app/383413/strategy/entity-collection/226063) | 教程与学习路径 | — | TapTap官方攻略合集，手把手教元件使用、场景搭建与地图发布流程。 |
| [开星造梦！《元梦之星》地图编辑器介绍（4399）](https://a.4399.cn/gl/41658965_267393.html) | 教程与学习路径 | — | 4399攻略页转载的编辑器介绍，面向手机端玩家讲解造梦空间基础操作。 |
| [《元梦之星》UGC创作者征集 - 腾讯游戏创作者平台](https://topd.tencent.com/activity/detail/818) | 创作者计划与变现 | — | 腾讯游戏官方创作者平台上的元梦之星UGC征集活动，面向地图与内容创作者。 |
| [《元梦之星》：派对游戏UGC的未来 - 触乐](https://www.chuapp.com/mobile/289687.html) | 创作者计划与变现 | — | 深度解读造梦计划的三层创作者扶持（超级Offer/收益/平台）与职业化路径。 |
| [既是玩家也是创作者，《元梦之星》用「造梦」铸就未来 - 游戏陀螺](https://www.youxituoluo.com/531609.html) | 创作者计划与变现 | — | 解析10亿造梦计划、首赛季4330万激励、模组社区与联手创作机制。 |
| [元梦之星造梦局 官方创作UP主页（bilibili）](https://space.bilibili.com/3546586778962030) | 社区与交流 | — | 官方造梦局B站账号，发布造梦师专访、编辑器教程与创作赛事动态。 |

### 奥拉星

百田系页游/手游 IP，以亚比养成与同人创作为核心的社区生态，官方站为 http 站点。

> 深度笔记：[docs/PLATFORMS/aola-star.md](docs/PLATFORMS/aola-star.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [奥拉星 H5（免下载网页版）](https://aola.100bt.com/h5) | 平台与官方文档 | — | 《奥拉星》HTML5 版入口，浏览器即点即玩，替代原 Flash 客户端。 |
| [奥拉星 官方网站（百田/百奥游戏）](https://aola.100bt.com) | 平台与官方文档 | — | 广州百田《奥拉星》页游官方门户，含亚比大全、练级与秘籍心得栏目。 |
| [4399 奥拉星专区](https://www.4399.com/flash/35538.htm) | 社区与交流 | — | 4399 奥拉星专题，聚合小游戏、亚比大全、攻略秘籍与视频。 |
| [奥拉星 TapTap 官方页](https://www.taptap.cn/app/84327) | 社区与交流 | — | 奥拉星手游 TapTap 官方下载与社区页，含攻略、评价与版本更新记录。 |
| [奥拉星 维基百科词条](https://zh.wikipedia.org/zh-hans/%E5%A5%A5%E6%8B%89%E6%98%9F) | 社区与交流 | — | 《奥拉星》词条，记载开发商、平台、运营时间与手游/《奥拉星2》等衍生的权威背景。 |

### 迷你世界

国产沙盒创作平台，皮肤/地图创作与创作者分成是核心 UGC 面。

> 深度笔记：[docs/PLATFORMS/mini-world.md](docs/PLATFORMS/mini-world.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [迷你世界 官方网站](https://www.mini1.cn) | 平台与官方文档 | — | 《迷你世界》官网，PC/移动端下载与创作入口，国内头部沙盒 UGC 平台。 |
| [迷你世界开发者学院：地图制作流程](https://dev-wiki.mini1.cn/courses/article/955) | 教程与学习路径 | — | 官方课程，从下载 PC 版、申请开发者到场景搭建/插件/触发器/商业化全流程教学。 |
| [迷你世界商业化教程（海外站）](https://www.miniworldgame.com/zh-hant/news/46) | 创作者计划与变现 | — | 官方商业化指南：开发者权益与申请通道、开发者商店售卖、触发器广告与提现规则。 |
| [迷你世界星启计划（创作者扶持）](https://activities.mini1.cn/fe/starPlan) | 创作者计划与变现 | — | 官方开发者扶持计划官网，提供现金扶持、孵化培育与流量曝光，报名成为创作者。 |
| [迷你世界开发者服务中心](https://developers.miniworldgame.com) | 数据与选品 | — | 开发者中心/服务中心，查看近 30 天地图数据与广告、贡献点等收益结算。 |

### 我的世界

皮肤、材质包、数据包与 Mod 的创作与分发，社区工具链最成熟。

> 深度笔记：[docs/PLATFORMS/minecraft.md](docs/PLATFORMS/minecraft.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [Modrinth](https://modrinth.com) | 平台与官方文档 | — | 开源友好的 Minecraft Mod/资源包/数据包/整合包托管与分发平台，创作者发布主渠道之一。 |
| [Blockbench](https://www.blockbench.net) | 编辑器与开发工具 | — | 免费开源的体素/低多边形 3D 建模工具，Minecraft 模型、皮肤与动画创作标准工具。 |
| [Bedrock Wiki（技术文档）](https://wiki.bedrock.dev) | 教程与学习路径 | — | 基岩版技术文档，覆盖 Add-on、行为包、自定义方块/实体与脚本 API，社区维护教程库。 |
| [Minecraft Add-On 创作者教程（官方）](https://www.minecraft.net/zh-hans/creator) | 教程与学习路径 | — | 官方创作者中心，教做皮肤包、世界、材质、方块与实体，含 Item/Block Wizard 等高效工具指南。 |
| [NeoForged 官方文档：Resources](https://docs.neoforged.net/docs/resources) | 教程与学习路径 | — | 讲解 assets/data 资源目录结构与资源包、数据包加载机制，是写作资产规范的官方依据。 |
| [我的世界开发者官网（中国版创造者计划）](https://mc.163.com/dev) | 创作者计划与变现 | — | 网易《我的世界》中国版开发者平台，提供开发工作台、模组 SDK 与作品上传/社区交流。 |
| [Minecraft Wiki](https://minecraft.wiki) | 社区与交流 | — | 官方社区维基，含 Creator 板块（Marketplace、Add-ons、资源包、数据包、Mods 与协议文档）。 |
| [Minecraft 粉丝与创作者使用准则](https://www.minecraft.net/en-us/usage-guidelines) | 政策与合规 | — | 官方 Usage Guidelines，规定品牌、素材与二创内容的合规边界，UGC 仓库必备政策参考。 |
| [NeoForge（GitHub）](https://github.com/NeoForged/NeoForge) | 开源项目 | — | 开源 Java 版 Modding API（Forge 分支），开发者可据此构建与分发自定义内容。 |

### 发布与分发渠道

B站 / 抖音 / 小红书 / TikTok 的社区规则与 AIGC 标识要求——作品做得出来，还得发得出去。

> 深度笔记：[docs/PLATFORMS/channels.md](docs/PLATFORMS/channels.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [bilibili 社区公约](https://member.bilibili.com/studio/convention?navhide=1) | 政策与合规 | — | B站社区公约与投稿规范，含自制/转载判定、创作声明与 AI 内容标识要求。 |
| [TikTok Community Guidelines](https://www.tiktok.com/community-guidelines) | 政策与合规 | — | TikTok 社区规则，覆盖内容安全、未成年人保护、AI 生成内容与商业内容披露要求。 |
| [小红书用户协议（含 AI 标识条款）](https://agree.xiaohongshu.com/h5/terms/ZXXY20220331001/-1) | 政策与合规 | — | 小红书用户协议，明确 AI 生成内容显式/隐式标识义务、内容授权范围与违规处置。 |
| [抖音社区自律公约](https://www.douyin.com/rule/policy) | 政策与合规 | — | 抖音内容发布与平台治理规则（含未成年规范、违规分类与处置），创作者内容合规必读。 |

### AI 工具链（跨平台）

按工序落位的开源与商用 AI 工具：概念图 → 出图 → 建模 → 贴图 → 放大 → 抠图 → 视频 → 配音 → 批量 → 发布。

> 深度笔记：[docs/AI-WORKFLOW.md](docs/AI-WORKFLOW.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [chaiNNer](https://github.com/chaiNNer-org/chaiNNer) | 美术与建模 | 放大与修复 | 节点式图像处理 GUI，把放大/修复/后处理串成批处理链。 |
| [Dream Textures](https://github.com/carson-katri/dream-textures) | 美术与建模 | 贴图与材质 | Blender 内嵌 SD，直接在 3D 模型上生成/绘制贴图。 |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | 美术与建模 | 出图与修图 | 免调参的 SDXL 出图前端，只写提示词即可批量出图。 |
| [Krita AI Diffusion](https://github.com/Acly/krita-ai-diffusion) | 美术与建模 | 概念与设定图 | 在 Krita 画布内直接 AI 生成/修复/扩图，画师边画边出概念图。 |
| [Upscayl](https://github.com/upscayl/upscayl) | 美术与建模 | 放大与修复 | 跨平台开源 AI 放大 GUI，批量把小图放大到印刷/4K。 |
| [Bannerbear](https://www.bannerbear.com) | AI 提效工具 | 批量排版与批处理 | 模板化 API 批量生成图片/视频，把出图批量套版成社媒素材。 |
| [Meshy（AI 3D 生成）](https://www.meshy.ai) | AI 提效工具 | — | 文/图生 3D 模型服务，UGC 创作者用 AI 快速产出道具、角色与体素模型提效。 |
| [BLIP](https://github.com/salesforce/BLIP) | 素材与资源库 | 数据与训练 | 图像自动打标/描述，为训练集批量生成 caption。 |
| [BRIA RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4) | 素材与资源库 | 抠图与去背 | 商用级背景移除权重，商品/Banner 素材批量透明化。 |
| [Florence-2](https://huggingface.co/microsoft/Florence-2-large) | 素材与资源库 | 数据与训练 | 微软通用视觉模型，批量 caption/检测/分割以清洗数据集。 |
| [kohya sd-scripts](https://github.com/kohya-ss/sd-scripts) | 素材与资源库 | 数据与训练 | 训练 LoRA/微调 SD，用自有素材训练专属出图风格。 |
| [AnimateDiff](https://github.com/guoyww/AnimateDiff) | 开源项目 | 视频与动效 | 给 SD 加运动模块，把静图/角色图转成短视频。 |
| [BiRefNet](https://github.com/ZhengPeng7/BiRefNet) | 开源项目 | 抠图与去背 | 双边参考高分辨率二值分割，抠毛发/细边更干净。 |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 开源项目 | 出图与修图 | 节点式扩散工作流引擎，把出图/放大/抠图/视频串成可复用流水线。 |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | 开源项目 | 配音与音频 | 多语种大语音生成模型，TTS+音色克隆+生成一体。 |
| [Fish Speech](https://github.com/fishaudio/fish-speech) | 开源项目 | 配音与音频 | SOTA 开源 TTS，多语言零样本克隆做旁白。 |
| [FLUX.1](https://github.com/black-forest-labs/flux) | 开源项目 | 出图与修图 | FLUX.1 官方推理代码，高文本服从度文生图，用于封面/主图出图。 |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 开源项目 | 配音与音频 | 1 分钟样本克隆音色，给口播/短视频配音。 |
| [Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | 开源项目 | 建模与 3D | 腾讯混元 3D，单图/文生高分辨率带贴图 3D 资产。 |
| [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 开源项目 | 视频与动效 | 腾讯混元视频大模型，开源文生视频用于短片素材。 |
| [ImageMagick](https://github.com/ImageMagick/ImageMagick) | 开源项目 | 批量排版与批处理 | 命令行批量缩放/加水印/切图/合成，批量排版脚本底座。 |
| [Mixpost](https://github.com/inovector/mixpost) | 开源项目 | 发布与自动化 | 自托管社媒内容排期与发布（Buffer 替代）。 |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | 开源项目 | 视频与动效 | 开源复现 Sora 的视频生成流水线，可控文生/图生视频。 |
| [Postiz](https://github.com/gitroomhq/postiz-app) | 开源项目 | 发布与自动化 | 自托管社媒排期/多平台发布工具（含 Agent）。 |
| [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 开源项目 | 放大与修复 | 实用级通用图像/视频超分，抠图后放大保细节。 |
| [rembg](https://github.com/danielgatis/rembg) | 开源项目 | 抠图与去背 | 一条命令去背景（图片），批量抠图出透明 PNG 素材。 |
| [SAM 2](https://github.com/facebookresearch/sam2) | 开源项目 | 抠图与去背 | Meta 可提示分割模型，图片/视频一键框选生成抠图蒙版。 |
| [social-auto-upload](https://github.com/dreammis/social-auto-upload) | 开源项目 | 发布与自动化 | 自动上传视频到抖音/小红书/视频号/B站/TikTok/YouTube。 |
| [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 开源项目 | 概念与设定图 | 本地跑 SD 文生图/图生图/局部重绘，最通用的概念图起稿台。 |
| [Text2Tex](https://github.com/daveredrum/Text2Tex) | 开源项目 | 贴图与材质 | 文本驱动扩散为 3D 网格多视角合成贴图（ICCV 2023）。 |
| [TRELLIS](https://github.com/microsoft/TRELLIS) | 开源项目 | 建模与 3D | 微软结构化 3D 潜变量模型，文/图生可编辑 3D 资产。 |
| [TripoSR](https://github.com/VAST-AI-Research/TripoSR) | 开源项目 | 建模与 3D | 单张图秒级重建 3D 网格，快速把概念图转成可雕刻模型。 |
| [Wan2.1](https://github.com/Wan-Video/Wan2.1) | 开源项目 | 视频与动效 | 阿里万相开源视频生成，文/图生多秒高清视频。 |
| [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | 开源项目 | 发布与自动化 | 小红书 MCP 服务，Agent 直接发布/检索笔记。 |

### 生态横切面

素材库与授权、数据与选品、创作者社区、平台政策与合规。

> 深度笔记：[docs/ECOSYSTEM.md](docs/ECOSYSTEM.md)

| 名称 | 类别 | 工序 | 说明 |
| --- | --- | --- | --- |
| [mod.io（跨平台 Mod 分发）](https://mod.io) | 平台与官方文档 | — | 跨平台 UGC/Mod 托管与分发服务，为多款游戏提供 Mod 浏览、订阅与创作者后台。 |
| [Poly Pizza](https://poly.pizza) | 美术与建模 | — | 免费低多边形 3D 模型库（CC/免版权素材），沙盒与 UGC 创作者快速取用美术资产。 |
| [CC0 1.0 公共领域贡献协议](https://creativecommons.org/publicdomain/zero/1.0) | 素材与资源库 | — | CC0 官方法律文本：作者放弃全部权利，素材可无署名、无限制商用，是最宽松的素材授权依据。 |
| [Creative Commons 许可协议总览](https://creativecommons.org/licenses) | 素材与资源库 | — | CC 全部许可协议（CC0/CC-BY/CC-BY-SA 等）官方总览，含各协议署名、商用、演绎等权利与义务说明。 |
| [Freesound](https://freesound.org) | 素材与资源库 | — | 音效与采样素材库，条目多为 CC0 或 CC-BY 授权，可按协议筛选后用于商业项目。 |
| [Kenney（游戏素材库）](https://kenney.nl) | 素材与资源库 | — | 高知名度 CC0 游戏素材站，提供 2D/3D/UI/音效成套资产包，UGC 作品可直接商用。 |
| [OpenGameArt.org](https://opengameart.org) | 素材与资源库 | — | 社区开源游戏美术/音效资源库，按 CC 等许可分类，可筛选可商用素材。 |
| [Pexels License](https://www.pexels.com/license) | 素材与资源库 | — | Pexels 授权说明：照片与视频免费商用、可修改、无需署名，禁止转售及侵犯人物肖像/商标的用途。 |
| [unDraw](https://undraw.co/illustrations) | 素材与资源库 | — | 可商用开源插画库，支持主题换色与 SVG 下载，授权宽松、无需署名。 |
| [Unsplash License](https://unsplash.com/license) | 素材与资源库 | — | Unsplash 授权页：图片免费商用、可修改、无需强制署名，禁止原样转售或搭建竞品图库。 |
| [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) | 素材与资源库 | — | 自由版权媒体库，图片/音频/视频多采用 CC0、CC-BY、CC-BY-SA 或公有领域授权，商用需按各自协议署名。 |
| [mod.io 文档：UGC Best Practices](https://docs.mod.io/unity/ugc-best-practices) | 教程与学习路径 | — | UGC 系统设计最佳实践：资源路径隔离、着色器复用与创作工具选型，平台方接入指南。 |
| [Creative Bloq](https://www.creativebloq.com) | 社区与交流 | — | 英文创意设计媒体，聚合插画/设计教程、软件技巧与行业资讯。 |
| [DeviantArt](https://www.deviantart.com) | 社区与交流 | — | 全球大型插画/同人作品社区，含作品授权标注、委托创作与 DeviantArt Protect 版权保护。 |
| [pixiv](https://www.pixiv.net) | 社区与交流 | — | 日本插画/漫画投稿社区，含排行榜、约稿（Commission）与 AI 作品标注与投稿规范。 |
| [优设 UISDC](https://www.uisdc.com) | 社区与交流 | — | 国内设计师社区与教程聚合站，涵盖 UI、品牌、AIGC 教程与设计素材导航。 |
| [数英 DIGITALING](https://www.digitaling.com) | 社区与交流 | — | 广告与营销创意案例/作品库，可按行业、奖项与品牌检索创意参考。 |
| [站酷 ZCOOL](https://www.zcool.com.cn) | 社区与交流 | — | 中文设计师互动平台，涵盖作品展示、教程文章、招聘接单与 AIGC 专题内容。 |
| [Google Trends](https://trends.google.com/trends) | 数据与选品 | — | 全球搜索热度趋势工具，可按地区与时间对比关键词、话题的流行度。 |
| [QuestMobile](https://www.questmobile.com.cn) | 数据与选品 | — | 移动互联网商业智能平台，发布行业研究报告与 App/用户行为数据洞察。 |
| [千瓜数据](https://www.qian-gua.com) | 数据与选品 | — | 小红书种草营销数据服务，提供笔记、达人、品牌与选品分析。 |
| [新榜](https://www.newrank.cn) | 数据与选品 | — | 新媒体内容与账号数据榜（公众号/抖音/小红书等），用于选题、账号对标与内容趋势分析。 |
| [蝉妈妈](https://www.chanmama.com) | 数据与选品 | — | 短视频与直播电商数据分析平台，含达人榜、选品库与带货销量洞察。 |
| [飞瓜数据](https://www.feigua.cn) | 数据与选品 | — | 抖音/快手等短视频与电商数据分析，覆盖销量、营销声量与达人榜单。 |
| [互联网信息服务深度合成管理规定](https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm) | 政策与合规 | — | 深度合成/AIGC 部门规章（2023-01-10 施行），确立内容标识、真实身份认证与安全评估要求。 |
| [人工智能生成合成内容标识办法](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm) | 政策与合规 | — | AIGC 标识办法（2025-09-01 施行），强制显式+隐式标识，配套 GB 45438-2025 标准与备案要求。 |
| [国家互联网信息办公室（CAC）](https://www.cac.gov.cn) | 政策与合规 | — | 网信办官网，发布生成式 AI、深度合成、算法推荐、内容生态治理等法规与算法/内容备案入口。 |
| [国家版权局](https://www.ncac.gov.cn) | 政策与合规 | — | 国家版权局官网，著作权法规、版权登记与侵权执法信息的权威来源。 |
| [未成年人网络保护条例](https://www.gov.cn/zhengce/content/202310/content_6911288.htm) | 政策与合规 | — | 国务院令第766号（2024-01-01 施行），未成年人网络保护、防沉迷与个人信息保护的专项行政法规。 |
| [生成式人工智能服务管理暂行办法](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm) | 政策与合规 | — | 生成式 AI 服务专项规章（2023-08-15 施行），规定训练数据合法来源、标注规则、内容安全与备案义务。 |
| [网络信息内容生态治理规定](https://www.cac.gov.cn/2019-12/20/c_1578375159509309.htm) | 政策与合规 | — | 内容审核与平台治理基础规章（2020-03-01 施行），明确平台信息内容管理主体责任与处置流程。 |
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
- 条目总数：**145**（收录时实测 HTTP 200：142）
- 按平台：AI 工具链（跨平台） 34 · 生态横切面 31 · 蛋仔派对 20 · Roblox / 罗布乐思 20 · 元梦之星 17 · 我的世界 9 · 奥拉星 5 · 迷你世界 5 · 发布与分发渠道 4
- 按类别：开源项目 25 · 素材与资源库 16 · 社区与交流 16 · 教程与学习路径 15 · 平台与官方文档 14 · 政策与合规 14 · 创作者计划与变现 11 · 美术与建模 10 · 数据与选品 9 · 编辑器与开发工具 9 · AI 提效工具 6
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

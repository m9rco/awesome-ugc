# Roblox / 罗布乐思

**定位**：全球 UGC 生态的标杆——编辑器（Studio）、资产市场（Marketplace / Creator Store）、开发者变现（DevEx）、人才协作（Talent Hub）四件套完整闭环。中国版由「罗布乐思开发者网站」承接本地化内容。

## 交付物有两条完全不同的线

| 线 | 交付物 | 上架/发布路径 |
| --- | --- | --- |
| **体验（游戏）** | 一个可玩的 UGC 体验 | Studio 里发布，走 Creator Hub 后台与[分析文档](https://create.roblox.com/docs/production/analytics)看留存 |
| **资产** | 配饰、服装、模型等 Marketplace 商品 | [发布到 Marketplace](https://create.roblox.com/docs/marketplace/publish-to-marketplace)，受[市场政策](https://create.roblox.com/docs/marketplace/marketplace-policy)约束 |

**资产线是本仓库最关心的那条**：它的美术管线就是"外包级"的 3D 规格，做图能力直接决定能不能上架。

## 硬约束（抄自官方规格页，做图前先读）

来源：[3D 资产通用规格](https://create.roblox.com/docs/art/modeling/specifications)

- 单个网格 **≤ 20,000 三角面**；必须是**水密**网格；
- **禁止 N-gon**（优先四边面）；**禁止零厚度**几何；
- 骨骼要**冻结变换**：scale = (1,1,1)、rotation = (0,0,0)；
- **单顶点最多 4 个骨骼影响**，且不要有 root 影响；
- 单次导出的动画文件**只允许一条动画轨**；
- 角色配饰/分层服装走**内外 cage**体系：主网格名 + `_InnerCage` / `_OuterCage`，**不要删改 cage 的顶点与 UV**；
- 平台支持基础色贴图与 **PBR 贴图**，贴图侧另有独立规范页——别把建模规格当贴图规格用。

导出细节见[导出要求](https://create.roblox.com/docs/art/modeling/export-requirements)与[建模总览](https://create.roblox.com/docs/art/modeling)。

## 推荐工作流（专业作者的实际姿势）

1. **外部 DCC 建模**：Blender / Maya 里完成造型（不在 Studio 里硬雕）；
2. **规格自检**：水密、四边面、非零厚度、面数、变换冻结——一次对齐，省下后期全部返工；
3. **UV 与 PBR 烘焙**：先展开 UV 再画贴图/烘焙，避免拉伸；
4. **导出**：按导出要求设置；
5. **Studio 内校验**：光照、材质、动画逐一确认；
6. **工程化（可选但强烈推荐）**：[Rojo](https://github.com/rojo-rbx/rojo) 把 Studio 项目映射到文件系统，从而能用 Git 做版本管理与多人协作——这是把"美术项目"变成"可协作工程"的关键一步；
7. **上架**：Marketplace / Creator Store，按政策核对内容与定价。

## AI 能力（官方内置优先级最高）

来源：[AI on Roblox 加速工作流](https://create.roblox.com/docs/ai/accelerated-workflows)

- **生成**：网格生成、材质生成、贴图生成、程序化模型；
- **助手**：Code Assist、Assistant（可选不同厂商模型）；
- **自动化**：**Studio MCP 服务器**——允许外部 AI 客户端读写数据模型、创建/修改脚本与实例、跑 playtest；
- **角色**：Avatar Auto-Setup；
- **语音**：官方文本转语音 / 语音转文本 API；
- **硬规则**：LLM 驱动的 NPC 对话**必须经 `TextService:FilterStringAsync()` 过滤**才能展示；
- **开源**：官方 3D 生成基础模型 [Cube](https://github.com/Roblox/cube)（可自建，不必依赖云端）。

## 变现与协作

- [DevEx（开发者兑换计划）](https://create.roblox.com/docs/production/monetization/developer-exchange)：把 Robux 收益兑换为现金，有门槛与规则；
- [Talent Hub](https://create.roblox.com/talent)：找美术/程序/策划组队的官方入口；
- [Creator Store 文档](https://create.roblox.com/docs/production/creator-store) 与 [在线商店](https://create.roblox.com/store)：资产流通的主场。

## 生态入口

- [Creator Hub](https://create.roblox.com) · [官方文档](https://create.roblox.com/docs) · [官方教程](https://create.roblox.com/docs/tutorials) · [教育计划](https://education.roblox.com)
- [开发者论坛 DevForum](https://devforum.roblox.com) · [中国版：罗布乐思开发者](https://dev.roblox.cn)
- [3D 艺术文档](https://create.roblox.com/docs/art) · [Studio 文档](https://create.roblox.com/docs/studio)

## 风险与合规

- 资产上架前**必读市场政策**（内容分级、IP 侵权、AI 生成内容的声明要求）；
- LLM/NPC 输出过滤是**强制**项，不是建议项；
- 外部 DCC 里使用的模型/贴图素材，授权要能追溯到商用许可（见[素材与授权](../ECOSYSTEM.md)）。

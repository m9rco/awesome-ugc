# 蛋仔派对

**定位**：网易派对游戏，UGC 侧的核心是**蛋仔工坊**（地图编辑器）+ **乐园**（UGC 地图大厅）+ **共创蛋时代**创作者激励。编辑器文档分移动端与 PC 端两套，PC 端（`Eggitor`）是生产力主场。

## 编辑器能力面（决定"做图"到底做什么）

来源：[工坊手册 · PC 端](https://u5-creator.s3.game.163.com/manual/pc)｜[移动端](https://u5-creator.s3.game.163.com/manual/mobile)

| 模块 | 内容 | 对美术的意义 |
| --- | --- | --- |
| 组件编辑 | **组件皮肤编辑**、特效编辑器（含光束/粒子法阵实例） | 换皮与特效是出量的主要手段，不必从零建模 |
| 生物与行为 | 生物组件（**蛋仔类骨骼说明**）、行为树自定义 AI 行为 | 角色要按平台骨骼规范来，否则动作失真 |
| 规则逻辑 | **蛋码**（积木/触发器）+ **Lua**（含 `EditorCli`、调试工具、周更 API 手册） | 会写代码在这里是加分项，能做出别人做不出的玩法 |
| 资源 | **资源包上传**、**自定义模型上传** | 外部美术资产的正式入口 |
| 界面 | 界面编辑 | HUD / 结算页的自定义 |
| 商业化 | 激励方式、商品、广告、盲盒、会员权益 | 先读激励规则再定设计目标 |

## 关键：先查资产目录，再决定自制

平台侧直接提供**蛋仔时装套装 / 配饰 / 外观散件**的资产目录。**"先用官方资产拼装、只自制差异化部分"是这条线最省工时的策略**——自制全量资产在派对游戏的产能模型里通常不划算。

## 参考工艺：Q 版角色的标准做法

蛋仔风格的 Q 版角色，社区里最通用的工艺是**"ZBrush 高模雕刻 → 拓扑低模 → 烘焙法线/材质 → 贴图着色"**，有完整流程课可参考（[ZBrush 全流程雕刻教程](https://www.youtube.com/watch?v=B7G5uppQNeo)）。要点：

1. **比例先行**：Q 版头身比定死后，所有配件按同一比例尺做，避免"每个部件都好看、拼起来不搭"；
2. **硬边圆润化**：Q 版靠大色块 + 圆角轮廓，细节靠贴图而不是几何；
3. **材质统一**：同一套皮肤内材质参数保持一致，否则在乐园光照下会花。

## 创作与发布流程

1. 读[工坊手册](https://u5-creator.s3.game.163.com/manual/pc)，按 PC 端[安装指引](https://u5-creator.s3.game.163.com/manual/pc_md/installation.html)装好编辑器；
2. 新建地图 → 组件拼装 → 特效/皮肤 → 行为树与蛋码逻辑；
3. 自制资产走**资源包上传 / 自定义模型上传**；
4. 上架到[工坊乐园](https://party.163.com/m/workplace_ugc?tab=0)（UGC 地图大厅），参与[全民乐园狂欢](https://eggy.163.com/202401/lys)等活动获得曝光；
5. 收益按[地图激励获取方式](https://u5-creator.s3.game.163.com/manual/mobile/ugcgoods/ugcearnings.html)结算。

**学习路径**：[蛋仔大学·开发者学院](https://ugc.163.com/study) 是官方教程中心；B 站上也有大量从零建图教程（[新建一幅地图](https://www.bilibili.com/video/BV16M411872t)、[零基础超详细制作地图](https://www.bilibili.com/video/BV1rd4y1L7uH)），YouTube 有官方 Creator Workshop 系列（[Tutorial 01](https://www.youtube.com/watch?v=XKTyWjw6Whk)）。

## 创作者计划与变现

- [创作者中心](https://party.163.com/2023/czzzx)：官方任务、素材与激励入口；
- [共创蛋时代](https://party.163.com/2023/czz)：创作者激励计划（官方口径的奖励规模在活动页）；
- [创作者维权中心](https://eggy.163.com/m/202401/dtwq)：被抄袭/侵权时的官方通道——**这条线维权成本存在，作品发布前注意留痕**。

## AI 与工具

- 官方在编辑器侧持续加 AI 创作能力（[中国日报报道：升级自研编辑器](https://tech.chinadaily.com.cn/a/202607/14/WS6a55ea5fa310d709c2fbd71d.html)），**优先用编辑器内置能力**，合规成本由平台承担；
- 第三方地图数据工具可做选品参考（[乐园图库工具](https://www.onebiji.com/hykb_tools/dzpd/dtdq/index.php)），用于看什么题材在跑量。

## 生态入口

- [官方网站](https://party.163.com)｜[港澳台官网](https://www.eggyparty.com/hmt)
- B 站官方号：[蛋仔派对](https://space.bilibili.com/1306451842)｜[主官方](https://space.bilibili.com/3493108171934127)

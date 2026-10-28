# 我的世界（Minecraft）

**定位**：UGC 生态最成熟的平台——皮肤、材质包、数据包、模组（Mod）、附加包（Add-On）各有独立的创作与分发链路，且**衣钵从 2009 年传到现在**，社区规范与工具链都高度沉淀。

## 出图工艺：低模 + 像素贴图

来源：[Blockbench Minecraft 风格指南](https://www.blockbench.net/wiki/guides/minecraft-style-guide/)

- **形状靠模型、细节靠贴图**：元素数量要尽量少，但也不能简化到认不出；
- **不要用台阶堆斜面**：斜面应该用**旋转元素**实现，且旋转要"有理由"（相邻元素连成曲线不符合 MC 审美）；
- **球/柱体 = 单个元素**：游戏内本身就这么做（木桶、蛋糕、原木、砂轮、南瓜、西瓜、可可果……）；
- **平面 + 透明度优于碎元素**：小零件可以用一个大元素 + 局部完全透明的像素来表现，比堆一堆小元素更"MC"；
- **UV 是 box UV，且纹理像素与模型像素 1:1**：绝不允许贴图被压扁或拉伸。

### 实体贴图（Entity Textures）的四步做法

1. 生成贴图模板（Blockbench 会自动映射元素）；
2. 铺色块分布 → 加暗部与高光；
3. 扩充色阶到调色板；
4. **靠调整同色阶簇的相对位置来定义材质**，消掉 banding 等阴影瑕疵。

另外一条硬性风格规则：**顶部与正面必须比底部与背面亮**（单面内部与面与面之间的明暗关系都要遵守）。

## 皮肤：固定网格的两层贴图

来源：[中文 Minecraft Wiki · 皮肤](https://minecraft.wiki)

- 皮肤按区域对应实体表面（头/前部、左脚……），**不是自由画布**；
- **宽型皮肤共 3264 个可自定义像素（每层 1632）；纤细型 3136（每层 1568）**；
- **外套层（第二层）**用于眼镜、帽子等配件——身体/手臂/腿的第二层像素比第一层大 0.25 像素，头部第二层大 0.5 像素；
- 手臂宽度区分宽型（4 像素）与纤细型（3 像素），做皮肤时先确认目标体型。

工具：[Blockbench](https://www.blockbench.net) 同时覆盖模型与皮肤。

## 分发与开发

- **模组/资源包分发**：[Modrinth](https://modrinth.com) 等社区平台；跨平台 Mod 分发也可参考 [mod.io](https://mod.io)；
- **模组开发**：[NeoForge](https://github.com/NeoForged/NeoForge) + [官方资源文档](https://docs.neoforged.net/docs/resources)；
- **基岩版技术文档**：[Bedrock Wiki](https://wiki.bedrock.dev)；
- **附加包教程**：[官方 Add-On 创作者页](https://www.minecraft.net/zh-hans/creator)；
- **中国版创作者**：[我的世界开发者官网](https://mc.163.com/dev)（创造者计划与开发者工具）。

## 合规（这条线最该先读）

[Minecraft 粉丝与创作者使用准则](https://www.minecraft.net/en-us/usage-guidelines) 明确了：个人/非商用创作、视频与直播、Mod 与服务器的允许范围，以及**商业化需要走哪些通道**。把"能不能卖"这个问题的答案交给官方文档，而不是社区传言。

## 生态入口

- [Minecraft Wiki](https://minecraft.wiki)（社区权威资料，浏览器访问；命令行直连会被反爬拦截）
- [官方创造者页](https://www.minecraft.net/zh-hans/creator)｜[中国版开发者](https://mc.163.com/dev)｜[Blockbench](https://www.blockbench.net)｜[Modrinth](https://modrinth.com)

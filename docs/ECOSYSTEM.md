# 生态横切面：素材、数据、社区、合规

平台之外，还有四类东西决定你能不能持续产出：**素材能不能商用、选题从哪来、同行的水平线在哪、红线在哪。** 本页把目录里 `agnostic` 类别的条目按这四面整理成可执行的做法。

## 1. 素材与授权：只信授权页原文

**硬规矩：看到"免费下载"不等于可以商用。** 每个站点的授权类型必须点进授权页确认，并注意区分"素材本身"与"素材里的第三方内容"（音乐、字体、角色形象常有独立条款）。

| 站点 | 收录形态 | 先确认什么 |
| --- | --- | --- |
| [Kenney](https://kenney.nl) | 游戏美术素材（2D/3D/UI/音效） | 授权页的 CC0 声明与署名要求 |
| [OpenGameArt.org](https://opengameart.org) | 社区游戏素材 | **逐条看**，同站不同素材授权不同（CC0/CC-BY/GPL…） |
| [Poly Pizza](https://poly.pizza) | 低模 3D 资源 | 单模型授权与署名 |
| [unDraw](https://undraw.co/illustrations) | 矢量插画 | 是否要求署名、是否限制再分发 |
| [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) | 通用媒体库 | 每个文件独立的授权与来源声明 |
| [Freesound](https://freesound.org) | 音效库 | CC0 与 CC-BY 混合，商用前逐条核对 |
| [Unsplash License](https://unsplash.com/license) / [Pexels License](https://www.pexels.com/license) | 摄影图 | 允许范围与"不得转售原图"类限制 |
| [Creative Commons 许可总览](https://creativecommons.org/licenses) / [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0) | 协议原文 | 条款差异（BY / NC / ND / SA 的组合含义） |

**工程化建议**：把用到的每个素材记录成一行台账（来源 URL、授权类型、获取日期、用在哪），发布前扫一遍。这一步在"被投诉下架"时能救命。

## 2. 数据与选品：先看需求，再投入产能

| 用途 | 工具 |
| --- | --- |
| 大盘趋势 / 关键词热度 | [Google Trends](https://trends.google.com/trends) |
| 移动互联网大盘与人群 | [QuestMobile](https://www.questmobile.com.cn) |
| 内容与账号表现（微信/全网） | [新榜](https://www.newrank.cn) |
| 抖音带货/内容数据 | [蝉妈妈](https://www.chanmama.com)、[飞瓜数据](https://www.feigua.cn) |
| 小红书内容与达人数据 | [千瓜数据](https://www.qian-gua.com) |
| 平台内部数据 | [Roblox 分析文档](https://create.roblox.com/docs/production/analytics)、[迷你世界开发者服务中心](https://developers.miniworldgame.com) |

**用法**：不要只看"什么火"，要看**"火的内容用什么形态承载"**（题材、时长、封面风格、系列化程度），再决定自己的产能投在哪。

## 3. 社区：水平线与反馈来源

- **国际化视觉社区**：[pixiv](https://www.pixiv.net)（日系插画，注意其作品授权文化：默认保留全部权利）、[DeviantArt](https://www.deviantart.com)（浏览器访问；命令行直连会被反爬 403）；
- **国内设计社区**：[站酷 ZCOOL](https://www.zcool.com.cn)、[优设 UISDC](https://www.uisdc.com)、[数英 DIGITALING](https://www.digitaling.com)；
- **行业观察**：[Creative Bloq](https://www.creativebloq.com)。

**用法**：把它们当"同行基准线"，定期看头部作品的完成度与发布节奏，用来校准自己的产出标准，而不是当素材库刷。

## 4. 政策与合规：一份可以直接查的清单

### 法规层（中国境内）

| 法规 | 与本仓库的关系 |
| --- | --- |
| [人工智能生成合成内容标识办法](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm) | **AI 生成内容必须标识**——直接决定你的发布流程里有没有"标识"这一步 |
| [生成式人工智能服务管理暂行办法](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm) | 使用生成式 AI 服务的合规边界 |
| [互联网信息服务深度合成管理规定](https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm) | 换脸/合成类内容的管理要求 |
| [网络信息内容生态治理规定](https://www.cac.gov.cn/2019-12/20/c_1578375159509309.htm) | 内容生态的红线框架 |
| [未成年人网络保护条例](https://www.gov.cn/zhengce/content/202310/content_6911288.htm) | 涉未成年人内容的专门要求（账号、时长、内容） |
| [国家版权局](https://www.ncac.gov.cn) | 版权登记与侵权投诉的官方口 |
| [国家互联网信息办公室（CAC）](https://www.cac.gov.cn) | 上述法规的发布主体，改版时以本站为准 |

### 平台层

四个主要发布渠道的规则文档见[发布与分发渠道](PLATFORMS/channels.md)；各游戏平台的资产上架政策见对应平台笔记（例如 Roblox 的[市场政策](https://create.roblox.com/docs/marketplace/marketplace-policy)）。

### 合规动作对照表

| 你的动作 | 必须做什么 |
| --- | --- |
| 用 AI 生成图片/视频/音频并公开发布 | 按《标识办法》与平台规则**显著标识** |
| 使用 CC-BY 素材 | **署名**，保留来源链接 |
| 使用带角色的同人素材商用 | 先确认官方条款，**别默认允许** |
| 面向未成年人发布 | 核对未成年人保护相关条款 |
| 搬运 / 二创 | 按平台规则标注来源与授权状态 |
| 自动化批量发布 | 自动化**只加速合规动作**，不得绕过平台标识与审核 |

## 5. 一句话总结

**素材可商用性、选题依据、合规标识**这三件事，都属于"做之前花 10 分钟、不做则可能全盘损失"的工作。把它们变成清单与台账，是这套体系里性价比最高的自动化对象。

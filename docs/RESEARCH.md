# 调研方法与核验证据

这份文档回答一个问题：**`data/catalog.json` 里的每一条，凭什么在这里？**

## 0. 原则

1. **官方优先**：平台官方站点 / 官方文档 / 官方创作者计划 > 社区教程 > 第三方聚合；
2. **实测为准**：每条链接在收录时**用 HTTP GET 实测**，记录状态码与页面标题；不采信"我印象里有这个站"；
3. **宁缺毋滥**：4xx/5xx 或页面主题与条目描述不符的，直接剔除，不做"大概能打开"的侥幸收录。
4. **收录即不背书**：被收录只表示"该资源真实存在且主题相关"，**不代表推荐其服务条款、内容质量或商业信誉**。商用前请自行核对授权与规则。

## 1. 执行记录（2026-10-28）

调研按 **6 条并行轨道**展开，每条轨道独立产出候选条目：

| 轨道 | 覆盖范围 | 产出条目 |
| --- | --- | --- |
| T1 | Roblox / 罗布乐思（Studio、资产规格、AI、DevEx、社区） | 20 |
| T2 | 蛋仔派对（工坊/编辑器手册、资产、激励、教程） | 20 |
| T3 | 元梦之星（编辑器、创作者计划、AI/自研引擎、社区） | 19 |
| T4 | 奥拉星 + 迷你世界 + 我的世界 + 跨平台 Mod 分发 | 25 |
| T5 | AI 工具链（概念图→出图→3D→贴图→放大→抠图→视频→配音→批量→发布） | 34 |
| T6 | 生态横切面（素材授权、数据选品、社区、政策合规） | 30 |

**原始 148 条 → 去重后 147 条**（1 条 Meshy 重复，跨轨道合并）。

## 2. 复核（父进程独立重跑，不采信子进程自述）

所有 147 条在合并**之后**又独立重跑了一遍 HTTP GET（直连优先，失败再走代理），并解析返回页面 `<title>` 与条目声明核对：

| 结果 | 条数 | 说明 |
| --- | --- | --- |
| HTTP 200 | 144 | 标题与条目描述一致（Roblox 等站点会按 `Accept-Language` 返回中/英文标题，属正常差异） |
| 反爬拦截 | 3 | [minecraft.wiki](https://minecraft.wiki)（403）、[Unsplash License](https://unsplash.com/license)（401）、[DeviantArt](https://www.deviantart.com/)（403）——**已用真实浏览器复核，站点存活、标题正确**，属 bot 拦截而非死链 |

即：**147/147 站点存活**，其中 3 条对命令行客户端不可复核。

### 2.1 final pass：3 条边缘案例的处置

体检器（`scripts/check_links.py`，直连优先 + 代理回退）在 final pass 抓到 3 条需要人工判断的链接，逐条处置如下：

| 条目 | 现象 | 处置 |
| --- | --- | --- |
| Roblox 开发者论坛 | 直连 `404`、经代理 `200`（Discourse 边缘节点差异） | **保留**，URL 换为规范形式 `https://devforum.roblox.com/`，`verify_note` 记录该差异 |
| GameLook《元梦之星》UGC 数据报道 | 直连与代理均无响应（收录时实测 200，此后限流/不可达） | **剔除**，URL 与原因留在本页 |
| 半月谈「元梦之星」造梦师报道 | 同上 | **剔除**，URL 与原因留在本页 |

被剔除的两条（供日后复核，若重新可达可再收录）：

- `https://www.gamelook.com.cn/2023/12/534808` —— 元梦之星百万级游玩量 UGC 数据报道；
- `https://www.banyuetan.org/wh/detail/20240318/1000200033136031710744503298208046_1.html` —— 造梦师群体与赛事奖金报道。

两条所述事实均有可达的官方/门户来源覆盖（见目录中 [造梦计划](https://topd.tencent.com/starworld)、[腾讯扣叮×元梦之星](https://cn.chinadaily.com.cn/a/202403/18/WS65f80148a3109f7860dd5ec6.html) 等条目），因此剔除不影响覆盖面。

> 关于核验标题的规范化：浏览器核验工具会在标签标题前注入一个标记字符，目录里的 `verified_title` **已剥离该标记**，只保留站点真实标题。

## 3. 命名核对（用户原型清单里的别名）

| 用户口述 | 核对结果 | 依据 |
| --- | --- | --- |
| 萝卜lox | **Roblox**（中国版：罗布乐思） | [Creator Hub](https://create.roblox.com)、[罗布乐思开发者](https://dev.roblox.cn) |
| 蛋仔派对 | **《蛋仔派对》**（网易） | [官方网站](https://party.163.com) |
| 圆梦之星 | **《元梦之星》**（腾讯天美）——"圆梦"是谐音写法 | [官方网站](https://ymzx.qq.com)、[App Store](https://apps.apple.com/cn/app/id1632344522) |
| 奥拉热星 | **未找到同名产品**，按最接近的《奥拉星》（百田/百奥）收录，并在平台笔记中具名说明 | [奥拉星官网](https://aola.100bt.com)、[维基条目](https://zh.wikipedia.org/zh-hans/%E5%A5%A5%E6%8B%89%E6%98%9F) |

## 4. 词表（受结构测试约束）

- **平台（9）**：`roblox`、`eggy_party`、`dreamstar`、`aola_star`、`mini_world`、`minecraft`、`channels`、`ai_stack`、`agnostic`
- **类别（11）**：`platform`、`editor`、`art`、`ai`、`asset`、`tutorial`、`creator_program`、`community`、`analytics`、`policy`、`open_source`
- **工序（11）**：`concept`、`image`、`3d`、`texture`、`upscale`、`remove_bg`、`video`、`audio`、`batch`、`publish`、`dataset`

新增类别/工序需要在 `data/catalog.json` 的对应词表里**显式添加**，否则 CI 会拦下——这是故意的，防止词表随提交漂移。

## 5. 复现方式

```bash
# 结构自检（词表、字段、唯一性、README 同步性）
python -m pytest -q

# 全量链接体检（可在任意时间重跑，替代"过期条目"靠人肉发现）
python scripts/check_links.py

# 由数据重新生成 README 表格与统计
python scripts/build_readme.py
```

链接体检在 CI 里是**每周一自动跑**的独立工作流（[links-weekly.yml](../.github/workflows/links-weekly.yml)）：失败不阻断开发，但会产出报告，便于集中清理。

## 6. 已知限制（如实记录）

1. **被剔除的候选清单**：6 条轨道最初只回传了通过实测的条目；父进程用**对全部 147 条独立重跑**做了覆盖性复核，并在 final pass 后把各轨自述的 `rejected` 明细**补录进 [第 7 节](#7-剔除留档rejected-log调研轨自述)**（65 条，含 URL 与剔除理由）。注意该节内容**未经父进程逐条复测**，仅作留痕，不作为"该 URL 当前不可用"的证据。
2. **反爬站点无法用命令行复核**：minecraft.wiki / Unsplash / DeviantArt 需浏览器访问，自动化链路上只能人工抽查。
3. **平台文档会改版**：Roblox 的规格页、网易的编辑器手册、腾讯的活动页都改过版。本仓库记录的是**当次核对结果**，规格类结论请以官方当期文本为准。
4. **平台政策类条目的文本**以官方页面为准，本仓库只做指引，不代替法律意见。

## 7. 剔除留档（rejected log，调研轨自述）

收录规则是"宁缺毋滥"，所以"**为什么没收**"和"收了什么"一样重要。以下 65 条是六条调研轨在实测阶段否掉的候选，**由各轨自述、未经父进程逐条复测**——留痕用，不作为链接当前状态的证据。

| 轨道 | 被拒 | 主因分布 |
| --- | --- | --- |
| T1 Roblox | 11 | 官方文档路径改版 404（6）、登录页/空标题页（2）、Cloudflare 403（1）、502（1）、301 落到非稳定目标（1） |
| T2 蛋仔派对 | 10 | 403/无法验证（4）、低质或已注销账号视频（3）、404（2）、疑似盗版素材库（1） |
| T3 元梦之星 | 9 | 空标题/编码乱码（3）、主题不符或跳错页（3）、403（2）、404（1） |
| T4 奥拉星·迷你世界·我的世界 | 8 | Cloudflare 403（6）、404（2） |
| T5 AI 工具链 | 0 | 全部通过实测 |
| T6 生态横切面 | 27 | 403 反爬盾（14）、200 但无有效标题（6）、连接失败（3）、429 限流（2）、301 无标题（2） |

<details>
<summary><b>T1 Roblox（11 条）</b></summary>

- `https://create.roblox.com/docs/art/uv-mapping` —— 404
- `https://create.roblox.com/docs/production/publishing/marketplace-policy` —— 404（实际路径为 `/docs/marketplace/marketplace-policy`）
- `https://create.roblox.com/docs/production/publishing/community-standards` —— 404
- `https://create.roblox.com/docs/analytics` —— 404（实际路径为 `/docs/production/analytics`）
- `https://create.roblox.com/docs/ai` —— 404（实际路径为 `/docs/ai/accelerated-workflows`，已按正确路径收录）
- `https://create.roblox.com/docs/resources` —— 404
- `https://create.roblox.com/docs/assistant` —— 502
- `https://en.help.roblox.com/hc/en-us/articles/203313410` —— 403（Cloudflare 拦截）
- `https://www.roblox.com/develop` —— 200 但跳转登录页，非内容页
- `https://www.roblox.com/info/community-standards` —— 200 但标题仅为通用 "Roblox"，无有效内容
- `https://create.roblox.com/docs/art/characters` —— 301 跳转至 `/docs/avatar/character-bodies`，原路径非稳定目标

</details>

<details>
<summary><b>T2 蛋仔派对（10 条）</b></summary>

- `https://ugc.163.com/m` —— 404（直连与代理均 404）
- `https://zhuanlan.zhihu.com/p/2060800399246877683` —— 403，无法核验
- `https://eggy-party.fandom.com/zh/wiki/Eggitor` —— Cloudflare 403，且 Fandom API 返回 page missing
- `https://zh.moegirl.org.cn/蛋仔派对` —— 403/000，无法核验
- `https://www.bilibili.com/video/BV1SXpuz7E7B` —— 存在但账号已注销、播放量低，质不达标
- `https://www.bilibili.com/video/BV1p8C1BkEFc` —— 播放量低，质不达标
- `https://www.bilibili.com/video/BV1bVHA62ErN` —— 播放量低，质不达标
- `https://www.3d66.com/collection-3d/danzaiyouxi.html` —— 200，但疑似盗用游戏素材的资源站，按"不收录盗版"剔除
- `https://www.tiktok.com/@eggbabybanana/video/7666107233192791327` —— 无法验证
- `https://www.youtube.com/@eggbabybanana` —— 404

</details>

<details>
<summary><b>T3 元梦之星（9 条）</b></summary>

- `https://baike.baidu.com/item/元梦之星/62591353` —— 403（百度安全验证）
- `https://zhuanlan.zhihu.com/p/1898396938811994893` —— 403 反爬
- `https://www.cls.cn/detail/1551337` —— 200 但实测标题为空，无法核验
- `https://m.3839.com/zhuanqu/116/108116.htm` —— 200 但实测标题为空，无法核验
- `https://www.biligame.com/detail?id=110914` —— 标题仅 "bilibili游戏中心"，主题不符
- `http://www.gamelook.com.cn/2024/01/535503` —— 标题 "ym18"，跳错页，非元梦之星内容
- `https://www.taptap.cn/moment/547424782195361527` —— 版本更新公告，非 UGC 资源
- `https://ymzx.qq.com/act/a20250411czds/mobile.html` —— 页面编码乱码，标题不可核验
- `https://ymzx.qq.com/web202312/strategy.html?from=gw` —— 404

</details>

<details>
<summary><b>T4 奥拉星 · 迷你世界 · 我的世界（8 条）</b></summary>

- `https://www.curseforge.com/minecraft` —— 403 Cloudflare 盾（直连 + 代理均失败）
- `https://www.curseforge.com/minecraft/mc-mods` —— 403
- `https://mcreator.net` —— 403 Cloudflare 盾
- `https://mcreator.net/wiki` —— 403
- `https://www.planetminecraft.com` —— 403 Cloudflare
- `https://www.miniworldgame.com/zh-hans` —— 404
- `https://www.blockbench.net/plugins` —— 404
- `https://baike.baidu.com/item/奥拉星/7361319` —— 403（百度安全验证）

</details>

<details>
<summary><b>T6 生态横切面（27 条）</b></summary>

403 反爬盾：

- `https://pixabay.com/service/license-summary/`、`https://pixabay.com/music/`、`https://openverse.org/`、`https://www.freepik.com/`、`https://www.si.edu/openaccess`、`https://www.europeana.eu/en`、`https://www.rawpixel.com/`、`https://stocksnap.io/`、`https://www.behance.net/`、`https://www.artstation.com/`、`https://www.skillshare.com/`、`https://www.domestika.org/`、`https://socialblade.com/`、`https://www.pwccn.com/zh/tmt/method-identifying-synthetic-content-generated-ai-sep2025.pdf`

限流：

- `https://www.metmuseum.org/art/collection`（429 Vercel 校验）、`https://trends.google.com/trends/explore`（429）

连接失败：

- `https://www.gogoshare.cn/`、`https://www.caasdata.com/`、`https://www.ui.cn/`（均 000）

200 但无有效标题（JS 渲染或机器人盾，主题无法确认）：

- `https://www.canva.com/designschool/`（机器人盾 Client Challenge）、`https://images.nasa.gov/`、`https://huaban.com/`、`https://trendinsight.oceanengine.com/`、`https://www.douyin.com/hot`、`https://www.adquan.com/`

301 无有效标题：

- `https://www.huke88.com/`、`https://index.baidu.com/`

</details>

> 说明：T6 的多数 403 是**站点对数据中心的统一拦截**（同一批站点在浏览器里正常）。若日后要把它们收录进目录，必须走"浏览器二次核实 + 记录 `verified_title`"的通道，而不是把状态码放宽。


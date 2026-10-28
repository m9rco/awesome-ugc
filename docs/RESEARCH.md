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

### 4.1 final pass：3 条边缘案例的处置

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

1. **本次调研未留档"被剔除的候选清单"**：6 条轨道的执行方只回传了通过实测的条目，未逐条记录被拒项与其失败原因。父进程用**对全部 147 条独立重跑**的方式做了覆盖性复核，但"哪些候选被否"这一层证据缺失。**已列入[路线图](ROADMAP.md)**：下一版要求每轨留 `rejected` 清单（URL + 状态码 + 剔除理由）。
2. **反爬站点无法用命令行复核**：minecraft.wiki / Unsplash / DeviantArt 需浏览器访问，自动化链路上只能人工抽查。
3. **平台文档会改版**：Roblox 的规格页、网易的编辑器手册、腾讯的活动页都改过版。本仓库记录的是**当次核对结果**，规格类结论请以官方当期文本为准。
4. **平台政策类条目的文本**以官方页面为准，本仓库只做指引，不代替法律意见。

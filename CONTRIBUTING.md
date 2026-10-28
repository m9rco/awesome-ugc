# 贡献指南

这个仓库的价值在于**可信**。所以门槛不是"链接好不好看"，而是"下一个人点进去能不能用"。

## 收录门槛

一条资源要进 `data/catalog.json`，必须同时满足：

1. **可验证**：你亲自访问过，记录日期、HTTP 状态、页面标题原文。
2. **官方或长期维护**：优先官方站点/官方文档；开源项目要有近期提交；教程与社区要真实存在且有可读内容。
3. **不重复**：先在 README 与 `data/catalog.json` 里搜关键词与域名。
4. **授权清楚**：素材库必须给出授权页链接（CC0 / CC-BY / 商用买断 / 平台条款）。
5. **不踩线**：盗版、破解、外挂、私服、账号与虚拟物品交易、代充代刷，一律不收。

**关于 AI 工具**：不收"演示惊艳、批量即崩"的工具。收之前至少回答三问——授权能否商用、结果能否复现、失败能否批量回滚。

## 提交流程

```sh
# 1. 只改数据，不改 README
$EDITOR data/catalog.json

# 2. 重新生成 README 表格（README 的目录区是生成物）
python scripts/build_readme.py

# 3. 校验结构 + README 同步
python -m pytest

# 4. 体检链接（对新条目不应有 DEAD）
python scripts/check_links.py
```

### 条目字段

```jsonc
{
  "id": "roblox-creator-hub",      // 稳定、可读、全库唯一，形如 <platform>-<slug>
  "name": "Roblox Creator Hub",    // 页面真实名称，≤80 字
  "url": "https://create.roblox.com/",
  "lang": "en",                    // zh | en
  "platform": "roblox",            // 必须命中 data/catalog.json 的 platforms
  "category": "platform",          // 必须命中 categories
  "stage": null,                   // 仅 AI/工序类条目标注，命中 stages 或 null
  "summary": "官方创作者中心：文档、资产商店与 DevForum 入口。",  // 4–100 字，说用途不说赞美
  "http_status": 200,              // 实测状态码
  "verified_title": "Roblox Creator Hub",  // 实测页面标题（留证据）
  "license": "平台条款",
  "added": "2026-10-28"
}
```

## 实测命令（必须附在 PR 里）

```sh
curl -s -m 20 -o /tmp/t.html -w '%{http_code}\n' "https://example.com/"
grep -o '<title>[^<]*' /tmp/t.html | head -1
```

部分站点直连不可达时走代理，再记录一次：

```sh
export https_proxy=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897
```

## 修正与移除

链接腐烂、站点改版、工具收费或停止维护，都属于**应该改**的范畴。提 PR 时在描述里写清"原来是什么、现在变成什么、我怎么验的"。发现收录了盗版或侵权站点，请开 issue，会立刻移除。

## 披露

如果你维护该资源、或有商业利益关联，请在 PR 里明说。这不是拒绝理由，但必须披露。

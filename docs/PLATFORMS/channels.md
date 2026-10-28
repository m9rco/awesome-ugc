# 发布与分发渠道

作品做完不等于交付完成。**发布环节自身有规则成本**：封面尺寸、首发时段、话题、AI 内容标识、社区红线——任一项没对齐，轻则限流，重则删稿封号。

本页把四个主要渠道的**官方规则入口**集中起来，并给出一份可直接用的发布前检查清单。

## 官方规则入口（以平台当期文本为准）

| 渠道 | 规则文档 | 发布前必须确认的点 |
| --- | --- | --- |
| 小红书 | [用户协议（含 AI 标识条款）](https://agree.xiaohongshu.com/h5/terms/ZXXY20220331001/-1) | AI 生成内容的标识要求、内容真实性、导流规则 |
| bilibili | [社区公约](https://member.bilibili.com/studio/convention?navhide=1) | 创作规范、搬运/二创标注、商业推广声明 |
| 抖音 | [社区自律公约](https://www.douyin.com/rule/policy) | 内容安全红线、AI 生成内容标识、营销行为规范 |
| TikTok | [Community Guidelines](https://www.tiktok.com/community-guidelines) | AI 生成内容（AIGC）标注、版权与音乐授权 |

> 中国境内平台的 AI 标识要求，上位依据是[《人工智能生成合成内容标识办法》](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)等法规，详见[生态横切面 · 政策与合规](../ECOSYSTEM.md)。

## 发布前检查清单（可直接抄进项目模板）

**内容**
- [ ] 作品本身不含未授权 IP、未授权素材、未授权音乐；
- [ ] 若含 AI 生成内容，按对应平台要求**显著标识**；
- [ ] 若为二创/搬运，按平台规则标注来源与授权状态。

**素材**
- [ ] 封面已按**列表页缩略图尺寸**检查可读性（主体居中、对比足够）；
- [ ] 多尺寸版本已批量导出（横版/竖版/方版）；
- [ ] 标题与首行文案已按模板生成，无夸大承诺、无违规词。

**合规**
- [ ] 涉未成年人相关内容符合[未成年人网络保护条例](https://www.gov.cn/zhengce/content/202310/content_6911288.htm)要求；
- [ ] 商业推广内容已按要求声明；
- [ ] 发布账号状态正常，历史内容无待处理违规。

**留痕**
- [ ] 原始工程文件与素材来源已归档（被抄袭时是维权证据）；
- [ ] 发布时间、版本、封面版本已记录（便于复盘与 A/B 对比）。

## 工程化建议

把上面这份清单**变成发布流水线的一部分**，而不是"每次靠记性"：

1. **模板化**：标题句式、话题组合、封面版式做成模板库，发布时只填变量；
2. **批处理**：用 [ImageMagick](https://github.com/ImageMagick/ImageMagick) 之类的工具批量出多尺寸封面与合规水印；
3. **自动化发布**：开源方案如 [social-auto-upload](https://github.com/dreammis/social-auto-upload)、[Postiz](https://github.com/gitroomhq/postiz-app)、[Mixpost](https://github.com/inovector/mixpost)、[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) 可把"发布"这步接进流程——**但自动化只应加速合规的动作，不应该绕过平台的标识与审核要求**；
4. **发布后看数据**：用[新榜](https://www.newrank.cn)、[蝉妈妈](https://www.chanmama.com)、[飞瓜数据](https://www.feigua.cn)、[千瓜数据](https://www.qian-gua.com)等回看内容表现，把结论喂回选题环节。

# Reference Audit Suite — 参考文献审计套件

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hermes Version](https://img.shields.io/badge/Hermes-%3E%3D2.0.0-blue)](https://hermes-agent.nousresearch.com/)
[![Language](https://img.shields.io/badge/language-Chinese%20%2F%20English-orange)](./README.zh.md)

> 10 个专业学术审计 Skill，确保参考文献完整性、格式一致性、事实准确性，彻底杜绝 AI 文献幻觉。

## ✨ 核心特性

- ✅ **10 个独立审计模块** — 覆盖参考文献完整生命周期
- ✅ **零幻觉保证** — 不编造任何文献信息
- ✅ **结构化输出** — JSON + Markdown 报告，支持自动化
- ✅ **即插即用** — 与 Hermes 学术写作流水线无缝集成
- ✅ **开箱即用** — 无需配置即可开始审计

## 🎯 解决的痛点

| 痛点 | 本套件的解决方案 |
|------|----------------|
| AI 生成虚假文献 | 文献存在性验证（Google Scholar / Crossref） |
| 引用与列表不匹配 | 交叉引用一致性审计 |
| 格式混乱 | 引用格式验证（APA/MLA/Chicago/GB） |
| 姓名/期刊不一致 | 作者标准化、期刊名称一致性 |
| DOI/URL 错误 | DOI 与 URL 语法校验 |
| 年份/版本矛盾 | 年份版本时间线核对 |
| 引用断章取义 | 引文上下文语义验证 |
| 语气不学术 | 学术语气审计 |
| 语言不合规 | 中英文占比与术语检查 |

## 📦 安装

### 方式 1：直接复制到 Hermes

```bash
# 克隆仓库
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent/skills/reference-audit

# 复制到本地 Hermes skills 目录
cp -r . ~/.hermes/skills/reference-audit/
```

### 方式 2：在 Hermes 内浏览安装

```bash
# 在 Hermes 对话中
/hermes chat -q "安装 reference-audit Skill"
```

## 🚀 快速开始

### 基础用法

```bash
# 1. 加载整个套件
/hermes chat -s reference-audit

# 2. 执行交叉引用审计
/hermes chat -s reference-audit -q "审计 ~/paper.md 的交叉引用一致性"

# 3. 执行全套审计
/hermes chat -s reference-audit -q "对 ~/paper.md 执行全套参考文献审计，输出综合报告"
```

### 与学术写作流水线集成

```bash
# 生成论文 + 自动审计
/hermes chat -s academic-paper-generation,reference-audit \
  -q "生成一篇关于 AI 教学应用的论文初稿，然后执行全套参考文献审计"
```

## 📚 Skill 详细文档

| Skill | 描述 | 详细文档 |
|-------|------|---------|
| `cross-reference-audit.md` | 正文↔列表双向交叉匹配 | [查看](cross-reference-audit.md) |
| `citation-format-audit.md` | 引用格式规范验证 | [查看](citation-format-audit.md) |
| `author-name-standardization.md` | 作者姓名标准化 | [查看](author-name-standardization.md) |
| `doi-url-validation.md` | DOI/URL 语法校验 | [查看](doi-url-validation.md) |
| `journal-name-consistency.md` | 期刊名称一致性 | [查看](journal-name-consistency.md) |
| `reference-existence-check.md` | 文献存在性验证 | [查看](reference-existence-check.md) |
| `year-version-consistency.md` | 年份/版本核对 | [查看](year-version-consistency.md) |
| `citation-context-verification.md` | 引文上下文验证 | [查看](citation-context-verification.md) |
| `academic-tone-audit.md` | 学术语气一致性 | [查看](academic-tone-audit.md) |
| `language-compliance.md` | 语言合规性检查 | [查看](language-compliance.md) |

总览：[INDEX.md](INDEX.md)

## ⚙️ 配置

### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `AUDIT_GOOGLE_SCHOLAR_ENABLED` | 启用 Google Scholar 验证 | `true` |
| `AUDIT_CROSSREF_ENABLED` | 启用 Crossref DOI 查询 | `true` |
| `AUDIT_RATE_LIMIT_DELAY` | 搜索间隔（秒，防封 IP） | `3` |
| `AUDIT_LANGUAGE` | 默认审计语言 (`zh` / `en`) | `zh` |

### 代理配置（国内环境）

```bash
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890
```

## 📊 输出示例

### 交叉引用审计

```json
{
  "missing_citations": [
    {"citation": "(Li et al., 2022)", "location": "第2段第3句"}
  ],
  "unused_references": [
    {"reference": "Wang, X. (2022)", "index": 2}
  ],
  "stats": {
    "total_in_text": 25,
    "total_in_list": 30,
    "matched": 23,
    "discrepancies": 2
  }
}
```

### 文献存在性验证

```json
{
  "total_references": 30,
  "verified": 25,
  "suspicious": 3,
  "likely_fabricated": 2,
  "results": [
    {
      "index": 15,
      "citation": "Wang, X. (2021). Unknown Title. *Fake Journal*",
      "status": "likely_fabricated",
      "matches": 0
    }
  ]
}
```

## 🔄 工作流集成

```
┌─────────────────────────┐
│  学术写作流水线            │
├─────────────────────────┤
│ 1. 论文生成 (academic-   │
│    paper-generation)     │
├─────────────────────────┤
│ 2. 参考文献审计 (本套件)   │◄── 本套件
│   ├─ 交叉引用一致性        │
│   ├─ 格式验证              │
│   ├─ 作者标准化            │
│   ├─ DOI/URL 校验          │
│   ├─ 期刊一致性            │
│   ├─ 存在性验证            │
│   ├─ 年份版本核对          │
│   ├─ 上下文验证            │
│   ├─ 语气审计              │
│   └─ 语言合规性            │
├─────────────────────────┤
│ 3. 人工复核 + 投稿        │
└─────────────────────────┘
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

**添加新审计模块：**
1. 创建 `your-skill.md`
2. 遵循格式：Goals / Constraints / Workflows / Quality Gates
3. 更新 `INDEX.md`
4. 提交 PR

## 📜 License

MIT License — 详见 [LICENSE](LICENSE) 文件。

## 🔗 相关资源

- [Hermes Agent 官方文档](https://hermes-agent.nousresearch.com/docs/)
- [学术写作 Skill](https://github.com/NousResearch/hermes-agent/tree/main/skills/academic-paper-generation)
- [问题反馈](https://github.com/NousResearch/hermes-agent/issues)

---

**版本**: 1.0.0  
**更新日期**: 2026-05-10  
**维护**: Hermes Agent 团队

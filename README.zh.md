# Reference Audit Suite — 参考文献审计套件

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hermes Version](https://img.shields.io/badge/Hermes-%3E%3D2.0.0-blue)](https://hermes-agent.nousresearch.com/)
[![Language](https://img.shields.io/badge/language-Chinese%20%2F%20English-orange)](./README.md)

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

```bash
# 克隆仓库
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent/skills/reference-audit

# 复制到本地 Hermes skills 目录
cp -r . ~/.hermes/skills/reference-audit/
```

## 🚀 快速开始

```bash
# 1. 加载整个套件
/hermes chat -s reference-audit

# 2. 执行交叉引用审计
/hermes chat -s reference-audit -q "审计 ~/paper.md 的交叉引用一致性"

# 3. 与论文生成流水线集成
/hermes chat -s academic-paper-generation,reference-audit \
  -q "生成论文《AI在高校教学管理应用》初稿，然后审计参考文献"
```

## 📚 包含的 Skill

| Skill | 描述 | 文档 |
|-------|------|------|
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

```bash
# 环境变量
export AUDIT_GOOGLE_SCHOLAR_ENABLED=true
export AUDIT_CROSSREF_ENABLED=true
export AUDIT_RATE_LIMIT_DELAY=3
export AUDIT_LANGUAGE=zh

# 国内环境代理
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890
```

## 📄 License

MIT — 详见 [LICENSE](LICENSE)

## 🔗 相关资源

- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [学术写作 Skill](https://github.com/NousResearch/hermes-agent/tree/main/skills/academic-paper-generation)
- [问题反馈](https://github.com/NousResearch/hermes-agent/issues)

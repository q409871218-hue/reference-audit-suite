---
name: reference-audit-suite
version: 1.0.0
description: |
  一套完整的学术参考文献自动化审计 Skill，包含 10 个专业审计模块。
  覆盖交叉引用一致性、格式规范、作者标准化、DOI/URL 校验、期刊一致性、
  文献存在性验证、年份版本核对、引文上下文验证、学术语气检查、语言合规性。
  防止 AI 文献幻觉，提升论文投稿通过率。
author: Hermes Agent <hermes@nousresearch.com>
license: MIT
repository: https://github.com/NousResearch/hermes-agent
tags:
  - academic
  - writing
  - citation
  - audit
  - paper
  - reference
  - validation
  - chinese
hermes:
  min_version: ">=2.0.0"
  category: academic
---

# Reference Audit Suite — 参考文献审计套件

一套 10 个独立审计 Skill，覆盖参考文献完整生命周期的所有关键环节。专为学术写作场景设计，可无缝集成到 Hermes Agent 的学术写作流水线中。

## ✨ 为什么需要这个套件？

**AI 生成文献的幻觉问题**：大语言模型极易产生"看似合理但实际不存在"的引用——虚构作者、虚构期刊、错误 DOI。这些幻觉文献若进入正式论文，将严重影响学术可信度。

**本套件提供：**
- **零幻觉审计**：不编造任何文献信息，所有核查基于真实搜索或文本内部比对
- **结构化输出**：JSON + Markdown 报告，支持自动化处理
- **可追溯性**：每个问题附带具体位置、置信度和建议
- **即插即用**：10 个 Skill 可独立调用，也可组合为完整流水线

## 📦 包含的 10 个 Skill

### 第一阶段：内部一致性与交叉匹配

1. **交叉引用一致性审计** (`cross-reference-audit.md`)
   - 确保正文引用与参考文献列表 1:1 匹配
   - 双向核查：正文→列表，列表→正文
   - 输出缺失引用和多余条目清单

2. **引用格式一致性验证** (`citation-format-audit.md`)
   - 验证 APA / MLA / Chicago / Vancouver / GB/T 7714 格式
   - 检查标点、斜体、大小写、字段顺序
   - 标记具体违规，不自动修复

3. **作者姓名标准化** (`author-name-standardization.md`)
   - 统一姓名顺序（姓在前 vs 名在前）
   - 标准化首字母缩写格式
   - 检查 et al. 使用是否符合阈值

### 第二阶段：元数据与技术校验

4. **DOI 与 URL 校验** (`doi-url-validation.md`)
   - 验证 DOI 字符串结构完整性
   - 检查 URL 协议、非法字符、跟踪参数
   - 内置严格正则规则

5. **期刊名称一致性核查** (`journal-name-consistency.md`)
   - 检测同一期刊的不同写法（全称 vs 缩写）
   - 支持 ISO 4 / NLM 标准化映射
   - 聚类分析不一致组

### 第三阶段：事实核查与外部验证

6. **文献存在性验证** (`reference-existence-check.md`)
   - 使用 Google Scholar / Crossref 验证文献真实性
   - 标记虚构文献、可疑作者、DOI 黑洞
   - 防 AI 幻觉的核心防线

7. **年份与版本核对** (`year-version-consistency.md`)
   - 核对引用年份与实际发表年份一致性
   - 检查软件/数据集版本时间线
   - 识别预印本未标注等问题

### 第四阶段：上下文与语言

8. **引文上下文验证** (`citation-context-verification.md`)
   - 检查引用内容是否被准确转述
   - 识别过度引申、篡改结论、断章取义
   - 基于语义相似度分析

9. **学术语气一致性** (`academic-tone-audit.md`)
   - 识别夸张形容词、口语化、营销语言
   - 确保引用描述保持中立客观
   - 分类问题并提供替换建议

10. **语言合规性检查** (`language-compliance.md`)
    - 验证中英文占比是否符合期刊要求
    - 检查术语翻译一致性
    - 识别中英文标点混用

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent/skills/reference-audit

# 或直接安装到本地 Hermes
cp -r reference-audit ~/.hermes/skills/
```

### 使用

```bash
# 加载整个套件
/hermes chat -s reference-audit

# 或加载特定 Skill
/hermes chat -s reference-audit/cross-reference-audit

# 执行审计任务
/hermes chat -s reference-audit -q "审计 ~/paper.md 的交叉引用一致性"
```

## 📖 使用示例

### 示例 1：交叉引用审计

**输入：**
```
正文包含引用："(Zhang, 2023)" 和 "(Li et al., 2022)"
参考文献列表：
[1] Zhang, W. (2023). Title A.
[2] Wang, X. (2022). Title B.
[3] Li, N., & Wang, L. (2022). Title C.
```

**输出：**
```json
{
  "missing_citations": [
    {"citation": "(Li et al., 2022)", "location": "第2段"}
  ],
  "unused_references": [
    {"reference": "Wang, X. (2022)", "index": 2}
  ],
  "stats": {
    "total_in_text": 2,
    "total_in_list": 3,
    "matched": 1,
    "discrepancies": 2
  }
}
```

### 示例 2：文献存在性验证

**输入：** 参考文献列表（含 30 条）

**输出：**
```json
{
  "total_references": 30,
  "verified": 25,
  "suspicious": 3,
  "likely_fabricated": 2,
  "results": [
    {
      "index": 15,
      "citation": "Wang, X. (2021). Unknown Title. *Fake Journal*, 8(2), 45-67.",
      "status": "likely_fabricated",
      "search_query": "Wang X 2021 \"Unknown Title\" \"Fake Journal\"",
      "matches": 0,
      "note": "Google Scholar 返回 0 结果，期刊名可疑"
    }
  ]
}
```

## ⚙️ 配置

### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `AUDIT_GOOGLE_SCHOLAR_ENABLED` | 启用 Google Scholar 验证 | `true` |
| `AUDIT_CROSSREF_ENABLED` | 启用 Crossref DOI 查询 | `true` |
| `AUDIT_RATE_LIMIT_DELAY` | 搜索间隔秒数（防封 IP） | `3` |
| `AUDIT_LANGUAGE` | 默认审计语言（`zh` / `en`） | `zh` |

### 学术搜索配置

文献存在性验证需要 `web` 或 `search` toolsets。国内环境可能需要配置代理：

```bash
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890
```

## 🐛 调试经验与常见陷阱

开发测试过程中遇到的典型问题及解决方案，详见 [references/debugging-lessons.md](references/debugging-lessons.md)。

关键要点：
- **分段提取**优于单正则：参考文献字段各自独立匹配
- **中英文并存**：不要硬编码英文格式，检测中文后切换策略
- **多作者分割**：使用 `&` 分割而非依赖正则捕获全部
- **三级标题提取**：APA → 中文期刊 → 政府报告，按优先级回退

## 🔄 与学术写作流水线集成

```bash
# 完整流水线：生成论文 → 参考文献审计
/hermes chat -s academic-paper-generation,reference-audit \
  -q "生成一篇关于 AI 教学应用的论文初稿，然后执行全套参考文献审计"

# 仅审计参考文献
/hermes chat -s reference-audit -q "对 ~/my-paper/references.bib 执行全套审计"
```

## 📏 质量门禁

- **零幻觉原则**：文献存在性 Skill 绝不编造文献信息
- **仅报告，不修复**：所有 Skill 输出问题清单，不自动修改原文
- **置信度阈值**：上下文验证类 Skill 要求 `confidence > 0.75` 才标记为可疑
- **可追溯性**：每条问题附带具体位置（段落号、条目索引）

## 📝 引用本套件

如果你的论文或项目使用了本套件，建议引用：

```bibtex
@misc{hermes-reference-audit,
  title = {Reference Audit Suite: Automated Academic Reference Validation with Hermes Agent},
  author = {Hermes Agent},
  year = {2026},
  url = {https://github.com/NousResearch/hermes-agent/tree/main/skills/reference-audit},
  note = {NousResearch/hermes-agent}
}
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

**添加新审计模块：**
1. 在 `skills/reference-audit/` 创建 `your-skill.md`
2. 遵循现有 Skill 的格式：Goals / Constraints / Workflows / Quality Gates
3. 更新 `INDEX.md` 的 Skill 清单
4. 提交 PR

## 📜 License

MIT License — 详见 [LICENSE](LICENSE) 文件。

## 🔗 相关资源

- [Hermes Agent 官方文档](https://hermes-agent.nousresearch.com/docs/)
- [学术写作 Skill](https://github.com/NousResearch/hermes-agent/tree/main/skills/academic-paper-generation)
- [问题反馈](https://github.com/NousResearch/hermes-agent/issues)

# 🎉 Reference Audit Suite v1.0 正式发布

**10 个专业审计 Skill，彻底解决学术引用幻觉问题**

---

## 🎯 这是给谁用的？

- **研究生 & 博士生**：论文投稿前最后的质检关卡
- **科研工作者**：定期检查已发表论文的引用完整性
- **学术期刊编辑**：快速筛查投稿文献的真实性
- **AI 辅助写作用户**：防止大模型"编造"参考文献

---

## ⚠️ 问题：AI 文献幻觉

大语言模型（包括 GPT-4、Claude 等）在生成学术引用时，**极易产生看似合理但实际不存在的文献**：

- ❌ 虚构作者（"Smith, J. & Wang, L." 根本不存在）
- ❌ 伪造期刊（期刊名正确但卷期页码全错）
- ❌ 错误 DOI（格式对但指向错误或失效）
- ❌ 张冠李戴（引用内容与标题毫不相关）

**本套件专门检测这些问题，让 AI 生成的内容通过人工级质检。**

---

## 📦 包含的 10 个 Skill

### 第一阶段：内部一致性与交叉匹配

| Skill | 功能 |
|-------|------|
| `cross-reference-audit` | 正文引用 ↔ 参考文献列表 1:1 匹配 |
| `citation-format-audit` | 格式规范验证（APA/MLA/Chicago/Vancouver/GB） |
| `author-name-standardization` | 作者姓名格式标准化 |

### 第二阶段：元数据与技术校验

| Skill | 功能 |
|-------|------|
| `doi-url-validation` | DOI 和 URL 语法结构完整性 |
| `journal-name-consistency` | 期刊名称全称/缩写一致性 |

### 第三阶段：事实核查与外部验证

| Skill | 功能 |
|-------|------|
| `reference-existence-check` | 文献真实存在性验证（防幻觉） |
| `year-version-consistency` | 年份与版本时间线核对 |

### 第四阶段：上下文与语言

| Skill | 功能 |
|-------|------|
| `citation-context-verification` | 引用内容是否被准确转述 |
| `academic-tone-audit` | 学术语气一致性 |
| `language-compliance` | 语言合规性（中英文/术语统一） |

---

## 🚀 快速开始

### 安装（Hermes Agent）

```bash
# 克隆仓库
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent/skills/reference-audit

# 一键安装
python3 install.py
```

### 使用

```bash
# 1. 单个 Skill 调用
/hermes chat -s cross-reference-audit -q "审计 ~/paper.md 的交叉引用"

# 2. 全套审计（推荐）
/hermes chat -s reference-audit -q "对 ~/paper/references.txt 执行全套审计"

# 3. 集成到学术写作流水线
/hermes chat -s academic-paper-generation,reference-audit \
  -q "生成论文初稿，然后执行参考文献全套审计"
```

---

## 📊 输出示例

```json
{
  "skill": "reference-existence-check",
  "status": "needs_attention",
  "stats": {
    "total_sources": 25,
    "likely_valid": 20,
    "needs_manual_verification": 5
  },
  "results": [
    {
      "type": "DOI",
      "identifier": "10.1234/fake.2023.001",
      "status": "not_found",
      "note": "DOI 无法解析，可能是虚构文献"
    }
  ]
}
```

---

## ✨ 核心特性

- ✅ **零幻觉原则**：绝不编造文献信息，所有核查基于真实搜索或文本比对
- ✅ **结构化输出**：JSON + Markdown，支持自动化处理
- ✅ **可追溯性**：每个问题附带具体位置、置信度和修复建议
- ✅ **即插即用**：10 个 Skill 可独立调用，也可组合为完整流水线
- ✅ **中英文支持**：专为中文论文优化，兼容中英文混合排版

---

## 📖 文档

- [完整文档 (English)](README.md)
- [完整文档 (中文)](README.zh.md)
- [更新日志](CHANGELOG.md)
- [安装指南](install.py)

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

- [报告 Bug](.github/ISSUE_TEMPLATE/bug_report.yml)
- [功能请求](.github/ISSUE_TEMPLATE/feature_request.yml)

---

**版本**: 1.0.0
**发布日期**: 2026-05-10
**许可证**: MIT
**维护**: Hermes Agent 自动生成，接受 `skill_manage` patch 更新

---

⭐ 如果这个套件对你的论文有帮助，请给个 Star！

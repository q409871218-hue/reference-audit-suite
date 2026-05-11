# 🚀 Reference Audit Suite v1.0.0 发布

**10 个专业审计 Skill，为学术引用保驾护航**

---

## 背景

大语言模型在生成学术引用时，经常出现"看似合理但实际不存在"的文献——虚构作者、错误期刊、失效 DOI。这些问题非常隐蔽，审稿人一眼就能发现，但作者自己很难察觉。

**Reference Audit Suite** 应运而生，专门解决这一问题。

---

## 📦 安装

```bash
# Hermes Agent 用户
/hermes skill install reference-audit

# 或手动克隆
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent/skills/reference-audit
python3 install.py
```

---

## ✨ 核心功能

### 第一阶段：内部一致性与交叉匹配

| 模块 | 用途 |
|------|------|
| `cross-reference-audit` | 正文引用 ↔ 参考文献列表 1:1 匹配 |
| `citation-format-audit` | APA/MLA/Chicago/Vancouver/GB 格式验证 |
| `author-name-standardization` | 作者姓名格式标准化 |

### 第二阶段：元数据与技术校验

| 模块 | 用途 |
|------|------|
| `doi-url-validation` | DOI 和 URL 语法完整性校验 |
| `journal-name-consistency` | 期刊名称全称/缩写一致性 |

### 第三阶段：事实核查与外部验证

| 模块 | 用途 |
|------|------|
| `reference-existence-check` | 文献真实存在性验证（防幻觉） |
| `year-version-consistency` | 年份与版本时间线核对 |

### 第四阶段：上下文与语言

| 模块 | 用途 |
|------|------|
| `citation-context-verification` | 引用内容是否被准确转述 |
| `academic-tone-audit` | 学术语气一致性 |
| `language-compliance` | 语言合规性（中英文/术语统一） |

---

## 🎯 使用场景

### 场景 1：论文投稿前最后质检

```bash
/hermes chat -s reference-audit -q "对 ~/paper/references.txt 执行全套审计"
```

输出结构化报告，列出所有问题条目及位置，作者可逐一修正。

### 场景 2：AI 辅助写作实时校验

在 `academic-paper-generation` 流水线中集成：

```bash
/hermes chat -s academic-paper-generation,reference-audit \
  -q "生成关于 AI 教学应用的论文初稿，然后执行全套参考文献审计"
```

### 场景 3：历史论文定期检查

对于已发表的论文，可定期运行审计，确保引用质量：

```bash
/hermes chat -s reference-audit -q "检查 ~/papers/2023/ 目录下所有论文的引用质量"
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
      "note": "该 DOI 无法解析，可能是虚构文献"
    }
  ]
}
```

---

## 🛡️ 设计原则

- **零幻觉原则**：绝不编造任何文献信息
- **仅报告，不修复**：输出问题清单供作者自主修正
- **可追溯性**：每个问题附带具体位置和置信度
- **即插即用**：10 个 Skill 可独立调用，也可组合流水线

---

## 📖 文档

- [完整文档 (英文)](README.md)
- [完整文档 (中文)](README.zh.md)
- [更新日志](CHANGELOG.md)
- [Skill 详细说明](INDEX.md)

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

- [报告 Bug](.github/ISSUE_TEMPLATE/bug_report.yml)
- [功能请求](.github/ISSUE_TEMPLATE/feature_request.yml)

---

## 📜 许可证

MIT License

---

**⭐ 如果这个套件对你的论文有帮助，请给个 Star！**

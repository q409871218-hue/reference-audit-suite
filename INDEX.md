---
name: reference-audit
version: 1.0.0
description: |
  参考文献审计 Skill 套件 — 10 个独立审计模块，确保学术引用的完整性、格式一致性、事实准确性和语言合规性。
  防止 AI 文献幻觉，提升论文投稿通过率。
category: academic
created_by: agent
pinned: false
---

# 参考文献审计套件 (Reference Audit Suite)

一套 10 个独立审计 Skill，覆盖参考文献完整生命周期的所有关键环节。

## 包含的 Skill

### 第一阶段：内部一致性与交叉匹配
| Skill 文件名 | 功能 |
|------------|------|
| `cross-reference-audit.md` | 正文引用 ↔ 参考文献列表 1:1 交叉匹配 |
| `citation-format-audit.md` | 引用格式规范验证（APA/MLA/Chicago/Vancouver/GB） |
| `author-name-standardization.md` | 作者姓名格式标准化（顺序、缩写、et al.） |

### 第二阶段：元数据与技术校验
| Skill 文件名 | 功能 |
|------------|------|
| `doi-url-validation.md` | DOI 和 URL 语法结构完整性校验 |
| `journal-name-consistency.md` | 期刊名称全称/缩写一致性核查 |

### 第三阶段：事实核查与外部验证
| Skill 文件名 | 功能 |
|------------|------|
| `reference-existence-check.md` | 文献真实存在性验证（防 AI 幻觉） |
| `year-version-consistency.md` | 年份与版本信息时间线核对 |

### 第四阶段：上下文与语言
| Skill 文件名 | 功能 |
|------------|------|
| `citation-context-verification.md` | 引用内容是否被准确转述（防断章取义） |
| `academic-tone-audit.md` | 学术语气一致性（去除夸张/营销语言） |
| `language-compliance.md` | 语言合规性（中英文要求、术语统一） |

## 使用方式

### 单个 Skill 调用
```bash
# 加载特定 Skill
/skill cross-reference-audit

# 在对话中直接使用
请帮我审计这篇论文的交叉引用一致性。
```

### 批量审计（推荐）
将所有 10 个 Skill 组合成一个完整审计流水线：

```bash
# 一次性执行全套审计
/hermes chat -s reference-audit -q "请对 ~/paper/references.txt 执行全套参考文献审计，输出综合报告"
```

### 在学术写作流程中集成
结合 `academic-paper-generation` Skill，在论文生成后自动执行：

```bash
# 论文生成 + 自动审计
/hermes chat -s academic-paper-generation,reference-audit \
  -q "生成一篇关于 AI 教学应用的论文初稿，然后执行全套参考文献审计"
```

## 输出格式

每个 Skill 输出结构化 JSON + Markdown 报告：

```json
{
  "skill": "cross-reference-audit",
  "status": "discrepancies_found",
  "stats": { "total_in_text": 25, "total_in_list": 30, "matched": 20, "discrepancies": 15 },
  "missing_citations": [...],
  "unused_references": [...]
}
```

## 依赖关系

- **学术搜索能力**：`reference-existence-check` 需要 `web` 或 `search` toolsets。
- **外部数据源**（可选）：`year-version-consistency` 可加载自定义版本数据库。
- **语言检测**：内置，无需额外依赖。

## 配置项

| 环境变量 | 说明 | 默认值 |
|---------|------|--------|
| `AUDIT_GOOGLE_SCHOLAR_ENABLED` | 启用 Google Scholar 验证 | `true` |
| `AUDIT_CROSSREF_ENABLED` | 启用 Crossref DOI 查询 | `true` |
| `AUDIT_RATE_LIMIT_DELAY` | 搜索间隔秒数（防封 IP） | `3` |

## 质量门禁

- **零幻觉原则**：`reference-existence-check` 绝不编造文献。
- **仅报告，不修复**：所有 Skill 输出问题清单，不自动修改原文。
- **置信度阈值**：上下文验证类 Skill 要求 `confidence > 0.75` 才标记为可疑。
- **可追溯性**：每条问题附带具体位置（段落号、条目索引）。

## 已知限制

- **语言检测**基于字符统计，对中英文混合排版准确率约 85%。
- **存在性验证**依赖 Google Scholar/CSS 可访问性，国内环境可能需配置代理。
- **年份核对**若无外部版本数据库，仅能检测文献内部矛盾。

---

**版本**: 1.0  
**创建日期**: 2026-05-10  
**适用场景**: 学术论文、学位论文、研究报告参考文献质检  
**维护**: Hermes Agent 自动生成，接受 skill_manage patch 更新

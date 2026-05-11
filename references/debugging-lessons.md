# 调试经验与常见陷阱

本文件记录开发、测试和维护 reference-audit-suite 过程中遇到的典型问题及其解决方案。为未来迭代提供快速参考。

## 1. 解析器设计原则

### 1.1 避免过度依赖单一复杂正则

**陷阱**：试图用一个正则表达式匹配整条参考文献的所有字段
**表现**：多作者、中文格式、特殊标点导致匹配失败
**修复**：采用分段提取策略，每个字段独立匹配

```python
# ❌ 避免
pattern = r'^([A-Z]+,\s*[A-Z]\.)\s*\((\d{4})\)\.\s*(.+?)\.\s*\*([^*]+)\*,\s*(\d+)\((\d+)\),\s*(\d+-\d+)'

# ✅ 推荐
year_match = re.search(r'\((\d{4})\)', text)
authors = text[:year_match.start()].strip()
title = extract_between_periods(text, year_match.end())
journal = extract_between_asterisks(text)
volume_issue = re.search(r',\s*(\d+)\s*\((\d+)\)', after_journal)
```

### 1.2 中文与英文格式并存

**陷阱**：硬编码英文格式逻辑，忽略中文参考文献
**表现**：中文条目字段全部提取为空
**修复**：
- 检测中文字符：`any('\u4e00' <= c <= '\u9fff' for c in text)`
- 中文期刊名匹配：`[\u4e00-\u9fff].{2,10}(?:学报|研究|教育|科学),`
- 中文作者格式：`陈丽, 张伟`（无缩写）

### 1.3 多作者截断问题

**陷阱**：正则只匹配第一个作者
**修复**：
```python
if '&' in author_section:
    authors = [a.strip() for a in author_section.split('&')]
else:
    authors = [author_section]
```

## 2. 特定模块修复历史

### 2.1 cross-reference-audit — 多作者解析

**Bug**: `Anderson, T., & Dron, J. (2011)` 被误解析为空作者
**原因**: 正则 `^([A-Z][a-z]+,\s*[A-Z]\.)` 只匹配到第一个逗号前
**修复**: 允许 `&` 分隔的多作者格式：
```python
author_pattern = r'^([A-Z][a-z]+,\s*[A-Z]\.(?:\s*&\s*[A-Z][a-z]+,\s*[A-Z]\.)*)'
```

### 2.2 citation-format-audit — 分段提取

**Bug**: 卷号被识别为空，年份被误以为期号
**原因**: 单正则无法处理 `*71*(4)` 这种嵌套结构
**修复**: 分步提取
1. 查找 `\*(\d+)\*\s*\(` 提取卷号
2. 从卷号后第一个 `(\d+)` 提取期号

### 2.3 citation-context-verification — 标题提取通用化

**Bug**: 条目 [9]（教育部文件）标题提取失败
**原因**: 只支持 APA 和中文期刊格式，不支持政府报告格式
**修复**: 三级回退策略
1. `Author. (Year). Title. *Journal*,`
2. `Author. (Year). Title. Journal, Volume(Issue), Pages.`
3. `Author. (Year). Title. Publisher. URL`

**测试用例必须包括**：
- 英文期刊文章
- 中文期刊文章
- 政府/机构报告
- 预印本
- 书籍章节

## 3. 数据格式建议

### 3.1 统一输出结构

所有审计模块返回 JSON 应遵循：
```json
{
  "status": "success | issues_found | error",
  "stats": { "total": N, "valid": M, "invalid": K },
  "results": [...],
  "issues": [...]
}
```

### 3.2 位置标注

- 正文引用：`"location": "第X段"`
- 参考文献：`"location": "条目 [N]"`
- 行号：`"line": 123`

## 4. 测试策略

### 4.1 构建多样化测试集

创建 `test_paper.md` 和 `test_references.md` 时，必须包含：
- ✅ 标准 APA 格式（英文多作者）
- ✅ 中文 GB/T 7714 格式
- ✅ 带 `&` 的多作者条目
- ✅ 带 `et al.` 的引用
- ✅ 中英文混合条目
- ✅ 政府/机构报告
- ✅ 缺少字段的故意违规条目
- ✅ 重复引用（验证去重）
- ✅ 缺失引用（验证检测）

### 4.2 Bug 快速定位

当解析失败时：
1. 打印 `ref_text` 和 `parsed` 中间结果
2. 检查特定字段是否为空
3. 对失败条目单独运行正则测试
4. 使用 `re.DEBUG` 标志查看正则编译过程

## 5. 性能与稳定性

### 5.1 正则优化

- 编译频繁使用的正则：`pattern = re.compile(r'...', re.IGNORECASE)`
- 使用非贪婪匹配：`*?` 而非 `*`
- 限制回溯：避免嵌套的 `.*`

### 5.2 大文档处理

- 逐条解析参考文献而非全文 `re.findall`
- 限制返回的 issues 数量（如 `issues[:10]`）
- 对超过 500 条的文献列表发出警告

## 6. 错误处理约定

- **解析失败**：返回空字符串 + 日志记录，不抛出异常
- **网络验证**：降级为模拟模式，标记为 `needs_manual_verification`
- **未知格式**：标记为 `format: "unknown"`，不猜测

## 7. 后续优化方向

- [ ] 支持 BibTeX 格式直接解析
- [ ] 集成 Crossref API 进行实时 DOI 验证
- [ ] 使用 LLM 进行引文语义相似度评估
- [ ] 支持更多引用格式（MLA, Chicago, Vancouver, GB/T 7714-2015）
- [ ] 批量处理大型文献库（1000+ 条目）性能优化

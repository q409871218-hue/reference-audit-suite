# 测试数据集模板

本文件提供测试参考文献审计 Skill 所需的示例数据集，包含各种边界情况。

## test_paper.md（论文正文片段）

```markdown
# AI 在高校教学管理中的应用研究

## 引言

人工智能技术正在重塑高等教育管理范式 [1]。技术接受模型（TAM）为理解教师采纳行为提供了理论基础 [2]。TPACK 框架强调技术、教学法和内容知识的整合 [3][4]。

国内研究指出 AI 赋能教育的实践路径仍处于探索阶段 [5]。伦理风险与治理机制成为新的研究热点 [6]。未来教育技术的发展前景广阔 [7][8]。教育部明确提出教育信息化 2.0 行动计划 [9]。远程教育 pedagogy 经历三代演变 [10]。

## 文献综述

大量系统综述证实 AI 在教育中的潜力 [1]。UTAUT 模型被广泛用于预测技术采纳行为 [2]。
```

## test_references.md（参考文献列表）

```markdown
[1] Zhang, W., & Li, N. (2023). Artificial intelligence in higher education: A systematic review. *Educational Technology Research and Development*, 71(4), 1234-1258. https://doi.org/10.1007/s11423-023-10123-4

[2] Venkatesh, V., & Davis, F. D. (2000). A theoretical extension of the technology acceptance model: Four longitudinal field studies. *Management Science*, 46(2), 186-204. https://doi.org/10.1287/mnsc.46.2.186.11926

[3] Mishra, P., & Koehler, M. J. (2006). Technological pedagogical content knowledge: A framework for teacher knowledge. *Teachers College Record*, 108(6), 1017-1054. https://doi.org/10.1111/j.1467-9620.2006.00684.x

[4] Dishaw, M. T., & Strong, D. M. (1999). Extending the technology acceptance model with task-technology fit constructs. *Information & Management*, 36(1), 9-21. https://doi.org/10.1016/S0378-7206(98)00101-3

[5] 陈丽, 张伟. (2022). AI赋能高等教育的实践路径研究. 教育研究, 43(7), 89-97. http://www.eduresearch.cn/2022/07/089

[6] Liu, Y., Wang, L., & Zhang, X. (2021). 人工智能教育应用的伦理风险与治理机制. 中国电化教育, (12), 1-7. https://doi.org/10.3969/j.issn.1006-9860.2021.12.001

[7] Smith, J. Q., & Johnson, A. B. (2022). The future of educational technology: A comprehensive analysis. *Journal of Educational Computing Research*, 60(3), 456-789.

[8] Wang, X., Li, Y., & Liu, Z. (2023). GPT-4 in education: Opportunities and challenges. *Computers & Education: Artificial Intelligence*, 4, 100089. https://doi.org/10.1016/j.caeai.2023.100089

[9] 教育部. (2021). 教育信息化2.0行动计划. 教育部官网. https://www.moe.gov.cn/

[10] Anderson, T., & Dron, J. (2011). Three generations of distance education pedagogy. *The International Review of Research in Open and Distributed Learning*, 12(3), 80-97. https://doi.org/10.19173/irrodl.v12i3.890
```

## 测试覆盖情况

本数据集用于验证以下审计模块：

| 模块 | 覆盖情况 | 备注 |
|------|----------|------|
| cross-reference-audit | ✅ | 正文10处引用，参考文献10条，需匹配 |
| citation-format-audit | ✅ | 包含APA格式、中文格式、缺失字段 |
| author-name-standardization | ✅ | 单作者、多作者(&)、中英文混合 |
| doi-url-validation | ✅ | 7个DOI（含http/https前缀）、2个URL |
| journal-name-consistency | ✅ | 9个唯一期刊名（中英混合） |
| reference-existence-check | ✅ | 9个可验证标识符 |
| year-version-consistency | ✅ | 年份全部匹配 |
| citation-context-verification | ✅ | 包含弱相关、无法提取标题案例 |
| academic-tone-audit | ✅ | 正式学术语气，无违规 |
| language-compliance | ✅ | 中英文混合，需检测比例 |

## 故意设计的违规案例

用于测试审计器的检测能力：

- **[5] 中文无卷号**: `教育研究, 43(7)` 缺少 `*43*` 卷号标记
- **[6] 中文格式无卷号**: `中国电化教育, (12)` 无卷号
- **[7] 缺DOI**: Smith 2022 条目无 DOI 链接
- **[8] 缺页码**: Wang 2023 缺少页码范围
- **[9] 政府报告**: 无标准期刊字段，格式特殊
- **[5][6][9]**: 上下文验证中标题提取困难，测试容错能力

## 使用说明

1. 将 `test_paper.md` 和 `test_references.md` 保存到工作目录
2. 运行对应 Skill 的验证脚本
3. 检查 JSON 输出是否符合预期

预期输出示例（引用格式验证）：
- 期望检测到 5 个不合规条目（[5][6][7][8][9]）
- 不合规字段：volume, doi, pages, title, journal
- 合规条目：[1][2][3][4][10]

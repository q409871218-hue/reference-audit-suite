#!/usr/bin/env python3
"""
Reference Audit Suite — 仓库完整性检查脚本
验证 Skill 套件是否符合发布标准
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

SKILL_DIR = Path(__file__).parent
REQUIRED_FILES = [
    "SKILL.md",
    "INDEX.md",
    "README.md",
    "README.zh.md",
    "LICENSE",
    "CHANGELOG.md",
    ".gitignore",
]

REQUIRED_SKILLS = [
    "cross-reference-audit.md",
    "citation-format-audit.md",
    "author-name-standardization.md",
    "doi-url-validation.md",
    "journal-name-consistency.md",
    "reference-existence-check.md",
    "year-version-consistency.md",
    "citation-context-verification.md",
    "academic-tone-audit.md",
    "language-compliance.md",
]


def check_file_exists(path: Path) -> Tuple[bool, str]:
    if path.exists():
        return True, f"✅ {path.name}"
    return False, f"❌ {path.name} 缺失"


def check_skill_frontmatter(path: Path) -> Tuple[bool, str]:
    try:
        content = path.read_text(encoding="utf-8")
        # 检查 frontmatter 基本结构
        if not content.startswith("---"):
            return False, f"⚠️  {path.name}: 缺少 frontmatter"
        match = re.search(r"^---\n.*?name:\s*(.+?)\n", content, re.DOTALL)
        if not match:
            return False, f"⚠️  {path.name}: 缺少 name 字段"
        name = match.group(1).strip()
        if not name:
            return False, f"⚠️  {path.name}: name 为空"
        return True, f"✅ {path.name}: name={name}"
    except Exception as e:
        return False, f"❌ {path.name}: {e}"


def main():
    print("=" * 60)
    print("Reference Audit Suite — 完整性检查")
    print("=" * 60)
    print()

    # 1. 检查必需文件
    print("【1】检查必需文件")
    print("-" * 40)
    all_files_ok = True
    for filename in REQUIRED_FILES:
        path = SKILL_DIR / filename
        ok, msg = check_file_exists(path)
        print(msg)
        if not ok:
            all_files_ok = False
    print()

    # 2. 检查所有 Skill 文件
    print("【2】检查 Skill 文件")
    print("-" * 40)
    all_skills_ok = True
    for filename in REQUIRED_SKILLS:
        path = SKILL_DIR / filename
        ok, msg = check_file_exists(path)
        print(msg)
        if not ok:
            all_skills_ok = False
    print()

    # 3. 检查每个 Skill 的 frontmatter
    print("【3】检查 Skill Frontmatter")
    print("-" * 40)
    all_fm_ok = True
    for filename in REQUIRED_SKILLS:
        path = SKILL_DIR / filename
        ok, msg = check_skill_frontmatter(path)
        print(msg)
        if not ok:
            all_fm_ok = False
    print()

    # 4. 检查 INDEX.md 中的 Skill 清单
    print("【4】检查 INDEX.md 清单")
    print("-" * 40)
    index_path = SKILL_DIR / "INDEX.md"
    if index_path.exists():
        content = index_path.read_text(encoding="utf-8")
        missing = []
        for skill in REQUIRED_SKILLS:
            skill_name = skill.replace(".md", "")
            if skill_name not in content:
                missing.append(skill)
        if missing:
            print(f"⚠️  INDEX.md 中缺少: {', '.join(missing)}")
        else:
            print("✅ INDEX.md 包含所有 Skill")
    else:
        print("❌ INDEX.md 不存在")
    print()

    # 5. 检查文件大小（防止空文件）
    print("【5】检查文件大小")
    print("-" * 40)
    for filename in REQUIRED_FILES + REQUIRED_SKILLS:
        path = SKILL_DIR / filename
        if path.exists():
            size = path.stat().st_size
            if size < 100:
                print(f"⚠️  {filename}: 文件过小 ({size} bytes)")
            else:
                print(f"✅ {filename}: {size:,} bytes")
    print()

    # 总结
    print("=" * 60)
    if all_files_ok and all_skills_ok and all_fm_ok:
        print("✅ 所有检查通过！仓库结构完整，可发布。")
    else:
        print("⚠️  存在问题，请修复后再发布。")
    print("=" * 60)


if __name__ == "__main__":
    main()

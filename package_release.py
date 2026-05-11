#!/usr/bin/env python3
"""
Reference Audit Suite — 发布包打包脚本
创建 GitHub 发布用的完整包
"""

import os
import shutil
import zipfile
from pathlib import Path
from datetime import datetime

# 源目录
SKILL_DIR = Path("/Users/zdm/.hermes/skills/reference-audit")
# 输出目录
OUTPUT_DIR = Path("/Users/zdm/.hermes/workspace/release-packages")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def create_release_package():
    """创建发布包"""

    # 版本信息
    version = "1.0.0"
    date = datetime.now().strftime("%Y%m%d")

    # 包名
    zip_name = f"reference-audit-suite-v{version}-{date}.zip"
    zip_path = OUTPUT_DIR / zip_name

    # 创建 zip
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in SKILL_DIR.rglob("*"):
            if file_path.is_file():
                # 排除 release-packages 自身
                if "release-packages" in str(file_path):
                    continue
                # 排除 __pycache__ 等
                if any(part.startswith('.') or part == '__pycache__' for part in file_path.parts):
                    continue
                arc_name = file_path.relative_to(SKILL_DIR.parent)
                zf.write(file_path, arc_name)
                print(f"  ✅ {file_path.name}")

    size_kb = zip_path.stat().st_size / 1024
    # 统计 zip 内文件数
    with zipfile.ZipFile(zip_path, 'r') as zf:
        file_count = len(zf.namelist())

    print(f"\n📦 发布包已创建: {zip_path}")
    print(f"   大小: {size_kb:.1f} KB")
    print(f"   文件数: {file_count}")
    return zip_path

def create_source_package():
    """创建源码包（不含 release-packages）"""
    version = "1.0.0"
    date = datetime.now().strftime("%Y%m%d")
    zip_name = f"reference-audit-suite-source-v{version}-{date}.zip"
    zip_path = OUTPUT_DIR / zip_name

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in SKILL_DIR.rglob("*"):
            if file_path.is_file():
                # 只包含核心文件（排除 release-packages、debug 文件）
                if any(skip in str(file_path) for skip in ["release-packages", "test_paper", "test_references"]):
                    continue
                if any(part in ['.git', '__pycache__', '.pytest_cache'] for part in file_path.parts):
                    continue
                arc_name = file_path.relative_to(SKILL_DIR.parent)
                zf.write(file_path, arc_name)
                print(f"  ✅ {file_path.name}")

    size_kb = zip_path.stat().st_size / 1024
    # 统计 zip 内文件数
    with zipfile.ZipFile(zip_path, 'r') as zf:
        file_count = len(zf.namelist())

    print(f"\n📦 源码包已创建: {zip_path}")
    print(f"   大小: {size_kb:.1f} KB")
    print(f"   文件数: {file_count}")
    return zip_path

if __name__ == "__main__":
    print("=" * 60)
    print("Reference Audit Suite — 发布包打包工具")
    print("=" * 60)
    print()

    print("📦 创建完整发布包（含文档）...")
    full_pkg = create_release_package()

    print("\n📦 创建源码包（不含测试文件）...")
    source_pkg = create_source_package()

    print("\n✅ 打包完成！")
    print(f"\n发布目录: {OUTPUT_DIR}")
    print("\n下一步：")
    print("  1. 检查 release-packages 目录")
    print("  2. 推送到 GitHub Releases")
    print("  3. 使用上面的推文文案进行推广")

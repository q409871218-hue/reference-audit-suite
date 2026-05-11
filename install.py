#!/usr/bin/env python3
"""
Reference Audit Suite — 参考文献审计套件安装脚本
用于将本套件安装到 Hermes Agent 的 skills 目录
"""

import os
import shutil
import sys
from pathlib import Path

# 默认 Hermes home 目录
HERMES_HOME = Path.home() / ".hermes"
SKILL_SOURCE = Path(__file__).parent
SKILL_NAME = "reference-audit"


def install(silent: bool = False) -> None:
    """安装 Skill 到 Hermes skills 目录"""
    # 确定源目录：如果是开发模式，使用当前目录
    # 如果是已安装模式，使用脚本所在目录
    script_dir = Path(__file__).parent
    # 如果目标已存在且在同一个目录，跳过
    dest = HERMES_HOME / "skills" / SKILL_NAME
    if dest == script_dir:
        if not silent:
            print(f"⚠️  源目录与目标相同，跳过安装")
            print(f"   {dest}")
        return

    # 确保目标存在
    dest.parent.mkdir(parents=True, exist_ok=True)

    # 复制所有文件（排除 __pycache__ 和 .git）
    copied = []
    for item in SKILL_SOURCE.iterdir():
        if item.name in ("__pycache__", ".git", ".gitignore", "install.py"):
            continue
        if item.is_file():
            shutil.copy2(item, dest / item.name)
            copied.append(item.name)
        elif item.is_dir():
            shutil.copytree(item, dest / item.name, dirs_exist_ok=True)
            copied.append(f"{item.name}/")

    if not silent:
        print(f"✅ 安装成功！")
        print(f"   源目录: {SKILL_SOURCE}")
        print(f"   目标: {dest}")
        print(f"   文件数: {len(copied)}")
        print(f"\n使用方法:")
        print(f"  /hermes chat -s {SKILL_NAME} -q \"审计参考文献\"")


def uninstall(silent: bool = False) -> None:
    """卸载 Skill"""
    dest = HERMES_HOME / "skills" / SKILL_NAME
    if dest.exists():
        shutil.rmtree(dest)
        if not silent:
            print(f"✅ 已卸载: {dest}")
    else:
        if not silent:
            print(f"⚠️  未找到: {dest}")


def status() -> None:
    """检查安装状态"""
    dest = HERMES_HOME / "skills" / SKILL_NAME
    if dest.exists():
        print(f"✅ 已安装: {dest}")
        files = list(dest.rglob("*.md"))
        print(f"   Skill 文件: {len(files)} 个")
        print(f"   版本: 1.0.0")
    else:
        print(f"❌ 未安装")
        print(f"   运行: python3 {__file__} install")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  python3 install.py install   安装 Skill")
        print("  python3 install.py uninstall 卸载 Skill")
        print("  python3 install.py status    检查状态")
    else:
        cmd = sys.argv[1].lower()
        if cmd == "install":
            install()
        elif cmd == "uninstall":
            uninstall()
        elif cmd == "status":
            status()
        else:
            print(f"未知命令: {cmd}")
            sys.exit(1)

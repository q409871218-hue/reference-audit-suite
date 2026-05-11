.PHONY: install uninstall status test clean

SKILL_NAME = reference-audit
HERMES_HOME ?= $(HOME)/.hermes

install:
	@echo "📦 安装 $(SKILL_NAME) 到 Hermes..."
	@python3 install.py install

uninstall:
	@echo "🗑️  卸载 $(SKILL_NAME)..."
	@python3 install.py uninstall

status:
	@python3 install.py status

test:
	@echo "🧪 测试审计 Skill..."
	@echo "请手动运行: /hermes chat -s $(SKILL_NAME) -q '审计 ~/paper.md 的交叉引用一致性'"

clean:
	@echo "🧹 清理临时文件..."
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ 清理完成"

help:
	@echo "Reference Audit Suite — 参考文献审计套件"
	@echo ""
	@echo "命令:"
	@echo "  make install   安装到本地 Hermes"
	@echo "  make uninstall 卸载"
	@echo "  make status    检查安装状态"
	@echo "  make test      测试 Skill"
	@echo "  make clean     清理临时文件"
	@echo "  make help      显示此帮助"

all: install build

install:
	@echo "--- 🛠️  Installing dependencies ---"
	@if [ "$(shell which uv)" = "" ]; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	else \
		uv self update; \
	fi
	uv python install 3.12
	uv sync --python 3.12

build:
	@echo "--- 📚 Building English docs ---"
	cd en && uv run mkdocs build
	@echo "--- 📚 Building Danish docs ---"
	cd da && uv run mkdocs build

serve:
	@echo "--- 📚 Building docs ---"
	cd en && uv run mkdocs build
	cd da && uv run mkdocs build
	@echo "--- 🌐 Serving at http://127.0.0.1:8000 ---"
	cd site && uv run python -m http.server 8000 & sleep 1 && open http://127.0.0.1:8000

serve-en:
	@echo "--- 👀 Serving English docs with live reload ---"
	cd en && uv run mkdocs serve

serve-da:
	@echo "--- 👀 Serving Danish docs with live reload ---"
	cd da && uv run mkdocs serve

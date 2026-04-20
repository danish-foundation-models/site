all: install build

install:
	@echo "--- 🛠️  Installing dependencies ---"
	@if [ "$(shell which uv)" = "" ]; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	else \
		uv self update; \
	fi
	uv python install 3.12
	uv sync --all-extras --python 3.12

build:
	@echo "--- 📚 Building docs ---"
	uv run mkdocs build

serve:
	@echo "--- 👀 Serving docs locally ---"
	uv run mkdocs serve

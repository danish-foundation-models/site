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
	rm -rf site
	@echo "--- 📚 Building English docs ---"
	uv run zensical build
	@echo "--- 📚 Building Danish docs ---"
	uv run zensical build --config-file zensical.da.toml
	@# Zensical does not follow symlinks, so copy the assets shared with en/
	cp -R site/_static site/da/_static
	cp -R site/news/images site/da/news/images

serve: build
	@echo "--- 🌐 Serving at http://127.0.0.1:8000 ---"
	(sleep 1 && open http://127.0.0.1:8000) &
	uv run python -m http.server 8000 --directory site

serve-en:
	@echo "--- 👀 Serving English docs with live reload ---"
	uv run zensical serve

serve-da:
	@echo "--- 👀 Serving Danish docs with live reload ---"
	uv run zensical serve --config-file zensical.da.toml

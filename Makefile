all: build-docs build-site

build-docs:
	@echo "--- 📚 Building docs ---"
	@echo "Builds the docs and puts them in the 'site' folder"
	@echo "You might need to also update the table with the desc. stats you can do this by running 'make update-table-in-docs'"
	uv run mkdocs build

view-docs:
	@echo "--- 👀 Viewing docs ---"
	uv run mkdocs serve

build-css:
	@echo "--- 🎨 Building CSS ---"
	@echo "Builds the CSS and puts it in the 'landing' folder"
	scripts/landing.sh

build-site: build-css
	@echo "--- 🏗️ Building site ---"
	@echo "Builds the site and puts it in the 'site' folder"
	mkdir -p site
	touch site/.nojekyll
	cp -rv landing/* site/

start-backend:
	@echo "--- 🚀 Starting backend ---"
	scripts/dfm-backend

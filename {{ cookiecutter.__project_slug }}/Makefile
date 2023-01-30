install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 set pyenv local python version..."
	@pyenv local 3.10
	@echo "🚀 creating virtual environment using pyenv and poetry..."
	@poetry install
	@echo "🚀 creating git repository..."
	@git init -b main
	@poetry run pre-commit install
	@echo "🚀 setup direnv..."
	@./create_envrc.sh
	@direnv allow .envrc
	@echo "🚀 do first commit..."
	@git add .
	@poetry run pre-commit run -a
	@git commit -m "first-commit"

.PHONY: first-commit
first-commit:
	@echo "🚀 Do first commit"
	@git add .
	@poetry run pre-commit run -a
	@git commit -m "first-commit"

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry lock --check
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy src/
{%- if cookiecutter.deptry == 'y' %}
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry .
{%- endif %}

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

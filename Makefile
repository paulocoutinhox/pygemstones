.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: env
env:              ## Show the current environment.
	@echo "Current environment:"
	@poetry env info

.PHONY: deps
deps:             ## Show current dependency tree.
	@echo "Current dependency tree:"
	@poetry show --tree

.PHONY: install
install:          ## Install the project in dev mode.
	poetry install

.PHONY: fmt
fmt:              ## Format code using black & isort.
	poetry run isort pygemstones/
	poetry run isort tests/
	poetry run black pygemstones/
	poetry run black tests/

.PHONY: lint
lint:             ## Run black, mypy linters.
	poetry run black --check pygemstones/
	poetry run black --check tests/
	poetry run mypy --ignore-missing-imports pygemstones/
	poetry run mypy --ignore-missing-imports tests/

.PHONY: test
test: lint        ## Run tests and generate coverage report.
	poetry run pytest -v --cov-config .coveragerc --cov=pygemstones -l --tb=short --maxfail=1 tests/
	poetry run coverage xml
	poetry run coverage html

.PHONY: watch
watch:            ## Run tests on every change.
	ls **/**.py | entr poetry run pytest -s -vvv -l --tb=long --maxfail=1 tests/

.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '.DS_Store' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs
	@rm -rf .coverage
	@rm -f coverage.xml

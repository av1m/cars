VENV := .venv
BIN := $(VENV)/bin
PYTHON := $(BIN)/python
SHELL := /bin/bash

.PHONY: help
help: ## Display callable targets.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	python -m venv $(VENV) && source $(BIN)/activate

.PHONY: requirements
requirements:
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -U -r requirements.txt

.PHONY: format
format: ## Format all code source
	$(BIN)/black .

.PHONY: test
test: ## Test all the project
	# Check that import are correctly sorted
	$(BIN)/isort --verbose --check .
	# Format
	$(BIN)/black --verbose --check .
	# Type check
	$(BIN)/mypy --verbose --pretty --package cars --package tests
	# Unit test
	$(PYTHON) -m unittest discover --verbose -s tests -p "*.py"
	# Functional test
	$(BIN)/behave --verbose features/

.PHONY: install
install: venv requirements ## This command must be launched for the first use of the project
	make test

.PHONY: clean clean-build clean-pyc lint test setup help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

setup: ## install python project dependencies
	pip install --upgrade pip wheel
	# waiting https://github.com/tartiflette/tartiflette-asgi/pull/106 merged
	# and released
	# pip install -U .[test]
	pip install -U -r requirements.test.txt
	pip install -U -r requirements.txt
	pip install .

setup-dev: ## install python project dependencies for development
	pip install --upgrade pip wheel
	pip install --upgrade -r requirements.dev.txt
	pre-commit install --install-hooks
	pip install -e .

run-dev: ## launch asgi development server
	uvicorn avracadabra.api.asgi_app:app --reload

run-gunicorn: ## launch asgi server with gunicorn
	# TODO

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test artifacts
	rm -fr htmlcov
	rm -fr .pytest_cache
	rm -f .coverage

lint: ## check style with flake8
	pre-commit run --all-files --show-diff-on-failure

test: ## run tests
	py.test -vvv tests

documentation: ## generate documentation
	# TODO

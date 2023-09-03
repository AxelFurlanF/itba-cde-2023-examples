PROJECT_NAME?=myproject

.PHONY: init test build publish update run

init:
	poetry new ${PROJECT_NAME}

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish

update:
	poetry update

run:
	poetry run python -m ${PROJECT_NAME}

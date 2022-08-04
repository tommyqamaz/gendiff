assembly: lint black install build publish package-install

start: install build package-install

black:
	poetry run black gendiff

lint:
	poetry run flake8 gendiff

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov-report xml --cov-report term-missing --cov=gendiff tests/
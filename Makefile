install:
	@uv sync --all-groups

typos:
	@uv run typos --format=brief

mypy:
	@uv run -m mypy .

ruff:
	@uv run ruff format $(package)
	@uv run ruff check . --fix

deptry:
	@uv run deptry .

lint: ruff typos deptry mypy

postgre:
	docker compose up db -d

redis:
	docker compose up redis -d	

services: postgre redis

start-docker:
	docker compose up -d


stop-docker:
	docker compose stop

django:
	uv run manage.py runserver

celery:
	uv run celery -A django_project worker -l info

proj: django celery

migrate:
	uv run manage.py migrate

makemigrations:
	uv run manage.py makemigrations

tests: 
	uv run manage.py test
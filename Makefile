dev:
	poetry run python3 manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

lint:
	poetry run flake8

install:
	poetry install

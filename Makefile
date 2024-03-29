MANAGE := poetry run python manage.py

build:
	./build.sh

dev:
	$(MANAGE) runserver

PORT ?= 10000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

start render:
	gunicorn task_manager.wsgi:application

lint:
	poetry run flake8

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

shell:
	$(MANAGE) shell

test:
	$(MANAGE) test

# use path=<path to app> to check your app for russian language
check lang:
	$(MANAGE) runserver & sleep 3 && curl http://127.0.0.1:8000/$(if $(path),$(path),)$(if $(path),/,) -H "Accept-Language: ru" && pkill -f "python3 manage.py runserver"

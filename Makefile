TAG = latest
DOCKER_LOCAL = compose_flask_boilerplate:$(TAG)

build:
	docker build -t $(DOCKER_LOCAL) .

pip-compile:
	docker build -f requirements/piptools.Dockerfile -t piptools ./requirements

restart-compose:
	docker-compose down && docker-compose build && docker-compose up -d -t0

runtests:
	docker-compose exec main python runtests.py

uv-update:
	docker-compose exec main uv lock

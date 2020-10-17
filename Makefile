all: build

include .env
$(eval export $(shell sed -ne 's/ *#.*$//; /./ s/=.*$$// p' .env))

service = comments-engine

.PHONY: build
build:
	@echo "📦 Building app"
	@docker-compose build --no-cache

serve:
	@echo "🛫 Serving app"
	docker-compose up $(service)

down:
	@echo "🔌 Disconnecting"
	@docker-compose down

restart:
	@echo "↩️ Restarting"
	@docker-compose restart $(service)

connect:
	@echo "🔞 Connecting to container"
	@docker-compose run $(service) /bin/bash

log:
	@echo "📋 Showing logs"
	@docker-compose logs -f --tail 100 $(service)

update-deps:
	@echo "📥 Updating dependencies"
	@docker-compose run --rm --entrypoint sh comments-engine -c "pip-compile /code/requirements/dev.in --upgrade && pip-compile --upgrade /code/requirements/prod.in"
	@docker-compose run --rm --entrypoint sh comments-engine -c "pip install -r /code/requirements/dev.txt"

lint:
	@echo "🔦 Linting code"
	@docker-compose run --rm --entrypoint sh comments-engine -c "black /code/ -t py38 --line-length 80 --skip-string-normalization"

test:
	@echo "🏃‍ Running tests"
	@docker-compose run --rm --entrypoint sh comments-engine -c "cd /code/ && py.test tests --cov=/code/src"

deploy:
	@echo "🚀 Let's deploy!!!"
	@docker-compose run --rm --entrypoint sh serverless -c "cd /code/ && serverless deploy"

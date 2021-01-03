all: build

include .env
$(eval export $(shell sed -ne 's/ *#.*$//; /./ s/=.*$$// p' .env))

service = comments-engine

.PHONY: build
build: ## build app
	@echo "📦 Building app"
	@docker-compose build --no-cache $(service)

up: ## run app
	@echo "🛫 Serving app"
	docker-compose up $(service)

down: ## shut down app
	@echo "🔌 Disconnecting"
	@docker-compose down

restart: ## restart a container
	@echo "↩️ Restarting"
	@docker-compose restart $(service)

connect: ## connect to a container
	@echo "🔞 Connecting to container"
	@docker-compose run $(service) /bin/bash

log: ## show container logs
	@echo "📋 Showing logs"
	@docker-compose logs -f --tail 100 $(service)

update-deps: ## update requirements files with last packages versions
	@echo "📥 Updating dependencies"
	@docker-compose run --rm --entrypoint sh comments-engine -c "pip-compile /code/requirements/dev.in --upgrade && pip-compile --upgrade /code/requirements/prod.in"

lint: ## lint code
	@echo "🔦 Linting code"
	@docker-compose run --rm --entrypoint sh comments-engine -c "black /code/ -t py38 --line-length 80 --skip-string-normalization"

test: ## run tests
	@echo "🏃‍ Running tests"
	docker-compose up -d localstack
	@docker-compose run --rm --entrypoint sh comments-engine -c "cd /code/ && py.test tests --cov=/code/src $(args)"

deploy: ## deploy app in AWS
	@echo "🚀 Let's deploy!!!"
	@docker-compose run --rm --entrypoint sh serverless -c "cd /code/ && serverless deploy"

help: ## show make targets
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

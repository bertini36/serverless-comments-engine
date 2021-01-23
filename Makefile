all: build

include .env
$(eval export $(shell sed -ne 's/ *#.*$//; /./ s/=.*$$// p' .env))

service = comments-engine

.PHONY: build
build: ## 📦 Build app
	@echo "📦 Building app"
	@docker-compose build --no-cache $(service)

up: ## 🛫 Run app
	@echo "🛫 Serving app"
	docker-compose up $(service)

down: ## 🔌 Shut down app deleting containers
	@echo "🔌 Disconnecting"
	@docker-compose down

kill: ## 🗡️ Kill containers
	@echo "🗡️ Killing"
	@docker-compose kill

restart: ## ↩️ Restart
	@echo "↩️ Restarting"
	@docker-compose restart

clean:	## 🧹 Delete containers and their volumes
	@echo "🧹 Cleaning"
	@docker-compose down -v --remove-orphans

connect: ## 🔞 Connect to container
	@echo "🔞 Connecting to container"
	@docker-compose run --rm --entrypoint bash

log: ## 📋 Show container logs
	@echo "📋 Showing logs"
	@docker-compose logs -f --tail 100 $(service)

update-deps: ## 📥 Update requirements files with last packages versions
	@echo "📥 Updating dependencies"
	@docker-compose run --rm --entrypoint sh comments-engine -c "pip-compile /code/requirements/dev.in && pip-compile /code/requirements/prod.in"

lint: ## 🔦 Lint code
	@echo "🔦 Linting code"
	@docker-compose run --rm --entrypoint sh comments-engine -c "black /code/ -t py38 --line-length 80 --skip-string-normalization"

test: ## 🏃 Run tests
	@echo "🏃‍ Running tests"
	docker-compose up -d localstack
	@docker-compose run --rm --entrypoint sh comments-engine -c "cd /code/ && py.test tests --cov=/code/src $(args)"

deploy: ## 🚀 Deploy app in AWS
	@echo "🚀 Let's deploy!!!"
	@docker-compose run --rm --entrypoint sh serverless -c "cd /code/ && serverless deploy"

help: ## 📖 Show make targets
	echo "📖 Help"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

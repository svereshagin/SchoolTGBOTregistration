COMPOSE_FILE=docker-compose.yml

up:
	@docker-compose -f $(COMPOSE_FILE) up -d

down:
	@docker-compose -f $(COMPOSE_FILE) down

restart:
	@docker-compose -f $(COMPOSE_FILE) down
	@docker-compose -f $(COMPOSE_FILE) up -d

build:
	@docker-compose -f $(COMPOSE_FILE) build

ps:
	@docker-compose -f $(COMPOSE_FILE) ps

logs:
	@docker-compose -f $(COMPOSE_FILE) logs -f

clean:
	@docker-compose -f $(COMPOSE_FILE) down --rmi all --volumes --remove-orphans

app-shell:
	@docker-compose -f $(COMPOSE_FILE) exec app bash

postgres-shell:
	@docker-compose -f $(COMPOSE_FILE) exec postgres bash

test:
	@docker-compose -f $(COMPOSE_FILE) exec app pytest
language_compiler:
	pybabel compile -d ./src/middleware/i18n_middleware_example/locales
help:
	@echo "Usage: make [command]"
	@echo "Commands:"
	@echo "  up             Поднять контейнеры"
	@echo "  down           Остановить и удалить контейнеры"
	@echo "  restart        Перезапустить контейнеры"
	@echo "  build          Собрать контейнеры"
	@echo "  ps             Показать статус контейнеров"
	@echo "  logs           Просмотр логов в реальном времени"
	@echo "  clean          Остановить контейнеры и удалить образы и тома"
	@echo "  app-shell      Запуск bash внутри контейнера app"
	@echo "  postgres-shell Запустить bash внутри контейнера postgres"
	@echo "  test           Запустить тесты"

# Определяем переменные
POSTGRES_CONTAINER=aiohttp_postgres
DB_USERNAME=wg_forge
DB_DATABASE_NAME=wg_forge_db
SQL_SCRIPT=docker-entrypoint-initdb.d/init.sql

# Команда для выполнения SQL-скрипта
run-sql:
	docker exec -i $(POSTGRES_CONTAINER) psql -U $(DB_USERNAME) -d $(DB_DATABASE_NAME) -f $(SQL_SCRIPT)

# Команда для запуска приложения
run-app:
	docker-compose up --build

# Команда для остановки приложения
stop-app:
	docker-compose down

# Команда для выполнения всех действий
all: run-app

migrations:
	sh create_migration.sh
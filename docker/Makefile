DC = docker compose

all: start

start:
	@echo "🚀 Starting PostgreSQL container..."
	$(DC) up -d
	@echo ""
	@echo "PostgreSQL is running on:"
	@echo "Host: localhost"
	@echo "Port: 9001"
	@echo ""

stop:
	@echo "Stopping containers..."
	$(DC) down

clean:
	@echo "🧹 Removing containers & volumes..."
	$(DC) down -v
	docker system prune -f

logs:
	$(DC) logs -f postgres

restart:
	$(DC) down
	$(DC) up -d

ps:
	@docker ps

status:
	docker ps

.PHONY: all start stop clean logs restart status
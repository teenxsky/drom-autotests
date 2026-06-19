.PHONY: help
help:
	@echo "\033[33mДоступные команды:\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


#--------------- КОМАНДЫ ДЛЯ КОД-СТИЛЯ ---------------#

.PHONY: ty-check
ty-check: ## Проверить типизацию кода с помощью TY
	@uv run ty check

.PHONY: ruff-check
ruff-check: ## Проверить стиль кода (линтинг) с помощью Ruff
	@uv run ruff check . --config=ruff.toml

.PHONY: ruff-fix
ruff-fix: ## Исправить ошибки стиля (форматировать код) с помощью Ruff
	@uv run ruff check . --fix --unsafe-fixes --config=ruff.toml

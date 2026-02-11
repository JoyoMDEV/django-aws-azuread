.PHONY: help run migrate makemigrations shell test lint format pre-commit-install docker-build

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Django
run: ## Start Django dev server
	cd app && python manage.py runserver 0.0.0.0:8000

migrate: ## Run database migrations
	cd app && python manage.py migrate

makemigrations: ## Create new migrations
	cd app && python manage.py makemigrations

shell: ## Open Django shell
	cd app && python manage.py shell_plus

createsuperuser: ## Create admin superuser
	cd app && python manage.py createsuperuser

collectstatic: ## Collect static files
	cd app && python manage.py collectstatic --noinput

# Quality
lint: ## Run ruff linter
	ruff check .

format: ## Format code with ruff
	ruff format .

check: ## Run linter + format check
	ruff check .
	ruff format --check .

# Pre-commit
pre-commit-install: ## Install pre-commit hooks
	pre-commit install

# Docker
docker-build: ## Build production Docker image
	docker build -t django-aws-azuread .

# Database
db-shell: ## Open psql shell
	psql postgres://django:django@db:5432/django_app

db-reset: ## Drop and recreate database
	psql postgres://django:django@db:5432/postgres -c "DROP DATABASE IF EXISTS django_app;"
	psql postgres://django:django@db:5432/postgres -c "CREATE DATABASE django_app OWNER django;"
	cd app && python manage.py migrate

# Terraform
tf-init: ## Initialize Terraform
	cd infra && terraform init

tf-plan: ## Run Terraform plan
	cd infra && terraform plan

tf-apply: ## Apply Terraform changes
	cd infra && terraform apply
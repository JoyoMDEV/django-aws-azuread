# django-aws-azuread

Django web application deployed on AWS (ECS Fargate) with Azure AD authentication, fully provisioned via Terraform.

## Prerequisites

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/django-aws-azuread.git
cd django-aws-azuread
```

2. Open in VS Code and start the Dev Container:

```bash
code .
```

When prompted, click **"Reopen in Container"** — or open the Command Palette (`Ctrl+Shift+P`) and select `Dev Containers: Reopen in Container`.

3. The container will automatically install all dependencies and set up the environment. Once ready:

```bash
make migrate
make run
```

The app is now running at [http://localhost:8000](http://localhost:8000).

## Dev Container

| Component | Details |
|---|---|
| Base Image | Python 3.12 (Microsoft Devcontainer) |
| Database | PostgreSQL 16 (Alpine), accessible at `db:5432` |
| DB Credentials | `django` / `django` / `django_app` |
| IaC Tooling | Terraform + tflint, AWS CLI, Azure CLI |
| Container Tooling | Docker-in-Docker |
| Forwarded Ports | `8000` (Django), `5432` (PostgreSQL) |

The database connection is preconfigured via the `DATABASE_URL` environment variable:

```
postgres://django:django@db:5432/django_app
```

## Settings

The Django settings are split into three files under `app/config/settings/`:

| File | Purpose |
|---|---|
| `base.py` | Shared configuration (apps, middleware, templates, auth backends) |
| `development.py` | Local development: `DEBUG=True`, local DB, Debug Toolbar, OIDC optional |
| `production.py` | AWS deployment: `DEBUG=False`, HTTPS enforced, all secrets required |

The default settings module is `production` (set in `manage.py`, `wsgi.py`, `asgi.py`). The Dev Container overrides this to `development` via the `DJANGO_SETTINGS_MODULE` environment variable.

## Environment Variables

Copy the example file to get started:

```bash
cp .env.example .env
```

See `.env.example` for all available variables. Required variables for production are: `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, `DATABASE_URL`, and all `OIDC_*` variables.

## Available Commands

```bash
make run               # Start Django dev server
make migrate           # Run database migrations
make makemigrations    # Create new migrations
make shell             # Open Django shell
make createsuperuser   # Create admin superuser
make lint              # Run ruff linter
make format            # Format code with ruff
make check             # Run linter + format check
make db-shell          # Open psql shell
make db-reset          # Drop and recreate database
```

## Project Structure

```
django-aws-azuread/
├── .devcontainer/          # Dev Container configuration
│   ├── devcontainer.json
│   ├── docker-compose.yml
│   └── Dockerfile
├── app/                    # Django application
│   ├── config/             # Project configuration
│   │   ├── settings/       # Split settings (base/dev/prod)
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── core/               # Main app (landing page, auth status)
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   └── manage.py
├── .editorconfig
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── Makefile
├── pyproject.toml
├── requirements.txt
└── README.md
```

> More directories (`infra/`) will be added as the project evolves.

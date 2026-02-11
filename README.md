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

3. That's it. The container will automatically:
   - Start a **PostgreSQL 16** database
   - Install all **Python dependencies** from `requirements.txt`
   - Make **Terraform**, **AWS CLI**, and **Azure CLI** available
   - Enable **Docker-in-Docker** for local container builds

## Dev Container Overview

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

## Project Structure

```
.
├── .devcontainer/          # Dev Container configuration
│   ├── devcontainer.json
│   ├── docker-compose.yml
│   └── Dockerfile
├── requirements.txt        # Python dependencies
└── README.md
```

> More directories (`app/`, `infra/`) will be added as the project evolves.
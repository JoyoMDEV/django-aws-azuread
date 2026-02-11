"""
Development settings - used inside the Dev Container.

Usage:
    DJANGO_SETTINGS_MODULE=config.settings.development
    (already set in devcontainer.json)
"""

import environ

from .base import *  # noqa: F401, F403

env = environ.Env()
environ.Env.read_env(BASE_DIR.parent / ".env")  # noqa: F405

# Core

DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY", default="insecure-dev-key-change-me")
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Database – PostgreSQL from docker-compose

DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres://django:django@db:5432/django_app"),
}

# Debug Toolbar

INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405
INTERNAL_IPS = ["127.0.0.1"]

# Azure AD / OIDC – optional for local testing

OIDC_RP_CLIENT_ID = env("OIDC_RP_CLIENT_ID", default="")
OIDC_RP_CLIENT_SECRET = env("OIDC_RP_CLIENT_SECRET", default="")
OIDC_OP_AUTHORIZATION_ENDPOINT = env("OIDC_OP_AUTHORIZATION_ENDPOINT", default="")
OIDC_OP_TOKEN_ENDPOINT = env("OIDC_OP_TOKEN_ENDPOINT", default="")
OIDC_OP_USER_ENDPOINT = env("OIDC_OP_USER_ENDPOINT", default="")
OIDC_OP_JWKS_ENDPOINT = env("OIDC_OP_JWKS_ENDPOINT", default="")
OIDC_RP_SIGN_ALGO = "RS256"

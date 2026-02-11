"""
Production settings – used on AWS ECS Fargate.

All secrets are read from environment variables (injected via Secrets Manager).
No default values for sensitive settings – the app will fail to start
if required variables are missing. This is intentional.

Usage:
    DJANGO_SETTINGS_MODULE=config.settings.production
"""

import environ

from .base import *  # noqa: F401, F403

env = environ.Env()

# Core

DEBUG = False
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

# Database – RDS PostgreSQL

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

# Security – HTTPS enforced

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Azure AD / OIDC – all required

OIDC_RP_CLIENT_ID = env("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = env("OIDC_RP_CLIENT_SECRET")
OIDC_OP_AUTHORIZATION_ENDPOINT = env("OIDC_OP_AUTHORIZATION_ENDPOINT")
OIDC_OP_TOKEN_ENDPOINT = env("OIDC_OP_TOKEN_ENDPOINT")
OIDC_OP_USER_ENDPOINT = env("OIDC_OP_USER_ENDPOINT")
OIDC_OP_JWKS_ENDPOINT = env("OIDC_OP_JWKS_ENDPOINT")
OIDC_RP_SIGN_ALGO = "RS256"

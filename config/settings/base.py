"""
Gen'X Vision School System — Base Django Settings
==================================================
Sprint:       SPRINT-01
Task:         SPRINT-01 Task 2 — Split Settings Architecture
Traceability: NFR-008 (Maintainability), TBD-001 (Windows 10/11), TBD-002 (Django),
              TBD-003 (Bootstrap/HTMX), TBD-004 (PostgreSQL), TBD-069 (Session 30 min)
Author:       Sprint-01 Implementation Team
Date:         September 2026

This file contains settings that are common to ALL environments.
Environment-specific settings belong in development.py, production.py, or testing.py.
Sensitive values MUST come from environment variables — never hardcoded here.
"""

from pathlib import Path

import environ

# ---------------------------------------------------------------------------
# DIRECTORY REFERENCES
# ---------------------------------------------------------------------------
# BASE_DIR resolves to the repository root (gen'x project/)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ---------------------------------------------------------------------------
# ENVIRONMENT VARIABLE LOADING
# Reads from .env file in BASE_DIR when present; overridden by OS env vars.
# ---------------------------------------------------------------------------
env = environ.Env(
    # Declare types and defaults for environment variables
    DJANGO_DEBUG=(bool, False),
    DJANGO_ALLOWED_HOSTS=(list, ["localhost", "127.0.0.1"]),
    SESSION_COOKIE_AGE=(int, 1800),  # 30 minutes — TBD-069
    SESSION_EXPIRE_AT_BROWSER_CLOSE=(bool, True),
    SESSION_COOKIE_SECURE=(bool, True),
    CSRF_COOKIE_SECURE=(bool, True),
    LOG_LEVEL=(str, "INFO"),
    REPORT_EXPORT_TIMEOUT_SECONDS=(int, 15),  # NFR-018
)

# Read .env file if present (never committed; .gitignore excludes it)
environ.Env.read_env(BASE_DIR / ".env")

# ---------------------------------------------------------------------------
# SECURITY — SECRET KEY
# Must be provided via DJANGO_SECRET_KEY environment variable.
# Never hardcoded. NFR-003.
# ---------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY")

# ---------------------------------------------------------------------------
# APPLICATION DEFINITION
# All installed apps follow the approved monolithic Django modular hierarchy.
# Business apps live under apps/. Only foundation apps are loaded in Sprint-01.
# ---------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    # No third-party apps installed in Sprint-01 beyond django-environ
    # Future sprints will add: crispy_forms, etc.
]

LOCAL_APPS: list[str] = [
    # Sprint-01: No business apps installed yet.
    # Apps will be registered when their sprint creates them:
    #   SPRINT-02: "apps.core"
    #   SPRINT-03: "apps.accounts"
    #   SPRINT-04: "apps.academics"
    #   SPRINT-05: "apps.teachers"
    #   SPRINT-06: "apps.students"
    #   SPRINT-07/08: "apps.attendance"
    #   SPRINT-09/10: "apps.curriculum"
    #   SPRINT-11-13: "apps.finance"
    #   SPRINT-14/15: "apps.exams"
    #   SPRINT-16: (teachers extended)
    #   SPRINT-17: (finance extended)
    #   SPRINT-18: "apps.timetable"
    #   SPRINT-19: "apps.communication"
    #   SPRINT-20: "apps.dashboard"
    #   SPRINT-21: "apps.reports"
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ---------------------------------------------------------------------------
# MIDDLEWARE
# Order is significant in Django. Session and authentication middleware
# must appear before message and CSRF middleware.
# ---------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Sprint-03 will add:
    #   "apps.accounts.middleware.SessionTimeoutMiddleware"
    #   "apps.core.middleware.CurrentUserMiddleware"
]

# ---------------------------------------------------------------------------
# URL CONFIGURATION
# ---------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# ---------------------------------------------------------------------------
# TEMPLATE CONFIGURATION
# Templates live in templates/ at the project root (BASE_DIR/templates/).
# context_processors are required for messages and request access in templates.
# ---------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ---------------------------------------------------------------------------
# WSGI / ASGI APPLICATION
# ---------------------------------------------------------------------------
WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------------------------------------------------------
# DATABASE CONFIGURATION
# PostgreSQL 16 — TBD-004
# All credentials sourced from environment variables. Never hardcoded.
# ---------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": env("DB_NAME", default="genx_school_db"),
        "USER": env("DB_USER", default="postgres"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
        "CONN_MAX_AGE": 60,
        "OPTIONS": {
            "connect_timeout": 10,
        },
    }
}

# ---------------------------------------------------------------------------
# PASSWORD VALIDATION
# NFR-003 — Security. TBD-068 — Password Policy (8 chars minimum).
# Argon2 hashing configured in auth settings below.
# ---------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,  # TBD-068: Minimum 8 characters
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ---------------------------------------------------------------------------
# PASSWORD HASHERS
# NFR-003 — Argon2id as primary hasher; PBKDF2 as fallback.
# argon2-cffi must be installed (requirements/base.txt).
# ---------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",  # Primary — memory-hard
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",  # Fallback
]

# ---------------------------------------------------------------------------
# INTERNATIONALIZATION
# System operates in English and Urdu (C-03).
# ---------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Karachi"  # School operates on PKT (UTC+5)

USE_I18N = True

USE_TZ = True

# ---------------------------------------------------------------------------
# STATIC FILES
# Sprint-01 Task 5: Static asset structure established.
# Django collects static files from STATICFILES_DIRS for development.
# STATIC_ROOT is used by collectstatic for production (WhiteNoise).
# ---------------------------------------------------------------------------
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ---------------------------------------------------------------------------
# MEDIA FILES
# User-uploaded documents (student photos, teacher credentials, expense vouchers).
# TBD-022, TBD-023: Document types and size limits enforced in model validators.
# ---------------------------------------------------------------------------
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------------------------------------------------
# DEFAULT AUTO FIELD
# Use BigAutoField as default for future non-UUID primary keys.
# Core business models in SPRINT-02 will use UUIDModel for explicit UUIDv4 PKs.
# ---------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------------
# SESSION CONFIGURATION
# TBD-069: 30-minute inactivity timeout (1800 seconds).
# NFR-024: Session Security.
# Session timeout middleware will be implemented in SPRINT-03.
# ---------------------------------------------------------------------------
SESSION_COOKIE_AGE = env("SESSION_COOKIE_AGE")  # 1800 seconds = 30 minutes
SESSION_EXPIRE_AT_BROWSER_CLOSE = env("SESSION_EXPIRE_AT_BROWSER_CLOSE")
SESSION_SAVE_EVERY_REQUEST = True  # Refreshes session on every request
SESSION_COOKIE_HTTPONLY = True  # XSS protection
SESSION_COOKIE_SAMESITE = "Lax"  # CSRF protection

# ---------------------------------------------------------------------------
# CSRF CONFIGURATION
# NFR-003 — Security. CSRF protection enabled globally.
# ---------------------------------------------------------------------------
CSRF_COOKIE_HTTPONLY = False  # Needs to be readable by JS for HTMX
CSRF_COOKIE_SAMESITE = "Lax"

# ---------------------------------------------------------------------------
# SECURITY HEADERS
# Base security headers; tightened further in production.py.
# ---------------------------------------------------------------------------
X_FRAME_OPTIONS = "DENY"

# ---------------------------------------------------------------------------
# REDIS & CELERY CONFIGURATION
# Celery broker and result backend use Redis 7.
# Used for: WhatsApp throttled dispatch (TBD-056), auto-absent cron (TBD-012),
#           fee reminders, and dashboard metric caching (NFR-001).
# ---------------------------------------------------------------------------
REDIS_URL = env("REDIS_URL", default="redis://localhost:6379/0")

CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://localhost:6379/1")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True

# ---------------------------------------------------------------------------
# LOGGING CONFIGURATION
# Structured logging for application and security events.
# Log files never committed to version control (.gitignore excludes *.log).
# ---------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs" / "django.log",
            "maxBytes": 1024 * 1024 * 10,  # 10 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": env("LOG_LEVEL"),
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": env("LOG_LEVEL"),
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "genx": {
            "handlers": ["console", "file"],
            "level": env("LOG_LEVEL"),
            "propagate": False,
        },
    },
}

# ---------------------------------------------------------------------------
# REPORT GENERATION SETTINGS
# NFR-018: PDF/Excel export must complete within 15 seconds.
# WeasyPrint and OpenPyXL are used for PDF and Excel generation.
# ---------------------------------------------------------------------------
REPORT_EXPORT_TIMEOUT_SECONDS = env("REPORT_EXPORT_TIMEOUT_SECONDS")

# ---------------------------------------------------------------------------
# BIOMETRIC HARDWARE SETTINGS (LAN Adapter — SPRINT-07)
# TBD-007: ZKTeco device family over LAN.
# TBD-009: SDK Adapter on TCP port 4370.
# Configuration only — no business logic in settings.
# ---------------------------------------------------------------------------
BIOMETRIC_DEVICE_IP = env("BIOMETRIC_DEVICE_IP", default="192.168.1.201")
BIOMETRIC_DEVICE_PORT = env.int("BIOMETRIC_DEVICE_PORT", default=4370)
BIOMETRIC_DEVICE_TIMEOUT = env.int("BIOMETRIC_DEVICE_TIMEOUT", default=5)
BIOMETRIC_SYNC_INTERVAL_SECONDS = env.int("BIOMETRIC_SYNC_INTERVAL_SECONDS", default=60)

# ---------------------------------------------------------------------------
# WHATSAPP CLOUD API SETTINGS (SPRINT-19)
# TBD-008: Official Meta WhatsApp Business API.
# TBD-052: School-owned account and number.
# Zero credentials hardcoded.
# ---------------------------------------------------------------------------
WHATSAPP_API_URL = env("WHATSAPP_API_URL", default="https://graph.facebook.com/v20.0")
WHATSAPP_PHONE_NUMBER_ID = env("WHATSAPP_PHONE_NUMBER_ID", default="")
WHATSAPP_BUSINESS_ACCOUNT_ID = env("WHATSAPP_BUSINESS_ACCOUNT_ID", default="")
WHATSAPP_ACCESS_TOKEN = env("WHATSAPP_ACCESS_TOKEN", default="")
WHATSAPP_WEBHOOK_VERIFY_TOKEN = env("WHATSAPP_WEBHOOK_VERIFY_TOKEN", default="")
WHATSAPP_WEBHOOK_APP_SECRET = env("WHATSAPP_WEBHOOK_APP_SECRET", default="")

# ---------------------------------------------------------------------------
# BACKUP SETTINGS (SPRINT-22)
# TBD-073: Local encrypted backup.
# TBD-074: AES-256 GPG off-site cloud sync.
# ---------------------------------------------------------------------------
BACKUP_LOCAL_PATH = env("BACKUP_LOCAL_PATH", default="./backups/local/")
BACKUP_GPG_RECIPIENT_KEY_ID = env("BACKUP_GPG_RECIPIENT_KEY_ID", default="")
BACKUP_CLOUD_PROVIDER = env("BACKUP_CLOUD_PROVIDER", default="s3")
BACKUP_CLOUD_BUCKET = env("BACKUP_CLOUD_BUCKET", default="genx-school-offsite-backups")

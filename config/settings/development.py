"""
Gen'X Vision School System — Development Settings
==================================================
Sprint:       SPRINT-01
Task:         SPRINT-01 Task 2 — Split Settings Architecture
Traceability: NFR-008 (Maintainability), TBD-001 (Windows 10/11 Desktop)

Development-specific settings that override and extend base.py.
NEVER use these settings in production.
"""

from .base import *  # noqa: F401, F403

# ---------------------------------------------------------------------------
# SECURITY — Development overrides
# DEBUG must be True for development only.
# Never commit DEBUG=True to production.
# ---------------------------------------------------------------------------
DEBUG = env("DJANGO_DEBUG", default=True)  # type: ignore[name-defined]

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1", "0.0.0.0"])  # type: ignore[name-defined]

# Development: do not require HTTPS for session/CSRF cookies
SESSION_COOKIE_SECURE = env("SESSION_COOKIE_SECURE", default=False)  # type: ignore[name-defined]
CSRF_COOKIE_SECURE = env("CSRF_COOKIE_SECURE", default=False)  # type: ignore[name-defined]

# ---------------------------------------------------------------------------
# DEVELOPMENT APPS
# django-debug-toolbar provides SQL query visibility during development.
# Never include in production builds.
# ---------------------------------------------------------------------------
INSTALLED_APPS += [  # type: ignore[name-defined]
    "debug_toolbar",
]

MIDDLEWARE += [  # type: ignore[name-defined]
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# ---------------------------------------------------------------------------
# DEVELOPMENT EMAIL
# Use console backend — emails printed to terminal.
# No real email credentials needed in development.
# ---------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ---------------------------------------------------------------------------
# DEVELOPMENT LOGGING
# More verbose logging to console for development debugging.
# ---------------------------------------------------------------------------
LOGGING["loggers"]["django"]["level"] = "DEBUG"  # type: ignore[index]
LOGGING["loggers"]["genx"]["level"] = "DEBUG"  # type: ignore[index]

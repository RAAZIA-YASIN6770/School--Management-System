"""
Gen'X Vision School System — Production Settings
==================================================
Sprint:       SPRINT-01
Task:         SPRINT-01 Task 2 — Split Settings Architecture
Traceability: NFR-003 (Security), NFR-008 (Maintainability), TBD-005 (On-Premise Server),
              TBD-001 (Windows 10/11)

Production settings that override base.py.
These are the hardened settings for the school's on-premise local server.
All secrets MUST be injected via the server's OS environment variables.
"""

from .base import *  # noqa: F401, F403

# ---------------------------------------------------------------------------
# SECURITY — Production MANDATORY settings
# DEBUG must always be False in production. NFR-003.
# ---------------------------------------------------------------------------
DEBUG = False

# ALLOWED_HOSTS must be set to the school server's IP/hostname.
# Example: ["192.168.1.100", "school.local"]
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")  # type: ignore[name-defined]

# ---------------------------------------------------------------------------
# HTTPS / SECURE TRANSPORT
# Production deployment runs behind HTTPS on the school LAN server.
# TBD-005: On-Premise Local Server.
# ---------------------------------------------------------------------------
SESSION_COOKIE_SECURE = True  # Cookies only over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookie only over HTTPS
SECURE_SSL_REDIRECT = False  # Managed by nginx/gunicorn — not Django redirect
SECURE_HSTS_SECONDS = 31536000  # 1 year HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# ---------------------------------------------------------------------------
# STATIC FILES — WhiteNoise for Production
# WhiteNoise serves compressed static files efficiently without a CDN.
# Run `python manage.py collectstatic` before deployment.
# ---------------------------------------------------------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MIDDLEWARE = (
    [  # type: ignore[name-defined]
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",  # Must be after SecurityMiddleware
    ]
    + MIDDLEWARE[1:]
)  # type: ignore[name-defined]  # Prepend WhiteNoise at position 2

# ---------------------------------------------------------------------------
# EMAIL CONFIGURATION
# Production sends error reports to admins. Configure SMTP via environment.
# ---------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="localhost")  # type: ignore[name-defined]
EMAIL_PORT = env.int("EMAIL_PORT", default=25)  # type: ignore[name-defined]
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)  # type: ignore[name-defined]

# ---------------------------------------------------------------------------
# PRODUCTION LOGGING
# Structured file-based logging with rotation.
# Log files must NOT contain credentials or secret values.
# ---------------------------------------------------------------------------
LOGGING["handlers"]["file"]["level"] = "WARNING"  # type: ignore[index]
LOGGING["root"]["handlers"] = ["console", "file"]  # type: ignore[index]

"""
Gen'X Vision School System — Testing Settings
==============================================
Sprint:       SPRINT-01
Task:         SPRINT-01 Task 2 — Split Settings Architecture (Testing Profile)
Traceability: NFR-008 (Maintainability), NFR-019 (Single Database)

Testing settings used exclusively by the pytest test suite.
Configured in pyproject.toml: DJANGO_SETTINGS_MODULE = "config.settings.testing"

Key testing characteristics:
- Uses the same PostgreSQL 16 database engine (per NFR-019 — no SQLite substitution)
- Runs with --no-migrations per pyproject.toml addopts (tests create tables directly)
- Debug disabled to catch template errors
- Fast password hasher to speed up test execution
"""

from .base import *  # noqa: F401, F403

# ---------------------------------------------------------------------------
# TESTING FLAGS
# ---------------------------------------------------------------------------
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]

# ---------------------------------------------------------------------------
# DATABASE — Testing uses a dedicated test database on the same PostgreSQL 16
# Django automatically creates a test_ prefixed database for test runs.
# Never use SQLite for testing — NFR-019 mandates a single unified relational DB.
# ---------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="genx_school_db"),  # type: ignore[name-defined]
        "USER": env("DB_USER", default="postgres"),  # type: ignore[name-defined]
        "PASSWORD": env("DB_PASSWORD", default="postgres"),  # type: ignore[name-defined]
        "HOST": env("DB_HOST", default="localhost"),  # type: ignore[name-defined]
        "PORT": env("DB_PORT", default="5432"),  # type: ignore[name-defined]
        "TEST": {
            "NAME": "test_genx_school_db",
        },
        "CONN_MAX_AGE": 0,  # No persistent connections in tests
    }
}

# ---------------------------------------------------------------------------
# FAST PASSWORD HASHER FOR TESTS
# Replaces Argon2 with MD5 hasher for testing only — dramatically speeds up
# test suite without compromising security in real environments.
# ---------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# ---------------------------------------------------------------------------
# SESSION — Disable secure cookies for tests (running over HTTP)
# ---------------------------------------------------------------------------
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# ---------------------------------------------------------------------------
# EMAIL — Suppress emails in tests
# ---------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# ---------------------------------------------------------------------------
# CELERY — Always synchronous in tests (tasks execute inline)
# ---------------------------------------------------------------------------
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# ---------------------------------------------------------------------------
# MEDIA — Use temp directory for media files in tests
# ---------------------------------------------------------------------------
import tempfile  # noqa: E402

MEDIA_ROOT = tempfile.mkdtemp()

# ---------------------------------------------------------------------------
# LOGGING — Suppress logging noise during test runs
# ---------------------------------------------------------------------------
LOGGING["root"]["level"] = "CRITICAL"  # type: ignore[index]

"""
Gen'X Vision School System — ASGI Configuration
=================================================
Sprint:       SPRINT-01
Traceability: NFR-008 (Maintainability), NFR-020 (Future Expansion)

ASGI application entry point for Django.
Currently unused in Sprint-01 (system uses WSGI/Gunicorn for production).
Provided for future expansion compatibility (e.g., WebSocket channels).
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

application = get_asgi_application()

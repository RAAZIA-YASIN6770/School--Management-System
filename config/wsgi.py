"""
Gen'X Vision School System — WSGI Configuration
=================================================
Sprint:       SPRINT-01
Traceability: NFR-008 (Maintainability), TBD-005 (On-Premise Server with Gunicorn)

WSGI application for Django.
Production: served by Gunicorn under systemd supervision.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

application = get_wsgi_application()

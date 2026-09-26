"""
Gen'X Vision School System — Application Views (Foundation)
=============================================================
Sprint:       SPRINT-01
Task:         Sprint-01 Task 13 — Health / Basic System Verification
Traceability: NFR-008 (Maintainability), NFR-019 (Single Database)

Contains only the minimal infrastructure health check view.
Business views belong to their respective authorized sprint apps.

SECURITY NOTE:
This health check exposes NO sensitive information:
  - No passwords
  - No secret keys
  - No API credentials
  - No internal security configuration
  - No detailed stack traces
"""

import logging

from django.db import OperationalError, connection
from django.http import JsonResponse
from django.views import View

logger = logging.getLogger("genx")


class HealthCheckView(View):
    """
    Minimal system health check endpoint.

    Returns a JSON response indicating:
    - Django application is running (HTTP 200 / "status": "ok")
    - PostgreSQL database connectivity status

    On database failure, returns HTTP 503 with:
    - "status": "degraded"
    - "database": "unavailable"

    NEVER returns sensitive data, credentials, or configuration internals.
    """

    def get(self, request, *args, **kwargs):
        health_data = {
            "system": "Gen'X Vision School System",
            "status": "ok",
            "django": "running",
            "database": "unknown",
        }

        # Verify PostgreSQL connectivity
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()
            health_data["database"] = "connected"
            http_status = 200
        except OperationalError:
            logger.warning("Health check: PostgreSQL database connection failed.")
            health_data["database"] = "unavailable"
            health_data["status"] = "degraded"
            http_status = 503

        return JsonResponse(health_data, status=http_status)

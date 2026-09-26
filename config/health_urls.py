"""
Gen'X Vision School System — Health Check URLs
===============================================
Sprint:       SPRINT-01
Task:         Sprint-01 Task 13 — Health / Basic System Verification
Traceability: NFR-008 (Maintainability), NFR-019 (Single Database)

Provides a minimal technical health check endpoint.
Verifies Django is running and PostgreSQL connection is available.
DOES NOT expose: passwords, secret keys, API credentials, or internal security info.
"""

from django.urls import path

from config.views import HealthCheckView

urlpatterns = [
    path("", HealthCheckView.as_view(), name="health-check"),
]

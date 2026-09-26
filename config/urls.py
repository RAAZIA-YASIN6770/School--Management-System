"""
Gen'X Vision School System — Root URL Configuration
====================================================
Sprint:       SPRINT-01
Task:         SPRINT-01 Task (URL Foundation)
Traceability: NFR-008 (Maintainability), NFR-020 (Future Expansion Architecture)

This file defines the root URL structure.
Sprint-01 provides only the foundation:
  - Admin interface
  - Health check endpoint
  - Static/media file serving in development

Business module URLs will be added in their respective authorized sprints:
  SPRINT-03: accounts/ (authentication)
  SPRINT-04: academics/ (class management)
  SPRINT-05: teachers/
  SPRINT-06: students/
  SPRINT-07/08: attendance/
  SPRINT-09/10: curriculum/
  SPRINT-11-13: finance/
  SPRINT-14/15: exams/
  SPRINT-18: timetable/
  SPRINT-19: communication/
  SPRINT-20: dashboard/
  SPRINT-21: reports/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# ---------------------------------------------------------------------------
# URL PATTERNS — Sprint-01 Foundation
# ---------------------------------------------------------------------------
urlpatterns = [
    # Django Admin — accessible to authorized admin users
    path("admin/", admin.site.urls),
    # System health check — Sprint-01 infrastructure verification endpoint
    path("health/", include("config.health_urls")),
]

# ---------------------------------------------------------------------------
# DEVELOPMENT-ONLY URL ADDITIONS
# ---------------------------------------------------------------------------
if settings.DEBUG:
    # Django Debug Toolbar (development only)
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

    # Serve media files in development (production uses storage backend)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Serve static files in development (handled by WhiteNoise in production)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

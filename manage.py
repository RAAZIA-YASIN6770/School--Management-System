#!/usr/bin/env python
"""
Gen'X Vision School System — Django Management Script
======================================================
Sprint:       SPRINT-01
Traceability: NFR-008 (Maintainability)

Standard Django management entry point.
Default settings profile: config.settings.development

For production use:
  DJANGO_SETTINGS_MODULE=config.settings.production python manage.py <command>

For test runs:
  DJANGO_SETTINGS_MODULE=config.settings.testing python manage.py test
  (or use pytest directly — configured in pyproject.toml)
"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

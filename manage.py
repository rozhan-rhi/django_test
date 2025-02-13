#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

def start_celery():
    """Start Celery in the background when running Django"""
    try:
        subprocess.Popen(["celery", "-A", "core", "worker", "--loglevel=info"])
    except Exception as e:
        print(f"Could not start Celery: {e}")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

    if "runserver" in sys.argv:  # Start Celery only when running Django server
        start_celery()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

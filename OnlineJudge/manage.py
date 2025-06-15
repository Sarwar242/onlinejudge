#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from datetime import timedelta

# Add monkey patch for smart_text
import django.utils.encoding
if not hasattr(django.utils.encoding, 'smart_text'):
    django.utils.encoding.smart_text = django.utils.encoding.smart_str

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineJudge.settings')
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # ...
}
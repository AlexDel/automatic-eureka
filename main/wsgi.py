"""
WSGI config for inbox_receipt_backend project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
mode = os.getenv('MODE', 'development')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'main.settings.{mode}')

application = get_wsgi_application()

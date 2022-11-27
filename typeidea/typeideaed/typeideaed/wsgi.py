"""
WSGI config for typeideaed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('TYPEIDEAED_PROFILE', 'product')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeideaed.settings.%s' % profile)

application = get_wsgi_application()

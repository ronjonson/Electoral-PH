"""
WSGI config for electoral project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<<< HEAD:results/results/wsgi.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "results.settings")
========
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electoral.settings")
>>>>>>>> 078ccd3e7244a36c19106e4559875cd53b8a67fc:electoral/electoral/wsgi.py

application = get_wsgi_application()

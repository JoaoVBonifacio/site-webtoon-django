"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# config/wsgi.py (VERSÃO FINAL)
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Pega a aplicação Django padrão e DEPOIS a envelopa com o WhiteNoise
application = get_wsgi_application()
from whitenoise import WhiteNoise
application = WhiteNoise(application)

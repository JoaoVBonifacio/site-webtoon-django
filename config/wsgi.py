"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# config/wsgi.py (VERSÃO NOVA E CORRIGIDA)
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Pega a aplicação Django padrão
application = get_wsgi_application()

# Importa o WhiteNoise e "envelopa" a aplicação com ele
from whitenoise import WhiteNoise
application = WhiteNoise(application)

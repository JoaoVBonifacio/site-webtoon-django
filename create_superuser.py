# create_superuser.py

import os
import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Pega as informações das variáveis de ambiente
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

# Cria o superusuário apenas se ele não existir
if not User.objects.filter(email=email).exists():
    print(f"Criando superusuário com o email: {email}")
    User.objects.create_superuser(
        username=email, # Usamos o email como username
        email=email,
        password=password
    )
else:
    print("Superusuário já existe.")
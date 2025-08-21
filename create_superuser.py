# create_superuser.py (versão 2.0)

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if email and password:
    try:
        user = User.objects.get(email=email)
        print("Superusuário já existe. Atualizando a senha...")
        user.set_password(password)
        user.save()
    except User.DoesNotExist:
        print(f"Criando superusuário com o email: {email}")
        User.objects.create_superuser(
            username=email,
            email=email,
            password=password
        )
else:
    print("Variáveis de ambiente do superusuário não definidas. Pulando.")
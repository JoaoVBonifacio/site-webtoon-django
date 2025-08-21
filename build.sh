#!/bin/bash

# Instala as dependências
pip install -r requirements.txt

# Roda as migrações do banco de dados
python manage.py migrate

# Cria o superusuário usando nosso novo script
python create_superuser.py
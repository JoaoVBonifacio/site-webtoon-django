#!/bin/bash

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput

# Roda as migrações do banco de dados
python manage.py migrate
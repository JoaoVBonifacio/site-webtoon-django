#!/bin/bash

echo "Build script iniciado..."

# Coleta os arquivos estáticos usando python3
python3 manage.py collectstatic --noinput

# Roda as migrações do banco de dados usando python3
python3 manage.py migrate

echo "Build script finalizado."
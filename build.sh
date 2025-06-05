#!/bin/bash

echo ">>> Instalando dependências"

echo ">>> Criando banco de dados (se necessário)"
pip install -r requirements.txt

echo ">>> Criando tabelas no banco"
python -c "from app_factory import init, db; app = init(); from models import *; with app.app_context(): db.create_all()"

echo ">>> Preenchendo banco"
python init_db.py

echo ">>> Preenchendo banco com dados estáticos e CSV"
python -c "from importar_csv import carregar_csv; carregar_csv()"
python -c "from preenche_estatico import preenche_estatico; preenche_estatico()"
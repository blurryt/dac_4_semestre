#!/bin/bash

echo ">>> Instalando dependências"

echo ">>> Criando banco de dados (se necessário)"
pip install -r requirements.txt

echo ">>> Criando banco de dados (se necessário)"
python -c "from app import db, app; db.create_all(app=app)"

echo ">>> Preenchendo banco com dados estáticos e CSV"
python -c "from importar_csv import carregar_csv; carregar_csv()"
python -c "from preenche_estatico import preenche_estatico; preenche_estatico()"
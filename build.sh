#!/bin/bash

echo ">>> Instalando dependências"

echo ">>> Criando banco de dados (se necessário)"
pip install -r requirements.txt

echo ">>> Inicializando banco de dados"
python init_deploy.py

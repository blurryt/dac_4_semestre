from app_factory import init_app, db
from models import *
from importar_csv import carregar_csv
from preenche_estatico import preenche_estatico

app = init_app()

with app.app_context():
    print(">>> Criando tabelas no banco")
    db.create_all()

    print(">>> Preenchendo banco (estático)")
    preenche_estatico()

    print(">>> Preenchendo banco (escolas)")
    carregar_csv()

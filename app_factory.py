from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import getenv
from dotenv import load_dotenv


carregamento_feito = False
load_dotenv()
db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    # @app.before_request
    # def inicializar_banco():
    #     global carregamento_feito
    #     if not carregamento_feito:
    #         from models import Escola
    #         from importar_csv import carregar_csv
    #         from preenche_estatico import preenche_estatico 
            
    #         if not Escola.query.first():
    #             print(">> Populando banco pela primeira vez...")
    #             carregar_csv()
    #             preenche_estatico()
    #         carregamento_feito = True
    return app

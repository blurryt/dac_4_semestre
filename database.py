from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv
from importar_csv import importar_csv
from models import Escola
from preenche_estatico import preenche_estatico


load_dotenv()

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    @app.before_first_request
    def inicializar_banco():
        if not Escola.query.first():
            print(">> Populando banco pela primeira vez...")
            importar_csv()
            preenche_estatico()

    return app

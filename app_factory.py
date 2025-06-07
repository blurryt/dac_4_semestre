from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import getenv
from dotenv import load_dotenv
from flask_cors import CORS


carregamento_feito = False
load_dotenv()
db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app

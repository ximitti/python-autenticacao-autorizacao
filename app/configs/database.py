from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ---------------------------------

def init_app(app: Flask):
    db = SQLAlchemy()
    db.init_app(app)
    app.db = db


    # importar a model aqui

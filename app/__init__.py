from flask import Flask
from environs import Env

from app.configs import database, migrations
from app import views

# ---------------------------------

env = Env()
env.read_env()

# ---------------------------------


def create_app() -> Flask:

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] = env("JWT_SECRET_KEY")

    database.init_app(app)
    migrations.init_app(app)
    views.init_app(app)

    @app.get("/")
    def index():
        return "<h1>Acessar /api/signup para se cadastrar</h1>"

    return app

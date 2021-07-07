from flask import Flask
from flask_migrate import Migrate

# -------------------------------------

def init_app(app: Flask):
    mg = Migrate()
    mg.init_app(app, app.db)

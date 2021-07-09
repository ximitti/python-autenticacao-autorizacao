from flask import Flask
from flask_jwt_extended import JWTManager

# -------------------------------------------

token = JWTManager()

# -------------------------------------------


def ini_app(app: Flask):

    token.init_app(app)

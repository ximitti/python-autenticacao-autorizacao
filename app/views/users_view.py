from flask import Flask, Blueprint

# -----------------------------------------

bp = Blueprint('bp_users', __name__, url_prefix='/api')

# -----------------------------------------

@bp.get('/')
def index():
    ...

@bp.post('/signup')
def signup():
    ...

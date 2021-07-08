from flask import Blueprint
from flask_httpauth import HTTPBasicAuth

# -------------------------------------

bp = Blueprint("bp_admin", __name__, url_prefix="/admin")
auth = HTTPBasicAuth()

# -------------------------------------


@auth.verify_password
def verify_password(username, password):
    # buscar usuário no banco e checar o password
    if username:
        print(username, password)
        return username


@bp.get("/")
@auth.login_required
def index():
    # retornar um json com o API Key do usuário
    return f"<h1>Olá {auth.current_user()}!"

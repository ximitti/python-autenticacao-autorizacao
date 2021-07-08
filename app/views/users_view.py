from flask import Blueprint, request, render_template
from flask_httpauth import HTTPTokenAuth

# -----------------------------------------

bp = Blueprint("bp_users", __name__, url_prefix="/api")
auth = HTTPTokenAuth(scheme="Bearer")

# -----------------------------------------


@auth.verify_token
def verify_token(token):
    # usar o token para buscar o usuário
    # retornar o usuário atrelado ao token
    ...


@bp.get("/signup")
def form_register():
    # renderizar o formulário de cadastro de usuário
    return render_template("/users/form.html")


@bp.post("/")
def signup():
    # cadastrar o usuário e gerar um api key
    # gerar um password hash
    # renderizar as informações do usuário criado

    user = dict(request.form)

    print(dict(request.form))
    return render_template("/users/index.html", user=user)

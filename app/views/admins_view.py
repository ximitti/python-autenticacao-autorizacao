from flask import Blueprint
from flask_httpauth import HTTPDigestAuth
from http import HTTPStatus
from werkzeug.security import check_password_hash

from app.models.user_model import UserModel

from app.services.users_service import get_user

# -------------------------------------

bp = Blueprint("bp_admin", __name__, url_prefix="/admin")
auth = HTTPDigestAuth()

# -------------------------------------


@auth.get_password
def get_password(email):

    user: UserModel = get_user(email)
    if user:
        print(email)
        return user.password_hash

    return None


@bp.get("/")
@auth.login_required
def index():
    return {"token": auth.current_user()}, HTTPStatus.OK


@bp.get("/logout")
@auth.login_required
def logout():
    return "<h1>Deslogado</h1>", HTTPStatus.UNAUTHORIZED

from flask import Blueprint
from flask_httpauth import HTTPDigestAuth
from http import HTTPStatus

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
        return user.password

    return None


@bp.get("/")
@auth.login_required
def index() -> tuple:
    user: UserModel = get_user(auth.current_user())
    return (
        {"token": user.api_key},
        HTTPStatus.OK,
    )


@bp.get("/logout")
@auth.login_required
def logout() -> tuple:
    return (
        "<h1>Deslogado</h1>",
        HTTPStatus.UNAUTHORIZED,
    )

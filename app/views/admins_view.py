from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from http import HTTPStatus
from werkzeug.security import check_password_hash

from app.models.user_model import UserModel

# -------------------------------------

bp = Blueprint("bp_admin", __name__, url_prefix="/admin")
auth = HTTPBasicAuth()

# -------------------------------------


@auth.verify_password
def verify_password(email, password):
    user: UserModel = UserModel.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return user.api_key


@bp.get("/")
@auth.login_required
def index():
    return {"token": auth.current_user()}, HTTPStatus.OK


@bp.get("/logout")
@auth.login_required
def logout():
    return "<h1>Deslogado</h1>", HTTPStatus.UNAUTHORIZED

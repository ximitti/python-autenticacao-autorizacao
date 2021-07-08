from flask import Blueprint, request, render_template, current_app
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash
from http import HTTPStatus
import secrets

from app.models.user_model import UserModel

# -----------------------------------------

bp = Blueprint("bp_users", __name__, url_prefix="/api")
auth = HTTPTokenAuth(scheme="Bearer")

# -----------------------------------------


@auth.verify_token
def verify_token(token):
    user: UserModel = UserModel.query.filter_by(api_key=token).first()
    if user:
        return user


@bp.get("/signup")
def form_signup():

    return render_template("/users/form.html")


@bp.post("/signup")
def user_register():
    session = current_app.db.session

    user_request = dict(request.form)

    password = user_request.pop("password")
    user_request["password_hash"] = generate_password_hash(password)
    user_request["api_key"] = secrets.token_urlsafe(32)

    user = UserModel(**user_request)

    session.add(user)
    session.commit()

    return render_template("/users/index.html", user=user_request)


@bp.get("/")
@auth.login_required
def get_user():

    return {"user": auth.current_user()}, HTTPStatus.OK


@bp.put("/")
@auth.login_required
def change_user():
    session = current_app.db.session
    allowed_keys = ["name", "last_name", "email", "password"]

    payload = request.get_json()
    for key in payload.keys():
        if key not in allowed_keys:
            return {"forbidden_key": key}, HTTPStatus.FORBIDDEN

    if payload.get("password"):
        password = payload.pop("password")
        payload["password_hash"] = generate_password_hash(password)

    user: UserModel = auth.current_user()

    for key, value in payload.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()

    return {"user": user}, HTTPStatus.ACCEPTED


@bp.delete("/")
@auth.login_required
def delete_user():
    session = current_app.db.session

    user: UserModel = auth.current_user()

    session.delete(user)
    session.commit()

    return "No content", HTTPStatus.NO_CONTENT

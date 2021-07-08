from flask import Blueprint, request, render_template, current_app
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
import secrets

from app.services.helpers import add_commit, delete_commit
from app.services.users_service import create_user, get_user_token, update_user

from app.models.user_model import UserModel

from app.exc import AllowedKeysError, RequiredKeysError

# -----------------------------------------

bp = Blueprint("bp_users", __name__, url_prefix="/api")
auth = HTTPTokenAuth(scheme="Bearer")

# -----------------------------------------


@auth.verify_token
def verify_token(token: str):
    user: UserModel = get_user_token(token)
    if user:
        return user


@bp.get("/signup")
def form_signup() -> tuple:

    return (
        render_template("/users/form.html"),
        HTTPStatus.OK,
    )


@bp.post("/signup")
def user_register() -> tuple:

    try:
        user: Model = create_user(dict(request.form))

        return (
            render_template("/users/index.html", user=user),
            HTTPStatus.CREATED,
        )

    except RequiredKeysError as error:
        return error.message

    except IntegrityError as error:
        return (
            {"error": f"duplicate key: {error.params['email']}"},
            HTTPStatus.BAD_REQUEST,
        )


@bp.get("/")
@auth.login_required
def get_user() -> tuple:

    return (
        {"user": auth.current_user()},
        HTTPStatus.OK,
    )


@bp.put("/")
@auth.login_required
def update() -> tuple:

    try:
        user: UserModel = update_user(request.get_json(), auth.current_user())
        print(user)

        return (
            {"user": user},
            HTTPStatus.ACCEPTED,
        )

    except AllowedKeysError as error:
        return error.message

    except IntegrityError as error:
        return (
            {"error": f"duplicate key: {error.params['email']}"},
            HTTPStatus.BAD_REQUEST,
        )


@bp.delete("/")
@auth.login_required
def delete_user() -> tuple:

    user: UserModel = auth.current_user()

    delete_commit(user)

    return (
        "No content",
        HTTPStatus.NO_CONTENT,
    )

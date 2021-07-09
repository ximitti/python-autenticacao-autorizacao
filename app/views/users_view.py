from flask import Blueprint, request, render_template, jsonify
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.services.users_service import (
    create_user,
    get_user,
    update_user,
    delete_user,
    check_user_credential,
)

from app.models.user_model import UserModel

from app.exc import AllowedKeysError, RequiredKeysError

# -----------------------------------------

bp = Blueprint("bp_users", __name__, url_prefix="/api")

# -----------------------------------------


@bp.get("/signup")
def form() -> tuple:

    return (
        render_template("/users/form.html"),
        HTTPStatus.OK,
    )


@bp.post("/signup")
def register() -> tuple:

    try:
        user: UserModel = create_user(dict(request.form))

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


@bp.post("/login")
def login_user() -> tuple:

    if request.is_json:
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        user: UserModel = check_user_credential(email, password)
        if user:
            return (
                jsonify(access_token=create_access_token(identity=user.email)),
                HTTPStatus.ACCEPTED,
            )

    return (
        {"message": "Bad email or password"},
        HTTPStatus.UNAUTHORIZED,
    )


@bp.get("/")
@jwt_required()
def getter() -> tuple:

    return (
        {"user": get_user(get_jwt_identity())},
        HTTPStatus.OK,
    )


@bp.put("/")
@jwt_required()
def setter() -> tuple:

    try:
        user: UserModel = update_user(request.get_json(), get_user(get_jwt_identity()))

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
@jwt_required()
def remove_user() -> tuple:

    delete_user(get_user(get_jwt_identity()))

    return (
        "No content",
        HTTPStatus.NO_CONTENT,
    )

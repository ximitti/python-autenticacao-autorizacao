from app.models.user_model import UserModel
import secrets

from .helpers import (
    add_commit,
    delete_commit,
    verify_allowed_keys,
    verify_required_keys,
)
from app.exc import AllowedKeysError, RequiredKeysError

# ----------------------------------------


def create_user(payload: dict) -> UserModel:

    blank_fields = verify_required_keys(payload)
    if blank_fields:
        raise RequiredKeysError(payload, blank_fields)

    payload["api_key"] = secrets.token_urlsafe(32)

    user: UserModel = UserModel(**payload)

    add_commit(user)

    return user


def get_user_token(token: str) -> UserModel:

    return UserModel.query.filter_by(api_key=token).first()


def update_user(payload: dict, user_to_change: UserModel) -> UserModel:
    allowed_keys = ["name", "last_name", "email", "password"]

    if verify_allowed_keys(payload, allowed_keys):
        raise AllowedKeysError(payload, allowed_keys)

    for key, value in payload.items():
        setattr(user_to_change, key, value)

    add_commit(user_to_change)

    return user_to_change


def get_user(email: str) -> UserModel:
    return UserModel.query.filter_by(email=email).first()


def delete_user(user: UserModel) -> None:
    delete_commit(user)

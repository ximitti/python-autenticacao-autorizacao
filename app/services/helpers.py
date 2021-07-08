from flask import current_app
from flask_sqlalchemy import Model

# ----------------------------------------


def add_commit(model: Model):
    session = current_app.db.session

    session.add(model)
    session.commit()


def delete_commit(model: Model):
    session = current_app.db.session

    session.delete(model)
    session.commit()


def verify_required_keys(payload: dict) -> list:

    return [key for key, value in payload.items() if not value]


def verify_allowed_keys(payload: dict, allowed_keys: list) -> list:
    payload_keys = payload.keys()

    return [key for key in payload_keys if key not in allowed_keys]

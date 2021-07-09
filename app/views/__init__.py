from flask import Flask

# ----------------------------------


def init_app(app: Flask):

    from .users_view import bp as bp_users

    app.register_blueprint(bp_users)

from flask import Flask

# ----------------------------------


def init_app(app: Flask):

    from .users_view import bp as bp_users

    app.register_blueprint(bp_users)

    from .admins_view import bp as bp_admins

    app.register_blueprint(bp_admins)

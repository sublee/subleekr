from functools import wraps
from flask import *


__all__ = "www", "docs", "ubiq",


def FlaskModule(*args, **kwargs):
    """This is almost same as :class:`flask.Module`. But the module, which is
    an instance of this will serve :file:`"/static/favicon.ico"` file when
    somebody requests `/favicon.ico`.
    """
    app = Module(*args, **kwargs)
    @app.route("/favicon.ico")
    def favicon():
        return app.send_static_file("favicon.ico")
    return app


def check_auth(username, password):
    try:
        from subleekr.auth import USERS, encrypt
        return username in USERS and encrypt(password) == USERS[username]
    except ImportError:
        return False


def requires_auth(f):
    """Decorated function will need authenticate."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            headers = {"WWW-Authenticate": 'Basic realm="Login Required"'}
            return Response(status=401, headers=headers)
        return f(*args, **kwargs)
    return decorated


from functools import wraps
from flask import *
from subleekr.auth import check


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


def requires_auth(f):
    """Decorated function will need authenticate."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check(auth.username, auth.password):
            headers = {"WWW-Authenticate": 'Basic realm="Login Required"'}
            return Response(status=401, headers=headers)
        return f(*args, **kwargs)
    return decorated


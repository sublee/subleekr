import os.path
from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy


CONFIG_FILEPATH = os.path.join(os.path.dirname(__file__), "../config.cfg")


def auto_register_modules(app):
    """Registers modules from :mod:`subleekr` to application."""
    import subleekr
    for modname in subleekr.__modules__:
        __import__("{0}.{1}".format(subleekr.__name__, modname))
        module = getattr(subleekr, modname)
        module.app.super_app = app
        app.register_module(module.app)


app = Flask(__name__)
try:
    app.config.from_pyfile(CONFIG_FILEPATH)
except IOError:
    pass
auto_register_modules(app)
app.db = SQLAlchemy(app)


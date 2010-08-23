from werkzeug.contrib.fixers import ProxyFix
from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
import conf


def auto_register_modules(app):
    import subleekr
    for modname in subleekr.__all__:
        __import__("{0}.{1}".format(subleekr.__name__, modname))
        module = getattr(subleekr, modname)
        module.app.super_app = app
        app.register_module(module.app)


app = Flask(__name__)
app.config.from_object(conf)
app.wsgi_app = ProxyFix(app.wsgi_app)
auto_register_modules(app)
app.db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host=conf.HOST, port=conf.PORT)


from werkzeug.contrib.fixers import ProxyFix
from subleekr.app import create_app


if __name__ == "__main__":
    app = create_app()
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host="0.0.0.0", port=8080)


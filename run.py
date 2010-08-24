from meinheld import server
from werkzeug.contrib.fixers import ProxyFix
from subleekr.app import app


if __name__ == "__main__":
    #server.listen(("0.0.0.0", 8080))
    #server.run(app)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host="0.0.0.0", port=8080)


import os
from flask import render_template
from subleekr import FlaskModule, requires_auth
from subleekr.browse.models import Entry


app = FlaskModule(__name__, subdomain="browse")


@app.route("/<path:path>")
@app.route("/")
@requires_auth
def browse(path="."):
    entries = (Entry(name, path) for name in os.listdir(path))
    return render_template("browse/index.html", entries=entries)


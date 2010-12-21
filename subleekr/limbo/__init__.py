from flask import render_template
from subleekr import FlaskModule


app = FlaskModule(__name__, subdomain="limbo")


@app.route("/")
def index():
    return render_template("limbo/index.html")

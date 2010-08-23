import os.path
import datetime
from functools import wraps
from flask import *
from subleekr import FlaskModule, requires_auth


app = FlaskModule(__name__, subdomain="ubiq")


__session__ = None
def session():
    global __session__
    if not __session__:
        __session__ = app.super_app.db.session
    return __session__


@app.route("/")
def index():
    return render_template("ubiq/index.html")


@app.route("/status", methods=["GET"])
@requires_auth
def status():
    from subleekr.ubiq.models import Status
    log = Status.query.filter(Status.brightness != None) \
                      .filter(Status.temperature != None) \
                      .order_by(Status.logged_at.desc()).all()
    return render_template("ubiq/status.html", log=log)


@app.route("/status", methods=["POST"])
@requires_auth
def log_status():
    from subleekr.ubiq.models import Status
    brightness = request.form.get("brightness", type=int)
    temperature = request.form.get("temperature", type=int)
    new_status = Status(brightness, temperature)
    session().add(new_status)
    session().commit()
    return redirect(url_for("status"), 302)


@app.after_request
def shutdown_session(response):
    session().remove()
    return response


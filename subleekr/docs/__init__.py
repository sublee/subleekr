import os.path
from flask import *
from subleekr import FlaskModule
from subleekr.docs.conf import *


app = FlaskModule(__name__, subdomain="docs")


@app.route("/")
def index():
    return render_template("docs/index.html")


#@app.app_errorhandler(404)
#def notfound(error):
#    return render_template("docs/error.html", error=error)


@app.route("/<path:path>")
def doc(path):
    nodes = path.split("/")
    docdir = []
    filepath = []
    found = False
    for node in nodes:
        if not found:
            docdir.append(node)
            docpath = os.path.join(*tuple([LAB_DIR] + docdir + [DOC_DIR]))
            if os.path.isdir(docpath):
                found = True
        elif node:
            filepath.append(node)
    if not found:
        # does not found document.
        return abort(404)
    elif not filepath:
        if not path.endswith("/"):
            # when path is directory but it does not end with slash.
            return redirect(url_for("doc", path=path + "/"))
        else:
            # add index file name if path is directory
            filepath.append(INDEX_FILE)
    elif filepath[-1] == INDEX_FILE:
        # when path ends with index file name
        return redirect(url_for("doc", path="/".join(docdir + filepath[:-1])))
    path = os.path.join(docpath, *tuple(filepath))
    if os.path.isfile(path):
        # static serve
        return send_from_directory(docpath, os.path.join(*tuple(filepath)))
    else:
        return abort(404)


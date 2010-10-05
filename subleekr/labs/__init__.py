import os.path
import inspect
from flask import Module, url_for
from flaskext.autoindex import *
from subleekr import FlaskModule


browse_root = os.path.join(os.path.expanduser("~"), "labs")
app = FlaskModule(__name__, subdomain="labs")
idx = AutoIndex(app, browse_root)


def get_favicon(ent):
    favicon_paths = "favicon.ico", "resources/favicon.ico", \
                    "artwork/favicon.ico", "static/favicon.ico", \
                    "docs/_static/favicon.ico"
    favicon_paths = sorted(favicon_paths,
                           lambda x, y: -cmp(x.count("/"), y.count("/")))
    if type(ent) is Directory and ent.name != "build":
        for favicon_path in favicon_paths:
            dirname = os.path.dirname(favicon_path)
            if dirname and ent.path.endswith(dirname):
                return False
            elif favicon_path in ent:
                return url_for("autoindex",
                               path=os.path.join(ent.path, favicon_path))
    return False


idx.add_icon_rule("folder_brick.png", dirname="forks")
idx.add_icon_rule("/favicon.ico", cls=RootDirectory)
idx.add_icon_rule("http://sublee.kr/favicon.ico", dirname="subleekr")
idx.add_icon_rule(get_favicon)


@app.route("/")
@app.route("/<path:path>")
def autoindex(path="."):
    return idx.render_autoindex(path)


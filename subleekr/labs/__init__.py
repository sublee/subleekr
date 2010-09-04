import os.path
from flask import Module
from flaskext.autoindex import AutoIndexModule, RootFolder, Folder
from subleekr import FlaskModule


browse_root = os.path.join(os.path.expanduser("~"), "labs")
app = FlaskModule(__name__, subdomain="labs")
idx = AutoIndexModule(app, browse_root)


def get_favicon(ent):
    favicon_paths = "favicon.ico", "resources/favicon.ico", \
                    "artwork/favicon.ico", "static/favicon.ico", \
                    "docs/_static/favicon.ico"
    favicon_paths = sorted(favicon_paths,
                           lambda x, y: -cmp(x.count("/"), y.count("/")))
    if type(ent) is Folder and ent.name != "build":
        for favicon_path in favicon_paths:
            dirname = os.path.dirname(favicon_path)
            if dirname and ent.path.endswith(dirname):
                return False
            favicon = os.path.join(ent.path, favicon_path)
            if os.path.isfile(os.path.join(ent.root, favicon)):
                return "/" + favicon
    return False


idx.add_icon_rule("folder_brick.png", foldername="forks")
idx.add_icon_rule("/favicon.ico", cls=RootFolder)
idx.add_icon_rule("http://sublee.kr/favicon.ico", foldername="subleekr")
idx.add_icon_rule(get_favicon)


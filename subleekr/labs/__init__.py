import os.path
from flask import Module
from flaskext.autoindex import AutoIndexModule
from subleekr import FlaskModule


browse_root = os.path.join(os.path.expanduser("~"), "labs")
app = FlaskModule(__name__, subdomain="labs")
idx = AutoIndexModule(app, browse_root)


idx.add_icon_rule("folder_brick.png", foldername="forks")


import os.path
from flask import Module
from flaskext.autoindex import AutoIndexModule


browse_root = os.path.join(os.path.expanduser("~"), "lab")
app = Module(__name__, subdomain="browse")
AutoIndexModule(app, browse_root)


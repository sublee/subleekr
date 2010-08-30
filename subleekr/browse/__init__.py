import os.path
from flaskext.autoindex import AutoIndex


ROOT = os.path.join(os.path.expanduser("~"), "lab")
app = AutoIndex(__name__, browse_root=ROOT, subdomain="browse")


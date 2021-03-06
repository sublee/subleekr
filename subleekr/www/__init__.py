"""
                  ##
              ####  ##
            ######  ####
          ##    ##  ######
        ####  ##  ########
        ######    ##########
        ##      ############
          ######    ########
        ######      ######  ##
        ######    ######  ####
      ##############    ######
      ############    ##    ##
      ############  ####    ##
      ############  ##########
        ############  ######
              ##########

sublee's homepage. <http://sublee.kr/>
                  From August 25, 2010
"""
from flask import render_template
from subleekr import FlaskModule
from subleekr.www.models import Site


app = FlaskModule(__name__)


@app.route("/")
def index():
    from subleekr.www.sites import SITES
    result = {"categorized_sites": SITES,
              "duration": 70}
    return render_template("www/index.html", **result)


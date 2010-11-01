# vim: set ts=2 sts=2 sw=2:
from subleekr.www.models import Site


SITES = [
  ("internals", [
    Site("sublee.kr",
         "http://sublee.kr/",
         "Just here",
         icon=True),
    Site("labs.sublee.kr",
         "http://labs.sublee.kr/",
         "My laboratory",
         icon=True),
    Site("readme.sublee.kr",
         "http://readme.sublee.kr/",
         "My blog",
         icon="http://lab.sublee.kr/favicons/readme.sublee.kr.ico"),
    Site("docs.sublee.kr",
         "http://docs.sublee.kr/",
         "The documentations in my laboratory",
         icon=True),
    Site("me2apps.sublee.kr",
         "http://me2apps.sublee.kr/",
         "Applications(developed by me) for me2DAY",
         icon=True),
    Site("ubiq.sublee.kr",
         "http://ubiq.sublee.kr/",
         "The ubiquitous system for my personal room",
         icon="/static/favicon.ico"),
    Site("limbo.sublee.kr",
         "http://limbo.sublee.kr/",
         "The virtual server maintained by me",
         icon=True),
#    Site("history.sublee.kr",
#         "http://history.sublee.kr/",
#         "The history of my hompages",
#         icon="http://lab.sublee.kr/favicons/history.sublee.kr.ico"),
#    Site("hire.sublee.kr",
#         "http://hire.sublee.kr/",
#         "The history of my hompages",
#         icon="http://lab.sublee.kr/favicons/hire.sublee.kr.ico"),
#    Site("game.sublee.kr",
#         "http://game.sublee.kr/",
#         "The history of my hompages,
#         icon="http://lab.sublee.kr/favicons/game.sublee.kr.ico"),
  ]),
  ("projects", [
    Site("jDoctest",
         "http://jdoctest.lunant.org/",
         "An interactive JavaScript test framework",
         icon="http://jdoctest.lunant.org/_static/favicon.ico"),
    Site("Hangulize",
         "http://www.hangulize.org/",
         "Korean Alphabet Transcription",
         icon=True),
    Site("Flask-AutoIndex",
         "http://packages.python.org/Flask-AutoIndex",
         "A mod_autoindex for Flask"),
    Site("Flask-Silk",
         "http://packages.python.org/Flask-Silk",
         "Adds silk icons to Flask"),
    Site("VLAAH",
         "http://vlaah.com/",
         "A social network service focuses on favorites of people",
         icon="http://lab.sublee.kr/favicons/vlaah.com.ico"),
    Site("VLAAH Embed",
         "http://vlaah-embed.appspot.com/",
         "A script to embed VLAAH candybar to any webpages",
         icon="/static/favicon.ico"),
    Site("fontface.kr",
         "http://fontface.kr/",
         "An API which serves hangul fonts just like Google Font API"),
#    Site("AwtoIndex",
#         "http://lab.sublee.kr/awtoindex",
#         "More awesome Apache2's mod_autoindex"),
    Site("jquery.paged-table.js",
         "http://github.com/sublee/jquery.paged-table.js",
         "A pager for the HTML table with jQuery"),
    Site("Vlastic",
         "http://vlastic.ruree.net/",
         "A web framework for Python 3.0"),
    Site("me2PHeungP",
         "http://bitbucket.org/heungsub/me2pheungp",
         "me2DAY API client library for PHP",
         icon="http://lab.sublee.kr/favicons/sublee.kr-apps-me2pheungp.ico"),
  ]),
  ("externals", [
    Site("GitHub",
         "http://github.com/sublee",
         "My git repositories",
         icon="http://sublee.kr/static/github.com.ico"),
    Site("Flickr",
         "http://www.flickr.com/photos/heungsub",
         "My photos",
         icon=True),
    Site("YouTube",
         "http://www.youtube.com/lhs8912",
         "My videos",
         icon=True),
    Site("VLAAH",
         "http://vlaah.com/heungsub",
         "My favorites",
         icon="http://static.vlaah.com/images/favicon.ico"),
    Site("me2DAY",
         "http://me2day.net/sub",
         "My micro blog",
         icon=True)
  ])
]


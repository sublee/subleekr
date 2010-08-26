import os.path
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import distutils.cmd
from distutils import log
from functools import wraps


__commands__ = {}


def command(f):
    global __commands__
    __commands__[f.__name__] = f
    return f


@command
class initialize(distutils.cmd.Command):
    """Initializes subleekr."""

    CONFIG_FILEPATH = os.path.join(os.path.dirname(__file__), "config.cfg")
    DEFAULT_CONFIG = {"SERVER_NAME": "sublee.kr",
                      "SQLALCHEMY_DATABASE_URI": "sqlite:///subleekr/"
                                                 "db.sqlite"}

    user_options = [("server=", "s", "the server name"),
                    ("db=", "d", "a connection string for the database"),
                    ("createdb", None, "creates the database if not exists")]

    def initialize_options(self):
        self.server = None
        self.db = None
        self.createdb = False
        self.same_config = False

    def finalize_options(self):
        if not self.server and not self.db:
            self.same_config = True
        config = {}
        d = type(os.path)("config")
        d.__file__ = self.CONFIG_FILEPATH
        try:
            execfile(d.__file__, d.__dict__)
            for key in dir(d):
                if key.isupper():
                    config[key] = getattr(d, key)
        except IOError:
            config = self.DEFAULT_CONFIG
        if not self.server:
            self.server = config["SERVER_NAME"]
        if not self.db:
            self.db = config["SQLALCHEMY_DATABASE_URI"]

    def run(self):
        if not self.same_config:
            if os.path.isfile(self.CONFIG_FILEPATH):
                replace = raw_input("config file already exists. "
                                    "do you want ro replace it? "
                                    "[Y/n]").lower() == "y"
                if not replace:
                    log.info("initialization is canceled.")
                    return
            with open(self.CONFIG_FILEPATH, "w") as config:
                blank = re.compile("^\s*", re.MULTILINE)
                config_code = re.sub(blank, "", """
                    SERVER_NAME = {server!r}
                    SQLALCHEMY_DATABASE_URI = {db!r}
                """.format(server=self.server, db=self.db))
                config.write(config_code)
                del config
        if self.createdb:
            from subleekr.app import app
            log.info("create the database...")
            app.db.create_all()
        log.info("initialization has completed successfully.")


@command
class adduser(distutils.cmd.Command):
    """Adds a new user into auth file."""

    user_options = [("name=", "n", "the name of user"),
                    ("password=", "p", "the password of user")]

    def initialize_options(self):
        self.name = None
        self.password = None

    def finalize_options(self):
        pass

    def run(self):
        if not self.name:
            self.name = raw_input("Name: ")
        while not self.password:
            from getpass import getpass
            password = getpass()
            retype = getpass("Re-type password: ")
            if password == retype:
                self.password = password
            else:
                log.warn("password verification error.")
        from subleekr.auth import add_user, DuplicatedUserError
        try:
            add_user(self.name, self.password)
            log.info("user addition has completed successfully.")
        except DuplicatedUserError:
            msg = "'{0}' already exists. user addition has failed."
            log.error(msg.format(self.name))


@command
class deluser(distutils.cmd.Command):
    """Deletes a user from auth file."""

    user_options = [("name=", "n", "the name of user.")]

    def initialize_options(self):
        self.name = None

    def finalize_options(self):
        pass

    def run(self):
        if not self.name:
            self.name = raw_input("Name: ")
        from subleekr.auth import del_user, UnregisteredUserError
        try:
            del_user(self.name)
            log.info("user deletion has completed successfully.")
        except UnregisteredUserError:
            msg = "'{0}' does not exist. user deletion has failed."
            log.error(msg.format(self.name))


setup(name="subleekr",
      version="0.9.0",
      packages=["subleekr"],
      package_dir={"subleekr": "subleekr"},
      cmdclass=__commands__,
      url="http://sublee.kr/")


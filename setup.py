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
class adduser(distutils.cmd.Command):
    """Adds a new user into auth file."""

    user_options = [("name=", "n", "the name of user."),
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


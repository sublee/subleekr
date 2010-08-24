import os.path
import crypt
import hashlib
import pickle


__all__ = "encrypt", "adduser", "deluser", \
          "DuplicatedUserError", "UnregisteredUserError"


AUTH_FILEPATH = os.path.join(os.path.dirname(__file__), "../.auth")


def encrypt(word):
    """Encrypts a word."""
    return hashlib.sha1(crypt.crypt(word, "\n" * len(word))).digest()


def check(name, password):
    users = _load_users()
    password = encrypt(password)
    return name in users and users[name] == password


def _load_users():
    """Loads users from auth file."""
    try:
        auth_file = open(AUTH_FILEPATH)
        users = pickle.load(auth_file)
        auth_file.close()
    except IOError:
        users = {}
    return users


def _save_users(users):
    """Saves users into auth file."""
    auth_file = open(AUTH_FILEPATH, "w")
    pickle.dump(users, auth_file)
    auth_file.close()


def add_user(name, password):
    """Adds a new user into auth file."""
    users = _load_users()
    if name in users:
        raise DuplicatedUserError()
    password = encrypt(password)
    users[name] = password
    _save_users(users)


def del_user(name, password):
    """Deletes a user from auth file."""
    users = _load_users()
    if name not in users:
        raise UnregisteredUserError()
    del users[name]
    _save_users(users)


class DuplicatedUserError(RuntimeError): pass
class UnregisteredUserError(RuntimeError): pass


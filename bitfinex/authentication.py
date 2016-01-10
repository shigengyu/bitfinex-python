import hashlib

from configobj import ConfigObj

__author__ = 'Univer'


class Crypto(object):
    KEY_FILE = "config/keys"

    def __init__(self, key_file):
        self._api_key, secret_key = load_keys(key_file)
        self._hash = hashlib.sha384(secret_key)

    def encrypt_payload(self, payload):
        return self._hash.hexdigest(payload)


def load_keys(key_file):
    config = ConfigObj(key_file)
    return config["api_key"], config["secret_key"]

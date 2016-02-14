import base64
import hashlib
import hmac
import json

from configobj import ConfigObj

from config.config_files import get_config_file_path

__author__ = 'Univer'


class Crypto(object):
    DEFAULT_KEY_FILE = "config/keys"

    def __init__(self, key_file=get_config_file_path(DEFAULT_KEY_FILE)):
        self._api_key, self._secret_key = load_keys(key_file)

    def encrypt_payload(self, payload):
        payload_json = json.dumps(payload)
        payload_base64 = base64.standard_b64encode(payload_json)

        h = hmac.new(self._secret_key, payload_base64, hashlib.sha384)
        signature = h.hexdigest()

        return {
            "X-BFX-APIKEY": self._api_key,
            "X-BFX-SIGNATURE": signature,
            "X-BFX-PAYLOAD": payload_base64
        }


def load_keys(key_file):
    config = ConfigObj(key_file)
    return config["api_key"], config["secret_key"]

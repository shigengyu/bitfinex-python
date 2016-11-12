import unittest

from bitfinex.crypto import load_keys
from tests.test_data import get_test_data_path

__author__ = "Gengyu Shi"


class TestAuthentication(unittest.TestCase):
    def test_load_keys(self):
        key_file = get_test_data_path("test_keys")
        api_key, secret_key = load_keys(key_file)

        self.assertEqual(api_key, "dummy_api_key")
        self.assertEqual(secret_key, "dummy_secret_key")

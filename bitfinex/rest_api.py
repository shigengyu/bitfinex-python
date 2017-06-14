import requests

from bitfinex.bitfinex_config import DEFAULT
from bitfinex.ticker import Ticker

__author__ = 'Gengyu Shi'

URL_PREFIX = DEFAULT.url_prefix


def ticker(symbol):
    return Ticker(requests.get(URL_PREFIX + "/pubticker/" + symbol, verify=True).json())


DEFAULT.url_prefix

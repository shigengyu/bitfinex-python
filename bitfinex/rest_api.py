import requests

from bitfinex.bitfinex_config import DEFAULT
from bitfinex.constants import Symbols
from bitfinex.ticker import Ticker

__author__ = "Gengyu Shi"

URL_PREFIX = DEFAULT.url_prefix


def ticker(symbol):
    json = requests.get(URL_PREFIX + "/pubticker/" + symbol.value, verify=True).json()
    json.update({"symbol": symbol.value})
    return Ticker(**json)


if __name__ == '__main__':
    print(ticker(Symbols.BTCUSD))

from datetime import datetime

__author__ = 'Gengyu Shi'


class Ticker(object):
    def __init__(self, **kwargs):
        self.mid = kwargs.get("mid")
        self.bid = kwargs.get("bid")
        self.ask = kwargs.get("ask")
        self.last_price = kwargs.get("last_price")
        self.low = kwargs.get("low")
        self.high = kwargs.get("high")
        self.volume = kwargs.get("volume")
        self.timestamp = datetime.fromtimestamp(self.timestamp)

        if self.timestamp:
            self.timestamp = datetime.fromtimestamp(self.timestamp)

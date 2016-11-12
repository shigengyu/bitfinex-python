from datetime import datetime

from bitfinex.constants import DATETIME_FORMAT_MS
from structures.dataframe_entities import Field, DataFrameEntity

__author__ = "Gengyu Shi"


class Ticker(DataFrameEntity):
    symbol = Field(str)
    mid = Field(float)
    big = Field(float)
    ask = Field(float)
    last_price = Field(float)
    low = Field(float)
    high = Field(float)
    volume = Field(float)
    timestamp = Field(datetime, value_parser=lambda x: datetime.fromtimestamp(float(x)))

    def __repr__(self):
        return "Ticker %s %.2f @ %s" % (self.symbol, self.mid, self.timestamp.strftime(DATETIME_FORMAT_MS))

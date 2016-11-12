from configobj import ConfigObj

from config import config_files

__author__ = "Gengyu Shi"


class BitfinexProperties(object):
    def __init__(self, file_name):
        self._config = ConfigObj(config_files.get_config_file_path(file_name))

    @property
    def url_prefix(self):
        return self._config["url_prefix"]


DEFAULT = BitfinexProperties("bitfinex.properties")

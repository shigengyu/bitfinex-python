import os

__author__ = 'Gengyu Shi'


def get_config_file_path(*args):
    return os.path.join(os.path.dirname(__file__), *args)

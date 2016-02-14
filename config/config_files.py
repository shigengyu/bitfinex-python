import os

__author__ = 'Univer'


def get_config_file_path(*args):
    return os.path.join(os.path.dirname(__file__), *args)

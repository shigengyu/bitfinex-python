import os

__author__ = 'Gengyu Shi'


def get_test_data_path(*args):
    return os.path.join(os.path.dirname(__file__), r"..\test-data", *args)

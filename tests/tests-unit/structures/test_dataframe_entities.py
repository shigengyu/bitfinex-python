from structures.dataframe_entities import Field, collection, DataFrameEntity

__author__ = "Gengyu Shi"


class DummyModel(DataFrameEntity):
    id = Field(int)
    name = Field(str)


class DummyModelCollection(collection(DummyModel)):
    pass


class TestDataFrameEntities(object):
    def test_get_empty_data_frame(self):
        DummyModelCollection.get_empty_data_frame()

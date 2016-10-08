from structures.dataframe_entities import DataFrameEntity, Field, collection

__author__ = 'Univer'


class DummyModel(DataFrameEntity):
    id = Field(int)
    name = Field(str)


class DummyModelCollection(collection(DummyModel)):
    pass


class TestDataFrameEntities(object):
    pass

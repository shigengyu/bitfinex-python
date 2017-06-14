from __future__ import division, print_function

from copy import copy
from collections import OrderedDict

import pandas as pd

__author__ = 'Gengyu Shi'


class DataframeEntity(object):
    logger = None
    _ordered_fields = None

    def __init__(self, **kwargs):
        for name, field in {field.name: field for field in self.fields()}.iteritems():
            value = kwargs.get(field.field_name, None)
            if is_null(value) and field.default_value is not None:
                value = field.default_value
            if is_null(value) and field.default_value_generator is not None:
                value = field.default_value_generator(field)
            setattr(self, field.field_name, value)

    @classmethod
    def fields(cls):
        return cls._ordered_fields

    @property
    def field_values(self):
        result = OrderedDict()
        for field in self.fields():
            result[field.name] = getattr(self, field.field_name)
        return result

    @classmethod
    def columns(cls):
        return [field.name for field in cls.fields()]

    def has_value(self, field):
        field_value = getattr(self, field)
        return field_value is not None and type(field_value) != Field

    def totuple(self, columns=None):
        columns = columns if columns else self.columns()
        return tuple([getattr(self, column, None) for column in columns])

    def copy(self):
        return copy(self)

    @classmethod
    def _get_default_field_value_parser(cls, field):
        def convert_function(value):
            if is_null(value):
                return None

            if isinstance(value, basestring) and not issubclass(field.type, basestring) and len(value) == 0:
                return None

            if not isinstance(value, field.type):
                if field.value_parser is not None:
                    value = field.value_parser(value)
                else:
                    try:
                        value = field.type(value)
                    except Exception as e:
                        cls.logger.error("Failed to convert value [%s] of type [%s] to type [%s] for field [%s] - %s" % (
                            str(value), type(value), field.type, field.name, e.message))
                        raise
            return value

        return convert_function

    @classmethod
    def _get_field_by_field_name(cls, field_name):
        field = getattr(cls, field_name, None)
        return field if isinstance(field, Field) else None

    @classmethod
    def _get_field_by_column_name(cls, column_name):
        for field in cls.fields():
            if field.name == column_name:
                return field if isinstance(field, Field) else None
        return None

    @classmethod
    def _get_field_value_parser(cls, field_name):
        field = cls._get_field_by_field_name(field_name)
        if field is not None and isinstance(field, Field) and field.value_parser is not None:
            return field.value_parser
        else:
            return cls._get_default_field_value_parser(field)


def is_null(value, empty_as_null=False):
    if value is None:
        return True
    if isinstance(value, (tuple, list, dict, pd.DataFrame, pd.Series)):
        return empty_as_null and len(value) == 0
    if isinstance(value, DataframeEntity) or type(value).__base__.__name__ == "CollectionClass":
        return False
    return pd.isnull(value)


class Field(object):
    creation_counter = 0

    def __init__(self,
                 attribute_type,
                 column_name=None,
                 default_value=None,
                 default_value_generator=None,
                 is_transient=False,
                 value_parser=None):
        self.field_name = None
        self.name = column_name
        self.type = attribute_type
        self.default_value = default_value
        self.default_value_generator = default_value_generator
        self.is_transient = is_transient
        self.value_parser = value_parser

        self.creation_counter = Field.creation_counter
        Field.creation_counter += 1

    def __repr__(self):
        return "%s [%s]" % (self.name, self.type.__name__)


class DataframeEntityMetaClass(type):
    def __new__(mcs, name, bases, attributes):
        new_class = super(DataframeEntityMetaClass, mcs).__new__(mcs, name, bases, attributes)
        ordered_fields = [(attribute_name, attributes.pop(attribute_name)) for attribute_name, obj in attributes.items()
                          if hasattr(obj, "creation_counter")]
        ordered_fields.sort(key=lambda item: item[1].creation_counter)
        for name, field in ordered_fields:
            field.field_name = name
            if field.name is None:
                field.name = name

        base_class_fields = [] if len(bases) == 0 or bases[0] == DataframeEntity else bases[0].fields()
        new_class._ordered_fields = base_class_fields + [field for key, field in ordered_fields]
        return new_class

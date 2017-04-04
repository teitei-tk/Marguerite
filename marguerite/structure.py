# -*- coding: utf-8 -*-

import re
from werkzeug.utils import cached_property

from query import Query

class Structure(object):
    quries = None
    struct = None
    __table__ = None

    def __init__(self):
        self.is_valid()

    def is_valid(self):
        if self.quries.__len__() <= 0:
            raise NotImplementedError("Query is not defined")

        for k, v in self.quries.items():
            if not isinstance(k, str):
                raise RuntimeError("should be {} is string.".format(k))

            if not isinstance(v, str):
                raise RuntimeError("should be {} is string".format(v))

    @cached_property
    def table_name(self):
        if not self.__table__:
            self.__table__ = re.sub('(?!^)([A-Z]+)', r'_\1', self.__class__.__name__).lower().__str__()
        return self.__table__

    def get_query(self, name):
        return self.quries.get(name)

    def get_entity(self):
        return self.struct

    @cached_property
    def entity(self):
        return self.struct

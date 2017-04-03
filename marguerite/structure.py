# -*- coding: utf-8 -*-

import re
from werkzeug.utils import cached_property

from query import Query

class Structure(object):
    quries = None
    struct = None
    __table__ = None

    def __init__(self):
        self.validate()

    def validate(self):
        if not isinstance(self.quries, Query):
            raise NotImplementedError

        if self.quries.__len__() <= 0:
            raise NotImplementedError

        if not isinstance(self.struct, dict):
            raise NotImplementedError

        for k, v in self.struct.items():
            if not isinstance(k, str):
                raise NotImplementedError

            if not isinstance(v, str):
                raise NotImplementedError

    @cached_property
    def table_name(self):
        if not self.__table__:
            self.__table__ = re.sub('(?!^)([A-Z]+)', r'_\1', self.__name__).lower().__str__()
        return self.__table__

    def get_query(self, name):
        return self.quries.get(name)

    @cached_property
    def entity(self):
        return self.struct.__dict__.copy()

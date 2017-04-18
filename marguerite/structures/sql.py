# -*- coding: utf-8 -*-

import re
import copy

from .abstract import AbstractStructure

from ..accessors.sql import SQLAlchemyAccessor
from ..utils import cached_property


class SQLAlchemyStructure(AbstractStructure):
    __accessor__ = SQLAlchemyAccessor
    __table_name__ = None
    __table_alias__ = '__table__'
    __struct__ = dict()

    def is_valid(self):
        super(SQLAlchemyStructure, self).is_valid()

        if not isinstance(self.__struct__, dict):
            raise NotImplementedError("struct is not implemented")

    @cached_property
    def table_name(self):
        if not self.__table_name__ or not isinstance(self.__table_name__, str):
            # class name replace as snake case.
            # eg: Class Name is UserStructure -> user_structure
            return re.sub('(?!^)([A-Z]+)', r'_\1', self.__class__.__name__).lower().__str__()
        return self.__table_name__

    @cached_property
    def table_alias(self):
        return self.__table_alias__

    @cached_property
    def struct(self):
        return copy.copy(self.__struct__)

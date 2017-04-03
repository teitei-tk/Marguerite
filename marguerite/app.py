# -*- coding: utf-8 -*-

from werkzeug import import_string

from acceessor import SQLAlchemyAccessor
from structure import Structure

class Marguerite(object):
    __accessor__ = SQLAlchemyAccessor

    def __init__(self, engine):
        self.engine = engine
        self.accessores = {}

    def get_accessor(self, namespace_path, reload=False):
        accessor = self.accessores.get(namespace_path)
        if accessor and not reload:
            return accessor.reload(self.engine)

        struct = import_string(namespace_path)
        if not isinstance(struct, Structure):
            raise NotImplementedError

        accessor = self.__accessor__(self.engine, struct)
        self.structures[namespace_path] = accessor
        return accessor

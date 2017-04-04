# -*- coding: utf-8 -*-

from werkzeug import import_string
from werkzeug.utils import cached_property

from acceessor import SQLAlchemyAccessor as DefaultAccessor, AbstractAccessor
from structure import Structure

class Marguerite(object):
    __accessor__ = DefaultAccessor

    def __init__(self, driver):
        self.driver = driver
        self.accessores = {}

        self.is_valid()

    def is_valid(self):
        if not issubclass(self.__accessor__, AbstractAccessor):
            raise NotImplementedError("accessor is not implemented.")

    @cached_property
    def accessor(self):
        return self.__accessor__

    def get_accessor(self, namespace_path, reload=False):
        accessor = self.accessores.get(namespace_path)
        if accessor and not reload:
            return accessor.reload(self.driver)

        struct = import_string(namespace_path)
        if not issubclass(struct, Structure):
            raise NotImplementedError

        accessor = self.accessor(self.driver, struct())
        self.accessores[namespace_path] = accessor
        return accessor

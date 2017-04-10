# -*- coding: utf-8 -*-

from .accessors import AbstractAccessor
from .formaters import AbstractFormater
from .utils import cached_property, import_string

class Marguerite(object):
    def __init__(self, driver, accesor):
        self.driver = driver
        self.__accessor__ = accesor
        self.accessores = {}

    def assert_accessor(self, accessor):
        if not isinstance(accessor, AbstractAccessor):
            raise NotImplementedError("accessor is not implemented.")

    @cached_property
    def accessor(self):
        return self.__accessor__

    def get_accessor(self, namespace_path, reload=False):
        accessor = self.accessores.get(namespace_path)
        if accessor and not reload:
            return accessor.reload(self.driver)

        formater = import_string(namespace_path)()
        if not isinstance(formater, AbstractFormater):
            raise NotImplementedError("formater is must be extends AbstractFormater")

        accessor = self.accessor(self.driver, formater)
        self.assert_accessor(accessor)
        self.accessores[namespace_path] = accessor
        return accessor

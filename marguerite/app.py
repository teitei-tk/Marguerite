# -*- coding: utf-8 -*-

from .accessors import AbstractAccessor
from .structures import AbstractStructure
from .utils import import_string

class Marguerite(object):
    def __init__(self, driver=None):
        self.driver = driver
        self.accessores = {}

    def get_accessor(self, namespace_path, reload=False):
        accessor = self.accessores.get(namespace_path)
        if accessor and not reload:
            return accessor.reload(self.driver)

        structure = import_string(namespace_path)()
        if not isinstance(structure, AbstractStructure):
            raise NotImplementedError("structure is must be extends AbstractStructure")

        accessor = structure.accessor(self.driver, structure)
        assert isinstance(accessor, AbstractAccessor)
        self.accessores[namespace_path] = accessor
        return accessor

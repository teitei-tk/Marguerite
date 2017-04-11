# -*- coding: utf-8 -*-

import re
import copy

from ..accessors import AbstractAccessor
from ..utils import cached_property

class AbstractStructure(object):
    __accessor__ = AbstractAccessor

    orders = None

    def __init__(self, *args, **kwargs):
        self.is_valid()

    @cached_property
    def accessor(self):
        return self.__accessor__

    def is_valid(self):
        if not isinstance(self.orders, dict):
            raise NotImplementedError("{0}.orderes is must be dict subclass".format(self.__class__.__name__))

        if self.orders.__len__() <= 0:
            raise NotImplementedError("Order is not defined")

        for k, v in self.orders.items():
            if not isinstance(k, str):
                raise RuntimeError("should be {} is string.".format(k))

            if not isinstance(v, str):
                raise RuntimeError("should be {} is string".format(v))

    def get_order(self, name):
        return self.orders.get(name)

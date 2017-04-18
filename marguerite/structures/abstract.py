# -*- coding: utf-8 -*-

from ..accessors import AbstractAccessor
from ..utils import cached_property


class StructureAssertion(object):
    def assert_equal_order(self):
        if not isinstance(self.orders, dict):
            raise NotImplementedError("{0}.orderes is must be dict subclass".format(self.__class__.__name__))

    def assert_order_implemented(self):
        if self.orders.__len__() <= 0:
            raise NotImplementedError("Order is not defined")

    def assert_order_key_value(self):
        for k, v in self.orders.items():
            if not isinstance(k, str):
                raise RuntimeError("should be {} is string.".format(k))

            if not isinstance(v, str):
                raise RuntimeError("should be {} is string".format(v))


class AbstractStructure(StructureAssertion):
    __accessor__ = AbstractAccessor

    orders = None

    def __init__(self, *args, **kwargs):
        self.is_valid()

    def is_valid(self):
        self.assert_equal_order()
        self.assert_order_implemented()
        self.assert_order_key_value()

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

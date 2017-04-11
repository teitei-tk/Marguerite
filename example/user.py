# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from marguerite import AbstractStructure, Order, AbstractAccessor
from marguerite.accessors import bind

class Accessor(AbstractAccessor):
    def get(self, name, value={}):
        order = self.structure.get_order(name)
        return bind(order, value)

    def find(self, name, value={}):
        return self.get(name, value)

class User(AbstractStructure):
    __accessor__ = Accessor

    orders = Order(
        request = "https://example.com/users/:id",
        create = "https://example.com/users/:id?=username=:username"
    )

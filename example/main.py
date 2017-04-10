# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from marguerite import Marguerite, AbstractAccessor
from marguerite.accessors import bind

class Accessor(AbstractAccessor):
    def get(self, name, value={}):
        order = self.formater.get_order(name)
        return bind(order, value)

    def find(self, name, value={}):
        return self.get(name, value)

app = Marguerite(None, Accessor)
accessor = app.get_accessor("user.User")

print(accessor.find("users", {"ids": [1, 2]}))
# result
"""
        SELECT
            *
        FROM
            __table__
        WHERE
            id = 1

"""

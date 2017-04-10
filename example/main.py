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

app = Marguerite(None, Accessor)
accessor = app.get_accessor("user.User")

print(accessor.get("user", {"id": 1}))
# result
"""
        SELECT
            *
        FROM
            __table__
        WHERE
            id = 1

"""

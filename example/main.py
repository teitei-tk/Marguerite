# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from marguerite import Marguerite

app = Marguerite()
accessor = app.get_accessor("user.User")

print(accessor.get("request", {"id": 1})) # https://example.com/users/1
print(accessor.get("create", {"id": 1, "username": "marguerite"})) # https://example.com/users/1?=username=marguerite

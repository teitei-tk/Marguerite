# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from marguerite import Marguerite
from sqlalchemy import create_engine

engine = create_engine('mysql://root:@localhost/margruite')
marguerite = Marguerite(engine)

accessor = marguerite.get_accessor("user.User")
results = accessor.find("users", { "ids": [1, 2] })
print(results)

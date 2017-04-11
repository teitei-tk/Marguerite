# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from marguerite import AbstractStructure, Order

class User(AbstractStructure):
  struct = {
    "id"    : int(),
    "name"  : str(),
    "email" : str(),
  }

  orders = Order(
    user = """
        SELECT
            *
        FROM
            __table__
        WHERE
            id = :id
    """,

    users = """
        SELECT
            *
        FROM
            __table__
        WHERE
            id in (:ids)
    """
  )

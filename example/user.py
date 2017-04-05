# -*- coding: utf-8 -*-

from marguerite import Structure, Query

class User(Structure):
  struct = {
    "id"    : int(),
    "name"  : str(),
    "email" : str(),
  }

  quries = Query(
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

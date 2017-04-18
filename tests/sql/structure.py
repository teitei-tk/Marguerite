# -*- coding: utf-8 -*-

from marguerite import Order
from marguerite.accessors.sql import SQLAlchemyAccessor
from marguerite.structures.sql import SQLAlchemyStructure

class User(SQLAlchemyStructure):
    __struct__ = {
        "id":   int(),
        "name": str(),
        "email": str(),
    }

    orders = Order(
        create_table = """
            CREATE TABLE IF NOT EXISTS __table__(
              id int(11) unsigned NOT NULL AUTO_INCREMENT,
              name varchar(255) NOT NULL DEFAULT '',
              PRIMARY KEY (id)
            ) ENGINE=InnoDB CHARSET=utf8;
        """,

        drop_table = """
            DROP TABLE IF EXISTS __table__
        """,

        insert = """
            INSERT INTO
                __table__(name)
            VALUES
                (:name)
        """,

        select = """
            SELECT
                *
            FROM
                __table__
            WHERE
                id = :id
        """,

        find = """
            SELECT
                *
            FROM
                __table__
            WHERE
                id in (:id1, :id2)
        """
    )

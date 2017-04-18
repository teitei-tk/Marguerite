# -*- coding: utf-8 -*-

import sqlalchemy
from .abstract import AbstractAccessor

class SQLAlchemyAccessor(AbstractAccessor):
    connection = None

    def initialize(self):
        self.connection = self.driver.connect()

    def reload(self, driver):
        self.driver = driver
        self.connection = self.driver.connect()
        return self

    def close(self):
        self.connection.close()

    def get(self, name, value = {}):
        exec_result = self.execute(name, value)
        result = self.bind(exec_result)
        if result.__len__() <= 0:
            return None
        return result[0]

    def find(self, name, value = {}):
        exec_result = self.execute(name, value)
        result = self.bind(exec_result)
        if result.__len__() <= 0:
            return []
        return result

    def prepare(self, name):
        query = self.structure.get_order(name)
        if not query:
            return None
        if not isinstance(query, str):
            return None
        return query.lower().replace(self.structure.table_alias, self.structure.table_name)

    def execute(self, name, value = {}):
        query = self.prepare(name)
        if not query:
            return None
        exec_query = sqlalchemy.text(query)
        return self.connection.execute(exec_query, **value)

    def bind(self, exec_result):
        new_rows = []
        if not exec_result:
            return new_rows

        rows = [dict(x) for x in exec_result if x]
        for row in rows:
            struct = self.structure.struct.copy()
            for k, v in row.items():
                struct[k] = v
            new_rows += [struct]
        return new_rows

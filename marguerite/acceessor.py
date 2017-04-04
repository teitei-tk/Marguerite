# -*- coding: utf-8 -*-

import sqlalchemy

__all__ = ['AbstractAccessor', 'SQLAlchemyAccessor']

class AbstractAccessor(object):
    def __init__(self, driver, structure):
        self.driver = driver
        self.structure = structure

        self.is_valid()
        self.initialize()

    def is_valid(self):
        pass

    def initialize(self):
        pass

    def reload(self, driver):
        self.driver = driver
        return self

    def get(self, name, value = {}):
        raise NotImplementedError("get method is not implemented")

    def find(self, name, value = {}):
        raise NotImplementedError("find method is not implemented")

    def update(self, name, value = {}):
        return self.execute(name, value)

    def insert(self, name, value = {}):
        return self.execute(name, value)

    def execute(self, name, value):
        raise NotImplementedError("execute method is not implemented")

    def prepare(self, name):
        raise NotImplementedError("prepare method is not implemented")

    def call(self, name, value):
        """ alias method at execute. """
        return self.execute(name, value)

    def bind(self, exec_result):
        raise NotImplementedError("bind method is not implemented")


class SQLAlchemyAccessor(AbstractAccessor):
    def initialize(self):
        self.connection = self.driver.connect()

    def reload(self, driver):
        self.driver = driver
        self.connection = self.driver.connect()
        return self

    def get(self, name, value = {}):
        result = self.execute(name, value)
        return self.bind(result)

    def find(self, name, value = {}):
        result = self.execute(name, value)
        return [self.bind(x) for x in result if x]

    def prepare(self, name):
        query = self.structure.get_query(name)
        if not query:
            return None
        if not isinstance(query, str):
            return None
        return query.replace('__table__', self.structure.table_name)

    def execute(self, name, value):
        query = self.prepare(name)
        if not query:
            return None
        exec_query = sqlalchemy.text(query)
        return self.connection.execute(exec_query)

    def bind(self, exec_result):
        if not exec_result:
            return None

        entity = self.structure.entity.copy()
        for k, v in exec_result.items():
            entity[k] = v
        return entity

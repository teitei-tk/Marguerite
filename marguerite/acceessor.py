# -*- coding: utf-8 -*-

__all__ = ['AbstractAccessor', 'SQLAlchemyAccessor']

class AbstractAccessor(object):
    def reload(self, driver):
        raise NotImplementedError

    def get(self, name, value = {}):
        raise NotImplementedError

    def find(self, name, value = {}):
        raise NotImplementedError

    def update(self, name, value = {}):
        return self.execute(name, value)

    def insert(self, name, value = {}):
        return self.execute(name, value)

    def execute(self, name, value):
        raise NotImplementedError

    def prepare(self, name):
        raise NotImplementedError

    def call(self, name, value):
        """ alias method at execute. """
        return self.execute(name, value)


class SQLAlchemyAccessor(AbstractAccessor):
    def __init__(self, engine, structure):
        self.engine = engine
        self.struct = structure

    def reload(self, engine):
        self.engine = engine
        return self

    def get(self, name, value = {}):
        result = self.execute(name, value)
        return self.bind_entity(result)

    def find(self, name, value = {}):
        result = self.execute(name, value)
        return [self.bind_entity(row) for row in result]

    def prepare(self, name):
        query = self.struct.get_query(name)
        if not query:
            return None
        if not isinstance(query, str):
            return None
        return query.replace('__table__', self.struct.table_name)

    def execute(self, name, value):
        query = self.prepare(name)
        if not query:
            return None

    def call(self, name, value):
        return self.execute(name, value)

    def bind_entity(self, exec_result):
        entity = self.struct.entity
        return entity

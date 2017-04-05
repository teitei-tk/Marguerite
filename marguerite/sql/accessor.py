# -*- coding: utf-8 -*-

from sqlalchemy import text, bindparam
from sqlalchemy.types import String, Integer

from ..acceessor import AbstractAccessor

class SQLAlchemyAccessor(AbstractAccessor):
    def initialize(self):
        self.connection = self.driver.connect()

    def reload(self, driver, connect=True):
        self.driver = driver
        if connect:
            self.connection = self.driver.connect()
        return self

    def get(self, name, value = {}):
        result = self.execute(name, value)
        if result.__len__() <= 0:
            return None
        return self.bind(result[0])

    def find(self, name, value = {}):
        result = self.execute(name, value)
        return [self.bind(x) for x in result if x]

    def prepare(self, name, value):
        query = self.structure.get_query(name)
        if not query:
            return None
        if not isinstance(query, str):
            return None
        exec_query = query.replace('__table__', self.structure.table_name)
        params = self.correct_params(value)
        return exec_query, params

    def correct_params(self, value):
        def check_type(value, t):
            return any((isinstance(x, t) for x in value if x))

        params = []
        for k, v in value.items():
            print(k, v)
            value = v
            if isinstance(v, list):
                if check_type(v, int):
                    c = [x.__str__() for x in v if x]
                    v = ','.join(c)
                    params += [bindparam(k, value=v, type_=Integer())]
                elif check_type(v, str):
                    params += [bindparam(k, value=','.join(v), type_=String())]
            else:
                if isinstance(v, str):
                    params += [bindparam(k, value=v, type_=String())]
                elif isinstance(v, int):
                    params += [bindparam(k, value=v, type_=Integer())]
        return params

    def execute(self, name, value):
        query, params = self.prepare(name, value)
        if not query:
            return None
        stmt = text(query).bindparams(*params)
        return self.connection.execute(stmt)

    def bind(self, exec_result):
        if not exec_result:
            return None

        entity = self.structure.entity.copy()
        for k, v in exec_result.items():
            entity[k] = v
        return entity

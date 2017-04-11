# -*- coding: utf-8 -*-

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

    def create(self, name, value = {}):
        return self.execute(name, value)

    def get(self, name, value = {}):
        raise NotImplementedError("get method is not implemented")

    def find(self, name, value = {}):
        raise NotImplementedError("find method is not implemented")

    def update(self, name, value = {}):
        return self.execute(name, value)

    def destory(self, name, value = {}):
        return self.execute(name, value)

    def execute(self, name, value):
        raise NotImplementedError("execute method is not implemented")

    def prepare(self, name, value):
        raise NotImplementedError("prepare method is not implemented")

    def call(self, name, value):
        """ alias method at execute. """
        return self.execute(name, value)

    def bind(self, exec_result):
        raise NotImplementedError("bind method is not implemented")

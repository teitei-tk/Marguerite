# -*- coding: utf-8 -*-

import unittest
from sqlalchemy import create_engine
from marguerite import Marguerite

engine = create_engine("mysql+pymysql://root:@localhost/marguerite")
app = Marguerite(engine)

class TestSQLAlchemy(unittest.TestCase):
    def setUp(self):
        self.accessor = app.get_accessor("tests.sql.structure.User")
        self.accessor.execute("create_table")

    def tearDown(self):
        self.accessor.execute("drop_table")

    def test_get(self):
        # insert new record.
        self.accessor.execute("insert", {
            "name": "john"
        })

        r = self.accessor.get("select", {"id": 1})
        self.assertEqual(r["name"], "john")
        self.assertEqual(r["id"], 1)

    def test_get_fail(self):
        self.accessor.execute("insert", {
            "name": "john"
        })

        r = self.accessor.get("select", {"id": 2})
        self.assertEqual(r, None)

    def test_find(self):
        names = ["john", "doe"]

        for name in names:
            self.accessor.execute("insert", {
                "name": name
            })

        rows = self.accessor.find("find", {"id1": 1, "id2": 2})
        self.assertEqual(names.__len__(), 2)
        self.assertEqual(names.__len__(), rows.__len__())

        for i, row in enumerate(rows):
            self.assertEqual(i + 1, row["id"])
            self.assertEqual(names[i], row["name"])
            self.assertEqual("", row["email"])

    def test_find_fail(self):
        for name in ["john", "doe"]:
            self.accessor.execute("insert", { "name": name })

        rows = self.accessor.find("find", {"id1": 3, "id2": 4})
        self.assertEqual(rows.__len__(), 0)

    def test_execute(self):
        result = self.accessor.execute("insert", {
            "name": "john"
        })
        self.assertNotEqual(result, None)

    def test_execute_fail(self):
        result = self.accessor.execute("hogefuga", {
            "name": "foobar"
        })

        self.assertEqual(result, None)

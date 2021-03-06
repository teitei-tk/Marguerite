# Marguerite

Marguerite provides a declarative, consistent accessor to data layer.

---

[![Build Status](https://travis-ci.org/teitei-tk/Marguerite.svg?branch=master)](https://travis-ci.org/teitei-tk/Marguerite)
[![PyPI version](https://badge.fury.io/py/Marguerite.svg)](https://badge.fury.io/py/Marguerite)

# Dependencies
* Python 2.7 or later
* Werkzeug 0.12.7 or later

# Installation
```bash
$ pip install Marguerite
```

# Usage
## Example
Install requests as an example.

```bash
$ pip install requests
```

1. define data layer accessor, and writen access structure
```python
from marguerite import AbstractStructure, AbstractAccessor, Order
from marguerite.accessors import bind

class Accessor(AbstractAccessor):
    def prepare(self, name, value):
        order = self.structure.get_order(name)
        return bind(order, value)

    def create(self, name, value):
        order = self.prepare(name, value)
        return requests.post(order).json()

    def get(self, name, value={}):
        order = self.prepare(name, value)
        return requests.get(order).json()


class UserStructure(AbstractStructure):
    __accessor__ = Accessor

    orders = Order(
        user = "https://example.com/users/:id",
        create = "https://example.com/users/:id?=username=:username"
    )
```

2. get data layer accessor object
```python
from marguerite import Marguerite

marguerite = Marguerite()
accessor = marguerite.get_accessor("path.to.UserStructure")
```

3. fetch data
```python
# execute get logic
result = accessor.get("user", { "id": 1 })
print(result) # {"id": 1, "username": "john"...}

# execute post logic
result = accessor.create("create", { "id": 2, "username": "marguerite" })
print(result) # {"status": "success", {"result": {"id": 2, "username": "marguerite"...}}}
```

## SQLAlchemy

```bash
$ pip install SQLAlchemy PyMySQL
```

1. create database
```mysql
mysql> create database marguerite;
Query OK, 1 row affected (0.00 sec)
```

2. define database structure
```python
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
```

3. get database accessor object
```python
from marguerite import Marguerite

engine = create_engine("mysql+pymysql://root:@localhost/marguerite")

marguerite = Marguerite(engine)
accessor = marguerite.get_accessor("path.to.User")
```

4. create table
```python
accessor.execute("create_table")
```

5. check also
```mysql
mysql> use marguerite
Database changed
mysql> show tables;
+----------------------+
| Tables_in_marguerite |
+----------------------+
| user                 |
+----------------------+
```

3. fetch data
```python
# insert record at user table
accessor.execute("insert", {"name": "john"})

# get record
row = accessor.get("select", { "id": 1 })
print(row) # {"id": 1, "name": "john", "email": ""}

# find records
rows = accessor.find("find", { "id1": 1, "id2": 2 })
print(rows) # [{"id": 1, "name": "john", "email": ""}]
```

# LICENSE
Apache License 2.0

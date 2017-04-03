# Marguerite

Marguerite defines how to access the database and provide interface.

---

# Dependencies
* Python 2.7 or later
* SQLAlchemy 1.1.7 or later
* Werkzeug 0.12.7 or later

# Usage Flow.
1. define database structure.
```python
from marguerite import Structure, Query

class User(Structure):
  struct = {
    "id"  : int(),
    "name": str(),
  }

  queries = Query(
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
```

2. call database accessor object
```python
from marguerite import Marguerite
from sqlalchemy import create_engine

engine = create_engine("mysql://scott:tiger@localhost/foo")
marguerite = Marguerite(engine)

accessor = marguerite.get_accessor("User")
```

3. fetch database row
```python
# as dict
user = accessor.get("user", { "id": 1 })
print(user) # {'id': 1, 'name': 'john'}

# as array
users = accessor.find("users", { "ids": [1, 2] })
print(users) # [{'id': 1, 'name': 'john'}]
```

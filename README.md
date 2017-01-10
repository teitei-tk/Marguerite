# Marguerite

Marguerite defines how to access the database and provide interface.

---

# Dependencies
* Python 3.5 or later

# Usage Flow.
1. define database structure.
```python
from marguerite import Structure, Query

class Hello(Structure):
  primary_key = "id"

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

1. call database accessor

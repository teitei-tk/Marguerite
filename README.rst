Marguerite
==========

Marguerite provides a declarative, consistent accessor to data layer.

--------------

Dependencies
============

-  Python 2.7 or later
-  Werkzeug 0.12.7 or later

Usage Flow.
===========

1. define formater. \`\`\`python from marguerite import
   AbstractFormater, Order

class User(AbstractFormater): struct = { "id" : int(), "name" : str(),
"email" : str(), }

orders = Order( user = """ SELECT \* FROM **table** WHERE id = :id """,

::

    users = """
        SELECT
            *
        FROM
            __table__
        WHERE
            id in (:ids)
    """

) \`\`\`

2. get data layer accessor object \`\`\`python from marguerite import
   Marguerite, AbstractAccessor from marguerite.accessors import bind

class Accessor(AbstractAccessor): def get(self, name, value={}): order =
self.formater.get\_order(name) return bind(order, value)

marguerite = Marguerite(None, Accessor) accessor =
marguerite.get\_accessor("path.to.User") \`\`\`

3. fetch data \`\`\`python # as dict result = accessor.get("user", {
   "id": 1 }) print(result) # result """ SELECT

   -  FROM **table** WHERE id = 1 """

as array
========

result = accessor.find("users", { "ids": [1, 2] }) print(result) #
result """ SELECT \* FROM **table** WHERE id in (1, 2) """ \`\`\`

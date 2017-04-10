# -*- coding: utf-8 -*-

def replacer(query, key, value):
    return query.replace(":{0}".format(key), value)

def bind(order, params = {}):
    query = order
    for k, v in params.items():
        if not k or not v:
            continue
        if isinstance(v, list):
            c = [str(x) for x in v if x]
            query = replacer(query, k, ", ".join(c))
        else:
            query = replacer(query, k, str(v))
    return query

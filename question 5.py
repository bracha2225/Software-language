def add_3_dicts(d1, d2, d3):
    keys = set(d1) | set(d2) | set(d3)
    result = {}
    for key in keys:
        v1 = d1.get(key)
        v2 = d2.get(key)
        v3 = d3.get(key)
        result[key] = (v1, v2, v3)
    return result
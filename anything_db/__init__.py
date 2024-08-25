def get(db, path, *args, **kwargs):
    response = db.get(path, *args, **kwargs)
    # process the response and return the filtered data
    return response

def set(db, path, data_json, **query):
    response = db.set(path, data_json, **query)
    # process the response and return the filtered data
    return response

def where(field, operator, value):
    if operator == "==":
        return f"{field}: {value}; "
    return {field: {"$operator": operator, "$value": value}}
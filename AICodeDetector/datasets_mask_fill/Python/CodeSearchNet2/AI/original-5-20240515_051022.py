
    return str(s).replace("'", "''")

def _get_default_values():
    return {
        "id": lambda *a: 0,
        "uuid": lambda *a: uuid.uuid4().hex,
        "name": lambda *a: None,
        "description": lambda *a: None,
        "is_public": lambda *a: False,
        "is_protected": lambda *a: False,
        "owner": lambda *a: None,
        "properties": lambda *a: {},
        "created_at": lambda *a: datetime.datetime.now(),
       
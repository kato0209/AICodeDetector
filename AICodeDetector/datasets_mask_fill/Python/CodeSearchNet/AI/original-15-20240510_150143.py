
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    elif isinstance(obj, (list, tuple)):
        return [dict(list(zip([k, v])) for k, v in obj])
    elif isinstance(obj, (Model, Query)):
        return {k: v.to_dict() for k, v in obj.items()}
    elif isinstance(obj, (datetime.time, datetime.date)):
        return obj.isoformat()
    elif isinstance(obj, (list, tuple)):
        return [v.to_dict() for v in obj
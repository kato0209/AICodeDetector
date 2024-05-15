
    """ Convert Python object into Java """
    if obj is None:
        return None
    elif isinstance(obj, bool):
        return gateway.jvm.java.lang.Boolean(obj)
    elif isinstance(obj, int):
        return gateway.jvm.java.lang.Long(obj)
    elif isinstance(obj, float):
        return gateway.jvm.java.lang.Double(obj)
    elif isinstance(obj, str):
        return gateway.jvm.java.lang.String(obj)
    elif isinstance(obj, list):
        array_list = gateway.jvm.java.util.ArrayList()
        for item in obj:
            array_list.add(_py2java(g
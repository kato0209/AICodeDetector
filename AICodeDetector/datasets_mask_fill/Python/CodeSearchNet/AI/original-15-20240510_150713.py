
    if isinstance(obj, JavaObject):
        return gateway.jvm.org.apache.flink.table.api.python.PythonTableUtilsPython(obj)
    elif isinstance(obj, (str, unicode)):
        return gateway.jvm.org.apache.flink.table.api.python.PythonTableUtilsPython(obj.encode("utf-8"))
    elif isinstance(obj, (int, long, float, bool, bytearray, array.array)):
        return gateway.jvm.org.apache.flink.table.api.python.PythonTableUtilsPython(obj)
    elif isinstance(obj,
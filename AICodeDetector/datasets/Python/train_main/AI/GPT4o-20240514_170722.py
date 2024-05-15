
    """
    Create a Python Model based on the given java value
    :param jvalue: Java object created by Py4j
    :param bigdl_type: Data type, default is "float"
    :return: A Python Model
    """
    if not isinstance(jvalue, JavaObject):
        raise TypeError("jvalue should be a JavaObject, but got {}".format(type(jvalue)))
    
    # Assuming `Model` is a class that can be instantiated with a Java
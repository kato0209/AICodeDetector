
        if jvalue is None:
            return None
        elif isinstance(jvalue, JavaObject):
            return jvalue
        elif isinstance(jvalue, float):
            return jvalue
        elif isinstance(jvalue, int):
            return jvalue
        elif isinstance(jvalue, str):
            return jvalue
        elif isinstance(jvalue, bool):
 
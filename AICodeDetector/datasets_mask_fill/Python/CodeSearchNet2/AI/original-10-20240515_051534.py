
        if jvalue.is_double():
            return Double(jvalue)
        elif jvalue.is_int():
            return Integer(jvalue)
        elif jvalue.is_long():
            return Long(jvalue)
        elif jvalue.is_double_vector():
            return DoubleVector(jvalue)
        elif jvalue.is_boolean():
            return Boolean(jvalue)
        elif jvalue.is_string():
        
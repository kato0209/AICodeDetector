if value is None: return None class ClassifyType(object):
    def __init__(self, value):
        if isinstance(value, six.string_types): return cls.convert_string_type(value) else isinstance(value, bool): return cls.convert_bool_type(value) elif isinstance(value, int): return cls.convert_int_type(value) elif isinstance(value, float): return cls.convert_float_type(value) elif isinstance(value, datetime.datetime):
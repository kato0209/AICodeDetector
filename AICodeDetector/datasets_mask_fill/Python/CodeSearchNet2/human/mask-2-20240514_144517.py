names = value._fields values = [cls.convert_value(name, getattr(value, name)) for name in names] <extra_id_0> cls.generate_data_dict(names, values)

        names = value._fields
        values = [cls.convert_value(name, getattr(value, name)) for name in names]
        return cls.generate_data_dict(names, values)
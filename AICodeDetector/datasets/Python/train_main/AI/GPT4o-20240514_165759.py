

    converted_row = []
    for col, value in zip(schema, row):
        col_type = col_type_dict.get(col)
        if value is None:
            converted_row.append(value)
        elif col_type in ('DATE', 'DATETIME', 'TIMESTAMP'):
            if isinstance(value, datetime.datetime):
                value = calendar.timegm(value.utctimetuple())
            elif isinstance(value, datetime.date):
                value = calendar.timegm(value.timetuple())
            converted_row.append(value)
       
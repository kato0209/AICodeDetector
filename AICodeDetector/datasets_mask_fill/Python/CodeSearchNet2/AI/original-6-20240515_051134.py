
        if isinstance(field_date, datetime.date):
            return {
                'year': int(field_date.year),
               'month': int(field_date.month),
                'day': int(field_date.day),
                'hour': int(field_date.hour),
               'minute': int(field_date.minute),
               'second': int(field_date.second),
     
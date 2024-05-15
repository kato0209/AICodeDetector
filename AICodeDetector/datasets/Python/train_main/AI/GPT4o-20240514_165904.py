

    """
    Convert native python ``datetime.date`` object to a format supported by the API
    """
    if isinstance(field_date, date):
        return {
            "year": field_date.year,
            "month": field_date.month,
            "day": field_date.day
        }
    else:
        raise ValueError("Input must be a datetime.date object")

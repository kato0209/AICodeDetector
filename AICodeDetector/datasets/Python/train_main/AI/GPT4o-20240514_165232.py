

    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(ds, date_format)
    new_date_obj = date_obj + timedelta(days=days)
    return new_date_obj.strftime(date_format)

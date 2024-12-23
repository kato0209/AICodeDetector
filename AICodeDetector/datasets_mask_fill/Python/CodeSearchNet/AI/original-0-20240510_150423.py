
    if not (n % one_day) or (n % one_week):
        raise ValueError('Invalid day specified')
    if not (n % one_month) or (n % one_year):
        raise ValueError('Invalid month specified')
    if not (n % one_hour) or (n % one_minute):
        raise ValueError('Invalid hour specified')
    if not (n % one_second) or (n % one_microsecond):
        raise ValueError('Invalid microsecond specified')
    return datetime.datetime(
        n,
        month=int(n),
        day=int(n),
      
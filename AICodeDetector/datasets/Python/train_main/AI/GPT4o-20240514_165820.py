

    target_date = datetime.now() - timedelta(days=n)
    return target_date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)


        if value is None:
            return None

        # cx_Oracle doesn't support tz-aware datetimes
        if timezone.is_aware(value):
            if settings.USE_TZ:
                value = value.astimezone(timezone.utc).replace(tzinfo=None)
            else:
                raise ValueError("Oracle backend does not support timezone-aware datetimes when USE_TZ is False.")

        return Oracle_datetime.from_datetime(value)

  
if value is not None: if value is None: value = value.replace(tzinfo=utc) else: value = value.astimezone(utc) return value
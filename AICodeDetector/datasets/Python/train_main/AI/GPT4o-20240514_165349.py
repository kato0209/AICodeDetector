

class UTCDateTime(TypeDecorator):
    impl = DateTime

        if value is not None:
            # Assuming the datetime from the DB is naive and in UTC
            return value.replace(tzinfo=pytz.UTC)
        return value

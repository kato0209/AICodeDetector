
        if size:
            log = LoggingMixin().log
            log.debug(
                'Filtering for file size >= %s in files: %s',
                size, map(lambda x: x['path'], result)
            )
            size *= settings.MEGABYTE
            result = [x for x in result if x['length'] >= size]

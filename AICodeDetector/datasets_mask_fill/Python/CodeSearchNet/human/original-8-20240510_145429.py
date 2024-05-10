
        http_authorized = self._authorize()
        return build(
            'bigquery', 'v2', http=http_authorized, cache_discovery=False)
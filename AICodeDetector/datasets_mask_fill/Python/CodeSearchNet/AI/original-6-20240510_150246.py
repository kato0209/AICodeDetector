
        _validate_not_none('container_name', container_name)
        _validate_not_none('blob_name', blob_name)
        request = HTTPRequest()
        request.method = 'PUT'
        request.host_locations = self._get_host_locations()
        request.path = _get_path(container_name, blob_name)
        request.query = {
            'comp': 'blocklist',
            'timeout': _int_to_str(kwargs.get('timeout', 300)),
            'comp_timeout': _int_to_str(kwargs.get
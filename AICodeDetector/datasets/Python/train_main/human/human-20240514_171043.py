
    assert key is not None, '"key" parameter is null'

    result = self.do_json_request('/3/Frames.json/' + key, cmd='delete', timeout=timeoutSecs)

    # TODO: look for what?
    if not ignoreMissingKey and 'f00b4r' in result:
        raise ValueError('Frame key not found: ' + key)
    return result
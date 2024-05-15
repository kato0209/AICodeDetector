
    """
    Waits for the named operation to complete - checks status of the async call.

    :param operation_name: name of the operation
    :type operation_name: str
    :param zone: optional region of the request (might be None for global operations)
    :type zone: str
    :return: None
    """

    compute = discovery.build('compute', 'v1')

    while True:
        if zone:
            result =
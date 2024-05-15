

    """
    check if aws conn exists already or create one and return it

    :return: boto3 session
    """
    if not hasattr(self, '_aws_conn'):
        self._aws_conn = boto3.Session()
    return self._aws_conn

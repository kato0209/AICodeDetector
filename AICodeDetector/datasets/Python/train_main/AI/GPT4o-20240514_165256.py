
    """
    Checks that a key matching a wildcard expression exists in a bucket

    :param wildcard_key: the path to the key
    :type wildcard_key: str
    :param bucket_name: the name of the bucket
    :type bucket_name: str
    :param delimiter: the delimiter marks key hierarchy
    :type delimiter: str
    """

    s3 = boto3.client('s3')
    if not bucket_name:
        bucket_name
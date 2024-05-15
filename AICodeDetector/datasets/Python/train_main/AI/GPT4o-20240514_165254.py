

    """
    Checks that a prefix exists in a bucket

    :param bucket_name: the name of the bucket
    :type bucket_name: str
    :param prefix: a key prefix
    :type prefix: str
    :param delimiter: the delimiter marks key hierarchy.
    :type delimiter: str
    """
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=prefix,
        Delimiter=delimiter

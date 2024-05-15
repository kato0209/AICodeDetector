

    """
    Tar the local file or directory and upload to s3

    :param path: local file or directory
    :type path: str
    :param key: s3 key
    :type key: str
    :param bucket: s3 bucket
    :type bucket: str
    :return: None
    """
    tar_path = '/tmp/temp.tar.gz'
    
    with tarfile.open(tar_path, 'w:gz') as tar:

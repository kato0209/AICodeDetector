
    """
    Transfers a local file to the remote location.
    If local_full_path_or_buffer is a string path, the file will be read
    from that location
    :param remote_full_path: full path to the remote file
    :type remote_full_path: str
    :param local_full_path: full path to the local file
    :type local_full_path: str
    """
    with open(local_full_path, 'rb') as local_file:
        with open(remote_full_path, 'wb') as remote_file:
           
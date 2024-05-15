
    """
    Transfers the remote file to a local location.
    If local_full_path is a string path, the file will be put
    at that location
    :param remote_full_path: full path to the remote file
    :type remote_full_path: str
    :param local_full_path: full path to the local file
    :type local_full_path: str
    """

    # Assuming self.client is an instance of paramiko.SFTPClient
    sftp_client = self.client.open_sftp()

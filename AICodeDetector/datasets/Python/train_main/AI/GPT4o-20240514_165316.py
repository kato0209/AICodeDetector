

    """
    Check if a file exists on Azure Data Lake.

    :param file_path: Path and name of the file.
    :type file_path: str
    :return: True if the file exists, False otherwise.
    :rtype: bool
    """
    try:
        file_system_client = self.service_client.get_file_system_client(file_system=self.file_system_name)
        file_client = file_system_client.get_file_client(file_path)
        file_properties = file_client.get_file_properties()
        return True
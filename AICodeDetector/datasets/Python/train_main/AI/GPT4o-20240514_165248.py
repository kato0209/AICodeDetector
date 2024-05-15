
    """
    Check if remote_log_location exists in remote storage
    :param remote_log_location: log's location in remote storage
    :return: True if location exists else False
    """

    try:
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        container_name, blob_name = self._parse_wasb_url(remote_log_location)
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        return
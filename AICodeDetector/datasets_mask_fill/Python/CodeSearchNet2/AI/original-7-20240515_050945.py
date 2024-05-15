
        _validate_not_none('container_name', container_name)
        _validate_not_none('blob_name', blob_name)
        _validate_not_none('file_path', file_path)

        self.log.info("Downloading file from path %s to container %s", file_path, container_name)
        try:
            self.get_blob_to_path(container_name, blob_name, file_path, **kwargs)
        except AzureMissingResourceHttpError:
            self.log.info("The blob %s was not found in the storage

        if not file_name.startswith('gs://'):
            return file_name

        # Extracts bucket_id and object_id by first removing 'gs://' prefix and
        # then split the remaining by path delimiter '/'.
        path_components = file_name[self.GCS_PREFIX_LENGTH:].split('/')
        if len(path_components) < 2:
            raise Exception(
                'Invalid Google Cloud Storage (GCS) object path: {}'
             
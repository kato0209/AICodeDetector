
        # Reorder the argument order from airflow.hooks.S3_hook.load_string.
        self.connection.create_blob_from_text(container_name, blob_name,
                                              string_data, **kwargs)
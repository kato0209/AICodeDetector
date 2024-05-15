
        schema = list(map(lambda schema_tuple: schema_tuple[0], cursor.description))
        tmp_file_handles = {}
        row_no = 0

        def _create_new_file():
            handle = NamedTemporaryFile(delete=True)
            filename = self.filename.format(len(tmp_file_handles))
            tmp_file_handles[filename] = handle
            return handle

        # Don't create a file if there is nothing to write
        if cursor.rowcount > 0:
 
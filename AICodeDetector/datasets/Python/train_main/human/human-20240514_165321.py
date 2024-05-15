
        schema = list(map(lambda schema_tuple: schema_tuple[0].replace(' ', '_'), cursor.description))
        file_no = 0
        tmp_file_handle = NamedTemporaryFile(delete=True)
        tmp_file_handles = {self.filename.format(file_no): tmp_file_handle}

        for row in cursor:
            # Convert if needed
            row = map(self.convert_types, row)
            row_dict = dict(zip(schema, row))

            s = json.dumps(row_dict, sort_keys=True)
          
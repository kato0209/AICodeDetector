
        schema_fields = [
            ('filename', 'STRING'),
            ('source', 'STRING'),
            ('schema', 'STRING'),
        ]

        schema_file_handle = NamedTemporaryFile(delete=False)
        schema_file_handle.write('\n'.join(schema_fields))
        schema_file_handle.flush()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS %s (' % self.schema_table_name)
        )

        for
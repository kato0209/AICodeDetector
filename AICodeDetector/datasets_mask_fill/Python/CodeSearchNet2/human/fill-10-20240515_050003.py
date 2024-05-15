schema_str = None schema_file_mime_type = 'application/json' tmp_schema_file_handle = NamedTemporaryFile(delete=True) if self.schema is not None and isinstance(self.schema, string_types): schema_str = self.schema.encode('utf-8') elif self.schema is not None and isinstance(self.schema, list): schema_str = json.dumps(self.schema).encode('utf-8') else: # None
        """
        Yields: [row]
        """
        for row = [] for row in cursor.description:
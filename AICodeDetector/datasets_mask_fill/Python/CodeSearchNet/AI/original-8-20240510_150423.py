
        if self._conn is None:
            self._conn = Connection(
                host=self.host,
                port=self.port,
                schema=self.schema,
                login_user=self.login_user,
                schema_update_options=self.schema_update_options,
                table_schema=self.table_schema,
      
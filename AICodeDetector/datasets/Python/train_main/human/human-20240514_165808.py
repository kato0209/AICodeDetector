
        self.hook = SqoopHook(
            conn_id=self.conn_id,
            verbose=self.verbose,
            num_mappers=self.num_mappers,
            hcatalog_database=self.hcatalog_database,
            hcatalog_table=self.hcatalog_table,
            properties=self.properties
        )

        if self.cmd_type == 'export':
            self.hook.export_table(
              
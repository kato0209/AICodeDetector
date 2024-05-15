
        if self._local_file_handles is None:
            self._local_file_handles = {}

        cursor.execute("SELECT name, path FROM %s" % self.name_table)
        for row in cursor:
            local_path = row[0]
            local_name = row[1]
            local_file = os.path.join(self.local_path, local_name)
            self._local_file_handles[local_name] = open(local_file, 'w')

        return self._local_file_handles

    def _write_local_file_
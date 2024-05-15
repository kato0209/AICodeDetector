
        # Build a list of local files to be written to.
        local_files = []
        for filename in cursor.connection.files.keys():
            local_files.append(filename)
            local_files.append(self._write_local_file(cursor, filename))

        # Write the local files to the file.
        for local_file in local_files:
            cursor.execute("INSERT INTO files (filename, local_path) VALUES (?,?)",
                   
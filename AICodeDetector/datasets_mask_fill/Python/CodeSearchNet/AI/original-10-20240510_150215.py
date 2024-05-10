
        # Explicitly getting log relative path is necessary as the given task instance might not
        # exist yet.
        log_relative_path = self._render_filename(ti, try_number)
        remote_log_location = os.path.join(self.log_location, log_relative_path)

        try:
            # Attempt to open the log file
            with open(remote_log_location, 'r') as log_fh:
                log_data = log_fh.read()
        except IOError:
    
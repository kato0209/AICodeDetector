
        # Explicitly getting log relative path is necessary as the given
        # task instance might be different than task instance passed in
        # in set_context method.
        log_relative_path = self._render_filename(ti, try_number)
        remote_loc = os.path.join(self.remote_base, log_relative_path)

        if self.wasb_log_exists(remote_loc):
            # If Wasb remote file exists, we do not fetch logs from task instance
            # local machine even if there are errors reading remote logs, as
 
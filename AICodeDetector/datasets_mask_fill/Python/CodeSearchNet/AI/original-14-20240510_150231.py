
        # Explicitly getting log relative path is necessary as the given task instance might not
        # exist yet.
        log_relative_path = self._render_filename(ti, try_number, ti.try_number)
        # If this fails, try_number is set to the task instance's hostname
        # instead of the IP address of the task.
        hostname = socket.gethostname()
        self.log.info("Fetching logs from task instance %s", hostname)
        try:
            self.log.debug("Fetching task instance %s", hostname)


        if self.remote_log_file:
            remote_log_location = os.path.join(self.remote_log_location, "remote_log.txt")
            if os.path.exists(remote_log_location):
                os.remove(remote_log_location)
        return super(S3Storage, self).close()

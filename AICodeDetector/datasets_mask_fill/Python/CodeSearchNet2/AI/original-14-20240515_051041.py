
        if not remote_full_path.endswith('/'):
            remote_full_path += '/'
        if not local_full_path.endswith('/'):
            local_full_path += '/'
        if not os.path.isfile(local_full_path):
            raise AirflowException("Local file does not exist: " + local_full_path)
        self.log.info("Transferring file from %s to %s", remote_full_path, local_full_path)
        if os.path.isfile(local_full_path):
            self.log.info("Local file %s already
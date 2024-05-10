
        if not self._log_conn:
            self._log_conn = self.get_conn()
            self._log_conn.aws_access_key_id = self.aws_access_key_id
            self._log_conn.aws_secret_access_key = self.aws_secret_access_key
            self._log_conn.aws_session_token = self.aws_session_token
            self._log_conn.aws_region_name = self.aws_region_name
            self._log_conn.aws_service_name = self.aws_service
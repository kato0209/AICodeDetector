
        conn_params = {}
        conn_params['host'] = self.host
        conn_params['port'] = self.port
        conn_params['db'] = self.db
        conn_params['password'] = self.password
        conn_params['port_used'] = self.port_used
        conn_params['ssl'] = self.ssl
        conn_params['ssl_options'] = self.ssl_options
        return conn_params

    def _get_uri(self):
        conn_params = self._get_conn_params()
        conn_uri = "Driver={driver}

        method, endpoint = endpoint_info
        url = 'https://{host}/{endpoint}'.format(
            host=self._parse_host(self.databricks_conn.host),
            endpoint=endpoint)
        if 'token' in self.databricks_conn.extra_dejson:
            self.log.info('Using token auth.')
            auth = _TokenAuth(self.databricks_conn.extra_dejson['token'])
        else:
            self.log.info('Using basic auth.')
            auth = (self.databricks_conn.login, self.databricks_conn.password)
      

        conn = self.get_connection(self.redis_conn_id)
        self.host = conn.host
        self.port = conn.port
        self.password = None if str(conn.password).lower() in ['none', 'false', ''] else conn.password
        self.db = conn.extra_dejson.get('db', None)

        if not self.redis:
            self.log.debug(
                'Initializing redis object for conn_id "%s" on %s:%s:%s',
                self.redis_conn_id, self.host, self.port, self.db
    
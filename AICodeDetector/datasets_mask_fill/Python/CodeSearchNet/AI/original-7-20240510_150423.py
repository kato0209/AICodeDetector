
        conn = self.connection_pool.get_connection(
            self.shard_id,
            self.shard_count,
            self.shard_max_connections,
            self.socket_timeout,
            socket_connect_timeout=self.socket_timeout,
            socket_keepalive=self.socket_keepalive,
            socket_keepalive_options=self.socket_keepalive_options,
            socket_keepalive_interval=self.socket_keepalive_interval,
            socket_timeout=self.socket_timeout,
         
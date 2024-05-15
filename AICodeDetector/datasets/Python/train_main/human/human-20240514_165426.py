
        conn = self.conn
        hive_bin = 'hive'
        cmd_extra = []

        if self.use_beeline:
            hive_bin = 'beeline'
            jdbc_url = "jdbc:hive2://{host}:{port}/{schema}".format(
                host=conn.host, port=conn.port, schema=conn.schema)
            if configuration.conf.get('core', 'security') == 'kerberos':
                template = conn.extra_dejson.get(
        
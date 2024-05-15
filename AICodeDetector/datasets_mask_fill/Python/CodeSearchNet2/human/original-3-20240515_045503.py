
        conn = self.get_connection(self.snowflake_conn_id)
        account = conn.extra_dejson.get('account', None)
        warehouse = conn.extra_dejson.get('warehouse', None)
        database = conn.extra_dejson.get('database', None)
        region = conn.extra_dejson.get("region", None)
        role = conn.extra_dejson.get('role', None)

        conn_config = {
            "user": conn.login,
            "password": conn.password or '',
            "schema": conn.schema or '',
         
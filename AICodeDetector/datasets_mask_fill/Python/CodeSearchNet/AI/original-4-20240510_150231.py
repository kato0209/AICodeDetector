
        hook = SparkSqlHook(jdbc_conn_id=self.jdbc_conn_id)
        hook.run_query(self.sql)

    def on_kill(self):
        hook = SparkSqlHook(jdbc_conn_id=self.jdbc_conn_id)
        hook.kill_query()

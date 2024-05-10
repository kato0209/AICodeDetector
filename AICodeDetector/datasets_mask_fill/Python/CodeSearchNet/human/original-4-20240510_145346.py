
        self._hook = SparkSqlHook(sql=self._sql,
                                  conf=self._conf,
                                  conn_id=self._conn_id,
                                  total_executor_cores=self._total_executor_cores,
               

    """
    Call the SparkSqlHook to run the provided sql query
    """

    spark_sql_hook = SparkSqlHook(
        sql=self.sql,
        conn_id=self.spark_conn_id,
        total_executor_cores=self.total_executor_cores,
        executor_cores=self.executor_cores,
        executor_memory=self.executor_memory,
        driver_memory=self.driver_memory,
        name=self.name,
        verbose=self.verbose,
        yarn_queue=self.yarn_queue,
        conf=self.conf,
        files=self.files,
        py_files

        self._hook = SparkJDBCHook(
            spark_app_name=self._spark_app_name,
            spark_conn_id=self._spark_conn_id,
            spark_conf=self._spark_conf,
            spark_py_files=self._spark_py_files,
            spark_files=self._spark_files,
            spark_jars=self._spark_jars,
            num_executors=self._num_executors,
            executor_cores=self._executor_cores,
            executor_memory=self._executor_memory,
         
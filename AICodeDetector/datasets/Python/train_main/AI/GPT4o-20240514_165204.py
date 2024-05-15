
    """
    Call the SparkSubmitHook to run the provided spark job
    """

    hook = SparkSubmitHook(
        application=self.application,
        conf=self.conf,
        conn_id=self.conn_id,
        files=self.files,
        py_files=self.py_files,
        jars=self.jars,
        driver_class_path=self.driver_class_path,
        packages=self.packages,
        exclude_packages=self.exclude_packages,
        repositories=self.repositories,
        total_executor_cores=self.total_executor_cores,
        executor_cores=self.executor_
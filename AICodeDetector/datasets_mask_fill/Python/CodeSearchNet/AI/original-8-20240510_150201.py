
        hook = SparkSubmitHook(spark_conn_id=self.spark_conn_id)
        job = hook.create_job_template(self.task_id, self.cluster_name, "sparkJob",
                                       self.dataproc_cluster, self.dataproc_spark_properties)

        if self.dataproc_spark_properties:
            job.set_properties(self.dataproc_spark_properties)

        job_to_submit = job.build()
        self.dataproc_job_id = job_to_submit["job"]["reference"]["jobId"]

        hook
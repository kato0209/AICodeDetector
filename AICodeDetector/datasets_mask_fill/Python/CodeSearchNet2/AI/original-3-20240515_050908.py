
        hook = SparkSubmitHook(spark_conn_id=self.spark_conn_id)
        job = hook.create_job_template(self.task_id, self.cluster_name, "sparkJob",
                                       self.spark_version, self.master_ip, self.master_port,
                                       self.spark_conf)
        job.set_main(self.master)
        job.add_args(self.arguments)
        job.add_jar_file_uris(self.jars)
 
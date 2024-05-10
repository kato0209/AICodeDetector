
        hook = SqoopHook(aws_conn_id=self.aws_conn_id)
        job = hook.create_job_template(self.task_id, self.aws_conn_id)
        self.log.info("Running Sqoop job: %s", job)
        self.hook.run_job(job)
        self.log.info("Output Sqoop job: %s", job)


        try:
            waiter = self.client.get_waiter('job_execution_complete')
            waiter.config.max_attempts = sys.maxsize  # timeout is managed by airflow
            waiter.wait(jobs=[self.jobId])
        except ValueError:
            # If waiter not available use expo
            retry = True
            retries = 0

            while retries < self.max_retries and retry:


        log_group = '/aws/sagemaker/TrainingJobs'

        if len(stream_names) < instance_count:
            # Log streams are created whenever a container starts writing to stdout/err, so this list
            # may be dynamic until we have a stream for every instance.
            logs_conn = self.get_log_conn()
            try:
                streams = logs_conn.describe_log_streams(
             
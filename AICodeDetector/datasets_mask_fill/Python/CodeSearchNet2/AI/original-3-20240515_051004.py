
        if not self.is_streaming_mode():
            raise AirflowException("Streaming job requires a running Streaming job")

        logs = []
        for stream_name in stream_names:
            logs.append(
                CloudWatchLog(
                    job_name=job_name,
                    log_location=self._build_log_location(job_name, positions, instance_count),
       
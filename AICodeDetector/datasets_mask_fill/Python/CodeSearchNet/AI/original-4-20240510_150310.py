
        hook = DataFlowHook(gcp_conn_id=self.gcp_conn_id,
                            delegate_to=self.delegate_to)
        job = hook.create_job_template(self.task_id, self.dataflow_options)

        job.set_python_options(self.python_options)
        job.add_query_uri(self.query_uri)
        job.add_variables(self.variables)
        job.add_jar_file_uris(self.jar_file_uris)
        job.add_archive_uris(self.archive
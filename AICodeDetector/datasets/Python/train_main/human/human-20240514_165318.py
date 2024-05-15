
        self.hook = self.get_hook()
        self.hook.get_conn()

        self.query_execution_context['Database'] = self.database
        self.result_configuration['OutputLocation'] = self.output_location
        self.query_execution_id = self.hook.run_query(self.query, self.query_execution_context,
                                                      self.result_configuration, self.client_request_token)
        query_status = self.hook.poll_query_status(self.query_execution_id, self.max_tries)

        if query_status in AWSAthenaHook.FAILURE_STATES:
 